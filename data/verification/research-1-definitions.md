# Verification Report — Header Block, Table 1, and Citations

Card: "Cardiology — Asx Markedly Elevated BP & HTN Emergency"
Scope verified: header definitions, end-organ damage list, "Assess" line, TABLE 1, all four citations.
Date of verification: 2026-09-21. Verifier: research subagent.

Primary sources obtained in full text (PDF extracted locally):
- Bress et al., *Hypertension* 2024;81:e94–e106 (full text)
- Peixoto, *NEJM* 2019;381:1843–1852 (full text)
- Breu & Axon, *J Hosp Med* 2018;13:860–862 (full text)
- Rastogi et al., *JAMA Intern Med* 2021;181:345–352 (abstract + PMC full text)

Source NOT directly retrievable: the 2025 AHA/ACC guideline primary PDF (ahajournals.org, jacc.org, and nejm.org all sit behind Cloudflare and returned HTTP 403 to every fetch attempt). Its bibliographic record was confirmed against PubMed/Europe PMC; its *recommendation wording* was verified against a structured guideline summary (Guideline Central) plus three independent secondary syntheses that agree with each other. Those items are flagged **[2025 text via secondary sources]** below.

---

## 1. CITATION CHECK

### 1a. "NEJM 2019;381:1843" — **CONFIRMED**

**Peixoto AJ. Acute Severe Hypertension. N Engl J Med. 2019;381(19):1843–1852.**
DOI: 10.1056/NEJMcp1901117 · PMID 31693807 · single author, Aldo J. Peixoto, MD (Yale, Section of Nephrology).
- https://doi.org/10.1056/NEJMcp1901117
- https://pubmed.ncbi.nlm.nih.gov/31693807/
- Full text read from an open mirror: https://www.sahta.com/documentos/ceYm9kpHq03AKwUqea0LAZBuMluuiej0iODUbbGxUTk.pdf

**Does it support the attached claim?** The card cites it for "see Outpatient CV Health for workup." Yes — the article has a dedicated "Determination of Precipitating Factors" section that is exactly the card's "Assess" content. Peixoto (NEJM 2019) writes that nonadherence to prescribed antihypertensives "is the most common precipitating factor." The same paragraph names, for hospitalized patients specifically, mobilization of infused IV fluids, withholding of antihypertensive medications, pain, and urinary retention as common precipitants, and elsewhere lists dietary sodium, cocaine/amphetamines/sympathomimetics, NSAIDs, high-dose glucocorticoids, and anxiety or panic. It also directs work-up for secondary causes (renovascular disease, primary aldosteronism, glucocorticoid excess, pheochromocytoma, coarctation) when no precipitant is found.

It is a *Clinical Practice* review, not a guideline — worth knowing if the card implies guideline authority.

### 1b. "Hypertension 2024;81:e94" — **CONFIRMED** (your identification was right, including the page)

**Bress AP, Anderson TS, Flack JM, Ghazi L, Hall ME, Laffer CL, Still CH, Taler SJ, Zachrison KS, Chang TI; on behalf of the AHA Council on Hypertension; Council on Cardiovascular and Stroke Nursing; and Council on Clinical Cardiology. The Management of Elevated Blood Pressure in the Acute Care Setting: A Scientific Statement From the American Heart Association. Hypertension. 2024;81(8):e94–e106.**
DOI: 10.1161/HYP.0000000000000238 · PMID 38804130 · Epub 2024 May 28.
- Title: exact, as you guessed.
- First author / Chair: **Adam P. Bress, PharmD, MS** (Chair). Vice Chair: Tara I. Chang, MD, MS.
- Page e94: **correct**; full range e94–e106.
- https://www.ahajournals.org/doi/10.1161/HYP.0000000000000238
- https://pubmed.ncbi.nlm.nih.gov/38804130/

**Does it support the attached claims?** Yes, for the header definitions and for the Table 1 "Asx: floor vs outpatient" and "avoid IV" rows. The statement's Table 3 ("Ten Key Implications for Clinical Practice") states that use of IV antihypertensives "is not supported by the evidence in the absence of hypertensive emergency" (Bress et al., *Hypertension* 2024) and that the threshold to initiate or intensify antihypertensives for asymptomatic elevated inpatient BP should be high. It also advises against PRN antihypertensive orders for asymptomatic elevated inpatient BP.

### 1c. "Journal of Hospital Medicine 2018;13:860" — **CONFIRMED, with a title correction**

**Breu AC, Axon RN. Things We Do for No Reason: Acute Treatment of Hypertensive Urgency. J Hosp Med. 2018;13(12):860–862.**
DOI: 10.12788/jhm.3086 · PMID 30379139 · published online first 31 Oct 2018.
Authors: Anthony C. Breu, MD (VA Boston Healthcare System / Harvard Medical School); R. Neal Axon, MD, MSCR (Ralph H. Johnson VAMC / Medical University of South Carolina).
Series banner on the printed page: "Choosing Wisely: Things We Do for No Reason."
- https://doi.org/10.12788/jhm.3086
- Free full text: https://cdn.mdedge.com/files/s3fs-public/issues/articles/jhm013120860.pdf

**Correction to note:** the card labels Table 1 "Asymptomatic Markedly Elevated BP (JHM 2018;13:860)". The 2018 article is titled with the *old* term ("Hypertensive Urgency"), and internally defines hypertensive emergency as **SBP ≥180 and/or DBP ≥120** — i.e. a different diastolic cut-point from the card's 110–120. If the card is going to carry the new AHA terminology, this citation should be flagged as pre-dating it.

**Does it support the attached claims?** Yes for most of the Table 1 "Asx" column — and **it contradicts one of them**. Breu & Axon's explicit recommendation is: "Do not administer intravenous or immediate-acting oral antihypertensive medications" (Breu & Axon, *J Hosp Med* 2018). Captopril is an immediate-acting oral agent, and the paper explicitly lists ACE inhibitors (captopril named) among drug classes implicated in treatment-related adverse events. See §7, item C.
Also supported by this paper: search for treatable causes (pain, nausea, withdrawal syndromes, held home meds, OSA, delirium); allow ≥30 min rest and re-measure (32% of ED patients responded to rest alone in one study; a randomised trial found rest ≈ telmisartan, 68.5% vs 69.1% reaching the MAP endpoint); modify the chronic oral regimen rather than acutely lowering; arrange early post-discharge follow-up.

