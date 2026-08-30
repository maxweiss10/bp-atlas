"""Local implementation of the appendix's permutation combination model."""
import json
import math
from itertools import permutations

DRUGS = {d["name"]: d for d in json.load(open("drugs_model.json"))}
REF = {"sbp": 154, "dbp": 100}


def tau_base(drug, dose_mg, kind):
    """Effect of one drug at the reference baseline (appendix step 1)."""
    f = drug["fit"][kind]
    ld = math.log(dose_mg / drug["std_dose"])
    return f["alpha"] + f["beta"] * ld


def eps_of(drug, dose_mg, kind):
    """Baseline effect modifier, scaled by dose."""
    f = drug["fit"][kind]
    ld = math.log(dose_mg / drug["std_dose"])
    return f["eps"] + f["eps_dose"] * ld


def predict(regimen, baseline, kind="sbp"):
    """regimen: [(drug_name, dose_mg), ...]; returns mean over all orderings."""
    ref = REF[kind]
    items = [(DRUGS[n], d) for n, d in regimen]
    totals = []
    for order in permutations(items):
        used = 0.0
        total = 0.0
        for drug, dose in order:
            t = tau_base(drug, dose, kind) + (baseline - used - ref) * eps_of(drug, dose, kind)
            total += t
            used += t
        totals.append(total)
    return sum(totals) / len(totals)


if __name__ == "__main__":
    obs = json.load(open("combo_observed.json"))
    errs_s, errs_d = [], []
    print(f'{"regimen":<52} {"base":>5} {"app":>5} {"mine":>6} {"diff":>6}')
    for c in obs:
        o = c.get("observed")
        if not o:
            continue
        reg = [(d[0], d[1]) for d in c["drugs"]]
        ps = predict(reg, c["sbp"], "sbp")
        pd_ = predict(reg, c["dbp"], "dbp")
        ds = ps - o["sbp"]
        errs_s.append(ds)
        if o.get("dbp") is not None:
            errs_d.append(pd_ - o["dbp"])
        label = " + ".join(f"{n} {d}" for n, d in reg)
        print(f"{label:<52} {c['sbp']:>5} {o['sbp']:>5.0f} {ps:>6.2f} {ds:>+6.2f}")
    n = len(errs_s)
    mae_s = sum(abs(e) for e in errs_s) / n
    bias_s = sum(errs_s) / n
    within1 = sum(1 for e in errs_s if abs(e) <= 1.0) / n
    print(f"\nSBP: n={n}  MAE={mae_s:.2f}  bias={bias_s:+.2f}  within 1 mmHg={within1*100:.0f}%")
    if errs_d:
        m = len(errs_d)
        print(f"DBP: n={m}  MAE={sum(abs(e) for e in errs_d)/m:.2f}  "
              f"bias={sum(errs_d)/m:+.2f}  "
              f"within 1={sum(1 for e in errs_d if abs(e)<=1)/m*100:.0f}%")
