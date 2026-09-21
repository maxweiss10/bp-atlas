# Research 6 — Pre-procedure elevated BP & discharge with elevated BP

Compiled 2026-09-21. For the inpatient hypertension cheat sheet.

**Scope:** the two situations where the (correct) "don't treat asymptomatic inpatient
hypertension" guidance fails the intern because someone else is applying pressure to treat:
(A) the surgeon/proceduralist wants a better number before the case, and (B) the team or
institution won't discharge at 180-something systolic.

**Evidence-tier key used throughout:**
- **[GL]** = stated in a society guideline, with COR/LOE where one exists
- **[TRIAL]** = randomized or prospective comparative data
- **[OBS]** = observational / cohort
- **[CUSTOM]** = no evidence base located; institutional or historical practice

---

# A. PRE-PROCEDURE / PRE-OPERATIVE ELEVATED BP

## A1. The 2024 ACC/AHA perioperative guideline recommendation

**Citation:** 2024 AHA/ACC/ACS/ASNC/HRS/SCA/SCCT/SCMR/SVM Guideline for Perioperative
Cardiovascular Management for Noncardiac Surgery. *Circulation* 2024;150(19):e351-e442.
doi:10.1161/CIR.0000000000001285.
https://www.ahajournals.org/doi/10.1161/CIR.0000000000001285
(also *JACC* 2024;84(19):1869-1969, doi:10.1016/j.jacc.2024.06.013,
https://www.jacc.org/doi/10.1016/j.jacc.2024.06.013)

### The recommendation **[GL]**

> "In patients undergoing elective elevated-risk surgery who have cardiovascular risk factors
> for perioperative complications and recent history of poorly controlled hypertension
> (systolic blood pressure ≥180 mm Hg or diastolic blood pressure ≥110 mm Hg before the day of
> surgery), deferring surgery **may be considered** to reduce the risk of perioperative
> complications."
>
> **COR 2b, LOE C-LD**

**Answer to "recommended / reasonable / may be considered":** *may be considered.* This is the
weakest affirmative class in the ACC/AHA system. COR 2b = "benefit ≥ risk," phrased as
"may/might be reasonable," "usefulness/effectiveness is unknown/unclear/uncertain." LOE C-LD =
limited data: randomized or nonrandomized studies with limitations of design or execution.

**Answer to "is there a numeric threshold":** yes, ≥180 systolic **or** ≥110 diastolic — but
the threshold is loaded with four qualifiers that almost never all apply to the intern's
scenario:

| Qualifier in the recommendation | The 185/105 pre-op holding scenario |
|---|---|
| **elective** surgery | often yes |
| **elevated-risk** surgery | frequently not (most floor cases are low/intermediate risk) |
| patient has **cardiovascular risk factors** | variable |
| **recent history of poorly controlled hypertension** | a single reading is not a history |
| measured **before the day of surgery** | a reading in pre-op holding is explicitly *not* this |
| DBP ≥110 | 105 does not meet it |

**This is the single most useful fact in section A.** The guideline's 180/110 threshold is about
a *pattern of poorly controlled hypertension documented before the day of surgery*, not about a
one-off reading taken in the pre-op bay. A patient at 185/105 in holding does not meet the
recommendation's own criteria on at least two counts (DBP, and "before the day of surgery").

### Other 2024 perioperative recommendations relevant here **[GL]**

- **Class 1** (intraoperative): "Maintaining MAP ≥60 to 65 mmHg or SBP ≥90 at a minimum is
  recommended to decrease the chance of myocardial injury."
- Narrative guidance: "Continue most antihypertensive agents."
- Postoperative hypotension (MAP <60 or SBP <90) should be recognized and treated promptly.

### ⚠️ Verification caveat on the exact wording

ahajournals.org and jacc.org both return **HTTP 403** to automated fetch, so I could **not read
the recommendation table in the primary document directly.** The wording and the COR 2b / LOE
C-LD designation above are reconstructed from three concordant independent secondary sources:

1. Cleveland Clinic Journal of Medicine review (Cohn SL). *CCJM* 2025;92(4):213-219.
   https://www.ccjm.org/content/92/4/213 — full text extracted; states: *"Blood pressure.
   Continue most antihypertensive agents. If blood pressure is 180/110 mm Hg or higher before
   the day of surgery, consider delaying surgery until it is under better control. The
   anesthesiologist should maintain an intraoperative mean arterial pressure of at least 60 to
   65 mm Hg or systolic blood pressure of at least 90 mm Hg."*
2. "Highlights from the ACC and AHA 2024 Guideline for Perioperative Cardiovascular Management
   for Noncardiac Surgery," PMC12904102.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC12904102/ — gives the COR tiers for BP, beta
   blockers, RAASi, clonidine (see A5).
3. Guideline-summary search results reproducing the recommendation sentence verbatim with
   "(Class 2b, Level of Evidence C-LD)".

Independent corroboration that 2b/C-LD is the right tier: the **2017 ACC/AHA hypertension
guideline** carried a nearly identical recommendation at the same tier, reproduced verbatim in
POQI's Table 1 (see A3): *"In patients with planned elective major surgery and SBP of 180 mm Hg
or higher, or DBP of 110 mm Hg or higher, deferring surgery may be considered."* — **COR IIb,
LOE C-LD**.

**Before putting the exact sentence on the cheat sheet in quotation marks, pull the PDF through
UCSF library access and confirm.** The *substance* (2b, "may be considered," 180/110, "before
the day of surgery") is solid across all sources; the exact clause order is not 100% verified.

---

## A2. Does delaying actually help? — the trial evidence

### Weksler N, Klein M, Szendro G, et al. **[TRIAL]**

"The dilemma of immediate preoperative hypertension: to treat and operate, or to postpone
surgery?" *J Clin Anesth* 2003;15(3):179-183. PMID 12770652.
https://pubmed.ncbi.nlm.nih.gov/12770652/
(abstract retrieved in full via NCBI eutils)

| Element | Detail |
|---|---|
| **Design** | Prospective, randomized |
| **Setting** | University-affiliated 550-bed community hospital |
| **n** | **989** |
| **Population** | Well-controlled chronic hypertensives arriving in the OR with **DBP 110–130 mm Hg**. Excluded: prior MI, unstable/severe angina, renal failure, PIH, LVH, prior revascularization, aortic stenosis, preop dysrhythmias, conduction defects, stroke |
| **Intervention** | **589** → 10 mg nifedipine intranasally, **proceed to surgery** |
| **Control** | **400** → **surgery postponed**, admitted for BP control |
| **Outcomes** | Cardiovascular and neurological complications intraoperatively and over the first 3 postoperative days |
| **Result** | Groups similar in age, sex, surgery type, anesthesia duration, intraoperative fluids. **"There were no statistically significant differences in postoperative complications."** Hospitalization **considerably shorter** in the proceed group |
| **Conclusion (verbatim)** | *"Immediate preoperative reduction of DBP with intranasal nifedipine is safe in patients with well-controlled arterial hypertension but they presented with severe to very severe hypertension for patients in the OR. We were able to avoid unnecessary surgery postponement and attendant costs."* |

**⚠️ Could not verify:** the abstract gives **no event counts or percentages**. "Exact numbers"
for the complication rates are not in the abstract and the full text is paywalled
(sciencedirect.com/science/article/abs/pii/S0952818003000357). Do **not** put a specific
complication rate on the cheat sheet.

**Important framing caveat, from POQI:** this is *the only RCT of acute preoperative BP
lowering*, and POQI notes *"it is unclear whether a sufficient decrease in arterial pressure was
achieved, or for long enough, to induce a change in outcome."* So Weksler is best cited as
"postponing did not help and cost bed-days," not as "nifedipine works."

### Howell SJ, Sear JW, Foëx P. **[OBS — meta-analysis]**

"Hypertension, hypertensive heart disease and perioperative cardiac risk." *Br J Anaesth*
2004;92(4):570-583. doi:10.1093/bja/aeh091. PMID 15013960.
https://academic.oup.com/bja/article/92/4/570/251759 (full text retrieved)

- **30 observational studies**
- Pooled **OR 1.35 (95% CI 1.17–1.56)** for hypertensive disease vs perioperative cardiac outcomes
- Authors' verdict, verbatim: **"This association is statistically but not clinically
  significant."**
- **"There is little evidence for an association between admission arterial pressures of less
  than 180 mm Hg systolic or 110 mm Hg diastolic and perioperative complications."**
- **"anaesthesia and surgery should not be cancelled on the grounds of elevated preoperative
  arterial pressure."**
- Above 180/110 the authors acknowledge increased perioperative ischaemia, arrhythmias and
  cardiovascular lability, **but**: *"there is no clear evidence that deferring anaesthesia and
  surgery in such patients reduces perioperative risk."*

**This is where the 180/110 number originally comes from** — and note that even the paper that
anchors it says deferring above it has not been shown to help.

### POQI-3 consensus (2019) — the best modern synthesis **[GL, consensus]**

Sanders RD, Hughes F, Shaw A, et al., for the Perioperative Quality Initiative-3 Workgroup.
"Perioperative Quality Initiative consensus statement on preoperative blood pressure, risk and
outcomes for elective surgery." *Br J Anaesth* 2019;122(5):552-562.
doi:10.1016/j.bja.2019.01.018. PMID 30916006.
Open PDF: http://thepoqi.org/downloads/POQI-3%20Preop%20BP%202019.pdf (full text retrieved)

Four consensus statements, verbatim:

> **Consensus statement 1:** Preoperative arterial pressure values may be used to define targets
> for perioperative management; however, these should ideally reflect the patient's usual
> preoperative blood pressure.

> **Consensus statement 2:** Although extremes of preoperative blood pressure may be associated
> with increased perioperative risk, there is insufficient evidence to recommend a specific
> threshold of blood pressure upon which to decide whether or not to proceed with surgery,
> unless the extreme arterial pressure is associated with a medical emergency.

> **Consensus statement 3:** There is insufficient evidence to support lowering blood pressure
> in the immediate preoperative period to reduce perioperative risk.

> **Consensus statement 4:** There is insufficient evidence that any one measure of blood
> pressure (systolic pressure, diastolic pressure, MAP, or pulse pressure) is better than any
> other for risk prediction of adverse perioperative events.

And from the abstract: **"elective surgery should not be cancelled based solely upon a
preoperative arterial pressure value."**

POQI on the 180/110 threshold specifically — this is the most quotable passage in the whole
literature for the surgeon conversation:

> "The ACC/AHA and AAGBI/BHS guidelines suggest that elective surgery in patients with arterial
> pressure >180/110 mm Hg may be deferred; **however, this appears to be driven largely by
> expert opinion** (Table 1). **We were unable to identify consistent evidence that patients who
> underwent operations with preoperative arterial pressure above these values experienced
> increased harm.**"

POQI also names the **circularity** in the evidence base:

> "the data evaluated largely came from a period that was likely influenced by the expert
> opinion recommending deferral of surgery, potentially resulting in a lack of operations in
> patients with very high preoperative arterial pressure and a resultant lack of evidence."

POQI on the deferral studies (its refs 34 = Weksler, 35 = a subgroup analysis):

> "A small subgroup analysis of another study found similar event rates for postoperative
> myocardial injury and death in hypertensive patients deferred for surgery compared with those
> not deferred. **Importantly, a reduction in arterial pressure was not achieved by deferring
> surgery.** Consequently, **there is currently no evidence that deferring patients for better
> arterial pressure control changes their risk** unless they are manifesting acute pathological
> symptoms (defined as new onset end-organ damage) requiring urgent medical therapy."

### Newer data (2015–2026)

- **Insler J, Ortoleva JP, Notarianni AP.** "Reading Between the Guidelines: Perioperative
  Implications of the 2025 AHA/ACC Hypertension Update." *J Cardiothorac Vasc Anesth* 2026.
  doi:10.1053/j.jvca.2026.05.008. PMID 42250991. Abstract retrieved. Key line:
  *"Recommendations for surgical patients remain largely unchanged from prior iterations, with
  continued dependency on expert opinion and low-certainty evidence. Anesthesiologists are left
  to reconcile evolving outpatient management paradigms with conflicting perioperative data,
  including recent trials demonstrating no benefit from preoperative blood pressure optimization
  in noncardiac surgery."*
  **⚠️ I could not identify which specific trials that last clause refers to.** The recent large
  RCTs I located (IMPROVE-multi, PRETREAT) are trials of **intraoperative** BP management
  strategy, not of preoperative optimization/deferral — do not conflate them.
- **NCT06628648** — "Hypertension as a Reason for Cancellation of Elective Minor Abdominal
  Surgery," University Tunis El Manar. Prospective observational cohort, **n=120 actual**,
  started 2024-04, status **COMPLETED**, **no results posted**. Protocol: day-of-surgery SBP
  ≥180 and/or DBP ≥110 → fluid + 1 mg IV midazolam, recheck ×3; still high → postpone.
  https://clinicaltrials.gov/study/NCT06628648
  Worth watching, nothing citable yet.

**Bottom line for A2:** there has never been a trial showing that postponing an elective case for
blood pressure improves any outcome. The one RCT that exists showed no difference in
complications and a longer hospital stay in the postponed arm.

---

## A3. Anesthesia society position

### AAGBI / British Hypertension Society 2016 **[GL, consensus/GRADE]**

Hartle A, McCormack T, Carlisle J, et al. "The measurement of adult blood pressure and
management of hypertension before elective surgery. Joint Guidelines from the Association of
Anaesthetists of Great Britain and Ireland and the British Hypertension Society." *Anaesthesia*
2016;71(3):326-337. doi:10.1111/anae.13348. PMID 26776052.
Open PDF: https://preop.org.uk/wp-content/uploads/2016/05/2016-01-BP-guide-from-AAGBI.pdf
(full text retrieved)

Summary, verbatim:

> "This guideline aims to ensure that patients admitted to hospital for elective surgery are
> known to have blood pressures below 160 mmHg systolic and 100 mmHg diastolic in primary care.
> ... **Patients who present to pre-operative assessment clinics without documented primary care
> blood pressures should proceed to elective surgery if clinic blood pressures are below 180
> mmHg systolic and 110 mmHg diastolic.**"

Key recommendations, verbatim:

> - "General practitioners should refer patients for elective surgery with mean blood pressures
>   in primary care in the past 12 months less than 160 mmHg systolic and less than 100 mmHg
>   diastolic."
> - "Secondary care should accept referrals that document blood pressures below 160 mmHg
>   systolic and below 100 mmHg diastolic in the past 12 months."
> - "Pre-operative assessment clinics need not measure the blood pressure of patients being
>   prepared for elective surgery whose systolic and diastolic blood pressures are documented
>   below 160/100 mmHg in the referral letter."
> - "**Elective surgery should proceed** for patients who attend the pre-operative assessment
>   clinic without documentation of normotension in primary care **if their blood pressure is
>   less than 180 mmHg systolic and 110 mmHg diastolic when measured in clinic.**"

The guideline's own explanation of the two-tier threshold:

> "The disparity between the blood pressure thresholds for primary care (160/100 mmHg) and
> secondary care (180/110 mmHg) allows for a number of factors. Blood pressure reduction in
> primary care is based on good evidence that the rates of cardiovascular morbidity, in
> particular stroke, are reduced over years and decades. **There is no evidence that
> peri-operative blood pressure reduction affects rates of cardiovascular events beyond that
> expected in a month in primary care.**"

And on why it was written at all:

> "There is little evidence that raised pre-operative blood pressure affects postoperative
> outcomes. Local guidelines vary from area to area. **Hypertension is a common reason to cancel
> or postpone surgery.** In our sprint audit, 1–3% of elective patients had further
> investigations precipitated by blood pressure measurement, of whom half had their surgery
> postponed. Across the UK this would equate to ~100 concerned and inconvenienced patients each
> day."

Also explicitly: **"There is little guidance on a 'safe' blood pressure for planned anaesthesia
and surgery."**

### ⭐ 2026 UPDATE — thresholds have been RAISED **[GL, modified Delphi]**

McCormack T, Wickham A, McDonagh STJ, Wiles MD, Faconti L, Brooks R, Anderson SG, Hartle A.
"Measurement and management of adult blood pressure in the peri-operative period: updated
guidelines from the Association of Anaesthetists and the British and Irish Hypertension
Society." *Anaesthesia* 2026;81(3):402-414. doi:10.1111/anae.70082. PMID 41532177.
Open-access PDF retrieved from White Rose:
https://eprints.whiterose.ac.uk/id/eprint/236888/
(accepted 17 Sep 2025; supersedes the 2016 guideline)

**This matters — the diastolic proceed-threshold moved from 110 to 120.**

Recommendations verbatim (11 total; the relevant ones):

> **1.** "Patients referred for elective surgery should have a blood pressure measurement taken
> in a clinical setting in primary or secondary care in the past 12 months < 160/100 mmHg, or an
> ambulatory or home blood pressure measurement < 155/95 mmHg. Secondary care peri-operative
> teams should accept these blood pressure measurements (weak recommendation based on
> low-quality evidence)."

> **4.** "Patients who attend the pre-operative assessment clinic without documentation of
> normotension in primary care **may only proceed to elective surgery if their clinic blood
> pressure measurement is < 180/120 mmHg or ambulatory or home blood pressure measurement <
> 175/115 mmHg** (recommendation based on consensus opinion)."

> **7.** "**Patients should normally take their antihypertensive therapy, including
> angiotensin-converting enzyme inhibitors and angiotensin receptor blockers, on the day of
> surgery** (moderate recommendation based on moderate-quality evidence)."

> **8.** "Excess and prolonged intra-operative hypotension should be avoided. Intra-operative
> blood pressure management should be targeted to the individual patient and surgical procedure.
> Intra-operative targets that are used commonly in higher risk patients are **mean arterial
> pressure > 70 mmHg and/or systolic blood pressure > 100 mmHg** (moderate recommendation based
> on moderate-quality evidence)."

> **11.** "In the postoperative period, antihypertensive therapy should be reintroduced according
> to patients' blood pressure (weak recommendation based on moderate-quality evidence)."

**⚠️ Note the direct conflict with the 2024 ACC/AHA on ACEi/ARB — see A5.**

### ASA / ESAIC equivalent

**⚠️ Not found.** I located **no ASA (American Society of Anesthesiologists) practice guideline or
advisory that sets a numeric preoperative BP threshold** for proceeding vs cancelling. The ASA
Physical Status classification mentions "controlled hypertension" as an ASA II descriptor but
attaches no BP number and no cancellation rule. POQI-3 (above) is the closest thing to an
international anesthesiology consensus position and is co-authored by US academic
anesthesiologists (Duke, Brigham, Wisconsin) — use POQI as the "anesthesia says" citation for a
US audience.

---

## A4. Non-OR procedures — endoscopy, IR, cath, TEE, bronchoscopy

**Honest answer: there is no evidence base and, for endoscopy at least, no society threshold.
This is institutional custom. [CUSTOM]**

What I verified:

- **ASGE sedation guideline** — "Guidelines for sedation and anesthesia in GI endoscopy."
  *Gastrointest Endosc* 2018;87(2):327-337. PMID 29306520.
  Full text retrieved and searched:
  https://www.sages.org/wp-content/uploads/2013/04/SAGES_ASGE_Sedation_Endoscopy.pdf
  - Blood pressure appears **only as an intraprocedural monitoring parameter**: *"Monitoring may
    detect changes in pulse, blood pressure, ventilatory status... documentation of heart rate,
    blood pressure, respiratory rate, and oxygen saturation"* at five specified time points.
  - A full-text search for **"defer," "cancel," "postpone"** returns **zero hits** anywhere in
    the document. **There is no ASGE blood pressure threshold for proceeding with endoscopy.**
  - The only BP-adjacent mention is "controlled hypertension" as an example of ASA class II.

- **POQI explicitly disclaims procedure-specific thresholds:** *"We acknowledge that, for
  specific surgeries, for example, neurosurgery or endocrine surgery, specific pressure
  parameters may be recommended; however, this was considered beyond the scope of these general
  guidelines."* — i.e., even the consensus body declined to set numbers outside general surgery.

- **UK endoscopy accreditation body (JAG)** states plainly there is **"no national guidance
  regarding blood pressure limits before endoscopy procedures,"** while noting it is good
  practice to record observations.
  https://thejag.zendesk.com/hc/en-us/articles/360008770493

- The only numbers circulating in the GI literature (pre-procedure SBP >180 and/or DBP >120 as
  "unsafe") are **expert opinion extrapolated from the OR literature**, not derived from
  endoscopy outcome data.

- One small ACG abstract (Am J Gastroenterol 2011 suppl) reported 10 patients who underwent
  colonoscopy despite SBP >180 with **no difference in mean procedural and post-procedural heart
  rate, respiratory rate, or oxygen saturation** vs better-controlled patients.
  **⚠️ n=10, conference abstract, full text paywalled (HTTP 402). Too weak to cite on a cheat
  sheet** — mention only as "the little data that exist show no signal."

**⚠️ Could not verify anything at all for interventional radiology, cardiac catheterization, TEE,
or bronchoscopy.** No society document from SIR, SCAI, ASE, or CHEST/AABIP sets a pre-procedure
BP threshold that I could locate. Treat any such local rule as pure institutional policy.

---

## A5. If you do decide to lower it before a case — what's actually appropriate

### First-line: give the held home dose **[GL]**

- 2024 ACC/AHA: **"Continue most antihypertensive agents."**
- 2026 Association of Anaesthetists/BIHS **Recommendation 7**: *"Patients should normally take
  their antihypertensive therapy, including angiotensin-converting enzyme inhibitors and
  angiotensin receptor blockers, on the day of surgery"* (moderate rec, moderate-quality
  evidence).
- The single commonest fixable cause of a high pre-op number is that somebody made the patient
  NPO at midnight and the morning antihypertensives never went in. The AHA acute-care statement
  lists "holding of usual antihypertensive medications" among the treatable causes of elevated
  inpatient BP.

**Practical: the right "single oral dose" is almost always the patient's own held morning dose,
given with a sip of water.** There is no evidence supporting adding a *different* drug.

### ⚠️ MAJOR UNRESOLVED CONFLICT — ACEi/ARB on the day of surgery

| Source | Position |
|---|---|
| **2024 ACC/AHA** | **COR 2b:** "Hold RAASi in patients with controlled BP and undergoing elevated-risk surgical procedures 24 hours prior to surgery to limit intraoperative hypotension." **COR 2a:** "In patients with HFrEF, continue chronic RAASi." |
| **POQI-3 2019, Practice rec 1** | "Unless clinically contraindicated, withhold ACEIs/ARBs 24 h before surgery with attention to restarting the medications within 48 h after operation where appropriate." |
| **2026 Assoc. Anaesthetists/BIHS, Rec 7** | "Patients should **normally take** their antihypertensive therapy, **including** ACE inhibitors and ARBs, **on the day of surgery.**" |

**Flag this on the cheat sheet as unsettled rather than picking a side.** The US guideline and
the 2019 international consensus say hold 24h for elevated-risk surgery; the newest (2026) UK
anesthesia guideline says take it. POQI's own rationale: a VISION analysis suggested withholding
ACEi/ARB may reduce mortality, stroke and myocardial injury, but POQI explicitly says *"We
believe that a prospective randomised controlled trial is needed to confirm whether ACEI/ARB
withdrawal improves outcomes."* Also note POQI: *"delayed or omitted reinstitution of ACEIs/ARBs
has been associated with increased postoperative mortality."*

### Class-by-class — 2024 ACC/AHA perioperative guideline **[GL]**

| Class | Recommendation | COR |
|---|---|---|
| **Beta blockers** | "Continue chronic stable beta blocker therapy." | **Class 1** |
| **Beta blockers** | "If new beta blocker therapy is indicated, initiate therapy at least 7 days prior to NCS." (CCJM review says "at least 8 days before surgery to assess tolerability and dose titration") | **Class 2b** |
| **Beta blockers** | "**Beta blocker without immediate need should not be initiated on the day of surgery.**" | **Class 3: Harm** |
| **ACEi/ARB (RAASi)** | "Hold RAASi in patients with controlled BP and undergoing elevated-risk surgical procedures 24 hours prior to surgery to limit intraoperative hypotension." | **Class 2b** |
| **ACEi/ARB (RAASi)** | "In patients with HFrEF, continue chronic RAASi." | **Class 2a** |
| **Clonidine** | "**Initiation of low-dose clonidine is not recommended.**" | **Class 3: No Benefit** |
| **Clonidine** | Continue it if already taking it, to avoid rebound hypertension (narrative, per CCJM review) | — |
| **CCBs, thiazides, K-sparing diuretics** | Continue perioperatively | — |
| **Loop diuretics** | Per-patient decision (POQI practice rec 4) | — |
| **SGLT2 inhibitors** | Withhold 3–4 days before surgery (4 for ertugliflozin) — euglycemic DKA risk | — |
| **Statins** | Continue if already taking | — |

Carried forward from the **2017 ACC/AHA hypertension guideline** (reproduced verbatim in POQI
Table 1) — the two "never" recommendations the question asked for:

> **COR III: Harm, LOE B-NR** — "For patients undergoing surgery, **abrupt preoperative
> discontinuation of beta blockers or clonidine is potentially harmful.**"

> **COR III: Harm, LOE B-NR** — "**Beta blockers should not be started on the day of surgery in
> beta-blocker-naïve patients.**"

> **COR I, LOE B-NR** — "In patients with hypertension undergoing major surgery who have been on
> beta blockers chronically, **beta blockers should be continued.**"

> **COR IIa, LOE C-EO** — "In patients with hypertension undergoing planned elective major
> surgery, it is reasonable to continue medical therapy for hypertension until surgery."

### Why NOT IV hydralazine or labetalol the morning of **[OBS + mechanism]**

1. **It is the one thing shown to carry the most risk.** Anderson TS et al, *JAMA Intern Med*
   2023 (n=66,140): among intensively treated hospitalized older adults the composite harm
   signal was **weighted OR 1.28 (95% CI 1.18–1.39)** overall but **weighted OR 1.90 (95% CI
   1.65–2.19) in those receiving intravenous antihypertensives** — the highest-risk subgroup in
   the study. (Full details in B.)
2. **The magnitude and duration of effect are unpredictable**, and you are about to stack it on
   induction agents that drop MAP by themselves. The harm in the perioperative setting is the
   *overshoot*, not the starting number — see A6.
3. **Guideline language is explicit.** Breu & Axon TWDFNR: *"Do not administer intravenous or
   immediate-acting oral antihypertensive medications to acutely lower blood pressure."*
   2025 AHA/ACC Rec 6.2.4 is **Class 3: Harm** for intermittent IV or oral dosing in hospitalized
   patients without target organ damage.
4. **POQI Consensus statement 3** says flatly there is insufficient evidence that lowering BP
   immediately preoperatively reduces risk at all — so you are accepting a known hypotension
   risk for an unproven benefit.

### Rest alone works surprisingly often **[TRIAL]**

From Breu AC, Axon RN, "Things We Do for No Reason: Acute Treatment of Hypertensive Urgency,"
*J Hosp Med* 2018;13(12):860-862, doi:10.12788/jhm.3086 (full text in hand):

> "patients should be allowed to rest for at least 30 minutes without the administration of
> additional antihypertensive medications, after which time the blood pressure should be
> measured using the correct technique. **Clinical trials have shown that rest is effective at
> lowering blood pressure in patients with hypertensive urgency.**"

- One study of **549 ED patients**: after a 30-minute rest period, **32% responded** (SBP <180
  and DBP <110, with ≥20 mm Hg SBP and/or ≥10 mm Hg DBP reduction).
- An RCT of **138 patients** randomized to rest vs telmisartan, BP checked q30min ×4h: primary
  endpoint (MAP reduction 10–35%) reached in **68.5% with rest vs 69.1% with telmisartan** —
  essentially identical.

**Cheat-sheet-worthy:** before doing anything pharmacologic in pre-op holding, recheck with a
correctly sized cuff after 30 minutes of rest, and treat pain/anxiety/full bladder. One in three
resolves on rest alone, and rest performed as well as an ARB in a randomized comparison.

---

## A6. Intraoperative consequence — hypotension, myocardial injury, and whether pre-op treatment makes it worse

### Salmasi V, Maheshwari K, Yang D, Mascha EJ, Singh A, Sessler DI, Kurz A. **[OBS, large]**

"Relationship between Intraoperative Hypotension, Defined by Either Reduction from Baseline or
Absolute Thresholds, and Acute Kidney and Myocardial Injury after Noncardiac Surgery: A
Retrospective Cohort Analysis." *Anesthesiology* 2017;126(1):47-65.
doi:10.1097/ALN.0000000000001432
Abstract retrieved in full.

- **MAP below an absolute threshold of 65 mmHg, or a relative threshold of 20% below
  preoperative pressure, was progressively related to both myocardial and kidney injury.**
- **"At any given threshold, prolonged exposure was associated with increased odds."**
- **"There were no clinically important interactions between preoperative blood pressures and
  the relationship between hypotension and myocardial or kidney injury at intraoperative mean
  arterial blood pressures less than 65 mmHg."**
- **"Absolute and relative thresholds had comparable ability to discriminate patients with
  myocardial or kidney injury from those without."**
- Conclusion, verbatim: **"The associations based on relative thresholds were no stronger than
  those based on absolute thresholds. Furthermore, there was no clinically important interaction
  with preoperative pressure. Anesthetic management can thus be based on intraoperative
  pressures without regard to preoperative pressure."**

### Cohen B, Rivas E, Yang D, Mascha EJ, Ahuja S, Turan A, Sessler DI. **[OBS]**

"Intraoperative Hypotension and Myocardial Injury After Noncardiac Surgery in Adults With or
Without Chronic Hypertension: A Retrospective Cohort Analysis." *Anesth Analg*
2022;135(2):329-340. doi:10.1213/ANE.0000000000005922
Abstract retrieved in full.

- **n = 4,576** noncardiac surgeries, adults >45 y, scheduled (not symptom-driven) postoperative
  troponins.
- Normotensive group n=2,066, mean baseline MAP **100 (SD 7)**; hypertensive group n=2,510, mean
  baseline MAP **122 (SD 10)**.
- Composite (in-hospital mortality + myocardial injury within 30 d, troponin T ≥0.03 ng/mL):
  **5.6% normotensive vs 6.0% hypertensive, P = 0.55.**
- **"The relationship between intraoperative hypotension and the composite outcome was not found
  to depend on baseline MAP... no statistical change points were found for either baseline MAP
  group."**
- Conclusion, verbatim: **"we were not able to demonstrate a difference in the harm threshold
  between normotensive and chronically hypertensive patients. Our results do not support the
  theory that hypertensive patients should be kept at higher intraoperative pressures than
  normotensive patients."**

**This directly refutes the most common pro-treatment argument**, which is "he runs high, so
anesthesia will have to keep him high, so we should fix the number first."

### MAP thresholds and duration — numbers for the card

- **MAP <65 mmHg** = the consensus harm threshold for myocardial and kidney injury
  (Salmasi 2017). 2024 ACC/AHA **Class 1**: maintain **MAP ≥60–65 or SBP ≥90** intraoperatively.
- **2026 Assoc. Anaesthetists Rec 8**: targets commonly used in higher-risk patients are
  **MAP >70 and/or SBP >100**.
- **Duration matters as much as depth.** ⚠️ A frequently quoted gradient for MAP ≤60 mmHg is
  MINS odds **1.54 for 1–5 min rising to 3.81 for ≥21 min** — **I obtained this from a search
  summary and could NOT verify it against a primary source. Do not put these two numbers on the
  cheat sheet without checking the source article.** The qualitative claim (risk rises with
  cumulative minutes below threshold) is solidly supported by Salmasi 2017.

### Does pre-op treatment of chronic hypertension increase intraoperative hypotension?

- **For ACEi/ARB specifically: yes, probably.** POQI: a VISION analysis "suggested that
  withholding ACEIs/ARBs before surgery may reduce the risk of mortality, stroke, and myocardial
  injury, supporting prior concerns that these drugs may be associated with intraoperative
  haemodynamic instability." This is the entire rationale for the 2024 ACC/AHA Class 2b hold.
- **For acute day-of lowering: no direct trial data**, but mechanistically this is the concern,
  and POQI Consensus statement 3 declines to endorse the practice.
- **Historical anchor** (POQI cites it): **Prys-Roberts 1971** showed that patients with
  *untreated* hypertension (MAP ~130) had intraoperative hypotension, and **5 of 7 sustained
  myocardial ischaemia associated with MAP changes >50% from baseline.** Note the injury tracked
  the *swing*, not the baseline.

**Synthesis for the card:** the perioperative danger is the *drop*, not the *number*. Treating
the number the morning of surgery makes the drop bigger.

---

# B. DISCHARGE WITH AN ELEVATED BP

## B1. Is there any standard that says do not discharge above a given BP?

# ⭐ NO. Your suspicion is correct, and it is documented.

**[GL — systematic review of guidelines]**

Cohen JB et al. (Anderson TS senior author group). "Management of Inpatient Elevated Blood
Pressures: A Systematic Review of Clinical Practice Guidelines." *Ann Intern Med*
2024;177(4):497-506. doi:10.7326/M23-3251. PMID 38560900. PMC11103512.
https://pmc.ncbi.nlm.nih.gov/articles/PMC11103512/
(abstract retrieved in full via Europe PMC; full text via PMC)

Searched MEDLINE, Guidelines International Network, and specialty society websites from
1 Jan 2010 to 29 Jan 2024. **14 clinical practice guidelines** met inclusion criteria (11 rated
high-quality by AGREE II): ACC/AHA 2017, ACEP 2013, ACP/AAFP 2017, Brazilian SBC 2020,
British/Irish BIHS 2022, ESH 2023, Hypertension Canada 2020, Japanese JSH 2019, National Heart
Foundation Australia 2016, NICE 2022, Polish PSH 2015, Qatari QMoH 2021, VA/DoD 2020, WHO 2021.

Verbatim findings:

> **"No guidelines provided goals for inpatient BP or recommendations for managing asymptomatic
> moderately elevated BP in the hospital."**

> **"No guidelines provided an inpatient BP target or guidance on antihypertensive classes to
> use in the inpatient setting."**

> **"there were no recommendations relating to the management of BP during transitions from
> hospital to home, even after hypertensive urgency or emergency."**

> Conclusion: **"Despite general consensus on outpatient BP management, guidance on inpatient
> management of elevated BP without symptoms is lacking, which may contribute to variable
> practice patterns."**

**Verdict: [CUSTOM].** Fourteen guidelines across eleven countries, and not one sets a BP
threshold for hospital discharge. Any local "don't discharge above X" rule is institutional
custom with no society backing.

### The AHA names the custom explicitly

From the 2024 AHA acute-care scientific statement (full text in hand) — this passage is about ED
→ floor transfer, but the mechanism it describes is exactly the discharge situation:

> "**Admitting services can also ask that patients in the ED with markedly elevated BP first have
> the BPs be lowered to more 'acceptable' levels before patient transfer, a practice that may be
> reinforced by institutional policies. Such policies, although well intended, may perpetuate a
> culture of routinely treating asymptomatic elevated inpatient BP, even in the absence of
> evidence of benefit.**"

And:

> "**In general, it is prudent to avoid PRN orders for antihypertensive medications to treat
> asymptomatic elevated inpatient BP.**"

---

## B2. 2025 AHA/ACC hypertension guideline — transitions of care, discharge, follow-up

**Citation:** 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM Guideline for the
Prevention, Detection, Evaluation and Management of High Blood Pressure in Adults.
*Hypertension* 2025, doi:10.1161/HYP.0000000000000249 —
https://www.ahajournals.org/doi/10.1161/HYP.0000000000000249
(also *Circulation*, doi:10.1161/CIR.0000000000001356)

### The one recommendation that governs the inpatient number **[GL]**

> **Recommendation 6.2.4 — COR 3: Harm, LOE B-NR**
> "For adults with severe hypertension (>180/120 mm Hg) who are hospitalized for noncardiac
> conditions without evidence of acute target organ damage, intermittent use of additional IV or
> oral antihypertensive medications are not recommended to acutely reduce BP."

Contrast — the emergency pathway **[GL]**:

> **Recommendation 6.2.1 — COR 1, LOE B-R**
> "In adults with a hypertensive emergency (BP >180 and/or >120 mm Hg and evidence of acute
> target organ damage), admission to an intensive care unit is recommended for continuous
> monitoring of BP and target organ damage and for consideration of parenteral administration of
> appropriate therapy."

