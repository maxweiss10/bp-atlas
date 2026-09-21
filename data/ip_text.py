# -*- coding: utf-8 -*-
"""Prose blocks for the inpatient view.

Cheat-sheet register: fragments, standard abbreviations, no sentence that a
physician could have finished themselves.  Where a figure was corrected the
card's original is kept, because a reader carrying the paper version needs to
know which line moved - but it is stated as `card: X` rather than explained.
"""

LEDE = (
 'The White Book card, every line checked against source. Corrected figures carry the original. '
 'Two guidelines postdate it and rewrite several rows: <b>2025 AHA/ACC HTN</b> and '
 '<b>2026 AHA/ASA stroke</b>.'
)

DEFS = [
 {'k': 'mild', 'title': 'Asx elevated BP',
  'thr': '&ge;130/80 and &lt;180/110&ndash;120 &middot; no acute TOD',
  'body': '<em>Card: &ldquo;&le;180 and DBP &le;110&rdquo;</em> &mdash; no lower bound, and '
          'overlaps the row below.'},
 {'k': 'marked', 'title': 'Severe HTN',
  'old': 'was &ldquo;HTN urgency&rdquo;',
  'thr': '&gt;180/120 &middot; no acute TOD',
  'body': '2025 AHA/ACC term. The 2024 AHA statement says <b>asx markedly elevated BP</b>, '
          '&gt;180/110&ndash;120. Both current.'},
 {'k': 'crisis', 'title': 'HTN emergency',
  'thr': '&gt;180/120 <em>with</em> acute TOD',
  'body': 'TOD makes the dx, not the number. The only one of the three that earns IV.'},
]

EOD = [
 {'sys': 'Brain', 'items': [
   {'t': 'HTN encephalopathy / PRES'}, {'t': 'ICH'}, {'t': 'SAH'}, {'t': 'acute ischemic stroke'}]},
 {'sys': 'Eye', 'items': [
   {'t': 'KWB III&ndash;IV'}, {'t': 'hemorrhage'}, {'t': 'exudates', 'add': True},
   {'t': 'papilledema'}]},
 {'sys': 'Heart / lung', 'items': [
   {'t': 'ACS'}, {'t': 'acute HF', 'add': True}, {'t': 'pulmonary edema'},
   {'t': 'aortic dissection'}]},
 {'sys': 'Kidney', 'items': [{'t': 'AKI'}, {'t': 'TMA', 'add': True}]},
 {'sys': 'Heme', 'items': [{'t': 'MAHA'}, {'t': '+ thrombocytopenia', 'add': True}]},
 {'sys': 'Pregnancy', 'items': [
   {'t': 'pre-eclampsia w/ severe features', 'add': True}, {'t': 'HELLP', 'add': True},
   {'t': 'eclampsia', 'add': True}]},
 {'sys': 'Sympathetic', 'items': [
   {'t': 'catecholamine crisis: pheo, stimulants, clonidine withdrawal', 'add': True}]},
]

EOD_NOTE = (
 '<sup class="addmark">+</sup> on the 2024 AHA list, not the card. Card lists <b>TIA</b> and '
 '<b>hematuria</b>; neither is in any source list (completed stroke and AKI are). Thresholds are '
 'not a wall &mdash; TOD occurs below 180/110&ndash;120.'
)

ASSESS = (
 '<b>1 MAR.</b> Home meds not restarted is the commonest cause; 41% of pts on PRN antihypertensives '
 'were not getting their own. &nbsp; '
 '<b>2 Cuff.</b> Too small reads high: regular cuff on an XL arm <b>+19.5 SBP</b>; one size small '
 '+9.6; arm unsupported +6.5. Too large reads low. &nbsp; '
 '<b>3 Cause.</b> Pain &middot; retention &middot; nausea &middot; hypoxia/hypercapnia &middot; '
 'withdrawal (EtOH, benzo, clonidine, BB) &middot; steroids &middot; NSAIDs &middot; '
 'sympathomimetics &middot; CNI &middot; VEGFi &middot; OSA &middot; NPO. &nbsp; '
 '<b>4 Wait.</b> Recheck after 30 min rest &mdash; <b>44% resolve untreated within 3 h</b>.'
)

