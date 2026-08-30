"""Per-strength unit prices for single-ingredient ORAL antihypertensives,
from the CMS NADAC (National Average Drug Acquisition Cost) file."""
import json
import re
import pandas as pd

DRUGS = ['amiloride', 'amlodipine', 'atenolol', 'azilsartan', 'benazepril', 'betaxolol',
         'bisoprolol', 'candesartan', 'captopril', 'carvedilol', 'chlorthalidone', 'diltiazem',
         'enalapril', 'eplerenone', 'felodipine', 'fosinopril', 'furosemide',
         'hydrochlorothiazide', 'indapamide', 'irbesartan', 'isradipine', 'lisinopril',
         'losartan', 'metoprolol', 'nebivolol', 'nicardipine', 'nifedipine', 'nisoldipine',
         'olmesartan', 'perindopril', 'propranolol', 'quinapril', 'ramipril', 'spironolactone',
         'telmisartan', 'trandolapril', 'valsartan', 'verapamil']

NON_ORAL = re.compile(r'\b(VIAL|VL|INJ|SOLUTION|SOLN|SUSP|SYRINGE|IV|BOTTLE|CREAM|OPHTH|DROPS)\b')
SLASH_CONC = re.compile(r'MG\s*/')                    # "10 MG/ML" => liquid
DUAL = re.compile(r'\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?')  # "10-12.5" => combination
STRENGTH = re.compile(r'(\d+(?:\.\d+)?)\s*MG')
ER = re.compile(r'\b(ER|XL|SR|XR|LA|CD|CR|OSM)\b|24\s?HR|12\s?HR')


def classify(desc, drug):
    """Return (strength_mg, form) or None if this row is not a plain oral single-ingredient product."""
    d = desc.upper().replace(',', '')
    name = drug.upper()
    if not d.startswith(name):
        return None
    tail = d[len(name):]
    if tail[:1] == '-':                 # LISINOPRIL-HYDROCHLOROTHIAZIDE
        return None
    if NON_ORAL.search(d) or SLASH_CONC.search(d) or DUAL.search(d):
        return None
    if re.search(r'\bPM\b', d):      # bedtime chronotherapeutic formulation, a distinct product
        return None
    nums = STRENGTH.findall(d)
    if len(nums) != 1:
        return None
    salt = None
    for s in ('SUCCINATE', 'TARTRATE'):
        if s in d:
            salt = s
    form = 'ER' if ER.search(d) else 'IR'
    return float(nums[0]), (f'{salt}-{form}' if salt else form)


def main():
    df = pd.read_csv('nadac.csv', dtype=str)
    df['desc'] = df['NDC Description'].str.upper()
    df['price'] = pd.to_numeric(df['NADAC Per Unit'], errors='coerce')
    df = df[(df['Pricing Unit'] == 'EA') & df['price'].notna() & (df['OTC'] != 'Y')]

    out = {}
    for drug in DRUGS:
        sub = df[df['desc'].str.startswith(drug.upper())]
        buckets = {}
        for desc, price, cls in zip(sub['desc'], sub['price'], sub['Classification for Rate Setting']):
            c = classify(desc, drug)
            if c:
                kind = 'G' if str(cls).startswith('G') else 'B'
                buckets.setdefault(c[1], {}).setdefault(c[0], {}).setdefault(kind, []).append(price)
        entry = {}
        for form, by_strength in buckets.items():
            fe = {}
            for s, kinds in sorted(by_strength.items()):
                # Generic pricing when a generic exists; brand only as a fallback.
                use = kinds.get('G') or kinds.get('B')
                fe[str(s)] = {'p': round(sorted(use)[len(use) // 2], 5),
                              'g': 1 if kinds.get('G') else 0}
            entry[form] = fe
        out[drug] = entry
        flat = {f: {s: v['p'] for s, v in d.items()} for f, d in entry.items()}
        brandonly = [f'{f}{s}' for f, d in entry.items() for s, v in d.items() if not v['g']]
        print(f'{drug:<22} {json.dumps(flat)[:130]}  brand-only:{",".join(brandonly[:4]) or "-"}')
    json.dump(out, open('nadac_prices.json', 'w'), indent=1)
    missing = [d for d in DRUGS if not out[d]]
    print('\nno oral pricing found:', missing)


if __name__ == '__main__':
    main()