### On discharge specifically

- **There is no recommendation setting a BP threshold for discharge.** Confirmed against the
  Annals systematic review (B1) and against the guideline summaries.
- Severe hypertension >180/120 **without** acute target organ damage should be **"evaluated and
  treated in the outpatient setting with initiation, reinstitution, or intensification of oral
  antihypertensive medications in a timely manner."** — note the words *reinstitution* and
  *outpatient*.
- The discharge plan should include **medications, home BP monitoring (HBPM), and follow-up**,
  with patient education on return precautions (neurologic symptoms, chest pain, dyspnea, vision
  changes, anuria).
- **Follow-up:** monthly until BP is controlled in adults with uncontrolled hypertension on new
  or intensified therapy; **BMP (electrolytes, eGFR) 2–4 weeks after initiation or up-titration.**

**⚠️ Verification caveat:** ahajournals.org returns HTTP 403 to automated fetch and I could not
read the guideline PDF directly. Recommendation 6.2.4 wording and its **COR 3: Harm / LOE B-NR**
designation came from the Guideline Central structured summary
(https://www.guidelinecentral.com/guideline/6962/) and were corroborated by independent search
results and by the fact that the cheat sheet already carries this Class 3: Harm claim. The
discharge/follow-up items above are from guideline summaries, not the primary text. **Confirm
via UCSF library access before quoting verbatim.**

---

## B3. Anderson TS et al, JAMA Intern Med 2019 — CONFIRMED, all numbers

"Clinical Outcomes After Intensifying Antihypertensive Medication Regimens Among Older Adults at
Hospital Discharge." *JAMA Intern Med* 2019;**179**(11):**1528**-1536.
doi:10.1001/jamainternmed.2019.3007. PMID 31424475.
https://pubmed.ncbi.nlm.nih.gov/31424475/
(abstract retrieved in full via NCBI eutils — every number below is verbatim from the abstract)

| Item | Value |
|---|---|
| Design | Retrospective cohort, propensity-matched pairs; VA national system, 2011–2013, noncardiac admissions |
| Cohort | **4,056** adults ≥65 with hypertension; mean age **77 (SD 8)**; **3,961 men (97.7%)** |
| Exposure | New or higher-dose antihypertensive prescribed at discharge vs pre-hospitalization regimen |
| **30-day readmission** | **HR 1.23 (95% CI 1.07–1.42); NNH 27 (95% CI 16–76)** |
| **30-day serious adverse events** | **HR 1.41 (95% CI 1.06–1.88); NNH 63 (95% CI 34–370)** |
| **1-year cardiovascular events** | **HR 1.18 (95% CI 0.99–1.40)** — not significant |
| **1-year systolic BP** | **134.7 vs 134.4 mm Hg; difference-in-differences 0.6 mm Hg (95% CI −2.4 to 3.7)** |

Conclusion, verbatim:

> "Among older adults hospitalized for noncardiac conditions, prescription of intensified
> antihypertensives at discharge **was not associated with reduced cardiac events or improved BP
> control within 1 year** but **was associated with an increased risk of readmission and serious
> adverse events within 30 days.**"

**The killer line for the cheat sheet:** one year later the BP was **0.6 mm Hg** different — and
you bought a readmission for every 27 patients.

### Companion: Anderson TS et al, JAMA Intern Med 2023 (inpatient, not discharge)

"Clinical Outcomes of Intensive Inpatient Blood Pressure Management in Hospitalized Older
Adults." *JAMA Intern Med* 2023;183(7):715-723. doi:10.1001/jamainternmed.2023.1667.
PMID 37252732. (abstract retrieved in full)

- **n = 66,140** VA patients ≥65 hospitalized for noncardiovascular diagnoses with elevated BP
  in the first 48 h; mean age 74.4 (SD 8.1).
- **14,084 (21.3%)** received intensive treatment (IV antihypertensives or oral classes not used
  prior to admission) in the first 48 h.
- Treated patients then received **6.1 (95% CI 5.8–6.4)** additional antihypertensive doses vs
  **1.6 (95% CI 1.5–1.8)** — i.e. treating once begets treating repeatedly.
- Primary composite (inpatient mortality, ICU transfer, stroke, AKI, BNP elevation, troponin
  elevation): **1,220 (8.7%) vs 3,570 (6.9%); weighted OR 1.28 (95% CI 1.18–1.39)**.
- **Highest risk in those receiving IV antihypertensives: weighted OR 1.90 (95% CI 1.65–2.19).**
- Findings consistent across subgroups by age, frailty, preadmission BP, early hospitalization
  BP, and CVD history.
- Conclusion: **"These findings do not support the treatment of elevated inpatient BPs without
  evidence of end organ damage."**

---

## B4. Treating today's number vs treating the chronic disease — the line that matters

**Yes, this line is drawn explicitly, in several places.** This is the most useful distinction in
section B, because it lets you say "no" to the reflex and "yes" to the legitimate clinical need
in the same breath.

### The clearest statement — Breu & Axon TWDFNR **[GL-adjacent, SHM series]**

Breu AC, Axon RN. "Things We Do for No Reason: Acute Treatment of Hypertensive Urgency."
*J Hosp Med* 2018;13(12):860-862. doi:10.12788/jhm.3086 (full text in hand)

Recommendations, verbatim:

> - "Ensure that patients do not have symptoms and/or signs of end-organ damage..."
> - "Search for common causes of treatable hypertension in hospitalized patients; these include
>   pain, nausea, withdrawal syndromes, and holding of usual antihypertensive medications."
> - "In those patients without symptoms and/or signs of end-organ damage, allow rest, followed by
>   reassessment."
> - "**Do not administer intravenous or immediate-acting oral antihypertensive medications to
>   acutely lower blood pressure. Instead**, address the issues raised in Recommendation #2 and
>   **consider modifying the chronic oral antihypertensive regimen in patients who are
>   uncontrolled as outpatients or who are not treated as outpatients. Coordinate early
>   postdischarge follow-up for repeat blood pressure evaluation and continued modification of a
>   patient's chronic antihypertensive regimen.**"

And in the body:

> "If blood pressure remains consistently elevated, **augmentation of the home regimen (eg,
> increasing the dose of their next scheduled antihypertensive) of oral medications may be
> warranted.** Though not all agree with management of antihypertensives in hospitalized
> patients, **acute hospitalizations afford an opportunity to modify and observe chronic
> hypertension.**"

