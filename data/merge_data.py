"""Merge the efficacy model, US clinical dosing, NADAC cost, and adverse effects
into the single payload the artifact embeds."""
import json
from clinical import (DOSING, NOT_US_PRACTICE, RARE_IN_PRACTICE, AE, SOURCES,
                      CLASS_TEMPLATES, TEMPLATE_LABEL, TEMPLATE_OF)
from cost import monthly_cost
from patient import CLASS_TEXT, DRUG_TEXT, PROFILES

model = json.load(open('embed_data.json'))          # efficacy fits, per drug
SINGLE_PILL = json.load(open('single_pill.json'))   # fixed-dose combos on the US market
FORMULATIONS = json.load(open('formulations.json'))  # oral forms actually dispensable
_DIFF = json.load(open('differentiators.json'))       # researched within-class differentiators
DIFFERENTIATORS = _DIFF['diff']
DROP_EXISTING = _DIFF['dropExisting']                 # superseded by a better-sourced version

def freq_abbr(freq):
    """QD / BID / TID from the prose, ignoring any parenthetical about the form."""
    if not freq:
        return None
    base = freq.split('(')[0].strip()
    return {'once daily': 'QD', 'twice daily': 'BID', 'three times daily': 'TID',
            '2-3x daily': 'BID-TID', 'once-twice daily': 'QD-BID'}.get(base)
# Diuretics are dosed in the morning so the diuresis does not run overnight.
MORNING = {'hydrochlorothiazide', 'chlorthalidone', 'indapamide', 'furosemide',
           'spironolactone', 'eplerenone', 'amiloride'}