### 1d. "JAMA Internal Medicine 2021;181:345-352" — **CONFIRMED**

**Rastogi R, Sheehan MM, Hu B, Shaker V, Kojima L, Rothberg MB. Treatment and Outcomes of Inpatient Hypertension Among Adults With Noncardiac Admissions. JAMA Intern Med. 2021;181(3):345–352.**
DOI: 10.1001/jamainternmed.2020.7501 · PMID 33369614 · PMC7770615 · (online Dec 2020).
- https://doi.org/10.1001/jamainternmed.2020.7501
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7770615/

**Does it support the attached claim?** The card says: "If hospitalized for non-cardiac reason, worse outcomes w/ intensifying anti-HTN during admission (JAMA IM 2021;181:345-352)." **Yes, directly.** The authors conclude that intensification of therapy without signs of end-organ damage "was associated with worse outcomes" (Rastogi et al., *JAMA Intern Med* 2021). Numbers in §6 below.

---

## 2. TERMINOLOGY — the 2025 guideline

### Exact citation (verified against PubMed and Europe PMC)

**Writing Committee Members; Jones DW, Ferdinand KC, Taler SJ, Johnson HM, Shimbo D, Abdalla M, Altieri MM, Bansal N, Bello NA, Bress AP, Carter J, Cohen JB, Collins KJ, Commodore-Mensah Y, Davis LL, Egan B, Khan SS, Lloyd-Jones DM, Melnyk BM, Mistry EA, Ogunniyi MO, Schott SL, Smith SC Jr, Talbot AW, Vongpatanasin W, Watson KE, Whelton PK, Williamson JD. 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the Prevention, Detection, Evaluation and Management of High Blood Pressure in Adults: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. Hypertension. 2025;82(10):e212–e316.**
DOI: 10.1161/HYP.0000000000000249 · PMID **40811516** · Epub **2025 Aug 14**.
Chair: Daniel W. Jones, MD. Vice Chairs: Keith C. Ferdinand, MD; Sandra J. Taler, MD.
Co-published: *Circulation*. 2025;152(11):e114–e218, doi:10.1161/CIR.0000000000001356; *J Am Coll Cardiol*. 2025;86(18):1567–1678, doi:10.1016/j.jacc.2025.05.007 (PMID 40815242).
Errata exist: *Hypertension* 2025;82(12):e350; 2026;83(5):e000262; 2026;83(6):e00264.
Note: the guideline **retires and replaces the 2017 ACC/AHA guideline** (stated in its own AIM section).
- https://www.ahajournals.org/doi/10.1161/HYP.0000000000000249
- https://pubmed.ncbi.nlm.nih.gov/40811516/