**That is exactly the line:** not a PRN to move today's number; a change to the *scheduled
long-acting regimen* in someone genuinely untreated or undertreated, plus early follow-up.

### The AHA 2024 acute-care statement draws the same line **[GL, scientific statement]**

Bress AP et al. "The Management of Elevated Blood Pressure in the Acute Care Setting: A
Scientific Statement From the American Heart Association." *Hypertension* 2024;81(8):e94-e106.
doi:10.1161/HYP.0000000000000238. PMID 38804130.
https://www.ahajournals.org/doi/10.1161/HYP.0000000000000238 (full text in hand)

From "Optimizing Transitions of Care → Disposition After Hospital Admission," verbatim:

> "For patients with elevated inpatient BP with or without a preadmission diagnosis of
> hypertension, there are **2 crucial steps at discharge: (1) careful review and adjustment of
> medication with adequate patient counseling and (2) planning for future care coordination.**
> **The best available evidence suggests maintaining the prehospitalization antihypertensive
> medication regimen and avoiding intensification at discharge.**"

> "Assessment of the entire medication regimen at discharge is essential, focusing on identifying
> **guideline-discordant antihypertensive regimens** because many patients receive
> antihypertensive medications that do not align with guideline-recommended classes. **Any new
> antihypertensive medication initiated during the admission should align with the 2017
> Hypertension Clinical Practice Guidelines** and should account for factors that could affect
> treatment effectiveness and medication adherence such as health literacy, health insurance,
> affordability, social support, and self-management resources."

