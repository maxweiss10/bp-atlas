"""Embed the inpatient layer in index.html as `const INPATIENT = {...};`.

The inpatient view is a closed compartment: it shares the page's CSS and its
table plumbing, but none of its data touches model.json and the efficacy model
never reads it.  Keeping it in its own file and its own embedded constant is
what makes that separation checkable.

Run from data/:  python3 build_inpatient.py
"""
import json, os, re, sys
from inpatient import INPATIENT

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, os.pardir, 'index.html')

payload = json.dumps(INPATIENT, separators=(',', ':'), ensure_ascii=False)
html = open(PAGE, encoding='utf-8').read()

line = f'const INPATIENT = {payload};'
if re.search(r'^const INPATIENT = \{.*\};$', html, flags=re.M):
    html = re.sub(r'^const INPATIENT = \{.*\};$', lambda _: line, html, count=1, flags=re.M)
else:
    anchor = 'const DRUGS = PAYLOAD.drugs;'
    if anchor not in html:
        sys.exit('could not find the anchor to insert INPATIENT after')
    html = html.replace(anchor, anchor + '\n' + line, 1)

open(PAGE, 'w', encoding='utf-8').write(html)

ag = INPATIENT['agents']
by_src = {}
for a in ag:
    by_src[a['src']] = by_src.get(a['src'], 0) + 1
print(f'{len(ag)} agents, {len(INPATIENT["conds"])} conditions')
print('provenance:', {'on the card, unchanged': by_src.get('wb', 0),
                      'on the card, corrected': by_src.get('fix', 0),
                      'added here': by_src.get('add', 0)})
print('corrections:', sum(len(a.get('fix', [])) for a in ag))
print('payload bytes:', len(payload))
