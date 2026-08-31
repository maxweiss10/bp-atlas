"""Which oral formulations of each drug actually exist in the US market.

Derived from NADAC product descriptions rather than asserted, so the list
reflects what is dispensable now. Not every formulation was studied in the
trials the efficacy model is built on - it is a prescribing aid, not a claim
about the evidence.
"""
import json
import re
import pandas as pd

DRUGS = json.load(open('drugs.json'))
NAMES = [d['name'] for d in DRUGS]

# Longest-first so "ER 24HR" wins over a bare "ER".
FORMS = [
    (r'\b24\s?HR\s?ER\b|\bER\s?24\s?HR\b|\b24HR\b', 'ER 24h'),
    (r'\b12\s?HR\b', 'ER 12h'),
    (r'\bXL\b', 'XL'), (r'\bXR\b', 'XR'), (r'\bSR\b', 'SR'),
    (r'\bLA\b', 'LA'), (r'\bCD\b', 'CD'), (r'\bCR\b', 'CR'),
    (r'\bER\b', 'ER'), (r'\bOSM\b', 'ER osmotic'),
    (r'\bODT\b', 'ODT'),
]
SALTS = [(r'\bSUCCINATE\b', 'succinate'), (r'\bTARTRATE\b', 'tartrate'),
         (r'\bFUMARATE\b', 'fumarate'), (r'\bMESYLATE\b', 'mesylate'),
         (r'\bMALEATE\b', 'maleate'), (r'\bPOTASSIUM\b', 'potassium'),
         (r'\bHCL\b', 'HCl'), (r'\bHYDROCHLOROTHIAZIDE\b', None)]
KIND = [(r'\bCAP', 'capsule'), (r'\bTAB', 'tablet')]
NON_ORAL = re.compile(r'\b(VIAL|VL|INJ|SOLUTION|SOLN|SUSP|SYRINGE|IV|CREAM|OPHTH|DROPS)\b')
DUAL = re.compile(r'\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?')

df = pd.read_csv('nadac.csv', dtype=str)
df['d'] = df['NDC Description'].str.upper()

out = {}
for name in NAMES:
    sub = df[df['d'].str.startswith(name.upper())]
    if sub.empty:
        continue
    seen = {}
    for desc in sub['d'].drop_duplicates():
        if NON_ORAL.search(desc) or DUAL.search(desc) or re.search(r'MG\s*/', desc):
            continue
        if desc[len(name):len(name) + 1] == '-':      # combination product
            continue
        form = 'IR'
        for pat, label in FORMS:
            if re.search(pat, desc):
                form = label
                break
        salt = None
        for pat, label in SALTS:
            if label and re.search(pat, desc):
                salt = label
                break
        kind = None
        for pat, label in KIND:
            if re.search(pat, desc):
                kind = label
                break
        key = (salt, form)
        rec = seen.setdefault(key, {'salt': salt, 'form': form, 'kinds': set(), 'strengths': set()})
        if kind:
            rec['kinds'].add(kind)
        for s in re.findall(r'(\d+(?:\.\d+)?)\s*MG', desc):
            rec['strengths'].add(float(s))
    if not seen:
        continue
    rows = []
    for rec in seen.values():
        rows.append({
            'salt': rec['salt'], 'form': rec['form'],
            'kind': '/'.join(sorted(rec['kinds'])) or None,
            'strengths': sorted(rec['strengths']),
        })
    # IR first, then by name
    rows.sort(key=lambda r: (r['form'] != 'IR', r['form'], r['salt'] or ''))
    out[name] = rows

json.dump(out, open('formulations.json', 'w'), indent=1)
print(f'{len(out)} drugs with formulation data\n')
for n in ['metoprolol', 'verapamil', 'diltiazem', 'nifedipine', 'propranolol', 'amlodipine', 'carvedilol']:
    print(n)
    for r in out.get(n, []):
        lbl = ' '.join(x for x in [r['salt'], r['form'], r['kind']] if x)
        print(f'   {lbl:<34} {r["strengths"]}')