> "Among US adults with hypertension, ≈18% take at least 1 medication that can increase inpatient
> BP, and **these medications should be discontinued when possible.**"

> "some patients might **prefer to delay any changes until they recover from their acute illness
> and can reassess with their primary care clinician.**"

So: default = **don't intensify**; but if the regimen is *guideline-discordant* or the patient is
genuinely untreated, fix the *regimen* (correct class, long-acting, affordable), not the number.

### Adherence caveat that argues for fixing the regimen rather than adding drugs

Same AHA statement:

> "**one-third of antihypertensive medications prescribed at hospital discharge were never
> refilled, and half were discontinued by the end of the first year.**"

> "**1 in 7 patients experiences confusion about their medication, leading to a higher risk of
> readmission.**"

> Fixed-dose combinations "can improve adherence, help achieve adequate BP control sooner, and
> reduce medication burden," yet only **27%** of US adults on ≥2 antihypertensives use them.

### AFP 2026 says the same, more bluntly

"Severe Hypertension: Evaluation and Treatment." *Am Fam Physician* 2026 (May issue).
https://www.aafp.org/afp/2026/0500/severe-hypertension — PMID 42202349

> "**BP levels can take days to weeks to respond to medication changes, and these changes are
> best initiated in outpatient primary care.**"

> "Patients with severe asymptomatic hypertension (BP > 180/110 mm Hg) should be treated with
> oral therapy **only if they are at high risk for inpatient complications and if secondary
> causes have been excluded or addressed.**"

