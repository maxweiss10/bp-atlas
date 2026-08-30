"""AUDIT: re-validate the SHIPPED coefficients against the live source calculator.

Uses embed_v2.json (what the site actually runs on), a fresh randomised sample
including doses far outside the range the model was fitted on, and baselines away
from the 154/100 reference.
"""
import json
import math
import random
from itertools import permutations
from combo_probe import ComboApp, NAME2ATC
from harvest import parse_summary2

PAYLOAD = json.load(open('embed_v2.json'))
D = {d['n']: d for d in PAYLOAD['drugs']}
REF = {'sbp': 154, 'dbp': 100}


def tau_base(d, mg, k):
    f = d['fs'] if k == 'sbp' else d['fd']
    return f[0] + f[1] * math.log(mg / d['std'])


def eps_of(d, mg, k):
    f = d['fs'] if k == 'sbp' else d['fd']
    return f[2] + f[3] * math.log(mg / d['std'])


def predict(reg, baseline, k):
    ref = REF[k]
    tot, n = 0.0, 0
    for order in permutations(reg):
        used = t = 0.0
        for name, mg in order:
            d = D[name]
            v = tau_base(d, mg, k) + (baseline - used - ref) * eps_of(d, mg, k)
            t += v
            used += v
        tot += t
        n += 1
    return tot / n


def main():
    rnd = random.Random(20260830)
    us = [d for d in PAYLOAD['drugs'] if d['us'] and d['pr']]

    cases = []
    # monotherapy across every extrapolation tier
    for tier in (0, 1, 2):
        pool = [(d['n'], r['mg']) for d in us for r in d['rows'] if r['far'] == tier]
        for name, mg in rnd.sample(pool, min(12, len(pool))):
            cases.append({'reg': [[name, mg]], 'tier': tier,
                          'sbp': rnd.choice([130, 140, 154, 160, 175]),
                          'dbp': rnd.choice([80, 90, 100, 108])})
    # combinations
    for size in (2, 3):
        for _ in range(12):
            picked = rnd.sample(us, size)
            reg = [[d['n'], rnd.choice(d['rows'])['mg']] for d in picked]
            cases.append({'reg': reg, 'tier': 'combo%d' % size,
                          'sbp': rnd.choice([135, 145, 154, 165, 180]),
                          'dbp': rnd.choice([82, 92, 100, 105])})

    app = ComboApp()
    rows = []
    for i, c in enumerate(cases, 1):
        try:
            obs = app.query([(n, mg) for n, mg in c['reg']], c['sbp'], c['dbp'])
        except Exception as e:
            print(f'{i:>3} QUERY FAILED {c["reg"]}: {type(e).__name__}', flush=True)
            app.close()
            app_new = ComboApp()
            app.__dict__ = app_new.__dict__
            continue
        if not obs or obs.get('sbp') is None:
            print(f'{i:>3} NO RESULT {c["reg"]}', flush=True)
            continue
        ps = predict([(n, mg) for n, mg in c['reg']], c['sbp'], 'sbp')
        pd_ = predict([(n, mg) for n, mg in c['reg']], c['dbp'], 'dbp')
        rows.append({**c, 'app_sbp': obs['sbp'], 'app_dbp': obs['dbp'],
                     'mine_sbp': ps, 'mine_dbp': pd_,
                     'ds': ps - obs['sbp'], 'dd': pd_ - obs['dbp'],
                     'regimen': obs.get('regimen')})
        print(f'{i:>3} {str(c["tier"]):<7} {obs.get("regimen","")[:52]:<54} '
              f'base {c["sbp"]:>3} app {obs["sbp"]:>5.0f} mine {ps:>6.2f} d {ps-obs["sbp"]:>+5.2f}',
              flush=True)
    app.close()
    json.dump(rows, open('audit_model_results.json', 'w'), indent=1)

    def stats(sel, key_d, label):
        s = [r for r in rows if sel(r)]
        if not s:
            return
        e = [abs(r[key_d]) for r in s]
        print(f'{label:<26} n={len(s):>3}  MAE={sum(e)/len(e):.2f}  '
              f'max={max(e):.2f}  bias={sum(r[key_d] for r in s)/len(s):+.2f}  '
              f'within1={100*sum(1 for x in e if x <= 1)/len(s):.0f}%')

    print()
    stats(lambda r: True, 'ds', 'SBP overall')
    stats(lambda r: True, 'dd', 'DBP overall')
    for t in (0, 1, 2, 'combo2', 'combo3'):
        stats(lambda r, t=t: r['tier'] == t, 'ds', f'SBP tier {t}')


if __name__ == '__main__':
    main()
