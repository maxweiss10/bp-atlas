# -*- coding: utf-8 -*-
"""Condition-specific targets for hypertensive emergency.

One row per condition, ordered by how fast you are expected to move: the
dissection that wants 20 minutes at the top, the strokes and the renal crises
that want you to leave the pressure alone at the bottom.

`src` is the provenance mark - 'wb' on the White Book card unchanged, 'fix' on
the card with something corrected here, 'add' not on the card.  Corrections are
written into the `why` text rather than hidden, because the point of the mark
is that the reader can see what moved.
"""

CONDS = [
{
 'name': 'Aortic dissection', 'src': 'fix',
 'goal': 'SBP &lt;120 &middot; HR 60&ndash;80',
 'win': 'within 20 min',
 'pref': '<b>IV beta blocker first</b> &mdash; esmolol or labetalol. Vasodilator '
         '(nicardipine, clevidipine) only once the rate is controlled. IV opioid for pain.',
 'avoid': '<span class="no">Any vasodilator before rate control.</span> Hydralazine.',
 'why': 'Wall stress tracks <b>dP/dt</b>, not pressure alone, so a vasodilator given first '
        'causes reflex tachycardia and propagates the dissection. The target is the lowest '
        'pressure that still perfuses end organs. If beta blockade is contraindicated, IV '
        'diltiazem or verapamil; with acute aortic regurgitation do not slow the rate hard, '
        'because a long diastole worsens the regurgitant volume. '
        '<b>Corrected:</b> the card’s HR &lt;60 is the 2010 target &mdash; the 2022 ACC/AHA '
        'aortic guideline says 60&ndash;80.',
},
{
 'name': 'Pre-eclampsia, severe features', 'sub': 'and eclampsia, to 6 weeks postpartum',
 'src': 'add',
 'goal': '&lt;160/&lt;110, landing at 140&ndash;150/90&ndash;100',
 'win': 'within 30&ndash;60 min',
 'pref': 'All three are first-line. <b>IV labetalol</b> 20&rarr;40&rarr;80 mg q10min (max 300 mg). '
         '<b>IV hydralazine</b> 5&ndash;10 mg, then 10 mg q20min. '
         '<b>PO immediate-release nifedipine</b> 10&rarr;20&rarr;20 mg q20min.',
 'avoid': '<span class="no">ACE inhibitors, ARBs, renin inhibitors, atenolol, nitroprusside, '
          'MRAs</span> &mdash; Class 3: Harm.',
 'why': 'Severe range is &ge;160 systolic or &ge;110 diastolic persisting 15 minutes, and the '
        'goal is explicitly <b>not</b> a normal pressure. <b>Magnesium is seizure prophylaxis, '
        'not an antihypertensive</b> &mdash; ACOG says so in those words, and treating it as one '
        'is the commonest error on this topic. Nifedipine capsules are swallowed, never punctured '
        'or given sublingually. After three failed doses, call for help rather than repeating.',
},
{
 'name': 'Acute coronary syndrome', 'src': 'fix',
 'goal': 'SBP &lt;140 &middot; keep DBP &gt;60',
 'win': 'within 1 h',
 'pref': 'Nitroglycerin, topical or drip. Esmolol or labetalol. Nicardipine or clevidipine.',
 'avoid': '<span class="no">Nitroprusside</span> (coronary steal). Hydralazine. '
          '<span class="no">Nitrates within 24 h of sildenafil or vardenafil, 48 h of tadalafil, '
          '12 h of avanafil</span>, or with RV infarction. Beta blocker if there are heart-failure '
          'signs, HR &lt;60, SBP &lt;100, shock, high-grade block or bronchospasm.',
 'why': 'The DBP floor is physiology rather than a guideline recommendation: the left ventricle is '
        'perfused in diastole and coronary autoregulation fails below a perfusion pressure around '
        '60. COMMIT found early IV metoprolol bought no survival and caused more cardiogenic shock, '
        'which is why the 2025 ACS guideline asks for an <b>oral</b> beta blocker within 24 hours '
        'rather than a drip. '
        '<b>Corrected:</b> the card’s “judicious nitro with RVMI” is stated as '
        '<em>avoid</em> in the 2025 guideline, and the PDE5-inhibitor window is missing from the '
        'card entirely.',
},
{
 'name': 'Acute pulmonary edema', 'sub': 'the SCAPE presentation', 'src': 'fix',
 'goal': 'SBP &lt;140',
 'win': 'within 1 h',
 'pref': '<b>High-dose nitroglycerin plus non-invasive ventilation</b> are the first moves. '
         'Nitroprusside, nicardipine or clevidipine as adjuncts.',
 'avoid': '<span class="no">IV beta blockade while decompensated.</span> Nitroprusside alongside '
          'ACS or renal failure.',
 'why': 'Most of these patients are <b>volume-redistributed, not volume-overloaded</b>, so '
        'diuresis is not the primary move and must not delay vasodilation and positive pressure. '
        'Nitroglycerin here runs far above the 400 mcg/min ceiling used in ordinary heart failure. '
        '<b>Corrected:</b> the card’s “beta blockers not preferred” needs splitting '
        '&mdash; IV beta blockade in decompensation is contraindicated, but a <em>chronic oral</em> '
        'beta blocker should be continued unless the patient is hypotensive or low-output. '
        'Non-invasive ventilation is absent from the card.',
},
{
 'name': 'Intracerebral hemorrhage', 'src': 'fix',
 'goal': 'SBP 150&ndash;220 &rarr; 130 to &lt;140, held &ge;7 days',
 'win': 'start &lt;2 h, at target in 1 h',
 'pref': 'Nicardipine or clevidipine infusion; labetalol. Arterial line where feasible.',
 'avoid': '<span class="no">SBP &lt;130 &mdash; Class 3: Harm.</span> Bolus-and-chase dosing.',
 'why': 'Smoothness counts as much as the number: peaks and swings worsen outcome, and over-rapid '
        'lowering produced the renal harm signal in ATACH-2. Above SBP 220 the evidence thins out, '
        'because those patients were largely excluded from the trials &mdash; titrate, and do not '
        'go below 130. '
        '<b>This is the most out-of-date row on the card.</b> The entry band is 150&ndash;220, not '
        '180&ndash;220; the target is 130 to &lt;140, not 140&ndash;160; the floor is missing; and '
        'the “&gt;220, reduce 25%” rule is not supported by either current guideline.',
},
{
 'name': 'Ischemic stroke', 'src': 'fix',
 'goal': '&lt;185/110 before lysis, then &lt;180/105 &times; 24 h. '
         'No lysis or thrombectomy: treat only at &ge;220/120, then ~15% over 24 h',
 'win': 'otherwise permissive', 'slow': True,
 'pref': 'Labetalol, nicardipine, clevidipine. Nitroprusside is the named fallback for refractory '
         'pressure or DBP &gt;140.',
 'avoid': '<span class="no">SBP &lt;140 in the first 24&ndash;72 h after successful thrombectomy '
          '&mdash; Class 3: Harm, LOE A.</span> Targeting &lt;140 after lysis &mdash; no benefit.',
 'why': '<b>220/120 is a treatment threshold, not a target.</b> Below it, starting or restarting '
        'antihypertensives in the first 48&ndash;72 hours is Class 3: No Benefit; at or above it, '
        'lowering ~15% is only “might be reasonable”. The 2026 guideline added the '
        'post-reperfusion harm rule from ENCHANTED2/MT and OPTIMAL-BP. Treat regardless if a second '
        'condition demands it &mdash; ACS, acute heart failure, dissection, pre-eclampsia. '
        '<b>Corrected:</b> the card reads the threshold as a target and omits the post-lysis '
        '&lt;180/105 window and the post-thrombectomy harm rule.',
},
{
 'name': 'Subarachnoid hemorrhage', 'sub': 'aneurysm not yet secured', 'src': 'add',
 'goal': 'No evidence-based number. SBP &lt;160 is the figure most often used',
 'win': 'stability over speed', 'slow': True,
 'pref': 'Short-acting and titratable: nicardipine or clevidipine infusion, labetalol boluses.',
 'avoid': '<span class="no">Sudden profound drops.</span> Hypotension and variability count as '
          'harm here, not just hypertension.',
 'why': 'The 2023 guideline states outright that the evidence is insufficient to recommend any '
        'specific target, so a number on a card would be invented. Once the aneurysm is secured '
        'the logic <b>inverts</b> toward permissive or induced hypertension for delayed cerebral '
        'ischemia. <b>Nimodipine 60 mg q4h for 21 days is for ischemia, not for pressure</b> '
        '&mdash; it is not part of the antihypertensive regimen, and if it drops the pressure the '
        'move is to split it to 30 mg q2h rather than stop it. '
        'The card lists SAH as an indication for nicardipine and clevidipine but gives it no row.',
},
{
 'name': 'Hypertensive encephalopathy', 'sub': 'and PRES &mdash; the same row', 'src': 'fix',
 'goal': 'MAP down 20&ndash;25%',
 'win': 'over 1&ndash;2 h',
 'pref': 'Nicardipine or clevidipine; labetalol as an adjunct.',
 'avoid': 'Nitroglycerin and nitroprusside where raised ICP is a concern &mdash; both dilate '
          'cerebral vessels.',
 'why': '<b>Expert consensus, not trial evidence</b> &mdash; there is no randomised trial and no '
        'society guideline for PRES, and the 20&ndash;25% figure is the general emergency principle '
        'applied to it. PRES is the imaging correlate of the clinical syndrome, so they share a row; '
        'encephalopathy is a diagnosis of exclusion, and reversal with BP control is what confirms '
        'it. <b>Remove the trigger</b> &mdash; calcineurin inhibitors, VEGF inhibitors, cytotoxic '
        'chemotherapy. In pregnancy this is the eclampsia pathway, not this one.',
},
{
 'name': 'Sympathetic crisis', 'sub': 'pheochromocytoma, stimulants, MAOI, clonidine withdrawal',
 'src': 'add',
 'goal': 'No fixed number &mdash; titrate to symptoms and end-organ signs',
 'pref': '<b>Benzodiazepines first</b> in stimulant toxicity &mdash; they often fix the pressure by '
         'fixing the sympathetic outflow. Phentolamine. Nicardipine or clevidipine.',
 'avoid': '<span class="no">Beta-blocker monotherapy.</span>',
 'why': 'In pheochromocytoma, <b>alpha blockade always precedes beta blockade</b>: a beta blocker '
        'first removes beta-2 vasodilation and leaves alpha-mediated vasoconstriction unopposed. '
        'For clonidine withdrawal the definitive fix is to restart the clonidine. On cocaine, the '
        'classic prohibition is guideline-level but weakly evidenced &mdash; modern meta-analyses '
        'found no excess death or infarction and labetalol has the best safety data, so <b>do not '
        'reflexively stop a chronic beta blocker for a positive screen</b>.',
},
{
 'name': 'Scleroderma renal crisis', 'src': 'add',
 'goal': 'SBP down ~20 mmHg per 24 h, to baseline over ~72 h',
 'win': 'deliberately slow', 'slow': True,
 'pref': '<b>Captopril</b> 6.25&ndash;12.5 mg, increased by 12.5&ndash;25 mg q4&ndash;8h. Calcium '
         'blockers and ARBs are add-ons only, not substitutes.',
 'avoid': '<span class="no">Stopping the ACE inhibitor because the creatinine rose.</span> '
          'Prednisone above 15 mg/day precipitates it.',
 'why': 'The one hypertensive emergency defined by a specific <em>drug</em> rather than a specific '
        'number, because the crisis is renin-driven. Captopril is chosen over the other ACE '
        'inhibitors for its fast on and fast off, which is what lets you escalate every few hours. '
        '<b>Continue it through a rising creatinine and even through dialysis</b> &mdash; renal '
        'recovery can arrive months later. The card names this as captopril’s indication but '
        'gives it no row of its own.',
},
{
 'name': 'AKI with microangiopathy', 'sub': 'malignant hypertension', 'src': 'add',
 'goal': 'Gradual &mdash; SBP around 160 early, then slower',
 'win': 'hours, not minutes', 'slow': True,
 'pref': 'Nicardipine or clevidipine &mdash; no renal adjustment and no thiocyanate to accumulate.',
 'avoid': '<span class="no">Nitroprusside in renal impairment.</span> ACE inhibitors and ARBs '
          'acutely.',
 'why': 'Over-rapid lowering worsens the kidney injury, which is the cleanest lesson of ATACH-2. '
        'Acute renin-angiotensin blockade dilates the efferent arteriole and drops filtration '
        'pressure further, particularly in a volume-depleted patient. The card lists '
        'microangiopathic hemolysis as end-organ damage but gives it no management row.',
},
{
 'name': 'Perioperative', 'src': 'add',
 'goal': 'Avoid hypotension as hard as hypertension &mdash; MAP &ge;60&ndash;65',
 'pref': 'Esmolol, nicardipine, clevidipine. Treat pain, hypoxia, hypercarbia, a full bladder and '
         'shivering before reaching for any of them.',
 'avoid': '<span class="no">Starting a beta blocker on the day of surgery &mdash; Class 3: Harm.</span> '
          '<span class="no">Abruptly stopping a chronic one &mdash; Class 3: Harm.</span>',
 'why': 'The 2024 perioperative guideline is mostly a warning about the other direction: '
        'intraoperative hypotension is what drives myocardial injury. Withholding an ACE inhibitor '
        'or ARB for 24 hours before surgery is reasonable. Consider delaying elective surgery at '
        '&ge;180/110. The card already names peri-operative hypertension as an esmolol indication.',
},
{
 'name': 'Autonomic dysreflexia', 'sub': 'spinal cord injury at or above T6', 'src': 'add',
 'goal': 'Roughly 20&ndash;40 mmHg above <em>their</em> baseline, not an absolute number',
 'win': 'non-drug measures first',
 'pref': '<b>Sit them up, legs down, loosen anything constricting, then find and remove the '
         'stimulus</b> &mdash; nearly always a blocked catheter, a full bladder or an impacted '
         'bowel. Drug only if that fails and SBP &ge;150: nitroglycerin ointment applied above the '
         'level of injury, or bite-and-swallow nifedipine.',
 'avoid': '<span class="no">Nitrates within 24&ndash;48 h of a PDE5 inhibitor</span> &mdash; common '
          'in this population.',
 'why': 'Their usual systolic often sits at 90&ndash;110, so <b>a normal-looking 140 can be a '
        '40-point emergency</b>. Most episodes resolve with positioning and relieving the trigger '
        'and need no antihypertensive at all. The ointment is chosen because it can be wiped off '
        'if the pressure falls too far.',
},
]