> "**Use of short-acting or intravenous antihypertensive medications is associated with adverse
> outcomes and is not recommended.**"

> Management principle: "**Gradual blood pressure reduction over several days to weeks.**"

### The data proving the line is currently NOT being drawn **[OBS]**

Anderson TS, Jing B, Auerbach A, et al. "Intensification of older adults' outpatient blood
pressure treatment at hospital discharge: national retrospective cohort study." *BMJ*
2018;362:k3503. doi:10.1136/bmj.k3503. PMID 30209052.
(abstract retrieved in full — this is the sharpest evidence for the distinction)

- **n = 14,915** VA patients ≥65 with hypertension, noncardiac admissions 2011–2013, median age
  76 (IQR 69–84).
- **9,636 (65%) had well-controlled outpatient BP before hospital admission.**
- **2,074 (14%)** were discharged with intensified antihypertensive treatment — **more than half
  of whom (1,082) had well-controlled BP before admission.**
- Among patients with **previously well-controlled outpatient BP**, intensification rate scaled
  with the *inpatient* number:
  - **8% (95% CI 7–9%)** if no elevated inpatient BP
  - **24% (95% CI 21–26%)** if moderately elevated inpatient BP
  - **40% (95% CI 34–46%)** if severely elevated inpatient BP
- **"No differences were seen in rates of intensification among patients least likely to benefit
  from tight blood pressure control (limited life expectancy, dementia, or metastatic
  malignancy), nor in those most likely to benefit (history of myocardial infarction,
  cerebrovascular disease, or renal disease)."**

