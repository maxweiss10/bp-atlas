"""Harvest the full monotherapy grid from the DREAM BP model app.

For every drug at 0.5x / 1x / 2x standard dose, record the placebo-corrected
SBP and DBP reduction (with prediction interval), the intensity band, and the
model's own baseline-BP sweep.
"""
import json
import re
import threading
import queue
import websocket
from shiny_client import ShinyApp, values_from

BASELINES_SBP = [130, 140, 150, 160, 170, 180]
BASELINES_DBP = [80, 85, 90, 95, 100, 105]
NUM = r"(-?\d+(?:\.\d+)?)"
# Bounds may be "N/A" (thin trial data) or "<1" (rounds below 1).
VAL = r"(&lt;\s*-?\d+(?:\.\d+)?|-?\d+(?:\.\d+)?|N/A)"


def _num(s):
    if isinstance(s, str):
        s = s.replace("&lt;", "").strip()
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def _detag(html):
    """Strip tags after protecting literal '<' used as less-than."""
    return re.sub(r"<(?=\s*\d)", "&lt;", html)


def parse_summary2(html):
    txt = re.sub(r"<[^>]+>", " ", _detag(html)).replace("&emsp;", " ")
    txt = re.sub(r"\s+", " ", txt)
    m = re.search(rf"SBP: {VAL} \({VAL}, {VAL}\) mmHg", txt)
    d = re.search(rf"DBP: {VAL} \({VAL}, {VAL}\) mmHg", txt)
    inten = re.search(r"Regimen intensity b ?: ?(\w+) intensity", txt)
    if not (m and d):
        return None
    return {
        "sbp": _num(m.group(1)), "sbp_lo": _num(m.group(2)), "sbp_hi": _num(m.group(3)),
        "dbp": _num(d.group(1)), "dbp_lo": _num(d.group(2)), "dbp_hi": _num(d.group(3)),
        "intensity": (inten.group(1).lower() if inten else None),
    }


def parse_table(val):
    try:
        data = val["x"]["tag"]["attribs"]["data"]
    except (KeyError, TypeError):
        return None
    base = data.get("Baseline (mmHg)")
    red = data.get("Avg. reduction (mmHg)")
    if not base or not red:
        return None
    out = {}
    for b, r in zip(base, red):
        v = _num(str(r).replace("<", ""))
        if v is not None:
            out[int(b)] = v
    return out


def parse_cardio(html):
    txt = re.sub(r"<[^>]+>", " ", html)
    txt = re.sub(r"\s+", " ", txt)
    rrr = re.search(rf"risk reduction: {NUM}%", txt)
    nnt = re.search(rf"Number needed to treat = {NUM}", txt)
    return {
        "rrr_pct": float(rrr.group(1)) if rrr else None,
        "nnt": float(nnt.group(1)) if nnt else None,
    }


class Harvester:
    def __init__(self):
        self.app = None
        self.clicks = 0

    def open(self):
        self.app = ShinyApp().connect()
        self.app.init({
            "drug_1": "C08CA01", "dose_1": "5",
            "baseline_sbp": 154, "baseline_dbp": 100,
            "show_bp": True, "show_cardio": True,
            "abs_risk_yrs": "10", "baseline_cardio_risk": 10,
        })
        self.clicks = 0
        return self

    def query(self, atc, dose, tries=3):
        for attempt in range(tries):
            try:
                self.app.update({"drug_1": atc, "dose_1": str(dose)})
                self.clicks += 1
                self.app.update({"updateBtn:shiny.action": self.clicks})
                v = self.app.wait_for("summary2")
                s2 = v.get("summary2")
                s1 = v.get("summary1")
                if not s2:
                    raise RuntimeError("no summary2")
                html = s2["html"] if isinstance(s2, dict) else s2
                rec = parse_summary2(html)
                if rec is None:
                    raise RuntimeError("unparseable summary2")
                regimen = re.sub(r"<[^>]+>", "", (s1["html"] if isinstance(s1, dict) else s1) or "")
                rec["regimen"] = re.sub(r"\s+", " ", regimen).replace("Treatment regimen: ", "").strip()
                rec["sbp_by_baseline"] = parse_table(v.get("te_sbp_table"))
                rec["dbp_by_baseline"] = parse_table(v.get("te_dbp_table"))
                rec.update(parse_cardio(
                    (v.get("cardio") or {}).get("html") if isinstance(v.get("cardio"), dict) else (v.get("cardio") or "")
                ))
                return rec
            except (websocket.WebSocketException, RuntimeError, OSError) as e:
                if attempt == tries - 1:
                    return {"error": f"{type(e).__name__}: {e}"}
                try:
                    self.app.close()
                except Exception:
                    pass
                self.open()
        return {"error": "exhausted"}


def worker(jobs, results, lock, progress):
    h = Harvester().open()
    while True:
        try:
            atc, name, dose, label = jobs.get_nowait()
        except queue.Empty:
            break
        rec = h.query(atc, dose)
        rec.update({"atc": atc, "name": name, "dose_mg": dose, "dose_label": label})
        with lock:
            results.append(rec)
            progress[0] += 1
            print(f'{progress[0]:>4} {name:<22} {label:<5} {dose:>7}mg  '
                  f'SBP {rec.get("sbp", rec.get("error"))}', flush=True)
        jobs.task_done()
    h.app.close()


def main():
    drugs = json.load(open("drugs.json"))
    dose_opts = json.load(open("dose_options.json"))
    jobs = queue.Queue()
    n = 0
    for d in drugs:
        opts = (dose_opts.get(d["atc"]) or {}).get("doses")
        if not opts:
            print("NO DOSES:", d["name"])
            continue
        labels = {0: "0.5x", 1: "1x", 2: "2x"}
        for i, dose in enumerate(sorted(opts)):
            jobs.put((d["atc"], d["name"], dose, labels.get(i, f"opt{i}")))
            n += 1
    print(f"queued {n} queries")

    results, lock, progress = [], threading.Lock(), [0]
    threads = [threading.Thread(target=worker, args=(jobs, results, lock, progress))
               for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    results.sort(key=lambda r: (r["name"], r["dose_mg"]))
    json.dump(results, open("mono_grid.json", "w"), indent=1)
    ok = sum(1 for r in results if "error" not in r)
    print(f"\nDONE {ok}/{len(results)} succeeded -> mono_grid.json")


if __name__ == "__main__":
    main()