Note: there is no "AASK" society in the acronym string — the correct expansion is AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/**SGIM**.

### What it calls these entities  **[2025 text via secondary sources]**

- **"Hypertensive urgency" is retired and replaced by "severe hypertension"** — BP >180/120 mm Hg **without** acute target organ damage.
- **"Hypertensive emergency"** — BP >180 and/or >120 mm Hg **with** evidence of acute target organ damage.
- This is a *further* step beyond the 2024 acute-care statement, which had proposed "asymptomatic markedly elevated BP." The two are not identical: 2024 = "asymptomatic markedly elevated BP," 2025 = "severe hypertension."
- Sources: Guideline Central structured summary https://www.guidelinecentral.com/guideline/6962/ ; Brown C, Clark D III, Jones DW. Updates in the 2025 AHA/ACC Hypertension Guideline. *Curr Hypertens Rep.* 2026;28(1):19, https://pmc.ncbi.nlm.nih.gov/articles/PMC12995957/ ; NephJC http://www.nephjc.com/news/accaha2025-klno3 ; EM Mastery synthesis https://emmastery.academy/2025-hypertension-guidelines-updates-for-emergency-care/

### What it changes on this card  **[2025 text via secondary sources]**

1. **A new Class 3: Harm recommendation directly on point for Table 1.** For adults with severe hypertension (>180/120) hospitalized for **noncardiac** conditions **without** acute target organ damage, intermittent use of additional **intravenous *or oral*** antihypertensive medications is **not recommended** to acutely reduce BP. **COR 3: Harm, LOE B-NR** (Recommendation 6.2.4 in the Guideline Central rendering). This is the single most important addition for this card — the card currently gives an affirmative PO regimen for that exact scenario.
2. **ICU admission for hypertensive emergency is now a Class 1 (LOE B-R) recommendation** for continuous monitoring (Rec 6.2.1) — stronger than the card's "Floor vs ICU."
3. **Severe hypertension without TOD should be evaluated and treated in the outpatient setting**, with initiation/reinstitution/intensification of *oral* antihypertensives "in a timely manner." Patients should not be referred to the ED for asymptomatic severe BP elevation alone.
4. **The 24–48 h endpoint changed from "normal" to "130 to 140 mm Hg"** (see §5).
5. **Diastolic threshold moved cleanly to 120** (see §3).

---

## 3. THRESHOLD CHECK — is DBP 110 or 120?

**The card is internally inconsistent, and the answer depends on which source you anchor to.** Both 110 and 120 are defensible; 110–120 as a *range* is the 2024 AHA formulation; 120 alone is the ACC/AHA guideline formulation.

| Source | Threshold as written | URL |
|---|---|---|
| 2017 ACC/AHA guideline | SBP **>180** or DBP **>120** (quoted verbatim inside the 2024 AHA statement's Figure 1 legend) | https://doi.org/10.1161/HYP.0000000000000065 |
| **2024 AHA acute-care statement** | **SBP/DBP >180/110–120 mm Hg** (a range, deliberately) | https://doi.org/10.1161/HYP.0000000000000238 |
| **2025 AHA/ACC guideline** | **>180/120** (SBP >180 and/or DBP >120) | https://doi.org/10.1161/HYP.0000000000000249 |
| 2023 ESH | grade 3 HTN = SBP **≥180** or DBP **≥110**, no severity split by BP value alone | (cited in the 2024 AHA statement) |
| NEJM 2019 (Peixoto) | "above 180/110 to 120 mm Hg"; states all major guidelines adopt 180/110–120 | https://doi.org/10.1056/NEJMcp1901117 |
| JHM 2018 (Breu & Axon) | SBP **≥180** and/or DBP **≥120** | https://doi.org/10.12788/jhm.3086 |

### Findings on the card's three bullets

**Bullet 1 & 2 (markedly elevated BP / emergency: "SBP>=180 or DBP>=110-120"):**
- **Sign error.** Every source uses **>** (strictly greater than), not ≥. The 2024 statement writes ">180/110–120." Minor, but on a reference card it decides the BP of exactly 180/110.
- The 110–120 range is faithful to the 2024 AHA statement but **no longer matches the 2025 guideline**, which uses 120. Recommend rendering as ">180/120 (2025 ACC/AHA); the 2024 AHA acute-care statement uses >180/110–120."
- Missing the most important caveat in the 2024 statement: the thresholds are not absolute. Bress et al. state that target-organ damage "might manifest even when BP is below the 180/110 to 120" threshold, and that the benchmark "should not be perceived as an unequivocal aspect of the definition criteria." Card should carry a version of this.

**Bullet 3 ("Asymptomatic elevated BP: SBP<=180 and DBP<=110"): — INCORRECT on two counts.**
1. **Wrong lower bound / missing lower bound.** The 2024 AHA statement defines asymptomatic elevated inpatient BP as **SBP/DBP ≥130/80 mm Hg** without new or worsening target-organ damage (matching the 2017 definition of hypertension). The card gives no lower bound, implying anything below 180/110 is "asymptomatic elevated BP," including a normal BP.
2. **Wrong operator, and it opens a gap.** Using ≤110 for DBP while bullets 1–2 use ≥110–120 creates a band (DBP 110–120, and SBP exactly 180) that satisfies both definitions at once. Correct statement is **<180/110–120** (or, per 2025, <180/120).

**Suggested corrected wording:**
> Asymptomatic elevated BP: ≥130/80 and <180/110–120 mm Hg, no acute target-organ damage (2024 AHA; 2025 ACC/AHA uses <180/120).

---

## 4. END-ORGAN DAMAGE LIST — incomplete

### What the 2024 AHA statement actually lists (Bress et al., text + Table 1, BARKH)

Brain — hypertensive encephalopathy, intracranial hemorrhage, acute ischemic stroke; the table adds hypertensive encephalopathy (PRES), stroke, cerebral hemorrhage.
Arteries — dissecting aortic aneurysm; **the table's "Arteries" row also carries preeclampsia, HELLP, and eclampsia**.
Retina — high-grade retinopathy; table: **Grade III–IV Keith-Wagener-Barker hypertensive retinopathy**.
Kidney — acute kidney injury; table adds **thrombotic microangiopathy**.
Heart — acute myocardial infarction, unstable angina, acute left ventricular failure with pulmonary edema; table splits **acute heart failure**, **pulmonary edema**, **acute coronary syndrome**.
Microvasculature (narrative) — high-grade retinopathy, AKI, or **microangiopathic hemolytic anemia and thrombocytopenia**.
(BARKH is adapted from Rossi GP et al. *Blood Press.* 2021;30:208–219, https://doi.org/10.1080/08037051.2021.1917983)

NEJM 2019 Table 1 adds the umbrella term **"diffuse microvascular injury (malignant hypertension)"** = high-grade retinopathy (hemorrhages, **exudates**, or papilledema), AKI, or MAHA/thrombocytopenia, alone or in combination.

### Gaps in the card's list

| Missing / needs change | Source | Why it matters |
|---|---|---|
| **Eclampsia / preeclampsia with severe features / HELLP** | 2024 AHA Table 1 (under "Arteries"); 2017 & 2025 ACC/AHA "compelling conditions" | Distinct BP target (immediate SBP <160 and DBP <105 if severe) and distinct drug set (magnesium, labetalol, nicardipine, hydralazine). Card only mentions eclampsia buried in the hydralazine row of Table 4. |
| **Acute heart failure** as an entity distinct from flash pulmonary edema | 2024 AHA Table 1 | Different target: acute HF → SBP <180 **or** MAP decline 25%; pulmonary edema → immediate SBP <140. The card collapses both into "flash pulmonary edema." |
| **Sympathetic / adrenergic crisis** (pheochromocytoma, cocaine/amphetamine, MAOI–tyramine, clonidine or β-blocker withdrawal) | 2017 ACC/AHA compelling conditions (retained in 2025); named as an emergency by 5 of the guidelines in the 2026 systematic review (https://pmc.ncbi.nlm.nih.gov/articles/PMC12817854/); precipitants listed in NEJM 2019 | It is a *rapid-lowering* exception (SBP <140 in first hour) and contraindicates unopposed β-blockade. Complete omission from the card. |
| **Thrombocytopenia** alongside MAHA | 2024 AHA; NEJM 2019 Table 1 footnote | The card's "Heme: MAHA" is half the finding. |
| **Retinal exudates / cotton-wool spots**; grading | 2024 AHA (Grade III–IV KWB); NEJM 2019 | Card lists only papilledema + hemorrhage. |
| **Perioperative hypertension** | NEJM 2019 explicitly scopes it out; 2024 AHA discusses postsurgical inpatients | Optional, but worth a line since the ICU table already lists "peri-op HTN" as an esmolol indication. |
| **Scleroderma renal crisis** | NEJM 2019 precipitants | Card has it only as the captopril indication in Table 4. |

### Two items on the card that are NOT in the cited sources

- **"TIA"** under Neuro. Not listed as acute target-organ damage by the 2024 AHA statement, NEJM 2019, the 2017 guideline, or the 2025 guideline. Acute ischemic stroke is. Recommend removing or demoting to a "red-flag symptom" line.
- **"hematuria"** under Renal. Not in any of the canonical lists; AKI is. Hematuria is a reasonable clue to glomerulonephritis or thrombotic microangiopathy, but it is not a listed criterion — if kept, label it as a clue rather than a criterion.

---

## 5. CORRECTION TIME COURSE — the two formulations

### (a) "MAP down 10-20% in 1st hr, further 5-15% over next 23h" — **NOT a guideline recommendation**

- **It is not in JNC 7, not in the 2017 ACC/AHA guideline, not in the 2024 AHA acute-care statement, and not in the 2025 ACC/AHA guideline.** I searched the full text of the 2024 statement and the NEJM review; neither contains it.
- Its provenance is tertiary/textbook: it is the formulation used by the **StatPearls "Hypertensive Emergency" chapter** (https://www.ncbi.nlm.nih.gov/books/NBK470371/) and appears in the **Washington Manual of Medical Therapeutics** entry surfaced in search (https://www.unboundmedicine.com/washingtonmanual/view/Washington-Manual-of-Medical-Therapeutics/602304/all/Hypertension). Notably, the currently-fetchable Washington Manual text for hypertensive emergency actually gives the **25%/2–6 h/24–48 h** formulation, not the 10–20%/5–15% one, so even that attribution is unstable.
- **UNVERIFIABLE as a primary-source recommendation.** Recommend either deleting it or labelling it "textbook convention," not placing it beside a guideline citation.

### (b) "reduce BP by max 25% within first hour, and to no lower than 160/100 within 2-6h; reduce to normal over 24-48h" — **guideline-derived, but with a real error and an out-of-date endpoint**

Chain of custody: **JNC 7 (2003)** → **2017 ACC/AHA Section 11.2** → **2025 ACC/AHA Rec 6.2.3**.

- **2017 ACC/AHA (Class 1):** SBP should be reduced by no more than 25% within the first hour; then, if stable, **to 160/100 mm Hg** within the next 2 to 6 hours; then cautiously **to normal** during the following 24 to 48 hours.
- **2025 ACC/AHA (Rec 6.2.3, Class 1, LOE C-LD)  [2025 text via secondary sources]:** identical through the first two steps but the endpoint changed — "then cautiously to **130 to 140 mm Hg** during the next 24 to 48 hours."
- **NEJM 2019 (Peixoto), Table 1 and text:** decrease BP by **20–25%** during the first hour and to **160/100 mm Hg by 2–6 h** — Peixoto notes guidelines recommend BP "be decreased by no more than 20 to 25% during the first hour."
- ACCP CCSAP 2018 renders the same table as: first hour, reduce MAP by 25% while maintaining DBP ≥100; hours 2–6, SBP 160 and/or DBP 100–110 (https://www.accp.com/docs/bookstore/ccsap/ccsap2018b1_sample.pdf).

**ERROR on the card: "to no lower than 160/100 within 2-6h" inverts the guideline.** The guidelines say to bring BP **to** (2025: **to <**) 160/100 by 2–6 hours — 160/100 is the *target you descend to*, not a floor you must stay above. The card's phrasing tells the reader to stop above 160/100, which is the opposite bound. (The "don't overshoot" intent the card is reaching for is already carried by "no more than 25% in the first hour," and by CCSAP's "maintain DBP ≥100 during the first hour.")

**Second correction: "reduce to normal over 24-48h" is the retired 2017 wording.** Per the 2025 guideline the endpoint is **130–140 mm Hg** over 24–48 h.

### Are (a) and (b) consistent with each other?

**Only loosely, and they are not interchangeable.**
- Different variable: (a) targets **MAP**, (b) targets **SBP**. A 25% SBP fall is not a 25% MAP fall.
- Different first-hour ceiling: (a) caps at 20%, (b) caps at 25%.
- (a) has no absolute BP checkpoint at all; (b) is anchored to 160/100 at 2–6 h and 130–140 at 24–48 h.
- Cumulatively they land in similar territory (≈25–35% total over 24 h for (a); ~25% at 1 h then to 160/100 for (b)), so they are not contradictory in outcome — but printing both on one line, as the card does, implies they are two statements of one rule. They are not. Recommend keeping (b) only.

### Conditions that are EXCEPTIONS to gradual lowering (lower fast)

**Compelling conditions, 2017 → 2025 ACC/AHA:** reduce SBP to **<140 mm Hg during the first hour**, and to **<120 mm Hg in aortic dissection**.
- **Acute aortic dissection / acute aortic syndrome** — SBP <120 (2024 AHA table: SBP <120 immediate; card's Table 2: <120 and HR <60 within 20 min, consistent with the EM synthesis of the 2025 guideline).
- **Severe preeclampsia / eclampsia** — 2024 AHA: immediate SBP <160 and DBP <105 if severe.
- **Pheochromocytoma / sympathetic-adrenergic crisis** — SBP <140 in the first hour.
- **Acute pulmonary edema** and **acute coronary syndrome** — 2024 AHA: immediate SBP <140.
- **Acute intracerebral hemorrhage (SBP 150–220)** — the 2025 guideline moves this into the rapid camp: immediately lower to **130 to <140 mm Hg** and maintain ~7 days. (2024 AHA table still lists cerebral hemorrhage as MAP decline 15%; NEJM 2019 gives SBP 140–150 within 1 h with caveats, and warns lowering below 140 may be harmful.) **This is an active discordance between the card's Table 2 (SBP 180–220 → target 140–160) and the 2025 guideline.** Flagged here because it bears on the "correction time course" row even though Table 2 is outside my scope.
- **Counter-exception — acute ischemic stroke** is the one place where *not* lowering is correct: no intervention for the first 48–72 h if BP <220/120 and no lysis (NEJM 2019 Table 1), which matches the card's Table 2.

---

## 6. THE ASYMPTOMATIC CASE — evidence base and current recommendation

**Bottom line: there are still no randomized trials of treating asymptomatic elevated inpatient BP.** Bress et al. 2024 state this plainly, and Anderson et al. 2023 end by calling for exactly such trials. Everything below is observational, mostly propensity-matched or target-trial-emulated.

### Rastogi et al., JAMA Intern Med 2021 — the paper the card cites
Rastogi R, Sheehan MM, Hu B, Shaker V, Kojima L, Rothberg MB. *JAMA Intern Med.* 2021;181(3):345–352. doi:10.1001/jamainternmed.2020.7501. PMID 33369614. https://pmc.ncbi.nlm.nih.gov/articles/PMC7770615/
- Cohort: 22,834 adults admitted to medicine services at 10 Cleveland Clinic hospitals in 2017; cardiovascular admissions excluded.
- 17,821 (78%) had ≥1 hypertensive BP recording. 5,904 (33.1%) were treated. Of treated hypertensive systolic readings, 66% received oral agents.
- Propensity-matched (4,520 pairs), treated vs untreated: **AKI 10.3% vs 7.9%** (466 vs 357, P<.001); **myocardial injury 1.2% vs 0.6%** (53 vs 26, P=.003).
- **"There was no BP interval in which treated patients had better outcomes than untreated patients"** (Rastogi et al., *JAMA Intern Med* 2021).
- Only 9% were discharged on an intensified regimen, and intensification at discharge was not associated with better BP control over the following year.
- As re-analysed in the 2024 AHA statement: patients who received ≥1 **IV** antihypertensive had a composite of AKI/MI/stroke of **11% vs 8.2%**.

### Anderson et al. on intensification at discharge — **the card's implied "JAMA IM 2019" is correct, but there are two Anderson papers and they are often confused**
1. **Discharge intensification:** Anderson TS, Jing B, Auerbach A, Wray CM, Lee S, Boscardin WJ, Fung K, Ngo S, Silvestrini M, Steinman MA. **Clinical Outcomes After Intensifying Antihypertensive Medication Regimens Among Older Adults at Hospital Discharge.** *JAMA Intern Med.* 2019;179(11):1528–1536. doi:10.1001/jamainternmed.2019.3007. PMID 31424475. https://pmc.ncbi.nlm.nih.gov/articles/PMC6705136/
   - VA, ≥65 y, hospitalized 2011–2013 for noncardiac conditions; propensity-matched 4,056 patients.
   - Within 30 days: **readmission HR 1.23 (1.07–1.42), NNH 27 (16–76)**; **serious adverse events HR 1.41 (1.06–1.88), NNH 63 (34–370)**.
   - At 1 year: **no difference in cardiovascular events (HR 1.18, 0.99–1.40)** and **no difference in SBP** (134.7 vs 134.4; difference-in-differences 0.6 mm Hg, 95% CI −2.4 to 3.7).
2. **In-hospital intensification (different paper, often mis-cited as the 2019 one):** Anderson TS, Herzig SJ, Jing B, Boscardin WJ, Fung K, Marcantonio ER, Steinman MA. **Clinical Outcomes of Intensive Inpatient Blood Pressure Management in Hospitalized Older Adults.** *JAMA Intern Med.* 2023;183(7):715–723. doi:10.1001/jamainternmed.2023.1667. PMID 37252732. https://pmc.ncbi.nlm.nih.gov/articles/PMC10230372/
   - 66,140 VA patients ≥65 y, noncardiovascular admissions, elevated BP in first 48 h; 14,084 (21.3%) intensively treated.
   - Composite of in-hospital death, ICU transfer, stroke, AKI, BNP elevation, troponin elevation: **8.7% vs 6.9%, weighted OR 1.28 (1.18–1.39)**; **highest with IV agents, OR 1.90 (1.65–2.19)**.
   - Intensively treated patients then received far more antihypertensive doses for the rest of the stay (mean 6.1 vs 1.6).
   - Consistent across age, frailty, pre-admission BP, and CVD-history subgroups.

### "Ghazi et al 2024" — **CORRECTED: it is not JAMA Internal Medicine, and there are three separate Ghazi papers**
1. **Ghazi L, Chen X, Harhay MO, Hu L, Biswas A, Peixoto AJ, Li F, Wilson FP. Treatment Effect Heterogeneity in Acute Kidney Injury Incidence Following Intravenous Antihypertensive Administration for Severe Blood Pressure Elevation During Hospitalization. *Am J Kidney Dis.* 2025;85(4):442–453.** doi:10.1053/j.ajkd.2024.09.011. **Epub 2024 Nov 22**, PMID 39580068. https://doi.org/10.1053/j.ajkd.2024.09.011
   — This is the paper usually meant by "Ghazi 2024." Journal is **AJKD, not JAMA IM**. 11,951 patients who developed severe HTN (SBP >180 or DBP >110) in hospital; 741 treated with IV agents within 3 h, 11,210 not; **AKI 18% (treated) vs 13% (untreated)**. Bayesian heterogeneity analysis: most patients would have been *harmed*; a subgroup of only 317 patients was predicted to benefit.
2. **Ghazi L, Li F, Simonov M, Yamamoto Y, Nugent JT, Greenberg JH, Bakhoum CY, Peixoto AJ, Wilson FP. Effect of intravenous antihypertensives on outcomes of severe hypertension in hospitalized patients without acute target organ damage. *J Hypertens.* 2023;41(2):288–294.** doi:10.1097/HJH.0000000000003328. PMID 36583354. https://pmc.ncbi.nlm.nih.gov/articles/PMC9799038/
   — 224,265 non-ICU hospitalizations; 20,383 (9%) developed severe HTN; 5% got IV agents within 3 h. **Myocardial injury 5.9% treated vs 3.6% untreated, HR 1.6 (1.13–2.24).** No significant increase in stroke, AKI, or death in this analysis.
3. **Ghazi L, et al. Severe inpatient hypertension prevalence and blood pressure response to antihypertensive treatment. *J Clin Hypertens (Greenwich).* 2022;24:339–349.** doi:10.1111/jch.14431 — the 22,000-patient cohort the AHA statement cites for **40% greater likelihood of a ≥30% MAP drop** and **60% greater risk of myocardial injury** with IV antihypertensives.

### Other harm data cited by the 2024 AHA statement
- **Mohandas R, et al. Pro re nata antihypertensive medications and adverse outcomes in hospitalized patients: a propensity-matched cohort study. *Hypertension.* 2021;78:516–524.** doi:10.1161/HYPERTENSIONAHA.121.17279 — PRN antihypertensives (93% IV): **2-fold higher risk of death, 24% higher risk of AKI, 2-fold higher risk of abrupt BP lowering** (>25% SBP fall within 1 h). The AHA statement flags confounding by indication here.
- **Lipari M, Moser LR, Petrovitch EA, Farber M, Flack JM. As-needed intravenous antihypertensive therapy and blood pressure control. *J Hosp Med.* 2016;11:193–198.** doi:10.1002/jhm.2510 — **32.6% of patients given PRN IV antihypertensives had a >25% BP drop within 6 hours**; PRN doses were often ordered for BPs far below 180/100 and were not usually followed by oral intensification.
- **Brooks et al. (cited in Breu & Axon 2018):** among patients treated with IV nicardipine or nitroprusside for hypertensive emergency, **57% (27/47) had a >25% MAP reduction within the first 30 minutes**; 2 had acute ischemic events attributed to treatment.

### 2024–2026 data
- **Kushnir Y, Barrera N, Arias-Sanchez P, et al. Intensified blood pressure control during hospital admission and on discharge: a systematic review and meta-analysis of retrospective cohort studies. *Front Cardiovasc Med.* 2026;13:1691926.** doi:10.3389/fcvm.2026.1691926, PMID 41725942, PMC12916387. Four propensity-matched cohorts, **n = 77,448** (38,724 per arm). Intensified BP control associated with **stroke OR 3.77 (1.38–10.27)**, **AKI OR 1.23 (1.13–1.33)**, **longer LOS (MD 1.17 days)**; **MI not significant (OR 2.04, 0.85–4.89)**. Hypertensive emergency, stroke, MI, and dissection on admission were excluded.
- **Gauer RL, Rifaat AI, Blankinship DR. Severe Hypertension: Evaluation and Treatment. *Am Fam Physician.* 2026;113(5):459–468.** PMID 42202349. https://www.aafp.org/afp/2026/0500/severe-hypertension — states inpatient treatment of severe hypertension does not improve short-term outcomes and increases cardiovascular events, AKI, and length of stay; short-acting or IV antihypertensives "not recommended"; asymptomatic severe elevations should not be referred to the ED; **gradual reduction over days to weeks**. Also reports **13.1%** of adults with pre-existing hypertension have readings ≥180/120, and that BP fell spontaneously to <140/90 within 3 hours in **44%** of untreated patients in one retrospective study.
- **Wongtanasarasin W, Tangpaisarn T, Srisurapanont K, Kotruchin P. Comparative effectiveness and safety of oral antihypertensive agents for severe asymptomatic hypertension: systematic review and network meta-analysis of RCTs. *Hypertens Res.* 2026 (online 25 Aug 2026).** doi:10.1038/s41440-026-02783-6, PMID 42642627. Only **5 RCTs** exist, all short-term BP-response studies. β-blockers RR 1.07 (0.59–1.92), CCBs RR 1.02 (0.59–1.78), ACEi/ARB RR 1.01 (0.64–1.58) for treatment success at 120–240 min. **No class superior; overall certainty of evidence very low.** This is the direct answer to the card's "captopril, labetalol >> hydralazine" ranking: there is no comparative evidence supporting it.
- **Gorey S, Rothberg M, Chang TI. To Treat or Not to Treat? Watchful Waiting or Oral Antihypertensives for Asymptomatic Inpatient Hypertension. *N Engl J Med.* 2025;393(20):2051–2053.** doi:10.1056/NEJMclde2502632, PMID 41259762. NEJM Clinical Decisions piece — useful as a teaching reference showing the question is still genuinely contested (Rothberg is senior author of Rastogi 2021; Chang was vice-chair of the 2024 AHA statement).

### Current recommendation, synthesized
1. Confirm the reading with proper technique (seated, correct cuff, calibrated device); the 2024 AHA statement notes 36 of 100 inpatient measurements in one UK hospital used an inappropriately sized cuff, and that oscillometric devices can underestimate BP by up to 50/30 mm Hg vs arterial line above 180/100.
2. Screen for acute target-organ damage (BARKH; history, exam incl. bilateral pulses and fundoscopy, BMP, CBC, CXR, 12-lead ECG, volume status).
3. Identify and treat reversible causes: pain, anxiety, acute stress, sleep deprivation, nausea, urinary retention, withdrawal (alcohol/benzo/β-blocker rebound), excessive IV fluids, NSAIDs, stimulants, corticosteroids, illicit drugs, and **un-restarted home antihypertensives** (41% of patients prescribed PRN antihypertensives were not receiving their home regimen in one study; 25% in a postsurgical IV-treated cohort).
4. Allow ≥30 minutes of quiet rest and re-measure — roughly a third normalize.
5. **Do not give PRN IV, and (per 2025) do not give intermittent additional oral, antihypertensives purely to lower the number.** Class 3: Harm.
6. If BP is persistently markedly elevated *and* there is a history of high outpatient BPs, persistent uncontrolled hypertension, or high CVD risk, restarting or adjusting the **long-acting** regimen is reasonable — with the explicit caveat that a typical inpatient stay is too short to judge the effect of a medication change, and close outpatient follow-up is required.
7. Arrange out-of-office BP monitoring and follow-up (NEJM 2019: 1–7 days).

---

## 7. CARD-SPECIFIC FINDINGS — CONFIRMED / CORRECTED / UNVERIFIABLE

### CONFIRMED
| Card element | Source |
|---|---|
| Hypertensive emergency = markedly elevated BP **with** new/worsening target-organ damage | Bress 2024; Jones 2025; Peixoto 2019 |
| "Formerly HTN urgency" for asymptomatic markedly elevated BP | Bress 2024 (explicitly proposes replacing "hypertensive urgency") |
| Assess measurement variables — positioning, cuff size, device type | Bress 2024 (patient position, arm support, position relative to heart, leg crossing, cuff sizing; oscillometric vs arterial line vs auscultatory) |
| Assess underlying causes — pain, anxiety, urine retention, steroids, OSA, nausea, withdrawal | Bress 2024; Peixoto 2019 (urinary retention, IV fluids, pain, glucocorticoids); Breu & Axon 2018 (nausea, alcohol/benzo withdrawal, OSA, delirium) |
| Assess adherence to prior treatment before aggressive overcorrection | Peixoto 2019 ("most common precipitating factor"); Bress 2024 (home meds not restarted) |
| Asx triage: outpatient management with close follow-up | Bress 2024; Peixoto 2019; Jones 2025 |
| Asx: PO meds; avoid IV or high-dose meds; risk of AKI/stroke/MI from hypoperfusion | Bress 2024 Table 3 item 9; Rastogi 2021; Anderson 2023; Ghazi 2022/2023/2025 |
| Asx: worse outcomes with intensifying antihypertensives during a non-cardiac admission | Rastogi 2021 (the cited paper), plus Anderson 2023, Kushnir 2026 |
| Asx: if no established chronic HTN, risks may outweigh benefits; consider permissive HTN | Bress 2024 (period of acute illness "may be a less optimal time to intervene") |
| Emergency: start short-acting titratable IV agents, transition to PO | Bress 2024; Peixoto 2019 (start/resume long-acting during first 6–12 h) |
| Emergency: hydralazine has high risk of overcorrection | Peixoto 2019 (unpredictable effects, often excessive lowering, avoid as first option) |
| Emergency: arterial line for gtt / accurate titration | Bress 2024 (arterial lines preferred for hypertensive emergency and IV antihypertensives) |

### CORRECTED
| # | Card says | Should say | Source |
|---|---|---|---|
| A | "Asymptomatic elevated BP: SBP<=180 **and** DBP<=110" | **≥130/80 and <180/110–120** without target-organ damage (2025: <180/120) | Bress 2024, Figure 1 + Definitions |
| B | "SBP>=180 or DBP>=110-120" | **>**180/110–120 (2024 AHA) or **>**180/120 (2025 ACC/AHA); and these are not absolute — TOD can occur below them | Bress 2024; Jones 2025 |
| C | Asx suggested meds: "start captopril, labetalol >> hydralazine … convert to long-acting before discharge" | Do **not** give immediate-acting oral or IV agents to acutely lower an asymptomatic BP; restart/adjust **long-acting** agents instead. 2025 Rec 6.2.4 is **Class 3: Harm** for intermittent IV *or oral* dosing in noncardiac inpatients without TOD. No oral class has proven superiority (Hypertens Res 2026 NMA). Captopril is specifically named among agents implicated in treatment-related adverse events in the paper the card cites for this row. | Breu & Axon 2018 Rec #4; Jones 2025 Rec 6.2.4; Wongtanasarasin 2026 |
| D | "to **no lower than** 160/100 within 2-6h" | "**to <160/100** within 2–6 h" — 160/100 is the target you descend to, not a floor | 2017 ACC/AHA §11.2; Jones 2025 Rec 6.2.3; Peixoto 2019 Table 1 |
| E | "reduce to **normal** over 24-48h" | "cautiously to **130–140 mm Hg** over 24–48 h" (2025 endpoint; "normal" was the 2017 wording) | Jones 2025 Rec 6.2.3 |
| F | "MAP down by 10-20% in 1st hr, further 5-15% over next 23 hrs" | Delete, or relabel as textbook convention. Not in JNC 7, 2017 ACC/AHA, 2024 AHA, or 2025 ACC/AHA. The guideline figure is **20–25% in the first hour**. | Full-text search of Bress 2024 and Peixoto 2019; 2017/2025 recommendation text |
| G | Asx: "lower BP no more than 25-30% over hrs-days" | No source gives a 25–30% figure for asymptomatic markedly elevated BP. Current guidance is **gradual reduction over days to weeks** via the long-acting regimen, with outpatient follow-up. | AFP 2026; Bress 2024; Jones 2025 |
| H | Emergency triage: "Floor vs ICU" | **ICU admission is now Class 1 (LOE B-R)** for hypertensive emergency; NEJM 2019 says all such patients should go to an ICU. Floor management should be the exception, not the co-equal option. | Jones 2025 Rec 6.2.1; Peixoto 2019 |
| I | End-organ damage list | Add eclampsia/preeclampsia-HELLP, acute heart failure (separate from flash pulmonary edema), sympathetic/adrenergic crisis, thrombocytopenia with MAHA, retinal exudates + KWB grade III–IV. Remove or demote **TIA** and **hematuria** (neither appears in the cited sources' lists). | Bress 2024 Table 1; Peixoto 2019 Table 1; 2017/2025 ACC/AHA compelling conditions |
| J | Table 1 header citation "JHM 2018;13:860" | Cite as **Breu AC, Axon RN. Things We Do for No Reason: Acute Treatment of Hypertensive Urgency. J Hosp Med. 2018;13(12):860–862** — and note it predates the terminology change (it uses ≥180 and/or ≥120). | PubMed 30379139 |
| K | Header citation "HTN 2024;81:e94" | Correct as written; add the 2025 guideline alongside it, since the 2025 guideline retires and replaces the 2017 guideline that the 2024 statement was built on. | PMID 40811516 |

### UNVERIFIABLE
- **"time of day"** as a measurement variable. The 2024 AHA statement discusses a night-dosing/morning-BP cycle driven by PRN orders, and recommends considering supine vs seated measurement — but it does not list "time of day" as a discrete measurement variable. Defensible clinically; not directly sourced.
- The **10–20% / 5–15% over 23 h** formulation (item F) — traceable to tertiary references only; I could not find a primary source.
- The **25–30% over hours-to-days** figure for asymptomatic markedly elevated BP (item G) — no source found.
- Whether the card's DBP "110–120" is intended as "110 to 120" (the 2024 AHA range) or as two alternative cut-points. As printed it is ambiguous.
- The full 2025 guideline PDF could not be retrieved directly (Cloudflare 403 on ahajournals.org, jacc.org, nejm.org, ajkd.org, europepmc.org). All 2025 recommendation wording above is corroborated across ≥2 independent secondary renderings but should be spot-checked against the PDF from a UCSF library login before the card is published.

---

## 8. REFERENCE LIST WITH URLs

| Source | URL |
|---|---|
| Peixoto AJ. Acute Severe Hypertension. N Engl J Med. 2019;381(19):1843–1852 | https://doi.org/10.1056/NEJMcp1901117 · https://pubmed.ncbi.nlm.nih.gov/31693807/ |
| Bress AP, et al. Management of Elevated BP in the Acute Care Setting. Hypertension. 2024;81(8):e94–e106 | https://doi.org/10.1161/HYP.0000000000000238 · https://www.ahajournals.org/doi/10.1161/HYP.0000000000000238 · https://pubmed.ncbi.nlm.nih.gov/38804130/ |
| Breu AC, Axon RN. TWDFNR: Acute Treatment of Hypertensive Urgency. J Hosp Med. 2018;13(12):860–862 | https://doi.org/10.12788/jhm.3086 · https://cdn.mdedge.com/files/s3fs-public/issues/articles/jhm013120860.pdf |
| Rastogi R, et al. JAMA Intern Med. 2021;181(3):345–352 | https://doi.org/10.1001/jamainternmed.2020.7501 · https://pmc.ncbi.nlm.nih.gov/articles/PMC7770615/ |
| Jones DW, et al. 2025 AHA/ACC…SGIM Guideline. Hypertension. 2025;82(10):e212–e316 | https://doi.org/10.1161/HYP.0000000000000249 · https://pubmed.ncbi.nlm.nih.gov/40811516/ |
| Same, Circulation copy. 2025;152(11):e114–e218 | https://doi.org/10.1161/CIR.0000000000001356 |
| Same, JACC copy. 2025;86(18):1567–1678 | https://doi.org/10.1016/j.jacc.2025.05.007 · https://pubmed.ncbi.nlm.nih.gov/40815242/ |
| 2017 ACC/AHA Guideline (retired by the 2025) | https://doi.org/10.1161/HYP.0000000000000065 |
| Guideline Central structured summary of the 2025 guideline | https://www.guidelinecentral.com/guideline/6962/ |
| Brown C, Clark D III, Jones DW. Curr Hypertens Rep. 2026;28(1):19 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12995957/ |
| Anderson TS, et al. JAMA Intern Med. 2019;179(11):1528–1536 (discharge) | https://doi.org/10.1001/jamainternmed.2019.3007 · https://pmc.ncbi.nlm.nih.gov/articles/PMC6705136/ |
| Anderson TS, et al. JAMA Intern Med. 2023;183(7):715–723 (inpatient) | https://doi.org/10.1001/jamainternmed.2023.1667 · https://pmc.ncbi.nlm.nih.gov/articles/PMC10230372/ |
| Ghazi L, et al. Am J Kidney Dis. 2025;85(4):442–453 (epub 2024) | https://doi.org/10.1053/j.ajkd.2024.09.011 · https://pubmed.ncbi.nlm.nih.gov/39580068/ |
| Ghazi L, et al. J Hypertens. 2023;41(2):288–294 | https://doi.org/10.1097/HJH.0000000000003328 · https://pmc.ncbi.nlm.nih.gov/articles/PMC9799038/ |
| Ghazi L, et al. J Clin Hypertens. 2022;24:339–349 | https://doi.org/10.1111/jch.14431 |
| Mohandas R, et al. Hypertension. 2021;78:516–524 | https://doi.org/10.1161/HYPERTENSIONAHA.121.17279 |
| Lipari M, et al. J Hosp Med. 2016;11:193–198 | https://doi.org/10.1002/jhm.2510 |
| Kushnir Y, et al. Front Cardiovasc Med. 2026;13:1691926 | https://doi.org/10.3389/fcvm.2026.1691926 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12916387/ |
| Wongtanasarasin W, et al. Hypertens Res. 2026 (online) | https://doi.org/10.1038/s41440-026-02783-6 · https://pubmed.ncbi.nlm.nih.gov/42642627/ |
| Gorey S, Rothberg M, Chang TI. N Engl J Med. 2025;393(20):2051–2053 | https://doi.org/10.1056/NEJMclde2502632 |
| Gauer RL, et al. Am Fam Physician. 2026;113(5):459–468 | https://www.aafp.org/afp/2026/0500/severe-hypertension · https://pubmed.ncbi.nlm.nih.gov/42202349/ |
| Rossi GP, et al. Blood Press. 2021;30:208–219 (source of BARKH) | https://doi.org/10.1080/08037051.2021.1917983 |
| Systematic review of guidelines on extremely high BP (2026) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12817854/ |
| ACCP CCSAP 2018, Hypertensive Emergencies chapter (BP target table) | https://www.accp.com/docs/bookstore/ccsap/ccsap2018b1_sample.pdf |
| StatPearls, Hypertensive Emergency (source of the 10–20%/5–15% convention) | https://www.ncbi.nlm.nih.gov/books/NBK470371/ |
| Washington Manual of Medical Therapeutics, Hypertension | https://www.unboundmedicine.com/washingtonmanual/view/Washington-Manual-of-Medical-Therapeutics/602304/all/Hypertension |
| AHA Professional "Top Things to Know," 2024 acute care statement | https://professional.heart.org/en/science-news/management-of-elevated-blood-pressure-in-the-acute-care-setting |
| AAFP summary of the 2024 AHA acute-care statement | https://www.aafp.org/pubs/afp/issues/2026/0100/practice-guidelines-elevated-blood-pressure-management.html |

Local full-text copies extracted during this review:
`<scratchpad>/src/aha2024-acute.txt`, `<scratchpad>/src/aha2024-acute-flow.txt`, `<scratchpad>/src/nejm2019-peixoto.txt`, `<scratchpad>/src/jhm2018-breu.txt`, `<scratchpad>/src/ccsap.txt`