**This is the whole argument in one study:** discharge intensification tracked *the inpatient
reading* and was completely blind to *who would actually benefit*. That is treating the number,
not the disease.

---

## B5. Follow-up interval after discharge with an elevated BP

| Source | Recommended interval |
|---|---|
| **Annals 2024 systematic review of 14 guidelines** (after hypertensive urgency) | **3 guidelines: within 7 days. 2 guidelines: within 1–3 days. 3 guidelines: unspecified.** Overall summary: *"Outpatient treatment with oral medications and follow-up in days to weeks were most often advised."* |
| **2025 AHA/ACC guideline** | **Monthly until BP controlled** on new/intensified therapy; **BMP at 2–4 weeks** after initiation or up-titration |
| **AFP 2026** | *"BP levels can take days to weeks to respond"*; changes best initiated in outpatient primary care; out-of-office BP monitoring recommended |
| **AHA 2024 acute-care statement** | No numeric interval. *"establishing a follow-up appointment with the primary care clinicians is crucial"*; *"all necessary follow-up appointments with the primary care clinicians or pharmacist are scheduled before discharge"*; home BP monitoring with a **validated** device |
| **Breu & Axon TWDFNR 2018** | *"Coordinate early postdischarge follow-up for repeat blood pressure evaluation"* — no number |

**Practical synthesis for the card: follow-up within 7 days is the modal guideline
recommendation; 1–3 days if the BP was severe or you changed the regimen; recheck a BMP at 2–4
weeks if you started or up-titrated an ACEi/ARB/diuretic.**

**⚠️ Peixoto NEJM 2019 — COULD NOT VERIFY.** Peixoto AJ. "Acute Severe Hypertension." *N Engl J
Med* 2019;**381**(19):**1843-1852**. doi:10.1056/NEJMcp1901117. PMID 31693807. Citation
confirmed via Europe PMC, but **every full-text route failed** (nejm.org paywalled; one
open-mirror PDF had an invalid SSL certificate; no PMC deposit). I could only confirm the general
position via secondary sources — that asymptomatic acute severe hypertension without target-organ
damage is not associated with adverse short-term outcomes and can be managed in the ambulatory
setting with oral medications and prompt follow-up. **The specific NEJM follow-up interval is
unverified — do not attribute a number to Peixoto without reading it.**

---

## B6. Is inpatient BP even a valid measure of the patient's true BP?

**Your belief is directionally right and well supported, but the cleanest number is not the one
usually quoted. Be careful here.**

### What I can verify from a primary source **[OBS]**

- **Anderson TS et al, BMJ 2018;362:k3503** (abstract verbatim): of 14,915 hospitalized older
  adults with hypertension, **9,636 (65%) had well-controlled outpatient BP before hospital
  admission.** Among those with previously well-controlled BP, **40% (95% CI 34–46%)** of the
  severely-elevated-inpatient-BP group got intensified anyway.
  **This is the strongest verified number: roughly two-thirds of hospitalized hypertensives were
  controlled as outpatients before they came in.**

