# -*- coding: utf-8 -*-
"""Condition-specific targets. Ordered by how fast you move: 20 min at the top,
leave-it-alone at the bottom.

Cheat-sheet register. `src`: wb = card unchanged, fix = card corrected here,
add = not on the card. Corrections read `card: X` rather than arguing the case.
"""

CONDS = [
# --- the two defaults. Everything after this is an exception to one of them. ---
{
 'name': 'Severe HTN, asx', 'sub': 'no acute TOD', 'src': 'fix', 'base': True,
 'goal': 'No acute target',
 'win': 'days to weeks', 'slow': True,
 'pref': 'Fix the reversible cause first. Then restart or adjust the <b>long-acting</b> regimen, '
         'and arrange outpatient f/u.',
 'avoid': '<span class="no">Intermittent IV <em>or</em> PO for the number alone &mdash; Class 3 '
          'Harm.</span> PRN orders. Immediate-acting PO.',
 'why': '<b>Treat the patient, not the number.</b> Not an ordinary pt if: prior HTN emergency or TOD &middot; chronic uncontrolled + high CVD risk &middot; recent ICH, stroke, ACS, aortic disease &middot; procedure pending &middot; home regimen never restarted. Otherwise <b>44% resolve untreated in 3 h</b>, no RCTs, and treating cost AKI <b>10.3 vs 7.9%</b>.',
},
{
 'name': 'Pre-procedure', 'sub': 'the surgeon wants it lower first', 'src': 'add', 'base': True,
 'goal': 'No number to hit. Anaesthesia proceeds at &lt;180/120 clinic',
 'win': 'do not cancel for the number', 'slow': True,
 'pref': 'Give the <b>held home morning dose</b> &mdash; NPO at midnight is usually the whole problem. Recheck after <b>30 min rest</b>, correct cuff. Treat pain, anxiety, full bladder.',
 'avoid': '<span class="no">IV hydralazine or labetalol the morning of.</span> A <em>new</em> agent. Starting a BB day-of, or stopping a BB or clonidine (both Class 3 Harm).',
 'why': '180/110 is <b>COR 2b</b> and needs elective <em>high-risk</em> surgery + poor control documented <em>before the day</em>. A one-off in holding is neither. Howell, 30 studies: OR 1.35, <b>&ldquo;not clinically significant&rdquo;</b>; the only RCT found postponing changed nothing and lengthened stay. <b>No threshold exists for endoscopy, cath or IR.</b> Chronic HTN does not raise the intraop MAP floor.',
},
{
 'name': 'Discharge', 'sub': 'asx in the 180s, medically ready', 'src': 'add', 'base': True,
 'goal': 'No discharge threshold exists',
 'win': 'f/u within 7 d', 'slow': True,
 'pref': 'If the <em>chronic</em> disease is undertreated: optimise the <b>long-acting</b> regimen, f/u in 7 d (1&ndash;3 d if severe), BMP at 2&ndash;4 wk on a new ACEi, ARB or diuretic.',
 'avoid': '<span class="no">Adding a drug to move today&rsquo;s number.</span>',
 'why': '<b>14 guidelines, 11 countries: no inpatient BP goal, no discharge threshold</b> &mdash; the rule is institutional. <b>65%</b> were controlled as outpatients before admission, and intensification tracked the number (8&rarr;24&rarr;40%), not benefit. At discharge: readmit <b>NNH 27</b>, <b>0.6 mmHg</b> at 1 yr.',
},
{
 'name': 'HTN emergency, general', 'sub': 'when no row below applies', 'src': 'fix', 'base': True,
 'goal': '&le;25% in 1st h &rarr; &lt;160/100 by 2&ndash;6 h &rarr; 130&ndash;140 by 24&ndash;48 h',
 'win': 'the default rule',
 'pref': 'Titratable IV &mdash; labetalol or nicardipine cover most. <b>ICU is Class 1.</b> A-line '
         'if on a gtt.',
 'avoid': '<span class="no">Dropping &gt;25% in the first hour.</span> Hydralazine. PO or SL for '
          'acute control.',
 'why': 'TOD makes the dx, not the number. Overcorrection is the harm: <b>57%</b> on nicardipine or nitroprusside dropped MAP &gt;25% within 30 min. ICU is Class 1.',
},
{
 'name': 'Aortic dissection', 'src': 'fix',
 'goal': 'SBP &lt;120 &middot; HR 60&ndash;80',
 'win': 'within 20 min',
 'pref': '<b>IV BB first</b> &mdash; esmolol or labetalol. Vasodilator (nicardipine, clevidipine) '
         'only after rate control. IV opioid.',
 'avoid': '<span class="no">Any vasodilator before the BB.</span> Hydralazine.',
 'why': 'Wall stress tracks <b>dP/dt</b> &mdash; vasodilator first &rarr; reflex tachy &rarr; propagation. Or lowest BP that perfuses. BB contraindicated &rarr; IV dilt/verapamil. Acute AR: do not slow hard. <em>Card HR &lt;60 = the 2010 target.</em>',
},
{
 'name': 'Pre-eclampsia, severe', 'sub': 'and eclampsia, to 6 wks postpartum', 'src': 'add',
 'goal': '&lt;160/&lt;110, land 140&ndash;150/90&ndash;100',
 'win': 'within 30&ndash;60 min',
 'pref': 'All three first-line. <b>IV labetalol</b> 20&rarr;40&rarr;80 q10min (max 300). '
         '<b>IV hydralazine</b> 5&ndash;10, then 10 q20min. <b>PO IR nifedipine</b> '
         '10&rarr;20&rarr;20 q20min.',
 'avoid': '<span class="no">ACEi, ARB, renin inhibitors, atenolol, nitroprusside, MRA</span> '
          '&mdash; Class 3 Harm.',
 'why': 'Severe range = &ge;160 or &ge;110 for 15 min. Goal is <b>not</b> normal. <b>Mg is seizure ppx, not an antihypertensive</b> (ACOG, verbatim). Capsules swallowed, never punctured or SL. 3 failed doses &rarr; call.',
},
{
 'name': 'ACS', 'src': 'fix',
 'goal': 'SBP &lt;140 &middot; keep DBP &gt;60',
 'win': 'within 1 h',
 'pref': 'Nitro (topical or gtt). Esmolol or labetalol. Nicardipine or clevidipine.',
 'avoid': '<span class="no">Nitroprusside</span> (steal). Hydralazine. <span class="no">Nitrates within 24 h sildenafil/vardenafil, 48 h tadalafil, 12 h avanafil</span>, or RVMI. BB if HF signs, HR &lt;60, SBP &lt;100, shock, high-grade block, bronchospasm.',
 'why': 'DBP floor is physiology, not guideline: LV perfuses in diastole. COMMIT &mdash; early IV metoprolol bought no survival, +11 shocks/1000. 2025 wants <b>PO BB within 24 h</b>, not a drip. <em>Card: &ldquo;judicious nitro w/ RVMI&rdquo; is now <b>avoid</b>; PDE5i window missing entirely.</em>',
},
{
 'name': 'Acute pulmonary edema', 'sub': 'SCAPE', 'src': 'fix',
 'goal': 'SBP &lt;140',
 'win': 'within 1 h',
 'pref': '<b>High-dose NTG + NIPPV</b> first. Nitroprusside, nicardipine or clevidipine as adjuncts.',
 'avoid': '<span class="no">IV BB while decompensated.</span> Nitroprusside w/ ACS or renal failure.',
 'why': '<b>Volume-redistributed, not overloaded</b> &mdash; diuresis is not primary and must not delay NTG + PEEP. NTG here runs above 400 mcg/min. <em>Card: the BB line needs splitting &mdash; IV contraindicated, chronic PO continued. NIPPV absent.</em>',
},
{
 'name': 'ICH', 'src': 'fix',
 'goal': 'SBP 150&ndash;220 &rarr; 130 to &lt;140, hold &ge;7 d',
 'win': 'start &lt;2 h, at target in 1 h',
 'pref': 'Nicardipine or clevidipine gtt; labetalol. A-line where feasible.',
 'avoid': '<span class="no">SBP &lt;130 &mdash; Class 3 Harm.</span> Bolus-and-chase.',
 'why': 'Smoothness counts as much as the number: peaks and variability worsen outcome, over-rapid drops drove the ATACH-2 renal signal. &gt;220 is thin evidence &mdash; titrate, stay above 130. <em>Most out-of-date row: card band, target and floor all wrong.</em>',
},
{
 'name': 'Ischemic stroke', 'src': 'fix',
 'goal': '&lt;185/110 pre-lysis &rarr; &lt;180/105 &times; 24 h. No IVT/EVT: treat only at '
         '&ge;220/120, then ~15% over 24 h',
 'win': 'otherwise permissive', 'slow': True,
 'pref': 'Labetalol, nicardipine, clevidipine. Nitroprusside is the named fallback for refractory '
         'BP or DBP &gt;140.',
 'avoid': '<span class="no">SBP &lt;140 in the first 24&ndash;72 h after successful EVT &mdash; '
          'Class 3 Harm, LOE A.</span> &lt;140 after IVT: no benefit.',
 'why': '<b>220/120 is a threshold, not a target.</b> Below it, treating in 48&ndash;72 h is Class 3 No Benefit. Treat anyway for a second indication (ACS, HF, dissection, pre-eclampsia). <em>Card reads the threshold as a target and omits both post-reperfusion rules.</em>',
},
{
 'name': 'SAH', 'sub': 'aneurysm unsecured', 'src': 'add',
 'goal': 'No evidence-based number. SBP &lt;160 most used',
 'win': 'stability over speed', 'slow': True,
 'pref': 'Short-acting titratable: nicardipine or clevidipine gtt, labetalol boluses.',
 'avoid': '<span class="no">Sudden profound drops.</span> Hypotension and variability count as harm '
          'too.',
 'why': '2023 guideline: evidence insufficient for any target. Once secured the logic <b>inverts</b> to permissive/induced HTN for DCI. <b>Nimodipine 60 q4h &times; 21 d is for DCI, not BP</b> &mdash; if it drops the pressure, split to 30 q2h, do not stop.',
},
{
 'name': 'HTN encephalopathy', 'sub': 'and PRES &mdash; same row', 'src': 'fix',
 'goal': 'MAP &darr; 20&ndash;25%',
 'win': 'over 1&ndash;2 h',
 'pref': 'Nicardipine or clevidipine; labetalol adjunct.',
 'avoid': 'NTG and nitroprusside where ICP is a concern &mdash; both dilate cerebral vessels.',
 'why': '<b>Expert consensus, no RCT.</b> PRES is the imaging correlate; encephalopathy is a dx of exclusion confirmed by reversal. <b>Remove the trigger</b>: CNI, VEGFi, cytotoxics. Pregnant &rarr; eclampsia pathway.',
},
{
 'name': 'Sympathetic crisis', 'sub': 'pheo, stimulants, MAOI, clonidine withdrawal', 'src': 'add',
 'goal': 'No fixed number &mdash; titrate to symptoms and TOD',
 'pref': '<b>Benzos first</b> in stimulant toxicity. Phentolamine. Nicardipine or clevidipine.',
 'avoid': '<span class="no">BB monotherapy.</span>',
 'why': 'Pheo: <b>alpha before beta</b>, always. Clonidine withdrawal: restart the clonidine. Cocaine: the classic prohibition is weakly evidenced &mdash; modern meta-analyses show no excess death or MI. <b>Do not stop a chronic BB for a positive screen.</b>',
},
{
 'name': 'Scleroderma renal crisis', 'src': 'add',
 'goal': 'SBP &darr; ~20 mmHg per 24 h, baseline by ~72 h',
 'win': 'deliberately slow', 'slow': True,
 'pref': '<b>Captopril</b> 6.25&ndash;12.5 mg, up by 12.5&ndash;25 q4&ndash;8h. CCB and ARB are '
         'add-ons only.',
 'avoid': '<span class="no">Stopping the ACEi because the Cr rose.</span> Prednisone &gt;15 mg/d '
          'precipitates it.',
 'why': 'The one emergency defined by a <em>drug</em>, not a number &mdash; it is renin-driven. Captopril for fast on/off, which is what lets you escalate q4h. <b>Continue through rising Cr and through dialysis.</b>',
},
{
 'name': 'AKI w/ TMA', 'sub': 'malignant HTN', 'src': 'add',
 'goal': 'Gradual &mdash; SBP ~160 early, slower after',
 'win': 'hours, not minutes', 'slow': True,
 'pref': 'Nicardipine or clevidipine &mdash; no renal adjustment, no thiocyanate.',
 'avoid': '<span class="no">Nitroprusside in renal impairment.</span> ACEi/ARB acutely.',
 'why': 'Over-rapid lowering worsens the AKI. Acute RAS blockade dilates the efferent arteriole and drops filtration further. <em>Card lists MAHA as TOD but gives it no row.</em>',
},
{
 'name': 'Intra- and post-op', 'sub': 'not the pre-op ask &mdash; see Pre-procedure', 'src': 'add',
 'goal': 'Avoid hypotension as hard as HTN &mdash; MAP &ge;60&ndash;65',
 'pref': 'Esmolol, nicardipine, clevidipine. Treat pain, hypoxia, hypercarbia, full bladder and '
         'shivering first.',
 'avoid': '<span class="no">Starting a BB on the day of surgery &mdash; Class 3 Harm.</span> '
          '<span class="no">Stopping a chronic one abruptly &mdash; Class 3 Harm.</span>',
 'why': 'The 2024 guideline warns the other way: intraop hypotension drives myocardial injury. Hold ACEi/ARB 24 h pre-op. Consider delaying elective surgery at &ge;180/110.',
},
{
 'name': 'Autonomic dysreflexia', 'sub': 'SCI at or above T6', 'src': 'add',
 'goal': '~20&ndash;40 mmHg above <em>their</em> baseline',
 'win': 'non-drug first',
 'pref': '<b>Sit up, legs down, loosen binders, find the stimulus</b> &mdash; nearly always blocked catheter, full bladder or impacted bowel. Drug only if that fails and SBP &ge;150: NTG ointment above the injury, or bite-and-swallow nifedipine.',
 'avoid': '<span class="no">Nitrates within 24&ndash;48 h of a PDE5i</span> &mdash; common here.',
 'why': 'Their usual SBP is often 90&ndash;110, so <b>a normal-looking 140 is a 40-point emergency</b>. Most episodes need no drug. Ointment because it can be wiped off.',
},
]
