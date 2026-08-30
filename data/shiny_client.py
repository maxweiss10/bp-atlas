"""Minimal SockJS/Shiny client for the DREAM BP model app.

Speaks the Shiny websocket protocol directly so we can query the published
efficacy model programmatically instead of clicking through the UI.
"""
import json
import random
import re
import string
import requests
import websocket

BASE = "https://dream-bp-model.shinyapps.io/shiny-bootstrap/"
HOST = "dream-bp-model.shinyapps.io"


def _rand(n, alphabet=string.ascii_letters + string.digits):
    return "".join(random.choice(alphabet) for _ in range(n))


class ShinyApp:
    def __init__(self, timeout=30):
        self.timeout = timeout
        self.sess = requests.Session()
        self.sess.headers.update({"User-Agent": "Mozilla/5.0"})
        page = self.sess.get(BASE, timeout=timeout)
        page.raise_for_status()
        self.worker = re.search(r"_w_([0-9a-f]{32})", page.text).group(1)
        self.token = self.sess.get(BASE + "__token__", timeout=timeout).text.strip()
        self.ws = None
        self.msgs = []

    # ---- transport -------------------------------------------------
    def connect(self):
        n = _rand(18)
        url = (
            f"wss://{HOST}/shiny-bootstrap/__sockjs__/n={n}/t={self.token}"
            f"/w={self.worker}/s=0/{random.randint(100, 999)}/{_rand(8).lower()}/websocket"
        )
        cookie = "; ".join(f"{k}={v}" for k, v in self.sess.cookies.get_dict().items())
        self.ws = websocket.create_connection(
            url,
            timeout=self.timeout,
            origin=f"https://{HOST}",
            host=HOST,
            header=[f"Cookie: {cookie}"] if cookie else [],
            suppress_origin=False,
        )
        opener = self.ws.recv()
        if not opener.startswith("o"):
            raise RuntimeError(f"unexpected sockjs open frame: {opener!r}")
        self.out_id = 0      # robust-protocol outgoing message counter
        self.next_ack = 0    # id we expect next from the server
        # Open multiplex channel 0 before any Shiny traffic.
        self.ws.send(json.dumps([f"{self.out_id:X}#0|o|/shiny-bootstrap/"]))
        self.out_id += 1
        return self

    def _send(self, obj):
        """Send one Shiny message.

        Wire format is <HEXID>#<subapp>|<type>|<payload>: the outer tag is the
        robust-reconnect layer, the `0|m|` prefix the subapp multiplexer.
        """
        tagged = f"{self.out_id:X}#0|m|{json.dumps(obj)}"
        self.out_id += 1
        self.ws.send(json.dumps([tagged]))

    def _recv_frames(self):
        """Return list of decoded Shiny messages from one sockjs frame."""
        raw = self.ws.recv()
        if not raw or raw[0] == "h":  # heartbeat
            return []
        if raw[0] == "c":
            raise RuntimeError(f"sockjs closed: {raw}")
        if raw[0] != "a":
            return []
        out = []
        for payload in json.loads(raw[1:]):
            m = re.match(r"^([\dA-F]+)#([\s\S]*)$", payload)
            if m:
                self.next_ack = int(m.group(1), 16) + 1
                payload = m.group(2)
            elif payload.startswith(("ACK ", "CONTINUE ")):
                continue  # robust-layer control traffic
            sub = re.match(r"^\d+\|(\w)\|([\s\S]*)$", payload)
            if sub:
                if sub.group(1) != "m":
                    continue  # subapp control frame, not a Shiny message
                payload = sub.group(2)
            try:
                out.append(json.loads(payload))
            except json.JSONDecodeError:
                pass
        return out

    # ---- shiny -----------------------------------------------------
    def init(self, inputs):
        data = dict(inputs)
        for out in ("summary1", "summary2", "cardio", "te_sbp_table", "te_dbp_table"):
            data[f".clientdata_output_{out}_hidden"] = False
        data.update({
            ".clientdata_pixelratio": 2,
            ".clientdata_url_protocol": "https:",
            ".clientdata_url_hostname": HOST,
            ".clientdata_url_port": "",
            ".clientdata_url_pathname": "/shiny-bootstrap/",
            ".clientdata_url_search": "",
            ".clientdata_url_hash_initial": "",
            ".clientdata_url_hash": "",
            ".clientdata_singletons": "",
            ".clientdata_allowDataUriScheme": True,
        })
        self._send({"method": "init", "data": data})
        return self.pump(settle=1)

    def update(self, values):
        self._send({"method": "update", "data": values})

    def wait_for(self, output, max_wait=25.0, quiet_after=0.6):
        """Collect messages until `output` has a value, then drain briefly.

        Much faster than pump(): returns as soon as the server has answered
        rather than waiting out a fixed silence window.
        """
        import time
        vals, deadline = {}, time.time() + max_wait
        self.ws.settimeout(1.0)
        got_at = None
        try:
            while time.time() < deadline:
                if got_at and time.time() - got_at > quiet_after:
                    break
                try:
                    msgs = self._recv_frames()
                except websocket.WebSocketTimeoutException:
                    if got_at:
                        break
                    continue
                for m in msgs:
                    if isinstance(m, dict) and "values" in m:
                        vals.update(m["values"])
                if output in vals and got_at is None:
                    got_at = time.time()
        finally:
            self.ws.settimeout(self.timeout)
        return vals

    def pump(self, settle=2, max_frames=400):
        """Collect messages until the server goes quiet (`settle` timeouts)."""
        collected = []
        quiet = 0
        self.ws.settimeout(2.5)
        while quiet < settle and len(collected) < max_frames:
            try:
                msgs = self._recv_frames()
            except websocket.WebSocketTimeoutException:
                quiet += 1
                continue
            if msgs:
                collected.extend(msgs)
                quiet = 0
        self.ws.settimeout(self.timeout)
        self.msgs.extend(collected)
        return collected

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def values_from(msgs):
    """Flatten {'values': {...}} messages into one dict."""
    vals = {}
    for m in msgs:
        if isinstance(m, dict) and "values" in m:
            vals.update(m["values"])
    return vals


def strip_html(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r"<br\s*/?>", " | ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&nbsp;", " ").replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()