### The commonly cited "~half were normotensive before admission" **⚠️**

The figure **"nearly half of patients with elevated inpatient BP had normotensive BP before
admission"** (often rendered as **47%**) appears in:
- the SHM *Things We Do for No Reason* article (Rachoin et al 2024), attributed to a 2018 VHA study;
- the ACC "When Should We Treat Elevated Inpatient Blood Pressure?" review (2024),
  https://www.acc.org/latest-in-cardiology/articles/2024/10/28/10/47/when-should-we-treat-elevated-inpatient-blood-pressure

**⚠️ I could not trace this to a primary source stating it in those exact terms with a CI.** It is
almost certainly a restatement of the Anderson 2018 BMJ data. **Recommend citing the verified BMJ
figure (65% well-controlled before admission) rather than the 47%/"nearly half" figure**, unless
you can pull the Rachoin full text and check its reference.

### Other supporting findings (secondary sources — flagged)

From the ACC 2024 review (secondary, citations as given there):
- **Gaynor et al 2018:** "41% of patients prescribed as needing antihypertensive agents in the
  inpatient setting were not receiving their recommended regimens at home."
- **Anderson et al 2018:** "one-half of patients discharged on additional BP medications had good
  BP control before hospital admission." (concordant with the BMJ 1,082/2,074 = 52% figure —
  **this one IS verifiable from the BMJ abstract**)

From the AHA 2024 statement and AFP 2026 — mechanisms, well supported qualitatively:
- transient elevations triggered by **anxiety, hypervolemia, pain, withdrawal of home
  medications**, nausea, fever, sleep deprivation;
- **≈18% of US adults with hypertension take ≥1 medication that can raise inpatient BP;**
- measurement technique in hospital deviates from guideline technique, systematically
  **overestimating** BP (an audit reporting 100% deviation from NICE/ESH technique is cited in
  the secondary literature — **⚠️ single audit, secondary citation, do not quote the 100% figure
  on a cheat sheet**).

From the AHA 2024 statement, verbatim — the nocturnal-PRN vicious cycle, which is a nice
mechanistic point:

> "PRN parenteral antihypertensive orders may be used to minimize disturbances from overnight
> calls or pages... potentially lowering morning BP enough to withhold morning oral
> antihypertensive medications. Consequently, evening BP readings might run higher, contributing
> to a recurrent pattern of high BP at night and **increased overall BP variability.**"

**Safe cheat-sheet formulation:** *"Two-thirds of hospitalized patients with hypertension were
already controlled as outpatients before admission (Anderson, BMJ 2018). The inpatient number is
measured badly, in pain, off home meds, and does not predict the outpatient number."*

---

## B7. TWDFNR / Choosing Wisely / SHM items

| Item | Citation | Status |
|---|---|---|
| **TWDFNR: Intensifying antihypertensive medications for hospitalized patients at the time of discharge** | Rachoin JS, Cerceo E, Anderson TS. *J Hosp Med* 2024;**19**(3):**219-222**. doi:10.1002/jhm.13185. PMID 37545427 | Citation **verified** via PubMed + Europe PMC. **⚠️ Full text NOT retrieved** (Wiley 403, no PMC deposit, no abstract in PubMed). Content below is from secondary summaries only. |
| **TWDFNR: Acute Treatment of Hypertensive Urgency** | Breu AC, Axon RN. *J Hosp Med* 2018;**13**(12):**860-862**. doi:10.12788/jhm.3086 | **Full text in hand.** Runs under the *"Choosing Wisely®: Things We Do for No Reason"* banner. |
| **Editorial: Treatment of Inpatient Asymptomatic Hypertension: Not a Call to Act but to Think** | Anstey J, Lucas BP. *J Hosp Med* 2019;**14**(3):**190-191**. doi:10.12788/jhm.3160 | **Full text in hand.** |
| **QI: Assess Before Rx — Reducing the Overtreatment of Asymptomatic Blood Pressure Elevation in the Inpatient Setting** | Pasik SD et al. *J Hosp Med* 2019. doi:10.12788/jhm.3190 | Reduced IV antihypertensive use **60%**; ~half of treated patients had an adverse event; followed 111 untreated elevated-BP patients with **no adverse outcomes** |
| **QI: Jacobs et al** | *J Hosp Med* 2019 | **11%** of asymptomatic-hypertension patients treated inappropriately with IV agents, **14%** of those had an adverse event; liberalizing nursing call parameters from **160/80 → 180/90** cut IV orders **40%** |

**Known content of the Rachoin 2024 TWDFNR (secondary sources, flagged ⚠️):**
- Hospitalists extrapolate *outpatient* BP goals to *hospitalized* patients — the core error.
- Cites the 2018 VHA finding that nearly half of patients with elevated inpatient BP were
  normotensive before admission, and that **11.2%** of patients with controlled outpatient BP
  still had their regimen intensified.
- Bottom line: close outpatient follow-up and monitoring rather than intensification at discharge.

**⚠️ On "Choosing Wisely" specifically:** the SHM *Things We Do for No Reason* series is published
under the Choosing Wisely® banner, but I found **no item on the official Society of Hospital
Medicine Choosing Wisely list** that addresses discharge BP or asymptomatic inpatient
hypertension. **Do not write "Choosing Wisely recommends…" on the cheat sheet** — write "SHM's
Things We Do for No Reason series," which is accurate.

---

# C. WHAT TO SAY — published, quotable, sourced

Everything below is a real quotation from a real source. Nothing here is invented.

## For the surgeon / proceduralist

**1. The direct one (international anesthesia consensus):**
> "Elective surgery should not be cancelled based solely upon a preoperative arterial pressure
> value."
> — POQI-3 consensus statement, *Br J Anaesth* 2019;122:552-562

**2. When they name a threshold:**
> "There is insufficient evidence to recommend a specific threshold of blood pressure upon which
> to decide whether or not to proceed with surgery, unless the extreme arterial pressure is
> associated with a medical emergency."
> — POQI-3, Consensus statement 2

**3. When they ask you to bring it down first:**
> "There is insufficient evidence to support lowering blood pressure in the immediate
> preoperative period to reduce perioperative risk."
> — POQI-3, Consensus statement 3

**4. When they cite the 180/110 rule:**
> "The ACC/AHA and AAGBI/BHS guidelines suggest that elective surgery in patients with arterial
> pressure >180/110 mm Hg may be deferred; however, this appears to be driven largely by expert
> opinion. We were unable to identify consistent evidence that patients who underwent operations
> with preoperative arterial pressure above these values experienced increased harm."
> — POQI-3, *Br J Anaesth* 2019

**5. The classic:**
> "Anaesthesia and surgery should not be cancelled on the grounds of elevated preoperative
> arterial pressure."
> — Howell, Sear & Foëx, *Br J Anaesth* 2004;92:570-583

**6. On the risk magnitude (OR 1.35):**
> "This association is statistically but not clinically significant."
> — Howell, Sear & Foëx 2004

**7. When the argument is "he runs high so anesthesia needs higher pressures":**
> "Our results do not support the theory that hypertensive patients should be kept at higher
> intraoperative pressures than normotensive patients."
> — Cohen et al, *Anesth Analg* 2022;135:329-340

> "Anesthetic management can thus be based on intraoperative pressures without regard to
> preoperative pressure."
> — Salmasi et al, *Anesthesiology* 2017;126:47-65

**8. The permissive guideline sentence (useful because it reads as permission, not argument):**
> "Elective surgery should proceed for patients who attend the pre-operative assessment clinic
> without documentation of normotension in primary care if their blood pressure is less than
> 180 mmHg systolic and 110 mmHg diastolic when measured in clinic."
> — AAGBI/BHS 2016 (*Anaesthesia* 2016;71:326-337)
> — and the 2026 update raised this to **< 180/120 mmHg** (*Anaesthesia* 2026;81:402-414)

**9. If you want to name the cost of the reflex:**
> "Hypertension is a common reason to cancel or postpone surgery... Across the UK this would
> equate to ~100 concerned and inconvenienced patients each day, with associated costs to the NHS
> and the national economy."
> — AAGBI/BHS 2016

## For the reluctant team at discharge

