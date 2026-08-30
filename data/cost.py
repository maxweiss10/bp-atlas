"""Monthly cost for a given total daily dose, from NADAC per-unit prices.

Picks the cheapest way to deliver the dose with a single tablet strength at a
plausible tablets-per-day count.
"""
import json

PRICES = json.load(open('nadac_prices.json'))


def monthly_cost(drug, daily_mg, form_pref=None):
    """Return (usd_per_30d, strength_mg, tabs_per_day) or None."""
    forms = PRICES.get(drug) or {}
    if not forms:
        return None
    order = []
    if form_pref and form_pref in forms:
        order.append(form_pref)
    # metoprolol succinate ER is keyed plainly as ER; tartrate is TARTRATE-IR
    for f in ('ER', 'IR', 'TARTRATE-IR', 'SUCCINATE-ER'):
        if f in forms and f not in order:
            order.append(f)
    # Prefer whole tablets in the clinically-used form; only split if nothing else fits.
    for n in (1, 2, 3, 4, 0.5):
        for f in order:
            best = None
            for s_str, rec in forms[f].items():
                s = float(s_str)
                price = rec['p'] if isinstance(rec, dict) else rec
                if abs(s * n - daily_mg) < 1e-6:
                    cost = price * n * 30
                    if best is None or cost < best[0]:
                        best = (round(cost, 2), s, n, f)
            if best:
                return best
    return None


if __name__ == '__main__':
    tests = [('lisinopril', 40), ('lisinopril', 10), ('amlodipine', 10), ('chlorthalidone', 12.5),
             ('hydrochlorothiazide', 25), ('losartan', 100), ('azilsartan', 80),
             ('metoprolol', 100), ('carvedilol', 25), ('nisoldipine', 34), ('spironolactone', 25),
             ('nebivolol', 5), ('valsartan', 320), ('diltiazem', 240), ('verapamil', 240)]
    for d, mg in tests:
        r = monthly_cost(d, mg)
        print(f'{d:<22}{mg:>7} mg/d  ->  {r}')
