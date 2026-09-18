"""Fold the onset/offset layer into model.json and re-embed it in index.html.

Run from data/:  python3 add_kinetics.py
"""
import json, os, re, sys
from kinetics import kin_for, SOURCE

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'model.json')
PAGE = os.path.join(HERE, os.pardir, 'index.html')

m = json.load(open(MODEL))
missing = []
for d in m['drugs']:
    k = kin_for(d['n'], d.get('sub'))
    if k is None:
        missing.append(d['n'])
        continue
    d['kin'] = k
if missing:
    sys.exit(f'no kinetics for: {missing}')

m['sources']['kin'] = SOURCE
json.dump(m, open(MODEL, 'w'), separators=(',', ':'))

payload = json.dumps(m, separators=(',', ':'))
html = open(PAGE).read()
new, n = re.subn(r'^const PAYLOAD = \{.*\};$',
                 lambda _: f'const PAYLOAD = {payload};',
                 html, count=1, flags=re.M)
if n != 1:
    sys.exit('could not find the embedded PAYLOAD line in index.html')
open(PAGE, 'w').write(new)

byq = {}
for d in m['drugs']:
    for f in ('on', 'pk', 'full', 'off'):
        byq[d['kin'][f]['s']] = byq.get(d['kin'][f]['s'], 0) + 1
print(f'{len(m["drugs"])} drugs carry kinetics')
print('field provenance:', {'label': byq.get('L', 0), 'from PK': byq.get('K', 0),
                            'class-typical': byq.get('C', 0)})
print('taper-required:', sorted(d['n'] for d in m['drugs'] if d['kin'].get('tap')))
print('payload bytes:', len(payload))