**10. The fact that ends the "what's the rule?" conversation:**
> "No guidelines provided goals for inpatient BP or recommendations for managing asymptomatic
> moderately elevated BP in the hospital."
> and
> "there were no recommendations relating to the management of BP during transitions from
> hospital to home, even after hypertensive urgency or emergency."
> — Systematic review of 14 clinical practice guidelines, *Ann Intern Med* 2024;177:497-506

**11. The AHA's own statement on what to do at discharge:**
> "The best available evidence suggests maintaining the prehospitalization antihypertensive
> medication regimen and avoiding intensification at discharge."
> — AHA scientific statement, *Hypertension* 2024;81:e94-e106

**12. When the reluctance is "that's our policy" — the AHA names this exact dynamic:**
> "Such policies, although well intended, may perpetuate a culture of routinely treating
> asymptomatic elevated inpatient BP, even in the absence of evidence of benefit."
> — AHA scientific statement, *Hypertension* 2024

**13. On PRN antihypertensive orders:**
> "In general, it is prudent to avoid PRN orders for antihypertensive medications to treat
> asymptomatic elevated inpatient BP."
> — AHA scientific statement, *Hypertension* 2024

**14. The memorable framing line (SHM editorial, and a great closer):**
> "A call about inpatient hypertension is not a call to act, but to think."
> — Anstey J, Lucas BP, *J Hosp Med* 2019;14:190-191

**15. What you offer INSTEAD (so you're not just refusing):**
> "Do not administer intravenous or immediate-acting oral antihypertensive medications to acutely
> lower blood pressure. Instead... consider modifying the chronic oral antihypertensive regimen
> in patients who are uncontrolled as outpatients or who are not treated as outpatients.
> Coordinate early postdischarge follow-up for repeat blood pressure evaluation and continued
> modification of a patient's chronic antihypertensive regimen."
> — Breu & Axon, *J Hosp Med* 2018;13:860-862

**16. The outpatient-timescale point:**
> "BP levels can take days to weeks to respond to medication changes, and these changes are best
> initiated in outpatient primary care."
> — *Am Fam Physician* 2026, "Severe Hypertension: Evaluation and Treatment"

---

# EVIDENCE-TIER SUMMARY

## Guideline-backed (a society actually says this)
- 2024 ACC/AHA perioperative: defer elective **elevated-risk** surgery for **recent history** of
  poorly controlled HTN ≥180/110 **before the day of surgery** — **COR 2b, LOE C-LD** ("may be
  considered," weakest affirmative tier).
- 2024 ACC/AHA perioperative: **Class 1** continue chronic beta blockers; **Class 3: Harm** do
  not start a beta blocker on the day of surgery; **Class 3: No Benefit** do not initiate
  clonidine; **Class 2b** hold RAASi 24 h before elevated-risk surgery if BP controlled;
  **Class 2a** continue RAASi in HFrEF; **Class 1** intraoperative MAP ≥60–65 or SBP ≥90.
- 2017 ACC/AHA HTN: **Class 3: Harm** abrupt preoperative discontinuation of beta blockers or
  clonidine.
- 2025 AHA/ACC HTN **Rec 6.2.4, COR 3: Harm, LOE B-NR** — no intermittent IV or oral dosing to
  acutely lower BP in hospitalized patients without target organ damage.
- AAGBI/BHS 2016: proceed if clinic BP <180/110 without primary-care documentation.
  **2026 update: <180/120 clinic, or <175/115 ABPM/HBPM.**
- 2026 Assoc. Anaesthetists/BIHS **Rec 7**: take antihypertensives, **including ACEi/ARB**, on the
  day of surgery. (Conflicts with 2024 ACC/AHA.)
- 2025 AHA/ACC: follow-up **monthly until controlled**; BMP **2–4 weeks** after initiation/titration.
- **NO guideline anywhere sets a BP threshold for hospital discharge** (Ann Intern Med 2024 SR of
  14 guidelines).

## Trial-backed
- **Weksler 2003** (n=989, randomized): postponing surgery for DBP 110–130 produced **no
  significant difference in postoperative complications** and a **longer hospital stay** than
  proceeding. The only RCT of acute preoperative BP lowering that exists.
- **Rest works:** 32% of 549 ED patients responded to 30 minutes of rest alone; in a 138-patient
  RCT, rest (68.5%) ≈ telmisartan (69.1%) for MAP reduction.
- **Anderson 2019** (propensity-matched, n=4,056): discharge intensification → **30-d readmission
  HR 1.23, NNH 27**; **30-d serious adverse events HR 1.41, NNH 63**; **1-y CV events HR 1.18
  (NS)**; **1-y SBP difference 0.6 mm Hg.**

## Observational
- **Howell 2004** meta-analysis: 30 studies, **OR 1.35 (1.17–1.56)** — "statistically but not
  clinically significant."
- **Anderson 2023** (n=66,140): intensive inpatient treatment **weighted OR 1.28 (1.18–1.39)**;
  **IV route weighted OR 1.90 (1.65–2.19).**
- **Anderson 2018 BMJ** (n=14,915): **65% well-controlled as outpatients before admission**;
  intensification **8% / 24% / 40%** by inpatient BP severity; **no difference** by who would
  actually benefit.
- **Salmasi 2017 / Cohen 2022**: MAP <65 drives myocardial and kidney injury; **the harm
  threshold is the same in chronic hypertensives as in normotensives.**

## Custom with no evidence behind it
- **Any "don't discharge above X mm Hg" rule.** Zero of 14 guidelines set one. Institutional
  custom, and the AHA explicitly warns such policies "perpetuate a culture of routinely treating
  asymptomatic elevated inpatient BP, even in the absence of evidence of benefit."
- **Pre-procedure BP thresholds for endoscopy.** ASGE sedation guideline mentions BP only as a
  monitoring parameter; the words "defer," "cancel" and "postpone" appear nowhere in it. UK
  accreditation body: "no national guidance regarding blood pressure limits before endoscopy."
- **Pre-procedure BP thresholds for IR, cardiac cath, TEE, bronchoscopy.** No society document
  located. Pure local policy.
- **The 180/110 OR threshold itself** is, per POQI, "driven largely by expert opinion," and the
  supporting evidence is circular — cases above that threshold were systematically not performed
  because of the expert opinion recommending deferral.
- **Nursing call parameters** (e.g. 160/80) are not clinical thresholds; one QI study safely
  liberalized them to 180/90 and cut IV antihypertensive orders 40%.

---

# EXPLICIT LIST OF WHAT I COULD NOT VERIFY

1. **Exact verbatim clause order of the 2024 ACC/AHA perioperative BP recommendation.**
   ahajournals.org and jacc.org return HTTP 403. Substance (2b, C-LD, 180/110, "before the day of
   surgery," "elevated-risk," "recent history") confirmed across 3 independent secondary sources;
   exact sentence not read in the primary document.
2. **Weksler 2003 complication rates.** Abstract says "no statistically significant differences"
   but gives no event counts or percentages. Full text paywalled.
3. **The MAP ≤60 duration-response odds (1.54 at 1–5 min → 3.81 at ≥21 min).** From a search
   summary only; primary source not identified. **Do not use these two numbers.**
4. **Peixoto NEJM 2019 follow-up interval.** Citation confirmed (*NEJM* 2019;381:1843-1852) but
   every full-text route failed. No number should be attributed to Peixoto.
5. **Rachoin 2024 TWDFNR full text** (*J Hosp Med* 2024;19:219-222). Citation verified; Wiley 403;
   no PMC deposit; PubMed has no abstract. Its "what you should do instead" section is known only
   through secondary summaries.
6. **The "47% / nearly half of patients with elevated inpatient BP were normotensive before
   admission" figure.** Widely repeated, not traced to a primary statement with a CI. Use the
   verified Anderson 2018 BMJ figure (65% well-controlled before admission) instead.
7. **2025 AHA/ACC guideline primary text** for Rec 6.2.4's exact wording and the discharge /
   follow-up items. Read only via structured guideline summaries (ahajournals 403).
8. **Which "recent trials demonstrating no benefit from preoperative blood pressure optimization"**
   the 2026 JCVA review refers to. IMPROVE-multi and PRETREAT are *intraoperative* BP management
   trials — do not conflate.
9. **Any ASA / ESAIC numeric preoperative BP threshold.** Searched; none found. Absence of
   evidence, but a reasonably thorough search.
10. **Any IR / cath / TEE / bronchoscopy society BP threshold.** None found.
11. **Soni et al, *Anaesthesia* 2020** (cancellation rates after implementing the AAGBI/BHS
    guideline) — Wiley 403, not retrieved. Would be useful real-world implementation data.
