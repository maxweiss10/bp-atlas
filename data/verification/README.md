# Verification record — the inpatient layer

Five parallel research passes, run 21 September 2026, checking the White Book cardiology card
"Asx Markedly Elevated BP & HTN Emergency" line by line against primary sources. Every figure that
appears in the Inpatient & emergency tab traces to one of these files.

| File | Scope |
|---|---|
| `research-1-definitions.md` | Definitions, end-organ damage list, triage table, correction time course, the four cited papers, and the evidence base for treating asymptomatic inpatient hypertension |
| `research-2-conditions.md` | Condition-specific BP targets, each against its own specialty guideline, plus the conditions the card omits |
| `research-3-iv-drugs.md` | Parenteral agents — dosing, onset, offset, boxed warnings, from the FDA labels on DailyMed |
| `research-4-po-drugs.md` | Oral agents, same fields, plus the agents the card omits |
| `research-5-workflow.md` | Workup, measurement technique, the as-needed antihypertensive literature, drip-to-oral transition, discharge, and cost |

## What was found

28 individual figures were corrected. Most are not errors but age — the card predates the 2025
AHA/ACC hypertension guideline and the 2026 AHA/ASA stroke guideline, which between them rewrote
the intracerebral haemorrhage target, the aortic dissection heart rate, and the whole ischemic
stroke row.

A recurring pattern worth naming: **three of the card's timing figures are the label's peak or
recheck interval relabelled as onset.** Captopril's 30–90 minutes is the label's "maximal"; oral
labetalol's 20 minutes is the intravenous number; nifedipine's 20 minutes is the ACOG recheck
interval. Each error pushes the reader to wait too long before judging a dose, which is how doses
get stacked.

## Things deliberately not carried over

- The card's "MAP down 10–20% in the first hour, then 5–15%" appears in no guideline. It is a
  textbook convention, and the guideline figure is 20–25% in the first hour.
- "TIA" and "hematuria" as end-organ damage. Neither is in any cited source's list.
- Fenoldopam, which is still in the guideline tables but was discontinued in the US in 2023.

## Known verification debt

`ahajournals.org`, `jacc.org` and `nejm.org` all sit behind Cloudflare and refused automated
access, so the **2025 AHA/ACC guideline's exact recommendation wording** was corroborated across
several independent secondary renderings rather than read from the PDF. Its bibliographic record
was confirmed against PubMed. The class-of-recommendation and level-of-evidence designations in
particular are worth a check against the PDF through a library login before this is relied on in
any setting where the distinction matters.
