# Research 5 — Practical inpatient workflow around the drug tables
Inpatient hypertension reference card, internal medicine residency. Compiled 2026-09-21.
Scope: what the White Book card does NOT cover but an intern needs at 2am.

**Primary sources used repeatedly (short names below):**

- **AHA 2024** = Bress AP, Anderson TS, Flack JM, Ghazi L, Hall ME, Laffer CL, Still CH, Taler SJ, Zachrison KS, Chang TI. The Management of Elevated Blood Pressure in the Acute Care Setting: A Scientific Statement From the AHA. *Hypertension.* 2024;81(8):e94–e106. doi:10.1161/HYP.0000000000000238 — https://www.ahajournals.org/doi/10.1161/HYP.0000000000000238 (PMID 38804130). This is the `HTN 2024;81:e94` already cited on the card.
- **BMJ 2024** = Miller JB, Hrabec D, Krishnamoorthy V, Kinni H, Brook RD. Evaluation and management of hypertensive emergency. *BMJ.* 2024;386:e077205. doi:10.1136/bmj-2023-077205 — https://www.bmj.com/content/386/bmj-2023-077205
- **2025 AHA/ACC guideline** = 2025 AHA/ACC/... Guideline for the Prevention, Detection, Evaluation and Management of High Blood Pressure in Adults. *Circulation.* 2025. doi:10.1161/CIR.0000000000001356 — https://www.ahajournals.org/doi/10.1161/CIR.0000000000001356 (PMID 40811497). **Caveat: ahajournals.org blocked automated access; all 2025-guideline content below is from secondary summaries and is flagged as such. Verify recommendation wording/COR-LOE against the PDF before printing.**
- **Ann Intern Med 2024** = Wilson LM, Herzig SJ, Steinman MA, Schonberg MA, Cluett JL, Marcantonio ER, Anderson TS. Management of Inpatient Elevated Blood Pressures: A Systematic Review of Clinical Practice Guidelines. *Ann Intern Med.* 2024;177(4):497–506. doi:10.7326/M23-3251 — https://pubmed.ncbi.nlm.nih.gov/38560900/ (PMC11103512)

---

## 1. WORKUP FOR END-ORGAN DAMAGE — "BP is 200/115 on the floor, now what?"

### 1a. The single most important framing fact

