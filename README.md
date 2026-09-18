# Antihypertensive Potency Atlas

**Live: https://maxweiss10.github.io/bp-atlas**

Every antihypertensive in the published blood-pressure efficacy model, at every dose you would
actually prescribe, ranked side by side — with monthly cost and the adverse effects worth
mentioning. Plus a combination builder that applies the source paper's own permutation equations.

## What it does

- **Single drugs** — 128 real drug–dose rows across 37 US-marketed agents, sortable by systolic
  drop, diastolic drop, cost, weight of evidence, or how fast the drug turns on and off. Because
  the rows are real prescribing steps rather than multiples of a trial "standard dose", one drug at
  its maximum sits in the same ranking as another at its starting dose.
- **Onset and offset** — two columns for the question the mmHg figures cannot answer: how long
  before blood pressure starts to move, how long a fixed dose needs before the effect levels off,
  and how long the effect lasts once the drug is stopped.
- **Combinations** — every eligible pair or triple ranked by predicted effect, with same-class and
  ACEi+ARB combinations excluded by default and guideline first-line pairs flagged.
- **Build a regimen** — up to four drugs, live predicted BP, projected on-treatment BP, drug cost,
  interaction warnings, and number needed to treat from a baseline cardiovascular risk.
- Baseline BP is adjustable by slider or typed value; everything re-standardises live.

## Where the numbers come from

**Efficacy.** Wang N, Salam A, Pant R, et al. "Blood pressure-lowering efficacy of antihypertensive
drugs and their combinations: a systematic review and meta-analysis of randomised, double-blind,
placebo-controlled trials." *Lancet* 2025;406:915–25 — 484 trials, 104,176 participants, mean
baseline 154/100 mmHg. The paper's public calculator at [bpmodel.org](https://www.bpmodel.org)
answers one regimen at a time; this page holds the whole grid.

Each of 53 drugs was queried at half, standard, and double standard dose, along with the model's
own baseline-BP sweep. Per-drug coefficients (α, β, ε) were recovered by least squares from those
outputs — residual 0.27 mmHg, which is the source calculator's own integer rounding.

The combination model from the supplementary appendix (p. 14) was reimplemented and validated
against 44 live combination queries spanning 2- and 3-drug regimens at baselines from 140 to 170:

| | Systolic | Diastolic |
|---|---|---|
| Mean absolute error | 0.31 mmHg | 0.28 mmHg |
| Within 1 mmHg | 98% | 100% |
| Bias | −0.01 mmHg | +0.13 mmHg |

**Dosing.** FDA prescribing information via DailyMed, with marketed strengths from the RxNorm
prescribable set, as total mg per day for hypertension. Doses beyond 4× the trial standard dose are
dropped; those between 2× and 4× are marked as extrapolated.

**Onset and offset.** FDA prescribing information via openFDA/DailyMed, read from the Clinical
Pharmacology, Clinical Studies and Dosage sections of each drug's own single-ingredient label. Four
figures per drug: time to the first blood-pressure effect after one dose, time to that dose's peak
effect, time for a fixed dose to reach its full effect, and time for the effect to fade after
stopping. Every mmHg figure elsewhere on the page is a plateau figure — the source trials ran a
mean of 8.6 weeks — so these columns say how long you wait to get there.

Among the drugs in US practice, 46% of the individual figures are stated in that drug's own label;
the rest are inferred from its labelled pharmacokinetics, and the page marks which is which. The
agents in the efficacy model with no US label carry the class profile, marked separately again.

Offset is the weakest of the four. Only irbesartan (two-thirds of the effect still present a week
after the last dose), telmisartan (baseline over several days to one week) and eplerenone (+6/3
mmHg at one week) have a published withdrawal time course; every other offset is four to five
effective half-lives, which is when the drug has gone rather than when the blood pressure has
finished drifting back.

**Cost.** CMS National Average Drug Acquisition Cost (NADAC), file dated 26 August 2026. Median
generic price per unit for the cheapest whole-tablet regimen delivering the daily dose, × 30 days.
This is an acquisition benchmark, not what a patient pays.

**Adverse effects.** FDA prescribing information via DailyMed and the 2017/2025 ACC/AHA hypertension
guideline drug tables, plus Bangalore 2010 (ACE inhibitor cough), the FDA Drug Safety Communication
of July 2013 (olmesartan and sprue-like enteropathy), the FDA label change of August 2020
(hydrochlorothiazide and non-melanoma skin cancer), and the Diuretic Comparison Project, NEJM 2022.

A few entries deliberately correct common teaching:

- ACE inhibitor cough is the pooled ~11%, not the label's understated figure; label rates span
  0.5–35% purely by trial design and are not comparable across drugs.
- Urate-lowering is specific to **losartan** and is not an ARB class effect.
- Beta blockers carry the abrupt-withdrawal warning as an ordinary warning, **not** a boxed one —
  verified across all seven labels.
- Eplerenone's reputation for causing less gynecomastia than spironolactone is **not** supported by
  its label, which reports no rate and makes no comparison.
- The 2025 guideline **dropped** its preference for chlorthalidone over hydrochlorothiazide.

## Repository layout

```
index.html        the whole tool, self-contained, no build step
data/model.json   per-drug coefficients, doses, costs, adverse effects, kinetics
data/*.py         the pipeline that produced it
```

`data/shiny_client.py` speaks the Shiny websocket protocol to the source calculator;
`harvest.py` walks the dose grid; `prices.py` extracts NADAC pricing; `clinical.py` holds the
dosing and adverse-effect layer; `kinetics.py` the onset/offset layer, with the label sentence
behind each figure; `merge_data.py` assembles `model.json`, and `add_kinetics.py` folds the
kinetics layer into it and re-embeds the payload in `index.html`.

## Limits

Population means from short-term trials (mean follow-up 8.6 weeks), outcome is clinic blood
pressure, and the trial population averaged 54 years old at 154/100. Individual response varies
widely around these averages. Nothing here accounts for tolerability, adherence, pregnancy safety,
renal dosing, or outcome data.

**Not a prescribing tool and not clinical advice.** Verify dosing, interactions, and suitability
against current guidelines and a formulary before any clinical use.
