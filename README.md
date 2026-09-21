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
- **One line per row.** Every row in the drug and combination tables is a single line, so a screen
  holds three times what it used to. Where a cell held a list — contraindications, indications — the
  column shows the first entry and a count, and the full list is in the open row.
- **Δ SBP carries its own magnitude.** The bar column is gone; the number is coloured on a
  five-step sequential ramp, one hue, light to dark, cut at the quintiles of the real dose grid.
  Every step clears 4.5:1 body-text contrast on white and the lightness is strictly monotonic,
  which is what a sequential ramp has to satisfy. Weight rises with it as a second channel, so the
  scale survives greyscale printing and colour-vision deficiency.
- **Onset / Full effect / Wears off** — three columns for the question the mmHg figures cannot
  answer: when blood pressure first moves after a dose (with that dose's peak beneath it), how long
  a fixed dose needs before the effect levels off, and how long the effect lasts once the drug is
  stopped. Each column holds one figure and sorts on it, so reading down a column and sorting it
  give the same order.
- **Combinations** — every eligible pair or triple ranked by predicted effect, with same-class and
  ACEi+ARB combinations excluded by default and guideline first-line pairs flagged.
- **Build a regimen** — up to four drugs, live predicted BP, projected on-treatment BP, drug cost,
  interaction warnings, and number needed to treat from a baseline cardiovascular risk.
- Baseline BP is adjustable by slider or typed value; everything re-standardises live.
- **Inpatient & emergency** — a self-contained fourth view for hypertensive emergency and severe
  inpatient hypertension, reproducing a White Book cardiology card and checking every line of it
  against the primary sources. Definitions, 17 situations with their own BP targets, and 29
  agents with onset, offset, dosing, indications and how finely each can be
  steered. Nothing here touches the efficacy model, and the model never reads it.

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

**Full effect and wear-off.** FDA prescribing information via openFDA/DailyMed, read from the
Clinical Pharmacology, Clinical Studies and Dosage sections of each drug's own single-ingredient
label. Four figures per drug: time to the first blood-pressure effect after one dose, time to that
dose's peak effect, time for a fixed dose to reach its full effect, and time for the effect to fade
after stopping. Three of the four get a column; the peak sits under the onset figure, and the
expanded row carries all four with the label sentence behind each. Every mmHg figure elsewhere on the page is a plateau figure — the source trials ran a
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

The **Difference** column carries a short label — "More ↓K", "Sprue-like enteropathy", "Less
constipation than verapamil" — with a count chip for how many findings sit behind it. The sentences
are in the open row, which is where they were always duplicated to.

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

## The inpatient layer

The fourth tab is a closed compartment. The Wang model is built from chronic oral monotherapy
trials and has no coefficient for a titrated infusion, so there is no mmHg column there: putting an
esmolol drip in the same ranking as amlodipine 5 mg would imply a comparison that does not exist.
What it carries instead are the columns that decide an inpatient choice — onset, offset, and how
finely the agent can be steered.

It is written in ward shorthand: arrows, standard abbreviations, no articles and no sentence a
physician could have finished themselves. "Extravasation causes necrosis and blistering — large
vein, never a butterfly" becomes "Extrav→necrosis/blisters; lg vein only." The same pass ran over
the outpatient drug text via `data/abbrev.py`, which keeps the substitution list reviewable. The
**How it works** tab is deliberately exempt — it is the provenance record and has to stay
readable.

**Every agent carries a use tier**, and the table sorts on it first, so a floor BP question does
not mean scrolling past phentolamine to find labetalol:

| Tier | Meaning | n |
|---|---|---|
| first reach | the default answer for an ordinary inpatient BP problem | 13 |
| specific | right only for the situation named beside it | 14 |
| know only | listed to be recognised and declined, not given | 2 |

A segmented control filters to one tier, and each specific agent states its trigger in the same
cell, so "catecholamine excess" sits next to phentolamine rather than three columns away.

Every agent and every condition also carries a provenance mark, so the reader can see what moved:

| Mark | Meaning |
|---|---|
| `WB` | on the White Book card, checked against the primary source, unchanged |
| `WB ✎` | on the card, but at least one figure is corrected here — the row holds the original |
| `+` | not on the card, added here |

Of 29 agents, 1 is unchanged, 15 carry a correction and 13 are additions; of 17 condition rows, all six
that appear on the card needed a change and eleven are new. The first four are shaded and ruled
off, because they are the situations you are in most of the time: **severe asymptomatic
hypertension**, where the answer is usually to treat nothing; **pre-procedure** and **discharge**,
the two where someone else wants the number lower; and **hypertensive emergency with no specific
organ target**, the gradual-lowering rule every row beneath it departs from.

The two pressure rows carry the evidence you would need to hold the line. The perioperative
guideline's 180/110 is COR 2b, "may be considered", and requires elective *elevated-risk* surgery
plus a *recent history* of poor control documented *before the day of surgery* — a one-off reading
in the pre-op bay meets none of it. No society sets any threshold at all for endoscopy,
catheterisation or interventional radiology. And a systematic review of 14 guidelines across 11
countries found none setting an inpatient BP goal or a discharge threshold, which makes the local
"not above 180" rule institutional rather than clinical. **28 individual figures were corrected.**
Most of that is not error but age: the card predates the
[2025 AHA/ACC hypertension guideline](https://doi.org/10.1161/HYP.0000000000000249) (August 2025,
which retired the 2017 one and renamed hypertensive urgency "severe hypertension") and the
[2026 AHA/ASA acute ischemic stroke guideline](https://doi.org/10.1161/STR.0000000000000513)
(February 2026), and those two rewrote the intracerebral haemorrhage target, the aortic dissection
heart rate, and the whole of the ischemic stroke row.

The corrections that change what you would actually do:

- **Intracerebral haemorrhage** — entry band is 150–220, not 180–220; target is 130 to <140 held for
  seven days, not 140–160; and SBP <130 is Class 3: Harm, which the card has no floor for.
- **Ischemic stroke** — 220/120 is a treatment *threshold*, not a target. The post-thrombolysis
  <180/105 window and the Class 3: Harm rule against SBP <140 after successful thrombectomy are
  both absent from the card.
- **Aortic dissection** — heart rate 60–80, which is the 2022 target; <60 is the 2010 one.
- **Asymptomatic severe hypertension** — the card suggests captopril or labetalol. The 2025
  guideline makes intermittent IV *or oral* dosing for the number alone a Class 3: Harm
  recommendation, and the hospital-medicine paper the card itself cites says the same.
- **Captopril onset** — the card's 30–90 minutes is the label's *peak*; onset is 15–30 minutes.
  The same error pattern appears in oral labetalol (20 minutes is the IV figure) and amlodipine
  (24–48 hours is not in the label at all).
- **Routes.** Several agents can be given more than one way, and the way decides where. Nicardipine
  can be pushed and runs on a monitored floor, not only in an ICU. Hydralazine is push *or* IM and
  must never be an infusion. Labetalol has no IM route at all. Each row now names the alternatives
  and what the *label* asks for by way of monitoring, which is usually less than local policy: of
  the parenteral agents here, only nitroprusside's label mentions an arterial line, and only as a
  preference.
- **Nitroprusside** — an earlier version of this page "corrected" the card's ten-minute limit at the
  maximum rate. That was wrong and has been retracted. Two labels are currently marketed and they
  differ: the older-format one (Mylan, revised April 2026) carries the ten-minute rule in its boxed
  warning, and Nipride RTU instead says the cyanide buffer is exhausted in under an hour. The card
  quotes the first. Neither is legacy.
- **Nifedipine** — the immediate-release label says in those words that it "should not be used for
  the acute reduction of blood pressure." It is first-line in pregnancy and the wrong answer
  everywhere else, and the card gives the indication without the counter-warning.

Agents added because the card has no equivalent: **phentolamine** (it had no agent at all for
catecholamine excess), metoprolol IV and PO, diltiazem IV and ER, furosemide IV, enalaprilat,
carvedilol, losartan, chlorthalidone, spironolactone, nifedipine ER, and **clonidine as a hazard
entry** rather than a treatment one. Fenoldopam is deliberately absent: it is still in the guideline
tables but was discontinued in the US in 2023.

Every citation chip is a direct link to a specific FDA label on DailyMed, resolved through its API
and checked to return the right product — not a search URL, which is what the first version shipped
and why several of them came up empty. DailyMed rather than a subscription reference because it is
the actual label, it is free, and the link works for anyone the page is shared with.

Sources: the FDA prescribing information on DailyMed for every dosing, onset and offset figure; the
2024 AHA acute-care scientific statement (*Hypertension* 2024;81:e94, Bress et al) and the 2025 and
2026 guidelines above for the targets; ACOG Practice Bulletin 222 for pregnancy; and the named
trials behind each claim — COMMIT, ATACH-2, INTERACT2/3, ENCHANTED2/MT, OPTIMAL-BP, CLICK,
PATHWAY-2, A-HeFT.

## Design

Set like the MGH housestaff manual, matching the White Book treatment already used on
[Pearl](https://maxweiss10.github.io/pearls) so the two sites read as one system: Arial Narrow in
the data zone, a flat `#D9D9D9` small-caps band over every section, black header rows with white
type, hairline grids, and the manual's own blue for citations. No shadows, no rounded corners, no
dark mode — the manual is paper.

The palette is sampled from the book itself, plus Pearl's category inks:

| Token | Value | Use |
|---|---|---|
| band | `#D9D9D9` | the strip behind every section header |
| rule / rule-2 | `#000000` / `#B4B4B4` | table edges and the inner grid |
| link | `#0432FF` | citations, underlined |
| accent | `#1F6B45` | indications |
| warn | `#A61B1B` | contraindications and "avoid" |
| caution | `#8A5A12` | a figure corrected against its source |

Two deliberate departures from a literal copy. The drug-class marks keep distinct hues, because
eleven classes cannot be told apart in one colour — each also carries a distinct shape and a
letter abbreviation, so the class survives greyscale printing and colour-vision deficiency. And
the equation blocks keep a real monospace, because a condensed face will not align them.

## Repository layout

```
index.html          the whole tool, self-contained, no build step
data/model.json     per-drug coefficients, doses, costs, adverse effects, kinetics
data/ip_*.py        the inpatient layer: text, conditions, parenteral and oral agents
data/abbrev.py      the ward-shorthand substitution list, applied to the outpatient text
data/embed_model.py re-embeds model.json in the page without touching the kinetics layer
data/*.py           the pipeline that produced it
```

`data/shiny_client.py` speaks the Shiny websocket protocol to the source calculator;
`harvest.py` walks the dose grid; `prices.py` extracts NADAC pricing; `clinical.py` holds the
dosing and adverse-effect layer; `kinetics.py` the onset/wear-off layer, with the label sentence
behind each figure and the sort value parsed back off the string the column prints; `merge_data.py` assembles `model.json`, and `add_kinetics.py` folds the
kinetics layer into it and re-embeds the payload in `index.html`. The inpatient layer is separate
all the way down: `ip_text.py`, `ip_conds.py`, `ip_agents_iv.py` and `ip_agents_po.py` hold the
data, `inpatient.py` assembles it, and `build_inpatient.py` embeds it as its own constant.

## Limits

Population means from short-term trials (mean follow-up 8.6 weeks), outcome is clinic blood
pressure, and the trial population averaged 54 years old at 154/100. Individual response varies
widely around these averages. Nothing here accounts for tolerability, adherence, pregnancy safety,
renal dosing, or outcome data.

**Not a prescribing tool and not clinical advice.** Verify dosing, interactions, and suitability
against current guidelines and a formulary before any clinical use.