**No symptoms ⇒ essentially no emergency.** BMJ 2024 describes a hierarchical 5-symptom screen (chest pain, dyspnea, headache, visual disturbance, other neuro symptoms); in the retrospective study it cites, **absence of all five ruled out hypertensive emergency with NPV 99%**, while presence of any one had PPV only 23%. (BMJ 2024, "Clinical evaluation" section — https://www.bmj.com/content/386/bmj-2023-077205)

BMJ 2024 states directly: in acute severe hypertension **without** symptoms, **diagnostic testing can be minimal**; in symptomatic patients, testing is tuned to the symptom and the organ it implicates.

Headache alone is a trap: BMJ 2024 notes headache occurs in ~25% of patients with severely elevated BP and **does not by itself indicate a hypertensive emergency**.

### 1b. What AHA 2024 actually calls for (this is the routine panel)

AHA 2024 describes the evaluation of markedly elevated BP as history + physical + a short list of tests. Verbatim list from the statement:

**History:** chronic hypertension status, current antihypertensive regimen **and adherence to it**, and any available **outpatient** BP readings.

**Physical exam, focused on:** comparing **bilateral pulses**, cardiac and pulmonary auscultation, and a **fundoscopic exam**.

**"Further diagnostic investigations":**
- basic metabolic panel
- complete blood count
- chest radiograph
- 12-lead ECG **including heart rate**
- assessment of **volume status** and **risk of orthostasis**

Organ triage uses the **BARKH** acronym — **B**rain, **A**rteries, **R**etina, **K**idney, **H**eart (AHA 2024 Table 1, adapted from Rossi GP et al. Management of hypertensive emergencies: a practical approach. *Blood Press.* 2021;30:208–219. doi:10.1080/08037051.2021.1917983 — https://www.tandfonline.com/doi/full/10.1080/08037051.2021.1917983).

> **Key negative finding, worth putting on the card:** troponin, urinalysis, peripheral smear, and head CT do **not** appear anywhere in AHA 2024's routine evaluation list. I text-searched the full statement: "urinalysis," "urine," "smear," "schistocyte," "head CT," "computed tomography," "LDH," and "haptoglobin" return **zero** hits; "troponin" appears only as an outcome variable in the Anderson cohort. Those four tests are **symptom/organ-directed**, not routine.

### 1c. Which test, driven by which finding (synthesis of AHA 2024 + BMJ 2024 + 2017 ACC/AHA)

| Trigger | Test | Source |
|---|---|---|
| **Routine on everyone with markedly elevated BP** | BMP, CBC, CXR, 12-lead ECG + HR, volume status, orthostasis risk | AHA 2024 |
| Chest pain, dyspnea, ECG ischemia | **hs-troponin** (serial), BNP/NT-proBNP | BMJ 2024: troponin/BNP "valuable in evaluation of cardiovascular symptoms"; 2017 ACC/AHA: baseline troponin then repeat at ~3 h to rule out MI |
| Dyspnea / rales / hypoxia | CXR ± lung US (B-lines accurate for pulmonary edema) | BMJ 2024 |
| **Any** neuro deficit, seizure, AMS | **Non-contrast head CT** — to find/exclude ICH. BMJ 2024 is explicit that head CT is **insensitive for hypertensive encephalopathy and must not be used to rule it out**; hypertensive encephalopathy is a **clinical** diagnosis. MRI (T2/FLAIR, parieto-occipital vasogenic edema) if PRES suspected; microhemorrhages in ~65% of hypertensive encephalopathy on MRI | BMJ 2024 |
| Visual symptoms, headache, AMS | **Fundoscopy** — flame hemorrhages, cotton-wool spots, microaneurysms = acute (grade III); **papilledema = grade IV**, requires immediate lowering. AV nicking/tortuosity alone = chronic, not an emergency | BMJ 2024; AHA 2024 |
| Anemia + thrombocytopenia, or rising Cr | **CBC with peripheral smear for schistocytes** (MAHA / thrombotic microangiopathy); LDH — one small prospective study found **LDH >190 U/L** associated with hypertensive emergency (BMJ 2024 flags this as needing more study) | 2017 ACC/AHA; BMJ 2024 |
| Rising creatinine, edema, suspected renal injury | **Urinalysis for protein + urine sediment** for RBCs, WBCs, casts | BMJ 2024 ("urine analysis for protein, and urine sediment for erythrocytes, leukocytes, and casts"); 2017 ACC/AHA (hematuria/proteinuria, micro for RBC + casts) |
| Tearing chest/back pain, pulse or BP differential | CT angiography; POCUS is specific but not sensitive for dissection | BMJ 2024 |
| Sympathomimetic picture | Urine tox | BMJ 2024 |
| Palpitations + diaphoresis + labile BP | Consider pheo — but BMJ 2024 warns that **secondary-HTN labs drawn during acute severe HTN are confounded** (secondary hyperaldosteronism, volume depletion, sympathetic surge). Defer renin/aldo/metanephrines until stable, **except** when a hyperadrenergic state is strongly suspected | BMJ 2024 |

### 1d. ED/ACEP position (useful to quote to a consultant)

ACEP Clinical Policy 2013 (Wolf SJ et al. *Ann Emerg Med.* 2013;62(1):59–68. doi:10.1016/j.annemergmed.2013.05.012 — https://pubmed.ncbi.nlm.nih.gov/23842053/), all **Level C**:
1. "In ED patients with asymptomatic markedly elevated blood pressure, routine screening for acute target organ injury (eg, serum creatinine, urinalysis, ECG) is not required."
2. In select populations (eg, poor follow-up), screening creatinine may identify kidney injury that affects disposition.
3. "In patients with asymptomatic markedly elevated blood pressure, routine ED medical intervention is not required."
4. In select populations (eg, poor follow-up), may treat in ED and/or initiate long-term therapy [consensus].
5. Should be referred for outpatient follow-up [consensus].

Updated: ACEP Clinical Policy, approved 22 Jan 2025, *Ann Emerg Med.* 2025;86(1):e1–e11. doi:10.1016/j.annemergmed.2024.09.016 — https://pubmed.ncbi.nlm.nih.gov/40543987/ — narrower question (is it safe/effective to **start** an antihypertensive at ED discharge). Full recommendation text is behind ACEP login; **not verified here**.

### 1e. 2025 AHA/ACC guideline — what changed (SECONDARY SOURCES ONLY)

- The term **"hypertensive urgency" is retired**, replaced by **"severe hypertension"** (>180/120 without acute target-organ damage). — https://pmc.ncbi.nlm.nih.gov/articles/PMC12995957/ ; http://www.nephjc.com/news/accaha2025-klno3
- For severe hypertension **without** target-organ damage in nonpregnant adults: evaluate and treat **in the outpatient setting** with initiation/reinstitution/intensification of **oral** agents; the guideline **advises against intermittent IV or oral antihypertensives given solely to acutely lower BP**. — https://pmc.ncbi.nlm.nih.gov/articles/PMC12995957/
- Hypertensive **emergency**: ICU admission for continuous BP and target-organ monitoring with parenteral therapy; compelling condition (eg, aortic dissection) → SBP <120 in the first hour, <140 for most other compelling conditions; no compelling condition → ≤25% reduction in hour 1, then <160/100 over 2–6 h, then 130–140 over 24–48 h. **The class/level designations reported by secondary sources were inconsistent — verify.**
- Cuffless BP devices **not recommended** for diagnosis or treatment.
- Reassess therapeutic response ~**1 month** after starting/changing a regimen. — https://pmc.ncbi.nlm.nih.gov/articles/PMC12617343/

### 1f. The guideline vacuum (good line for the card)

Ann Intern Med 2024 systematically reviewed 14 guidelines: **"No guidelines provided goals for inpatient BP or recommendations for managing asymptomatic moderately elevated BP in the hospital."** Recommendations for "hypertensive urgency" were inconsistent, consensus-based, and ED-focused; outpatient oral therapy with follow-up in **days to weeks** was most often advised. https://pubmed.ncbi.nlm.nih.gov/38560900/

---

## 2. THE PRN ANTIHYPERTENSIVE PROBLEM

### Summary table (all associational — no RCTs exist)

| Study | Design / N | Exposure | Key numbers |
|---|---|---|---|
| **Rastogi 2021** | Retrospective cohort, 10 Cleveland Clinic hospitals, 2017; **22,834** adults on medicine service, noncardiac dx | New oral or any IV antihypertensive for SBP ≥140 | 78% had ≥1 elevated SBP; 33.1% of those treated (74% PO-only, 26% IV). **Propensity-matched (4,520/arm): AKI 10.3% vs 7.9%; myocardial injury 1.2% vs 0.6%; composite 11% vs 8.2% (all p≤0.003).** IPTW: composite OR 1.42 (1.27–1.59); AKI OR 1.36 (1.21–1.52); **myocardial injury OR 2.23 (1.56–3.20)**. BP trajectory identical: among index SBP>160, ≥20 mmHg fall at next reading in 58% treated vs 61% untreated. Discharge intensification (9.2%) gave **no** difference in 30-day MI/stroke and **no** difference in 1-yr BP control (41% vs 40% with SBP>139, p=0.86) |
| **Anderson 2023** | VA retrospective cohort, target-trial style, **66,140** adults ≥65 hospitalized for noncardiovascular dx with elevated BP in first 48 h | "Intensive" = IV antihypertensive or a new oral class | 21.3% treated intensively. Composite (death, ICU transfer, stroke, AKI, BNP rise, troponin rise) **8.7% vs 6.9%, weighted OR 1.28 (1.18–1.39)**; **IV subgroup OR 1.90 (1.65–2.19)**. Hypotensive episode 14.8% vs 14.0%, aOR 1.22 (1.15–1.30). Treated patients then got **6.1 vs 1.6** additional antihypertensive doses (escalation begets escalation). Consistent across age, frailty, preadmission BP, CVD history |
| **Ghazi 2023 (J Hypertens)** | Multihospital retrospective, **224,265** non-ICU admissions; 20,383 (9%) developed severe HTN (SBP>180 or DBP>110) without acute TOD | IV antihypertensive within 3 h of the elevated BP | Only 5% got IV, 79% untreated at 3 h. Overlap-weighted: **myocardial injury 5.9% vs 3.6%, HR 1.6 (1.13–2.24)**. No excess stroke (HR 0.7), AKI (HR 0.97) or death (HR 0.86) |
| **Ghazi 2022 (J Clin Hypertens)** | Same cohort, 224,265 adults; 10% developed severe inpatient HTN, 40% treated | Any antihypertensive within 6 h | Treated overall had **lower** rates of ≥30% MAP drop (HR 0.9), **but IV-only vs untreated had HIGHER rates: HR 1.4 (1.2–1.7).** MAP crashes happen in both groups |
| **Ghazi 2025 (AJKD)** | Bayesian heterogeneity-of-treatment-effect analysis, 11,951 patients with severe inpatient HTN | IV antihypertensive within 3 h | AKI in **18%** treated vs **13%** untreated. "Most patients would have been harmed"; only a subset of **317/11,951** had a predicted benefit. Exploratory/hypothesis-generating |
| **Mohandas 2021 (Hypertension)** | Single-center propensity-matched, UF Health 2012–2016; 42,771 admissions, **4,219 matched pairs** | PRN antihypertensive **in addition to** scheduled | **93% of PRN doses were IV**; hydralazine 53%, labetalol 43%. **43.5% of PRN doses were given for SBP 140–179.** AKI 15.5% vs 12.8%, **OR 1.24 (1.09–1.42)**; abrupt BP drop (>25% SBP in 1 h) 11.1% vs 5.9%, **OR 2.05 (1.56–2.71)**; in-hospital death 0.78% vs 0.33%, **OR 2.36 (1.26–4.41)**; ischemic stroke 0.40% vs 0.05%, OR 8.50 (1.96–36.79). **Dose–response:** ≥4 doses → AKI OR 2.73, mortality OR 4.29. **Oral PRN showed no excess AKI (OR 1.03)** — the harm tracked with the IV route. LOS 4.7 vs 2.9 days. Confounding by indication is the obvious limitation |
| **Lipari 2016 (J Hosp Med)** | Retrospective, urban academic hospital, non-critically ill; 246 patients with an episodic IV antihypertensive order, 172 received 458 doses | Episodic IV enalaprilat/labetalol/hydralazine/metoprolol | **>98% of doses given for SBP <200; 84.5% for SBP <180.** **32.6% had a BP fall of >25% within 6 h.** Oral regimen was adjusted after the IV dose in only **52%** |
| **Jacobs 2019 (J Hosp Med)** — UCSF | QI, general medicine + ICU, urban academic hospital | IV labetalol or hydralazine for asymptomatic BP >160/90 | Baseline: **251/2,306 (11%)** treated over 10 months → **70/934 (7%)** post-intervention; **adjusted OR 0.62 (0.47–0.83), p=.001**. Median SBP unchanged (167 vs 168). No excess ICU transfers, rapid responses or arrests. Intervention included **raising nursing BP call parameters from 160/80 to 180/90** |
| **Pasik 2019 (J Hosp Med)** — Mount Sinai | Quasi-experimental, 2 medical units, 2016–2018, 260 one-time IV orders | Inappropriate one-time IV antihypertensive | Inappropriate orders **8.3 → 3.3 per 1,000 patient-days (p=.0099)**; adverse events **3.7 → 0.8 per 1,000 patient-days (p=.0072)**. Nurses were empowered to assess for pain/anxiety and for end-organ damage via an algorithm before paging. **111 patients with elevated BP left untreated had no adverse outcomes** |
| **Gaynor 2018** | Retrospective review of PRN hydralazine/labetalol on medicine | — | **41% of patients ordered PRN antihypertensives were not receiving their home regimen** (cited in AHA 2024 as ref 22) |
| **Miller 2012** | Postsurgical inpatients receiving ≥1 IV antihypertensive dose | — | **25% were not started on their home antihypertensive regimen** (AHA 2024 ref 23) |

**URLs:**
- Rastogi R, Sheehan MM, Hu B, Shaker V, Kojima L, Rothberg MB. *JAMA Intern Med.* 2021;181(3):345–352. doi:10.1001/jamainternmed.2020.7501 — https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2774562 (free full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC7770615/)
- Anderson TS, Herzig SJ, Jing B, Boscardin WJ, Fung K, Marcantonio ER, Steinman MA. *JAMA Intern Med.* 2023;183(7):715–723. doi:10.1001/jamainternmed.2023.1667 — https://pubmed.ncbi.nlm.nih.gov/37252732/ (PMC10230372)
- Ghazi L, Li F, Simonov M, et al. *J Hypertens.* 2023;41(2):288–294. doi:10.1097/HJH.0000000000003328 — https://pubmed.ncbi.nlm.nih.gov/36583354/ (PMC9799038; erratum *J Hypertens.* 2023;41:873)
- Ghazi L, Li F, Chen X, et al. *J Clin Hypertens.* 2022;24(3):339–349. doi:10.1111/jch.14431 — https://onlinelibrary.wiley.com/doi/10.1111/jch.14431
- Ghazi L, Chen X, Harhay MO, et al. *Am J Kidney Dis.* 2025;85(4):442–453. doi:10.1053/j.ajkd.2024.09.011 — https://pubmed.ncbi.nlm.nih.gov/39580068/
- Mohandas R, Chamarthi G, Bozorgmehri S, et al. *Hypertension.* 2021;78(2):516–524. doi:10.1161/HYPERTENSIONAHA.121.17279 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8266743/
- Lipari M, Moser LR, Petrovitch EA, Farber M, Flack JM. *J Hosp Med.* 2016;11(3):193–198. doi:10.1002/jhm.2510 — https://pubmed.ncbi.nlm.nih.gov/26560085/
- Jacobs ZG, Najafi N, Fang MC, Prasad PA, Abe-Jones Y, Auerbach AD, Patel S. *J Hosp Med.* 2019;14(3):144–150. doi:10.12788/jhm.3087 — https://pubmed.ncbi.nlm.nih.gov/30811319/
- Pasik SD, Chiu S, Yang J, et al. *J Hosp Med.* 2019;14(3):151–156. doi:10.12788/jhm.3190 — https://pubmed.ncbi.nlm.nih.gov/30811320/
- Gaynor MF, Wright GC, Vondracek S. *Ther Adv Cardiovasc Dis.* 2018;12(1):7–15. doi:10.1177/1753944717746613
- Miller CP, Cook AM, Case CD, Bernard AC. *Am Surg.* 2012;78(2):250–253.

### "Things We Do for No Reason" — both of them

**Breu AC, Axon RN. Acute Treatment of Hypertensive Urgency.** *J Hosp Med.* 2018;13(12):860–862. doi:10.12788/jhm.3086 — https://shmpublications.onlinelibrary.wiley.com/doi/abs/10.12788/jhm.3086 (this is the `JHM 2018;13:860` already on the card). Content the card doesn't carry:
- ~1 in 7 hospitalized patients has a hypertensive crisis episode; **7.4%** of inpatients at one center had a PRN IV hydralazine/labetalol order and **60.3% of those received ≥1 dose**. Nearly half of IM/FM trainees surveyed said they would use IV meds for an asymptomatic BP >180.
- **Patel KK et al.** outpatient cohort: 58,836 clinic patients meeting hypertensive-urgency criteria; **426 referred to hospital, only 100 (0.17%) admitted**. 7-day MACE (MI/stroke/TIA) **0.1%** sent home vs **0.5%** sent to hospital. Even with SBP ≥220: 2/977 (0.2%) sent home vs 0/81 hospitalized. (Patel KK, Young L, Howell EH, et al. *JAMA Intern Med.* 2016;176(7):981–988.)
- **Rest works.** One ED study: 30-minute rest period → **32%** responded (SBP <180 and DBP <110 with ≥20 mmHg SBP or ≥10 mmHg DBP drop). An RCT of 138 patients randomized to rest vs telmisartan: primary endpoint met in **68.5% (rest) vs 69.1% (telmisartan)**. BMJ 2024 reports the same trial as mean BP fall at 2 h of **32.2 vs 32.8 mmHg (p=0.065)**.
- **Overshoot is common even in real emergencies:** Brooks et al., patients treated with IV nicardipine or nitroprusside for hypertensive emergency — **57% (27/47) had >25% MAP reduction within the first 30 minutes**; 2 had acute ischemic events attributed to treatment.
- Breu & Axon's four recommendations: (1) confirm no end-organ symptoms/signs — ROS + exam, ECG and CXR in select cases; (2) look for treatable causes — pain, nausea, withdrawal, held home meds; (3) allow rest, then reassess; (4) **do not give IV or immediate-acting oral antihypertensives to acutely lower BP**; modify the chronic oral regimen and arrange early post-discharge follow-up.
- Cites JNC 7's own words that the term "urgency" itself drove overtreatment.

**Rachoin JS, Cerceo E, Anderson TS. Things We Do for No Reason™: Intensifying antihypertensive medications for hospitalized patients at the time of discharge.** *J Hosp Med.* 2024;19(3):219–222. doi:10.1002/jhm.13185 — https://shmpublications.onlinelibrary.wiley.com/doi/full/10.1002/jhm.13185 (PMID 37545427). Note Anderson is senior author on both this and the two big cohorts, and is a co-author of AHA 2024 — the literature is coherent.

**Companion editorial** (useful framing quote source): Anstey J, Lucas BP. Treatment of Inpatient Asymptomatic Hypertension: Not a Call to Act but to Think. *J Hosp Med.* 2019;14(3):190–191. doi:10.12788/jhm.3160 — https://shmpublications.onlinelibrary.wiley.com/doi/10.12788/jhm.3160. Its core argument: when a patient is febrile, tachycardic or hypoxic we look for a cause; high BP is the one vital sign clinicians treat as **a number to fix rather than a sign to explain**. It also names the two reasons the practice persists — unfounded fear of imminent progression to emergency, and unawareness of the harms of overtreatment. (Anstey was UCSF Division of Hospital Medicine.)

### What AHA 2024 says about PRN orders specifically

- Roughly **one third** of asymptomatic elevated inpatient BP episodes get an oral or IV antihypertensive.
- **"In general, it is prudent to avoid PRN orders for antihypertensive medications to treat asymptomatic elevated inpatient BP."**
- It names the system drivers explicitly: vital-sign alarms, automated decision alerts, nursing notification thresholds, **standardized PRN order sets**, and PRN parenteral orders written specifically **to avoid overnight pages**.
- It describes the **iatrogenic BP-variability loop**: a night-time PRN dose lowers the morning BP → the morning scheduled oral dose gets held → evening BP runs higher → another PRN dose. This is a genuinely card-worthy mechanism.
- It also calls out the ED→floor handoff practice of demanding the BP be "acceptable" before transfer, as a policy that perpetuates the culture.
- AHA 2024 **Table 3, Ten Key Implications** — items most relevant here: #2 detect and correct reversible causes; #6 elevated BP without new/worsening target-organ damage "may be best served by accurate remeasurement and attention to contributing circumstantial factors"; #8 **the threshold to initiate or intensify should be high**; #9 **"Use of intravenous antihypertensives is not supported by the evidence in the absence of hypertensive emergency."**
- Conclusion sentence worth memorizing: treating asymptomatic elevated inpatient BP "should generally be the exception, not the rule."

### When treatment IS defensible (AHA 2024 — the nuance the card should keep)

Benefit may outweigh risk in: **persistent** markedly elevated readings (>180/110–120) **plus a history of high outpatient BPs**; persistently uncontrolled BP; high CVD risk or established CVD. Also: a hospitalization **for a CVD reason** in a patient with resistant HTN may be a good time for a secondary workup — but a hospitalization **unrelated** to HTN is a bad time to intervene. And: BP takes **days to weeks** to respond to a medication change, so a typical stay cannot assess the effect of a change.

### One more PRN agent to warn about: clonidine

Hanna J, Ghazi L, Yamamoto Y, et al. Excessive Blood Pressure Response to Clonidine in Hospitalized Patients With Asymptomatic Severe Hypertension. *Am J Hypertens.* 2022;35(5):433–440. doi:10.1093/ajh/hpac004 — https://pubmed.ncbi.nlm.nih.gov/35038322/ (PMC9088839). 200 encounters; **10% had a ≥30% MAP fall within 4 h**, 16% had ≥30% fall in SBP, DBP or MAP. 14 adverse events in 24 h, 9 of them AKI. Predictors: female sex and the **0.3 mg** dose. Conclusion: the response to clonidine "is generally not predictable on clinical grounds." Clonidine PRN is a common floor habit and is not on the card — worth a one-line warning, along with its rebound-hypertension risk on withdrawal.

### Choosing Wisely / SHM

The JHM "Things We Do for No Reason" series **is** the Society of Hospital Medicine's Choosing Wisely vehicle (the Breu & Axon article is published under the header "CHOOSING WISELY®: THINGS WE DO FOR NO REASON"). I found **no standalone SHM Choosing Wisely numbered recommendation** specifically on asymptomatic inpatient hypertension — cite the TWDFNR articles, AHA 2024 Table 3, and the 2025 guideline instead. https://www.mdedge.com/jhospmed/choosing-wisely-things-we-do-no-reason

---

## 3. SECONDARY / REVERSIBLE CAUSES ON THE WARDS — ranked for a medicine ward

The card's "Assess" line has: pain, anxiety, urine retention, meds (steroids), OSA, nausea, withdrawal. Here is the fuller list, ranked by how often it actually explains the number on a medicine floor.

### Tier 1 — check these every single time (high frequency, high yield, fixable in minutes)

1. **Missed / held / not-reconciled home antihypertensives.** The single most common cause.
   - **41%** of patients ordered PRN antihypertensives were not receiving their home regimen (Gaynor 2018, cited AHA 2024).
   - **25%** of postsurgical patients given IV antihypertensives had never been restarted on their home regimen (Miller 2012, cited AHA 2024).
   - Best current data: **Ribak Z, Miller JD, Burrack N, Novack V, Abuhasira R. Stopping or continuing chronic antihypertensive therapy during hospitalization. *J Intern Med.* 2026;300(3):284–298. doi:10.1111/joim.70093** — https://pmc.ncbi.nlm.nih.gov/articles/PMC13429002/ (PMID 41930616). 8 Israeli hospitals, 2014–2024; 82,230 propensity-matched patients. Discontinuation of ≥1 chronic antihypertensive was common (**31.3% internal medicine, 24.8% surgical**), most often CCBs (~30%), thiazides (~27%) and ACEIs (~27%). Internal medicine: in-hospital AKI **OR 1.23 (1.16–1.30)**, 90-day AKI OR 1.19 (1.14–1.24), in-hospital mortality **OR 2.69 (2.47–2.94)**, 90-day mortality OR 1.81 (1.72–1.90). Surgical: in-hospital myocardial injury OR 1.26 (1.10–1.44). Conclusion: withholding is "unlikely to confer benefit and may be harmful." **Caveat: observational; the mortality OR is almost certainly inflated by confounding by indication (dying patients get meds held). Cite the AKI signal, treat the mortality number cautiously.**
   - Also check for **formulary substitution** on admission silently changing the regimen (AHA 2024 names this).
   - Adherence downstream: Anderson TS, Jing B, Fung K, Steinman MA. *J Gen Intern Med.* 2021;36:3900–3902 — ~**one third** of antihypertensives prescribed at discharge are **never refilled**, and **half are stopped by 1 year**.
2. **NPO status / held meds around procedures** — the mechanical version of #1. AHA 2024 and the Pasik intervention both treat "NPO" as an explicit, legitimate reason for a one-time IV dose (Pasik's "inappropriate" definition explicitly excluded NPO orders).
3. **Pain.** AHA 2024: assessment and management of pain are "often overlooked." BMJ 2024: remeasuring **after adequate analgesia** frequently resolves the reading.
4. **Measurement artifact** — see section 4. AHA 2024's step 1 is literally repeat the measurement with proper technique.
5. **Anxiety, acute stress, sleep deprivation, being woken up for the vitals check** (AHA 2024 explicitly lists "patient woken up for BP measurement" as a contextual factor absent from the EHR).
6. **Alcohol / benzodiazepine withdrawal**, and **clonidine or beta-blocker withdrawal.** AHA 2024 names rebound hypertension after abrupt beta-blocker cessation. EMCrit singles out **clonidine withdrawal** as the classic nonadherence-driven severe HTN — https://emcrit.org/ibcc/htn/
7. **Urinary retention / obstructed Foley / bowel distension.** Also the trigger for autonomic dysreflexia (below).
8. **Volume overload / excessive IV fluids.** AHA 2024 lists "excessive intravenous fluids" among BP-raising exposures and instructs assessment of volume status.
9. **Agitation and delirium** (EMCrit: treat agitation with the appropriate agent rather than an antihypertensive).
10. **Nausea/vomiting** (already on the card).

### Tier 2 — common enough to scan the MAR for

11. **Medications that raise BP.** Vitarello JA, Fitzgerald CJ, Cluett JL, Juraschek SP, Anderson TS. *JAMA Intern Med.* 2022;182(1):90–93. doi:10.1001/jamainternmed.2021.6819 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8609458/ : **18.5%** of US adults with hypertension take ≥1 medication that may raise BP (14.9% one, 3.6% two or more). Class prevalence: **antidepressants 8.7%**, prescription **NSAIDs 6.5%**, steroids 1.9%, estrogens 1.7%, stimulants 0.9%, decongestants 0.4%, testosterone 0.4%, antiobesity 0.2%, antipsychotics 0.2%, immunosuppressants 0.2%. AHA 2024 cites this and says these "should be discontinued when possible."
    - AHA 2024's own inpatient list: **excessive IV fluids, NSAIDs, stimulants, corticosteroids, illicit substances (cocaine, methamphetamine).**
    - Add for the wards: **decongestants (pseudoephedrine/phenylephrine), calcineurin inhibitors (tacrolimus, cyclosporine), erythropoiesis-stimulating agents, VEGF-pathway inhibitors** (bevacizumab, and the TKIs — sunitinib, sorafenib, pazopanib, lenvatinib; hypertension is an on-target class effect), **high-dose caffeine, nicotine/vaping, ephedra and other supplements**, **midodrine**, **droxidopa**, **MAOI + tyramine**, and **abrupt cessation** of clonidine or beta-blocker. (Class-effect statements — verify individual agents against the local formulary before printing.)
12. **Hypoxia / hypercapnia.** EMCrit lists hypercapnia as a reversible cause; hypoxemia drives sympathetic tone. Check the sat and, if AMS + HTN, a gas.
13. **OSA** (already on the card) — the overnight/early-morning BP spike pattern.
14. **Hypoglycemia** — catecholamine surge; check a glucose in any diaphoretic, tremulous, anxious patient rather than treating the BP.
15. **Heart rate.** AHA 2024 devotes a paragraph to this: BP is HR-dependent, and both intrinsic and drug-induced HR changes (eg, AF with RVR, or reflex tachycardia after a BP drop) reshape the reading. A tachycardic hypertensive patient is a different problem from a bradycardic one.
16. **White-coat / measurement context.** AHA 2024 instructs comparing with **out-of-hospital BP readings** before deciding — persistent elevation both in and out of hospital is what points toward genuinely intensifying therapy.

### Tier 3 — rare, but you must not miss them, because the management is different or inverted

17. **Elevated ICP / Cushing reflex (hypertension + bradycardia + irregular respiration).** **This is the one where lowering the BP is actively harmful.** CPP = MAP − ICP, so the hypertension is a compensatory response maintaining cerebral perfusion; the treatment is to lower the ICP, not the MAP. Cushing's triad signals impending herniation. — https://www.ncbi.nlm.nih.gov/books/NBK549801/ (Dinallo S, Waseem M. Cushing Reflex. StatPearls, 2023)
18. **Autonomic dysreflexia** in spinal cord injury **at or above T6**. Sudden severe HTN triggered by a noxious stimulus below the lesion; **up to 85% of episodes are urologic — most often a blocked/blocked-off bladder catheter**. SBP >150, or >40 mmHg above the patient's (often low) baseline, should trigger immediate action. Management is to **remove the stimulus first** (unkink/flush or replace the catheter, sit the patient upright, loosen constrictive clothing), with a short-acting agent only if that fails. — https://www.ncbi.nlm.nih.gov/books/NBK482434/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC1939947/
19. **Thyroid storm** — HTN with wide pulse pressure, tachycardia, fever, AMS. BMJ 2024 lists thyroid function studies among the directed labs.
20. **Serotonin syndrome / NMS / sympathomimetic or anticholinergic toxidromes** — treat the syndrome, not the number.
21. **Pheochromocytoma / paraganglioma, cocaine or methamphetamine, MAOI crisis** — the hyperadrenergic states. BMJ 2024: maintain a high index of suspicion for these specifically, because they change management (**avoid unopposed beta-blockade**); defer the rest of the secondary workup until stable.
22. **Preeclampsia/eclampsia/HELLP** in any postpartum or pregnant patient — different thresholds and different drugs.
23. **Acute stroke / ICH / dissection presenting as "high BP"** — the BP is the symptom, not the disease.
24. **Scleroderma renal crisis** (the card's captopril indication), **acute glomerulonephritis**, **renal artery stenosis with flash pulmonary edema**.

### The "spontaneous resolution" fact that justifies waiting

Garg K, Staunton MK, Peixoto AJ, Wilson FP, Ghazi L. Correlates of Spontaneous Blood Pressure Reduction Following Severe Inpatient Hypertension Development. *Am J Hypertens.* 2024;37(4):273–279. doi:10.1093/ajh/hpad112 — https://pubmed.ncbi.nlm.nih.gov/37988620/ . Of **12,825** patients who developed severe inpatient HTN, **44.2% had spontaneous BP reduction (SBP <160 and DBP <100) within 3 hours with no antihypertensive at all**, and no clinical/demographic variable usefully predicted who would. Pair this with Rastogi's finding that treated and untreated patients were equally likely to drop ≥20 mmHg by the next reading (58% vs 61%).

---

## 4. BP MEASUREMENT TECHNIQUE — the errors that manufacture fake hypertensive urgency

### 4a. The prevalence of the problem in hospitals

AHA 2024: one UK inpatient audit found **36 of 100 inpatient BP measurements were taken with an inappropriately sized cuff.** AHA 2024 also lists the routinely-varying-and-never-recorded factors: device type, validation/calibration status, cuff placement, cuff size, patient position (supine vs seated), and situational factors (anxiety, pain, patient woken up).

### 4b. Magnitude of each error (with direction)

**Source A — Kallioinen N, Hill A, Horswill MS, Ward HE, Watson MO. Sources of inaccuracy in the measurement of adult patients' resting blood pressure in clinical settings: a systematic review.** *J Hypertens.* 2017;35(3):421–441. doi:10.1097/HJH.0000000000001197 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5278896/ (328 studies, 29 sources; overall significant effects span **−23.6 to +33 mmHg SBP** and **−14 to +23 mmHg DBP**).

| Error | SBP effect | DBP effect |
|---|---|---|
| **Cuff too small (undercuffing)** | **+2.1 to +11.2** | +1.6 to +6.6 |
| Cuff too large | −3.7 to −1.5 | −4.7 to −1.0 |
| Cuff over clothing | *no significant effect found* | *no significant effect* |
| Arm unsupported | +4.9 | +2.7 to +4.8 |
| **Arm below heart level** | **+3.7 to +23** | +2.8 to +12 |
| Back unsupported | *no significant SBP effect* | +6.5 |
| Legs crossed at the knee | +2.5 to +14.9 | +1.4 to +10.8 |
| **Full bladder** | **+4.2 to +33** | +2.8 to +18.5 |
| Talking during measurement | +4 to +19 | +5 to +14.3 |
| Recent caffeine | +3 to +14 | +2.1 to +13 |
| Recent smoking / nicotine | +2.8 to +25 | +2 to +18 |
| No rest period | +4.2 to +11.6 | +1.8 to +4.3 |
| White-coat effect | −12.7 to +26.7 | −8.2 to +21 |

*(Ranges are across studies, not confidence intervals. "Cuff over clothing" being null in this review contradicts the commonly-quoted 5–50 mmHg figure — see Source C. Do not put "cuff over clothing = 50 mmHg" on the card without the caveat.)*

**Source B — Muntner P, Shimbo D, Carey RM, et al. Measurement of Blood Pressure in Humans: A Scientific Statement From the AHA.** *Hypertension.* 2019;73(5):e35–e66. doi:10.1161/HYP.0000000000000087 — https://www.ahajournals.org/doi/10.1161/HYP.0000000000000087 . **Table 4** (body position):
- Supine vs seated: SBP **3–10 mmHg higher** supine; DBP ~**1–5 mmHg higher**. (Directly relevant: floor BPs are usually taken supine with the arm on the bed, which is **below** heart level.)
- **Back unsupported** (eg, seated on an exam table): SBP **+5 to +15**, DBP **+6**.
- **Legs crossed:** SBP **+5 to +8**, DBP **+3 to +5**.
- Arm below the level of the right atrium → readings too high. **If the patient holds their own arm up, BP is raised** (isometric contraction) — the arm must be supported by the observer or a table.
- Cuff bladder **length 75–100%** and **width 37–50%** of arm circumference. "Using a cuff that is too small will result in an artificially elevated BP reading, and using a cuff that is too large will result in a reading that is artificially low."

**Source C — AHA "Measure Accurately" teaching slide (Target: BP program)**, https://www2.heart.org/site/DocServer/Break_1_-_Measure_BP_Accurately.pdf — the widely circulated magnitudes, with their original citations (Pickering 2005 *Circulation* 111:697; Handler J, *Perm J.* 2009;13(3):51; Cushman 1990 *AJH* 3:240): crossed legs **2–8**; **cuff over clothing 5–50**; cuff too small **2–10**; full bladder **10**; talking or active listening **10**; unsupported arm **10**; unsupported back/feet **6.5**. The slide notes these are **not cumulative**. **These are secondary-source estimates and the clothing figure conflicts with Kallioinen — label as approximate.**

### 4c. The two definitive recent randomized trials

**Arm position — the ARMS trial.** Liu H, Zhao D, Sabit A, et al. **Arm Position and Blood Pressure Readings: The ARMS Crossover Randomized Clinical Trial.** *JAMA Intern Med.* 2024;184(12):1436–1442. doi:10.1001/jamainternmed.2024.5213 — https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2824754 (PMC11459360).
- N=133 adults 18–80 (mean 57, 53% female, 77% Black, 41% BMI ≥30); 12 BP measurements each in randomized order; desk-supported at heart level = reference, plus a second desk set to control for intrinsic variability.
- **Hand supported on the lap: SBP +3.9 mmHg (95% CI 2.5–5.2), DBP +4.0 (3.1–4.9).**
- **Arm unsupported at the side: SBP +6.5 mmHg (95% CI 5.1–7.9), DBP +4.4 (3.4–5.4).**
- Absolute means: desk 126/74, lap 130/78, side 133/78.
- The overestimate with the arm at the side was **larger** in those with SBP ≥130.
- Authors' framing: improper arm position could misclassify roughly 40 million US adults at a 140 threshold and 54 million at 130.
- **Ward translation:** the standard floor BP — patient supine or slumped, arm resting on the bed below heart level, unsupported — stacks the arm-position error on top of the supine error. Expect single-digit-to-low-teens mmHg of manufactured systolic elevation before anything else.

**Cuff size — the Cuff(SZ) trial.** Ishigami J, Charleston J, Miller ER 3rd, Matsushita K, Appel LJ, Brady TM. **Effects of Cuff Size on the Accuracy of Blood Pressure Readings: The Cuff(SZ) Randomized Crossover Trial.** *JAMA Intern Med.* 2023;183(10):1061–1068. doi:10.1001/jamainternmed.2023.3264 — https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2807853 (PMC10407761).
- N=195 adults, randomized order of appropriate / too-small / too-large cuff, then a 4th set with the appropriate cuff.
- Using a **regular** cuff when the appropriate size was:
  - **small** → SBP **−3.6** (95% CI −5.6 to −1.7), DBP −1.3 (−2.4 to −0.2) [too-large cuff **under**estimates]
  - **large** → SBP **+4.8** (3.0–6.6), DBP +1.8 (1.1–2.6)
  - **extra-large** → SBP **+19.5** (16.1–22.9), DBP **+7.4** (5.7–9.1)
- Even **one size too small** in someone needing extra-large: SBP **+9.6** (7.3–11.9).
- **Direction to memorize: cuff too SMALL → falsely HIGH. Cuff too LARGE → falsely LOW.** Error grows steeply with arm circumference, so the fake 200/115 is disproportionately likely in your patients with large arms.

### 4d. Oscillometric vs auscultatory vs arterial line — the inpatient-specific twist

AHA 2024, verbatim finding: in critical care and surgical inpatient populations, when BP is **>180/100 mmHg, oscillometric devices may UNDERestimate BP by as much as 50/30 mmHg compared with an arterial line.** (AHA 2024 refs 17–18: Ribezzo S et al. *ScientificWorldJournal.* 2014;2014:353628, doi:10.1155/2014/353628; **Wax DB, Lin HM, Leibowitz AB.** *Anesthesiology.* 2011;115(5):973–978, doi:10.1097/ALN.0b013e3182330286 — https://pubmed.ncbi.nlm.nih.gov/21952254/). Even research-quality manual auscultation with aneroid or mercury devices diverges notably from arterial-line values.

The Wax data show the specific pattern and the behavioral consequence: **NIBP reads higher than the arterial line during hypotension and LOWER than the arterial line during hypertension.** In 24,225 cases, among hypertensive patients, **44%** of those monitored with arterial line alone received an antihypertensive vs **12%** when NIBP was also displayed — ie, the cuff talks you out of treating. This cuts in the opposite direction from the outpatient "cuff overestimates" story, and is the reason AHA 2024 prefers arterial lines specifically for hypertensive emergency and IV antihypertensive titration.

AHA 2024 on arterial lines in the ICU: they are preferred for monitoring the **rate of BP decline** and for IV antihypertensive use, but are themselves subject to movement artifact and calibration error.

### 4e. What to actually do at the bedside (AHA 2024 sequence)

1. Confirm the device is calibrated and functioning (AHA 2024 puts the burden on hospital administration/biomed for routine calibration — implication #7 in Table 3).
2. **Repeat the BP with proper technique**, "as closely as the clinical situation allows (eg, having the patient sit up in bed rather than being supine)."
3. Correct cuff size; bare arm; arm supported at right-atrial level; back and feet supported; legs uncrossed; bladder empty; no talking; rest ≥3–5 min (AHA 2019 Table 5).
4. Only then interpret the number.

---

## 5. TRANSITIONING OFF A DRIP

### 5a. The one piece of hard label guidance (nicardipine)

FDA label for nicardipine HCl injection — "Drug Discontinuation and Transition to an Oral Antihypertensive Agent":
- "Discontinuation of infusion is followed by a 50% offset of action in about 30 minutes."
- "If treatment includes transfer to an oral antihypertensive agent **other than** oral nicardipine, **initiate therapy upon discontinuation** of nicardipine hydrochloride injection."
- "If **oral nicardipine** is to be used, administer the first dose **1 hour prior to discontinuation** of the infusion."
- (Same label: after reaching goal with rapid titration, back the infusion down to 3 mg/h; rotate the peripheral infusion site every 12 h.)
https://americanregent.com/media/2918/nicardipine_pi-insert_rev-mar2020_23apr2020.pdf

> **The failure mode this warns about:** nicardipine's offset is ~30 min for 50% of the effect, but **no oral antihypertensive reaches peak effect in 30 minutes.** If you stop the drip at the same moment you write the first PO dose, you get a rebound spike, a page, and a PRN IV dose — the exact loop AHA 2024 describes. The label's asymmetry (start "other" oral agents at discontinuation vs oral nicardipine 1 h before) is a quirk of oral nicardipine's own slow onset; in practice the safer general rule is **load the PO agent, watch it work, then wean the drip — not the reverse.**

### 5b. Published protocols and what they bought

| Study | Protocol | Result |
|---|---|---|
| **Zhu Z, Bower M, Stern-Nezer S, et al.** Early Initiation of Oral Antihypertensives Reduces ICU Stay and Hospital Cost for Patients with Hypertensive ICH. *Neurocrit Care.* 2020;32(3):707–714. doi:10.1007/s12028-020-00951-1 — https://pubmed.ncbi.nlm.nih.gov/32253732/ | Oral agents started **within 24 h of ED arrival** vs after 24 h; 90 vs 76 patients, UC Irvine | Nicardipine infusion **55.5 ± 60.1 h vs 121.6 ± 141.3 h** (p<0.005); nicardipine cost **$14,207 vs $29,299**; **ICU LOS 2 vs 5 days**; hospitalization cost **$24,564 vs $47,366**. **No difference in renal adverse events, functional outcome, or mortality** |
| **Shah NH, Do LV, Petrovich J, Crozier K, Azran C, Josephson SA.** Reducing Cost and Intravenous Duration of Nicardipine in Intracerebral Hemorrhage Patients via an Interdisciplinary Approach. *J Stroke Cerebrovasc Dis.* 2016;25(9):2290–2294. doi:10.1016/j.jstrokecerebrovasdis.2016.05.021 — https://pubmed.ncbi.nlm.nih.gov/27315743/ **(UCSF)** | Physician + pharmacist daily screening for readiness to transition to PO; 35 patients vs 44 historical controls | Median nicardipine duration **118 → 30 h** (p<.001); **$433,566/yr saved, $18,475 per patient**; total LOS unchanged (8.4 vs 8.9 d). **When the intervention stopped, duration rebounded to a mean of 96 h** — the effect was entirely process-dependent, not knowledge-dependent |
| Neurology abstract (P5.063), *Neurology.* 2017;88(16 Suppl) — https://www.neurology.org/doi/10.1212/WNL.88.16_supplement.P5.063 | Protocol-driven early initiation + prompt titration of orals | ICU LOS down **43%** (108.5 → 62.1 h); ~$5,000/patient pharmacy savings. *Conference abstract — lowest evidence tier* |
| **Alshaya AI, Alghamdi M, Almohareb SN, et al.** Systolic Blood Pressure Variability When Transitioning From Intravenous to Enteral Antihypertensive Agents in Patients With Hemorrhagic Strokes. *Front Neurol.* 2022;13:866557. doi:10.3389/fneur.2022.866557 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9284227/ | 102 ICH/SAH patients; examined **number** of enteral agents and **overlap time** | **Longer overlap between the enteral agent and the infusion was associated with LOWER systolic BP variability (p=0.012).** The **number** of enteral agents made no difference (p=0.274). Small, single-center, retrospective — but it is the only direct evidence on overlap duration I found, and it points the same way as the label |

### 5c. Which oral agent pairs with which drip (practice, not guideline)

There is **no guideline-level recommendation** for drip→PO pairing. The most coherent published framework is EMCrit's IBCC chapter (Farkas J, Hypertensive emergency & antihypertensive medications — https://emcrit.org/ibcc/htn/), which is expert opinion but explicit:

- **Match the mechanism that worked.** Good response to **nicardipine or clevidipine** → an oral **dihydropyridine CCB**; EMCrit recommends **nifedipine XR** as the workhorse (fast enough to titrate) and warns against **amlodipine** for acute work because its onset is too slow ("an absolute slug" in his words — the card already notes amlodipine onset 24–48 h, which is the same point).
- **Good response to labetalol or esmolol** → oral **labetalol** or **carvedilol** (alpha+beta).
- **HFrEF** → carvedilol plus ACEI/ARB rather than a CCB.
- **If the crisis was driven by nonadherence**, the right oral regimen is usually **the patient's own home regimen**, restarted.
- **Nitroglycerin drip** → oral/topical nitrate (isosorbide dinitrate/mononitrate) plus the disease-appropriate agent; nitrate tolerance means a drip cannot simply be converted 1:1.
- **Choose agents with onset measured in hours, not days**, so that you can titrate before the ICU day ends.

### 5d. Practical sequence to put on the card

1. Confirm the emergency has resolved and the patient is stable at goal for several hours on a **stable, low** infusion rate.
2. Give the **first oral dose while the drip is still running.**
3. Wait for the oral agent's **onset**, not its ordering time (labetalol PO ~20 min onset but 8–12 h duration; nifedipine ~20 min; lisinopril ~1 h; amlodipine 24–48 h — from the card's own Table 4).
4. **Wean the infusion down in steps** rather than stopping it; watch through at least one full dosing interval of the oral agent.
5. Re-dose/uptitrate the oral agent before the next scheduled interval if BP creeps.
6. Anticipate the **rebound window**: nicardipine loses half its effect in ~30 min; clevidipine 5–15 min; nitroprusside <2 min (card Table 3). The shorter the drip's offset, the more overlap you need.
7. **Do not discharge on a regimen you only observed for one dose** — AHA 2024: BP takes days to weeks to equilibrate to a change.

---

## 6. DISCHARGE — starting or intensifying antihypertensives at discharge

### 6a. The headline trial-equivalent: Anderson TS 2019

**Anderson TS, Jing B, Auerbach A, Wray CM, Lee S, Boscardin WJ, Fung K, Ngo S, Silvestrini M, Steinman MA. Clinical Outcomes After Intensifying Antihypertensive Medication Regimens Among Older Adults at Hospital Discharge.** *JAMA Intern Med.* 2019;179(11):1528–1536. doi:10.1001/jamainternmed.2019.3007 — https://pubmed.ncbi.nlm.nih.gov/31424475/ (PMC6705136)

- VA national, 2011–2013; adults **≥65** with hypertension hospitalized for **common noncardiac conditions**.
- Exposure: discharge prescription for a **new or higher-dose** antihypertensive than pre-admission. Propensity matched-pairs, **n=4,056** (mean age 77, 97.7% men).
- **30 days: readmission HR 1.23 (95% CI 1.07–1.42), NNH 27 (16–76).**
- **30 days: serious adverse events HR 1.41 (95% CI 1.06–1.88), NNH 63 (34–370).**
- **1 year: no difference in cardiovascular events, HR 1.18 (0.99–1.40).**
- **1 year: no difference in SBP** — 134.7 vs 134.4 mmHg; difference-in-differences **0.6 mmHg (−2.4 to 3.7)**.
- Bottom line: **you buy a readmission and an adverse event, and you do not buy any BP control.**

### 6b. Corroborating data

- **Rastogi 2021** (same numbers as section 2): 9.2% of hypertensive inpatients were discharged intensified. At 30 days, MI 0.1% vs 0.2% and stroke 0.5% vs 0.4% (both p>0.99). At **1 year**, proportion with SBP >139 was **0.41 vs 0.40 (p=0.86)** and max SBP **157.2 vs 157.8 (p=0.54)**. Explicitly: "medication intensification at discharge was not associated with improved blood pressure control."
- **Anderson TS, Jing B, Fung K, Steinman MA.** Older adults' persistence to antihypertensives prescribed at hospital discharge. *J Gen Intern Med.* 2021;36:3900–3902. doi:10.1007/s11606-020-06401-0 — **~1/3 of discharge antihypertensives are never refilled; ~half are discontinued within 1 year.** So even the theoretical benefit mostly evaporates.
- **Rachoin, Cerceo & Anderson, TWDFNR 2024** (*J Hosp Med.* 2024;19(3):219–222) — https://shmpublications.onlinelibrary.wiley.com/doi/full/10.1002/jhm.13185 — the dedicated Choosing Wisely treatment of exactly this practice. Their framing: don't react to a single BP; look at the trend, the risk factors, and the admitting diagnosis; hospital BPs are elevated by white-coat effect, medication interruption, stress, anxiety, nausea, fever and pain.

### 6c. What AHA 2024 says to do instead

- "The best available evidence suggests **maintaining the prehospitalization antihypertensive medication regimen and avoiding intensification at discharge**." (refs: Rastogi 2021, Anderson 2023, Mohandas 2021)
- Do a real **discharge medication reconciliation** — the goal is to find **guideline-discordant** regimens and to **stop the BP-raising drugs** (18.5% of hypertensive adults take one), not to add another antihypertensive.
- Anything genuinely new should follow outpatient guideline logic and account for health literacy, insurance, affordability, social support, mobility, transport.
- Consider **single-pill combination therapy** when a regimen is genuinely needed (only 27% of US adults on ≥2 agents use one).
- **1 in 7 patients is confused about their medications at discharge**, which itself raises readmission risk — so counseling matters more than the extra pill.
- Some patients reasonably prefer to **defer any change** until they've recovered and can reassess with their PCP.
- Recommend a **validated home BP monitor** (https://www.validatebp.com) and home BP monitoring.
- Table 3, implication #3 (ED context, but generalizes): prefer **restarting home medications** and **planning close outpatient follow-up** over intensification.

### 6d. Follow-up interval — what to actually write in the discharge summary

- **Ann Intern Med 2024** systematic review: across guidelines, the consensus for markedly elevated BP without target-organ damage is **outpatient oral therapy with follow-up in days to weeks**.
- **ACEP 2013**, Level C consensus: "Patients with asymptomatic markedly elevated blood pressure should be referred for outpatient follow-up."
- **2025 AHA/ACC guideline** (secondary source): reassess response **~1 month** after initiating or changing therapy, then titrate to max tolerated dose or add a second agent. https://pmc.ncbi.nlm.nih.gov/articles/PMC12617343/
- **Practical card line:** PCP or team-based follow-up **within 1–4 weeks** (sooner — days — if any change was made or follow-up is unreliable), with home BP readings on a validated cuff brought to the visit. If a timely PCP visit is not feasible, AHA 2024 says it is reasonable to book another team member (pharmacist, case manager) — team-based care beats usual care for BP control.

---

## 7. COST OF THE IV AGENTS

**All figures are approximate list prices (AWP or WAC), not what any hospital pays, and are dated. Institutional contract pricing differs substantially. Present as orders of magnitude.**

### 7a. The nitroprusside price shock — the story worth telling

**Khot UN, Vogan ED, Militello MA. Nitroprusside and Isoproterenol Use after Major Price Increases.** *N Engl J Med.* 2017;377(6):594–595. doi:10.1056/NEJMc1700244 — https://www.nejm.org/doi/full/10.1056/NEJMc1700244 (PMID 28792879). 47 US hospitals, 2012–2015:

| Drug | WAC 2012 | WAC 2015 | Fold increase | Utilization change |
|---|---|---|---|---|
| **Nitroprusside** (per 50 mg) | **$27.46** | **$880.88** | **~30×** | **use fell 53%** |
| Isoproterenol | $26.20 | $1,790.11 | ~70× | use fell 35% |

(Cleveland Clinic press summary, with the same numbers: https://newsroom.clevelandclinic.org/2017/08/09/use-of-common-heart-drugs-dropped-after-price-increases-cleveland-clinic-study-finds). Rights had passed through Marathon Pharmaceuticals before the increases. The point of the letter: **the price hike changed prescribing**, contradicting claims that it would not affect access. Generic entry after 2017 brought prices down substantially, but nitroprusside is still not a cheap drug and most academic formularies restrict it — which is a second, better reason to avoid it alongside cyanide toxicity and coronary steal.

### 7b. Per-vial comparisons

**Cruz JE, Thomas Z, Lee D, Moskowitz DM, Nemeth J. Therapeutic Interchange of Clevidipine For Sodium Nitroprusside in Cardiac Surgery.** *P T.* 2016;41(10):635–639 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5047001/ (pricing as of **2016**):

| Agent | Presentation | AWP | WAC |
|---|---|---|---|
| Sodium nitroprusside (Nitropress) | 50 mg / 2 mL | **$1,057** | $881 |
| Clevidipine (Cleviprex) | 25 mg / 50 mL | **$108** | $90 |
| Nicardipine (generic) | 25 mg / 10 mL | **$24** | $20 |

At those 2016 prices clevidipine was **<10% the cost of nitroprusside per vial** — which is why many centers interchanged them. Reported cost avoidance at one institution: ~$185,000 in the remainder of 2015 and an estimated $300,000 in 2016.

**Johnson L, Erdman M, Ferreira J. Comparison of clevidipine vs nicardipine in the treatment of hypertensive urgency and emergency in critically ill patients.** *Am J Health Syst Pharm.* 2024;81(21):e668–e676. doi:10.1093/ajhp/zxae156 — https://academic.oup.com/ajhp/article-abstract/81/21/e668/7699719 (PMID 38923443; erratum 2025;82:254):
- 182 critically ill patients (103 nicardipine, 79 clevidipine).
- **Clevidipine AWP $199.37 per vial as of June 2023 — 682% higher than a bag of nicardipine** (implies ~$25 per nicardipine bag).
- **Time to goal BP was the same: 33 min (nicardipine) vs 35 min (clevidipine), p=0.37.**
- Clevidipine delivered less drug volume (222 vs 518 mL) but **total ICU volume was identical** (3,370 vs 3,383 mL), so the volume argument evaporated.
- Authors' conclusion: the cost difference is not justified by outcomes.

**Saldana S, Breslin J, Hanify J, et al. Comparison of Clevidipine and Nicardipine for Acute Blood Pressure Reduction in Hemorrhagic Stroke.** *Neurocrit Care.* 2022;36(3):983–992. doi:10.1007/s12028-021-01407-w — https://pubmed.ncbi.nlm.nih.gov/34904214/ : nicardipine **$99.60 vs** clevidipine **$497.40** per treatment course (p<0.0001); time to goal SBP no different (30 vs 45 min, ns); nicardipine had **less rebound hypertension (40% vs 75.9%, p=0.0017)** and less bradycardia.

Perioperative cardiac surgery comparison (48 h): median **$128.58 clevidipine vs $55.74 nicardipine** — https://pubmed.ncbi.nlm.nih.gov/34693825/

### 7c. Rough ordering, cheapest to most expensive (approximate, 2016–2024 list prices)

**IV nitroglycerin ≈ IV hydralazine ≈ IV labetalol (single dollars to low tens of dollars per vial) << nicardipine (~$20–25 per bag) < esmolol < clevidipine (~$90–200 per vial) << nitroprusside (historically $27, post-2015 up to ~$880–1,057 per 50 mg vial; lower today with generics).** A frequently circulated per-course comparison lists fenoldopam $113.28, nicardipine $94.67, esmolol $82.15, nitroprusside $20.86, labetalol $14.40, nitroglycerin $2.90 — **source and vintage unverified; do not print these specific numbers.** Drugs.com lists IV labetalol 5 mg/mL, 20 mL from about **$6** (consumer price guide, undated).

### 7d. The cost lever that actually matters on the wards

It is not agent choice — it is **drip duration**. Zhu 2020: nicardipine cost **$14,207 vs $29,299 per patient** purely as a function of early vs late oral initiation. Shah 2016 (UCSF): **$18,475 saved per patient** by starting orals earlier. Getting the patient off the drip a day sooner dwarfs the per-vial difference between any two agents.

---

## 8. ICU vs FLOOR

### 8a. What the guidelines say

- **2017 ACC/AHA** (carried forward by the 2025 guideline per secondary sources): for hypertensive emergency, **ICU admission is recommended** for continuous BP and target-organ monitoring and for parenteral therapy. *(COR I; the LOE reported by secondary sources varied between B-NR and B-R — verify against the PDF.)*
- **AHA 2024, Table 3 implication #5:** "Hypertensive emergencies require immediate and acute treatment usually with parenteral medications and **often in the ICU setting**." Note the hedge — *often*, not *always*.
- **AHA 2024**: arterial lines are **preferred** for hypertensive emergency and for IV antihypertensive administration, because of the documented oscillometric underestimation at high BP and because you need to monitor the **rate** of decline.
- **Ann Intern Med 2024**: across 14 guidelines, hypertensive-emergency recommendations "consistently included use of intravenous antihypertensives **in intensive care settings**."

### 8b. The actual decision drivers at an average academic center

The card already has the right one-liner ("ICU if needs arterial line, antihypertensive gtt, or if severe end-organ damage"). Expanded:

1. **Does the patient need a continuously titrated infusion?** Almost every institution's nursing policy ties continuous vasoactive infusions to an ICU or step-down nurse:patient ratio, independent of the drug's pharmacology. This, not the drug, is usually what forces the ICU bed.
2. **How steep is the required BP drop, and how bad is the consequence of overshoot?** Aortic dissection (SBP <120 in 20 min), acute pulmonary edema, and ICH with SBP >220 all demand minute-to-minute control → ICU + arterial line. Ischemic stroke with permissive hypertension needs far less.
3. **What is the end-organ syndrome?** Dissection, acute HF/pulmonary edema, ACS, ICH/SAH, eclampsia, and encephalopathy all carry their own ICU indication for reasons beyond BP.
4. **Is an arterial line needed?** Not the same question as "does this need ICU."
5. **Local formulary/nursing restriction.** This is the real, unglamorous determinant and it varies by hospital — **check your own unit's policy**; do not print a generic list as if it were universal.

### 8c. Arterial line — the honest read

- **Mandatory by label for nitroprusside.** FDA boxed warning (eg, https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5a599880-c133-44ef-a9f2-bd1b681563be): nitroprusside "can cause precipitous decreases in blood pressure... In patients not properly monitored, these decreases can lead to irreversible ischemic injuries or death. Sodium nitroprusside should be used **only when available equipment and personnel allow blood pressure to be continuously monitored**." Same warning: above ~2 mcg/kg/min it generates clinically important cyanide; usual 0.5–10 mcg/kg/min; **infusion at the maximum rate must never last more than 10 minutes**, and if BP is not controlled after 10 min at max rate, stop the drug.
- **Strongly favored** for aortic dissection and for any situation where the *rate* of decline is itself the therapeutic target (AHA 2024; BMJ 2024 makes the same point for dissection).
- **Not universally required.** EMCrit argues an arterial line "is probably unnecessary in most cases of hypertensive emergency": the pain of insertion itself raises BP, there is no prospective evidence of benefit, and the BP targets are themselves arbitrary enough that chasing them to the mmHg is illogical. Reserve it for very labile pressure, extreme elevation, or deterioration despite therapy. https://emcrit.org/ibcc/htn/
- Counterweight: the Wax *Anesthesiology* data show that **an arterial line alone leads to more antihypertensive administration** than an arterial line plus cuff (44% vs 12% of hypertensive patients) — a line does not just measure, it changes behavior.

### 8d. What can run where (generalization — verify locally)

| Agent | Typical setting | Rationale |
|---|---|---|
| **Nitroglycerin paste/patch** | **Floor** | Already on the card as the floor-friendly option |
| **Labetalol IV bolus** | **Floor** (with the section-2 caveats) | Intermittent, self-limited, 3–6 h duration; EMCrit prefers sequential boluses precisely because they don't accumulate the way an infusion does |
| **Hydralazine IV bolus** | Floor, but discouraged | Unpredictable magnitude and timing; **BMJ 2024 explicitly does not recommend IV hydralazine or nitroprusside** for hypertensive emergency because both cause unexpected sudden drops beyond the intended target |
| **Nicardipine, clevidipine infusion** | **ICU or step-down**, per local policy | Continuous titratable infusion; arterial line commonly but not universally required |
| **Nitroglycerin, esmolol, labetalol infusion** | **ICU/step-down** | Continuous infusion policy |
| **Nitroprusside** | **ICU + continuous (usually arterial) BP monitoring — required by label** | Boxed warning above |

---

## 9. CONDENSED CANDIDATE LINES FOR THE CARD

Ordered by value per square centimeter.

1. **Workup (routine, everyone):** BMP, CBC, CXR, 12-lead ECG + HR, volume status/orthostasis, plus history (adherence, outpatient BPs) and exam (bilateral pulses, heart/lungs, **fundi**). *(AHA 2024)*
   **Directed only:** troponin ± serial (chest pain/ECG changes) · non-con head CT (any neuro deficit/AMS — **insensitive for hypertensive encephalopathy, which is clinical**) · MRI if PRES · **UA + sediment** (rising Cr) · **smear for schistocytes + LDH** (anemia + low plts) · CTA (dissection) · urine tox. **No symptoms → testing can be minimal (5-symptom screen NPV 99%).** *(BMJ 2024;386:e077205)*
2. **Do not write PRN antihypertensives for asymptomatic elevated BP.** AHA 2024: "In general, it is prudent to avoid PRN orders..."; "Use of intravenous antihypertensives is not supported by the evidence in the absence of hypertensive emergency."
3. **Numbers that end the argument:** IV/new-PO treatment → composite adverse events OR 1.28, **IV subgroup OR 1.90** (Anderson, JAMA IM 2023;183:715, n=66,140) · treated vs untreated AKI 10.3% vs 7.9%, myocardial injury OR 2.23 (Rastogi, JAMA IM 2021;181:345) · PRN (93% IV) → AKI OR 1.24, **>25% SBP drop in 1 h OR 2.05**, death OR 2.36 (Mohandas, Hypertension 2021;78:516) · **84.5% of IV doses were given for SBP <180; 32.6% dropped >25% within 6 h** (Lipari, JHM 2016;11:193).
4. **44% of severe inpatient HTN resolves spontaneously within 3 h with no drug at all** (Garg/Ghazi, Am J Hypertens 2024;37:273, n=12,825); treated and untreated are equally likely to drop ≥20 mmHg by the next reading (58% vs 61%, Rastogi).
5. **Rest, don't treat.** 30 min of quiet rest normalized 32% of ED hypertensive urgencies; rest vs telmisartan was a tie (68.5% vs 69.1%). *(Breu & Axon, JHM 2018;13:860)*
6. **Expand "Assess" — top of the list is the MAR:** *held/missed home antihypertensives* (**41%** of patients on PRN antihypertensives weren't getting their home regimen; discontinuation is associated with AKI OR 1.23 — J Intern Med 2026;300:284), **NPO**, pain, anxiety/poor sleep/being woken for vitals, **alcohol/benzo/clonidine/beta-blocker withdrawal**, retention or blocked Foley, volume overload/IV fluids, agitation-delirium, hypoxia/hypercapnia, hypoglycemia, HR (AF-RVR, reflex tachycardia), **18.5% of hypertensive adults take a BP-raising drug** — NSAIDs, steroids, antidepressants, decongestants, stimulants, calcineurin inhibitors, ESAs, VEGF inhibitors *(JAMA IM 2022;182:90)*.
   **Do NOT lower the BP in: Cushing reflex (HTN + bradycardia + irregular resp = raised ICP — lower the ICP).** Also think: autonomic dysreflexia (SCI ≥T6, usually a blocked catheter — **fix the stimulus first**), thyroid storm, serotonin syndrome, pheo/sympathomimetic, preeclampsia.
7. **Measurement:** cuff **too small → falsely HIGH** (regular cuff on an XL arm = **+19.5 mmHg SBP**; one size too small = **+9.6**; Cuff(SZ), JAMA IM 2023;183:1061); cuff too large → falsely low. Arm **unsupported at the side +6.5/+4.4**, **hand on lap +3.9/+4.0** vs desk at heart level (ARMS, JAMA IM 2024;184:1436). Supine +3–10 SBP; back unsupported +5–15/+6; legs crossed +5–8/+3–5 (AHA 2019 Table 4). Full bladder, talking, no rest period, recent caffeine/nicotine each add roughly 4–20 SBP (Kallioinen, J Hypertens 2017;35:421). **36% of inpatient cuffs are the wrong size** (AHA 2024). **Inverse trap in the ICU: above 180/100, oscillometric cuffs may UNDERestimate by up to 50/30 vs an arterial line** (AHA 2024).
8. **Off the drip:** start the PO agent **while the drip is still running**, wait for its onset, then wean the infusion in steps. Nicardipine loses 50% of effect in ~30 min; no oral agent peaks that fast — that gap is the rebound. Label: start a non-nicardipine oral **at** discontinuation; start oral nicardipine **1 h before**. Longer IV/PO overlap = **lower** systolic variability (Front Neurol 2022;13:866557). Pair nicardipine/clevidipine → nifedipine XR (**not amlodipine**); labetalol/esmolol → PO labetalol or carvedilol; nonadherence → just restart home meds. Early PO transition: nicardipine 118 → 30 h, **$18,475/patient saved (UCSF, JSCVD 2016;25:2290)**; ICU LOS 5 → 2 days (Neurocrit Care 2020;32:707).
9. **Discharge: do not intensify.** 30-day readmission **HR 1.23, NNH 27**; serious adverse events **HR 1.41, NNH 63**; **zero** benefit in 1-yr CV events or SBP (**0.6 mmHg** difference) — Anderson, JAMA IM 2019;179:1528. One third of discharge antihypertensives are never filled. **Instead:** restart the home regimen, reconcile and **stop** BP-raising drugs, arrange PCP/team follow-up in **days to 4 weeks**, validated home cuff (validatebp.com).
10. **Cost:** nitroprusside WAC went **$27 → $881 per 50 mg (2012→2015, ~30×)** and use fell 53% (NEJM 2017;377:594). Clevidipine ≈ **$199/vial (AWP 2023)** vs a nicardipine bag ≈ **$25** — **682% more for identical time-to-goal** (AJHP 2024;81:e668). The real money is **drip duration**, not agent choice.
11. **ICU vs floor:** driven by (a) need for a continuously titrated infusion — usually a nursing-ratio policy, not a pharmacology fact; (b) steepness of required drop and cost of overshoot; (c) the end-organ syndrome itself; (d) arterial-line need; (e) local formulary restriction. **Nitroprusside cannot be given without continuous BP monitoring (boxed warning)**; nicardipine/clevidipine infusions are ICU/step-down at most centers; labetalol boluses and nitro paste are floor agents. An arterial line is **not** mandatory for every hypertensive emergency (EMCrit) — but note that an a-line alone drives more antihypertensive dosing than an a-line plus cuff (44% vs 12%, Anesthesiology 2011;115:973).

---

## 10. VERIFICATION DEBT — check before printing

1. **2025 AHA/ACC guideline** (CIR.0000000000001356) and **AHA 2024** (HYP.0000000000000238) full text: ahajournals.org blocks automated access (403 / Cloudflare). AHA 2024 content above came from a complete PDF mirror at docshepherd.com and matches the PubMed abstract and multiple independent summaries, so I consider it reliable. **The 2025 guideline content is entirely secondary** — confirm the exact recommendation wording and the COR/LOE for the ICU-admission and severe-hypertension recommendations against the real PDF or a UCSF-authenticated copy.
2. The **2017 ACC/AHA** hypertensive-crisis workup items (UA for hematuria/proteinuria with microscopy for RBCs and casts; CBC + smear for MAHA; baseline troponin with repeat at ~3 h; head CT for neuro abnormality) came from secondary summaries of Section 11.2, not the guideline PDF. BMJ 2024 independently supports the substance of each. **Verify the exact wording.**
3. The **2025 ACEP clinical policy** (Ann Emerg Med 2025;86:e1) recommendation levels are behind ACEP login — not verified.
4. The per-course IV cost list (fenoldopam $113.28 / nicardipine $94.67 / esmolol $82.15 / nitroprusside $20.86 / labetalol $14.40 / nitroglycerin $2.90) has an **unverified source and date** — do not print.
5. "Cuff over clothing = 5–50 mmHg" is an **AHA teaching-slide figure** citing Handler 2009; the **Kallioinen 2017 systematic review found no significant effect**. If you use it, hedge it.
6. **UCSF Hospital Handbook** has a hypertension chapter at https://hospitalhandbook.ucsf.edu/05-hypertension/05-hypertension-0 that returned 503 on both attempts. Worth checking manually for local (Parnassus/ZSFG) drip-unit policy and nursing call parameters — that is the piece no published source can supply.