TRIAGE = {
 'cols': [
   {'title': 'Severe HTN', 'sub': 'no acute TOD'},
   {'title': 'HTN emergency', 'sub': 'TOD present'},
 ],
 'rows': [
  {'label': 'Where',
   'a': 'Floor or outpatient w/ close f/u. An asx severe reading is <b>not</b> an ED referral.',
   'b': '<b>ICU</b> &mdash; Class 1 for continuous monitoring. '
        '<em>Card offers floor vs ICU as equals.</em>'},
  {'label': 'How fast',
   'a': 'Days to weeks, via the long-acting regimen. '
        '<em>Card&rsquo;s 25&ndash;30% over hrs&ndash;days: no source.</em>',
   'b': '&le;25% in 1st h &rarr; <b>&lt;160/100</b> by 2&ndash;6 h &rarr; <b>130&ndash;140</b> over '
        '24&ndash;48 h. <em>Card&rsquo;s &ldquo;no lower than 160/100&rdquo; inverts it; endpoint is '
        '130&ndash;140, not &ldquo;normal&rdquo;. Its MAP 10&ndash;20% / 5&ndash;15% line is in no '
        'guideline.</em>'},
  {'label': 'Route',
   'a': 'PO, long-acting. Not IV, not immediate-acting PO.',
   'b': 'Short-acting titratable IV &rarr; PO before floor or discharge.'},
  {'label': 'Give',
   'a': '<b>Nothing for the number alone.</b> 2025: intermittent IV <em>or PO</em> to acutely lower '
        'an asx BP = <b>Class 3 Harm</b>. Reasonable: restart or adjust the <b>long-acting</b> '
        'regimen. <em>Card suggests captopril/labetalol; the JHM paper it cites says no '
        'immediate-acting PO and names captopril&rsquo;s class among those implicated.</em>',
   'b': 'Match the drip to the organ. Labetalol + nicardipine cover most; clevidipine if volume '
        'matters; esmolol if rate matters.'},
  {'label': 'Evidence',
   'a': '<b>Zero RCTs.</b> Treated vs matched untreated: AKI <b>10.3 vs 7.9%</b>, MI 1.2 vs 0.6%. '
        'In-hospital intensification: composite <b>8.7 vs 6.9%</b>, IV worst (OR 1.90). Discharge '
        'intensification: 30-d readmit <b>NNH 27</b>, no BP difference at 1 yr.',
   'b': 'Overcorrection is the harm: <b>57%</b> given nicardipine or nitroprusside dropped MAP '
        '&gt;25% within 30 min.'},
 ],
}

DZ_NOTES = [
 {'warn': True,
  't': '<b>Default is &le;25% in the first hour. This table is the exceptions.</b> Two want it down '
       'in 20 min, three in 1 h, three want it left alone. '
       '<b>All 6 card rows changed; 7 conditions added.</b>'},
]

NOTES = [
 {'t': '<b>Control</b> is the column the card implies but never states, and it decides pump vs '
       'syringe. <span class="ctrlb t3">minutes</span> overshoot comes back at the pump &middot; '
       '<span class="ctrlb t2">tens of min</span> titratable, not reversible &middot; '
       '<span class="ctrlb t1">hours</span> the dose is a commitment &middot; '
       '<span class="ctrlb t0">unpredictable</span> depth and timing unknowable &mdash; the case '
       'against hydralazine and enalaprilat.'},
 {'t': '<b>Not approved IV for HTN:</b> metoprolol (MI only), diltiazem (AF/flutter, PSVT), '
       'furosemide (edema; its label reserves HTN for PO). Nitroglycerin ointment is approved for '
       'angina only. Push IV metoprolol for 190/110 and the label&rsquo;s own data say the 110 does '
       'not move.'},
 {'warn': True,
  't': '<b>PRN antihypertensives.</b> 93% of PRN doses are IV. 2&times; risk of a &gt;25% SBP drop '
       'within 1 h, 24% more AKI, dose-response to &ge;4 doses. <b>84.5% of IV doses were given for '
       'SBP &lt;180.</b> 2024 AHA advises against the orders outright.'},
 {'t': '<b>Workup is small and mostly symptom-directed.</b> Routine: BMP, CBC, CXR, ECG, volume '
       'status, pulses, <b>fundi</b>. Not routine: troponin, UA, smear, head CT. A 5-symptom screen '
       '(CP, dyspnea, HA, visual, neuro) has <b>NPV ~99%</b>. Head CT is <em>insensitive</em> for '
       'HTN encephalopathy.'},
 {'t': '<b>Off the drip.</b> Nicardipine loses half its effect in ~30 min; no PO agent peaks that '
       'fast. Start PO <em>while the drip runs</em>, then wean in steps. Longer overlap &rarr; less '
       'SBP variability. A UCSF weaning protocol cut mean infusion 118 h &rarr; 30 h.'},
 {'warn': True,
  't': '<b>Two situations where lowering BP is the harm.</b> <b>Cushing reflex</b> (HTN + '
       'bradycardia + irregular resps) &mdash; treat the ICP. <b>Autonomic dysreflexia</b> (SCI '
       '&ge;T6) &mdash; sit up, find the stimulus. Neither is on the card.'},
 {'t': '<b>Cost</b> is duration, not agent. Clevidipine ~$199/vial vs ~$25 for a nicardipine bag '
       '(682% more, same time to goal). Nitroprusside went $27 &rarr; $881 per 50 mg, 2012&ndash;15; '
       'use fell 53%. <b>Fenoldopam</b> is still in the guideline tables but left the US market in '
       '2023, so it has no row here.'},
]