def patient_text(name, cls, sub):
    """Plain-language content for the handout: class text plus drug-specific lines."""
    key = ('CCB-DHP' if (cls == 'CCB' and sub == 'DHP')
           else 'CCB-nonDHP' if cls == 'CCB'
           else sub if sub in CLASS_TEXT else cls)
    base = CLASS_TEXT.get(key) or CLASS_TEXT.get(cls)
    if not base:
        return None
    ov = DRUG_TEXT.get(name, {})
    common = list(base['common']) + ov.get('add_common', [])
    # a drug-specific line that restates a class line, with numbers, wins
    common = [a for i, a in enumerate(common)
              if not any(j != i and a.lower().rstrip('.') in b.lower()
                         for j, b in enumerate(common))]
    return {'what': base['what'],
            'common': common,
            'call': list(base['call']),
            'rules': list(base['rules']) + ov.get('add_rules', [])}
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
        perday = dose_info.get('perday', 1)
    else:
        # Not used in US practice: fall back to the paper's own dose rungs.
        doses = [std / 2, std, std * 2]
        form, freq, note, perday = None, None, None, 1

    rows = []
    for mg in doses:
        ratio = mg / std
        # 0 = inside the 0.5-2x range the model was fitted on
        # 1 = a modest extrapolation along the log-dose curve
        # 2 = far outside it; a real prescribable dose, but the estimate is soft
        if 0.4999 <= ratio <= 2.0001:
            beyond = 0
        elif 0.2499 <= ratio <= 4.0001:
            beyond = 1
        else:
            beyond = 2
        c = monthly_cost(name, mg, form, perday) if us else None
        obs = next((o for o in d['obs'] if abs(o[0] - mg) < 1e-9), None)
        rows.append({
            'mg': mg,
            'x': round(ratio, 3),                       # multiple of the trial standard dose
            'far': beyond,                              # 0 inside / 1 near / 2 far outside studied range
            'usd': c[0] if c else None,                 # $ per 30 days
            'reg': f'{c[2]:g} x {c[1]:g} mg' if c else None,
            'pi': [obs[2], obs[3]] if obs else None,    # published 95% prediction interval
        })
        total_rows += 1
        extrapolated += 1 if beyond else 0
        far_out = 0

    def dedupe(items):
        """Drop a generic class entry when a drug-specific one restates it with detail."""
        return [a for i, a in enumerate(items)
                if not any(j != i and b.lower().startswith(a.lower()) and len(b) > len(a)
                           for j, b in enumerate(items))]

    clsf_l = d['clsf'].lower()
    if d['cls'] == 'CCB':
        sub = 'nonDHP' if 'non-dihydropyridine' in clsf_l else 'DHP'
    elif d['cls'] == 'Diuretic':
        sub = ('thiazide' if 'thiazide' in clsf_l else 'loop' if 'loop' in clsf_l
               else 'MRA' if 'mineralocorticoid' in clsf_l else 'kSparing')
    else:
        sub = d['cls']

    ae = AE.get(name)
    tmpl_key = TEMPLATE_OF.get(name)
    own_c, own_i = [], []
    if ae:
        ae = dict(ae, common=dedupe(ae['common']), important=dedupe(ae['important']))
        if tmpl_key:
            t = CLASS_TEMPLATES[tmpl_key]
            tc, ti = set(t['common']), set(t['important'])
            own_c = [x for x in ae['common'] if x not in tc]
            own_i = [x for x in ae['important'] if x not in ti]
        else:
            # no shared template, so everything this drug carries is its own
            own_c, own_i = list(ae['common']), list(ae['important'])
        dropped = set(DROP_EXISTING.get(name, []))
        own_c = [x for x in own_c if x not in dropped]
        own_i = [x for x in own_i if x not in dropped]
    out.append({
        'n': name, 'cls': d['cls'], 'clsf': d['clsf'], 'std': std,
        'tr': d['tr'], 'pt': d['pt'], 'us': 1 if us else 0,
        'pr': 0 if name in RARE_IN_PRACTICE else 1,
        'fs': d['fs'], 'fd': d['fd'],
        'freq': freq, 'note': note, 'form': form,
        'rows': rows,
        'ae': ({'c': ae['common'], 'i': ae['important'], 'm': ae['monitoring']} if ae else None),
        # within-class differentiators: curated (c/i) plus researched (d, with sources)
        'own': ({'c': own_c, 'i': own_i, 'd': DIFFERENTIATORS.get(name, [])} if ae else None),
        'tmpl': tmpl_key,
        'sub': sub,
        'abbr': freq_abbr(freq),
        'when': 'morning' if (name in MORNING or 'morning' in (freq or '')) else None,
        'forms': FORMULATIONS.get(name) if us else None,
        'pth': patient_text(name, d['cls'], sub) if us else None,
    })

out.sort(key=lambda x: x['n'])
class_ae = {k: {'label': TEMPLATE_LABEL[k], 'c': t['common'], 'i': t['important'],
                'm': t['monitoring']} for k, t in CLASS_TEMPLATES.items()}

json.dump({'drugs': out, 'sources': SOURCES, 'classAe': class_ae,
           'singlePill': sorted(SINGLE_PILL.keys()), 'profiles': PROFILES},
          open('embed_v2.json', 'w'), separators=(',', ':'))

us_drugs = [x for x in out if x['us']]
print(f'{len(out)} drugs ({len(us_drugs)} US practice), {total_rows} drug-dose rows')
print(f'{extrapolated} rows beyond the studied 0.5-2x range')
print('US rows:', sum(len(x["rows"]) for x in us_drugs))
print('drugs missing adverse effects:', [x['n'] for x in us_drugs if not x['ae']])
no_own = [x['n'] for x in us_drugs if x['pr'] and not (x['own'] and
          (x['own']['c'] or x['own']['i'] or x['own']['d']))]
print(f'drugs with NO within-class differentiator: {len(no_own)} -> {no_own}')
print('rows missing cost:', [(x['n'], r['mg']) for x in us_drugs for r in x['rows'] if r['usd'] is None])
import os
print('bytes:', os.path.getsize('embed_v2.json'))
