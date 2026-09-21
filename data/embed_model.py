"""Re-embed model.json in index.html, and nothing else.

add_kinetics.py also embeds the payload, but it regenerates the kinetics layer
from kinetics.py first, which would overwrite any edit made to model.json
directly. This script is the safe way to push a model.json change to the page.

Run from data/:  python3 embed_model.py
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'model.json')
PAGE = os.path.join(HERE, os.pardir, 'index.html')

m = json.load(open(MODEL, encoding='utf-8'))
payload = json.dumps(m, separators=(',', ':'), ensure_ascii=False)
html = open(PAGE, encoding='utf-8').read()
new, n = re.subn(r'^const PAYLOAD = \{.*\};$',
                 lambda _: 'const PAYLOAD = %s;' % payload, html, count=1, flags=re.M)
if n != 1:
    sys.exit('could not find the embedded PAYLOAD line in index.html')
open(PAGE, 'w', encoding='utf-8').write(new)
print('%d drugs re-embedded, %d payload bytes' % (len(m['drugs']), len(payload)))
print('tagged for the Difference column:', sum(1 for d in m['drugs'] if d.get('tag')))
