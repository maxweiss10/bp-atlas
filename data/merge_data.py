"""Merge the efficacy model, US clinical dosing, NADAC cost, and adverse effects
into the single payload the artifact embeds."""
import json
from clinical import DOSING, NOT_US_PRACTICE, RARE_IN_PRACTICE, AE, SOURCES
from cost import monthly_cost

model = json.load(open('embed_data.json'))          # efficacy fits, per drug
out = []
extrapolated = 0
total_rows = 0

for d in model:
    name = d['n']
    us = name not in NOT_US_PRACTICE
    dose_info = DOSING.get(name)
    std = d['std']

    if dose_info:
        doses = dose_info['doses']
        form, freq, note = dose_info['form'], dose_info['freq'], dose_info['note']
    else:
        # Not used in US practice: fall back to the paper's own dose rungs.
        doses = [std / 2, std, std * 2]
        form, freq, note = None, None, None

    # Beyond 4x the trial standard dose the log-dose extrapolation stops being
    # defensible, so those rungs are dropped rather than shown with a caveat.
    doses = [mg for mg in doses if mg / std <= 4.0001]

    rows = []
    for mg in doses:
        ratio = mg / std
        beyond = ratio > 2.0001 or ratio < 0.4999
        c = monthly_cost(name, mg, form) if us else None
        obs = next((o for o in d['obs'] if abs(o[0] - mg) < 1e-9), None)
        rows.append({
            'mg': mg,
            'x': round(ratio, 3),                       # multiple of the trial standard dose
            'far': 1 if beyond else 0,                  # outside the studied 0.5-2x range
            'usd': c[0] if c else None,                 # $ per 30 days
            'reg': f'{c[2]:g} x {c[1]:g} mg' if c else None,
            'pi': [obs[2], obs[3]] if obs else None,    # published 95% prediction interval
        })
        total_rows += 1
        extrapolated += 1 if beyond else 0

    def dedupe(items):
        """Drop a generic class entry when a drug-specific one restates it with detail."""
        return [a for i, a in enumerate(items)
                if not any(j != i and b.lower().startswith(a.lower()) and len(b) > len(a)
                           for j, b in enumerate(items))]

    ae = AE.get(name)
    if ae:
        ae = dict(ae, common=dedupe(ae['common']), important=dedupe(ae['important']))
    out.append({
        'n': name, 'cls': d['cls'], 'clsf': d['clsf'], 'std': std,
        'tr': d['tr'], 'pt': d['pt'], 'us': 1 if us else 0,
        'pr': 0 if name in RARE_IN_PRACTICE else 1,
        'fs': d['fs'], 'fd': d['fd'],
        'freq': freq, 'note': note, 'form': form,
        'rows': rows,
        'ae': ({'c': ae['common'], 'i': ae['important'], 'm': ae['monitoring'],
                'cl': 1 if ae.get('cls') else 0} if ae else None),
    })

out.sort(key=lambda x: x['n'])
json.dump({'drugs': out, 'sources': SOURCES}, open('embed_v2.json', 'w'), separators=(',', ':'))

us_drugs = [x for x in out if x['us']]
print(f'{len(out)} drugs ({len(us_drugs)} US practice), {total_rows} drug-dose rows')
print(f'{extrapolated} rows beyond the studied 0.5-2x range')
print('US rows:', sum(len(x["rows"]) for x in us_drugs))
print('drugs missing adverse effects:', [x['n'] for x in us_drugs if not x['ae']])
print('rows missing cost:', [(x['n'], r['mg']) for x in us_drugs for r in x['rows'] if r['usd'] is None])
import os
print('bytes:', os.path.getsize('embed_v2.json'))
