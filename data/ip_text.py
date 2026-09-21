# -*- coding: utf-8 -*-
"""Prose blocks for the inpatient view.

Cheat-sheet register: fragments, standard abbreviations, no sentence that a
physician could have finished themselves.  Where a figure was corrected the
card's original is kept, because a reader carrying the paper version needs to
know which line moved - but it is stated as `card: X` rather than explained.
"""

LEDE = (
 '<b>White Book card, checked line by line.</b> Corrected figures keep the original. 2 guidelines postdate it + rewrite several rows: <b>2025 AHA/ACC HTN</b>, <b>2026 AHA/ASA stroke</b>. Drug names link to the agent table.'
)

DEFS = [
 {'k': 'mild', 'title': 'Asx elevated BP',
  'thr': '&ge;130/80 and &lt;180/110&ndash;120 &middot; no acute TOD',
  'body': '<em>Card: &ldquo;&le;180 <b>and</b> DBP &le;110&rdquo;</em> &mdash; no lower bound, overlaps the row below.'},
 {'k': 'marked', 'title': 'Severe HTN',
  'old': 'was &ldquo;HTN urgency&rdquo;',
  'thr': '&gt;180/120 &middot; no acute TOD',
  'body': '2025 AHA/ACC term. 2024 statement: <b>asx markedly elevated BP</b>, &gt;180/110&ndash;120. Both current.'},
 {'k': 'crisis', 'title': 'HTN emergency',
  'thr': '&gt;180/120 <em>with</em> acute TOD',
  'body': 'The only one of the three that earns IV.'},
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
 '<sup class="addmark">+</sup> on the 2024 AHA list, not the card. Card lists <b>TIA</b> + <b>hematuria</b>; neither is in any source list. TOD occurs below 180/110&ndash;120 &mdash; the threshold is not a wall.'
)

ASSESS = (
 '<b>1 MAR.</b> Home meds not restarted = commonest cause; 41% of PRN pts were not on theirs. &nbsp; '
 '<b>2 Cuff.</b> Too small reads high: regular cuff on XL arm <b>+19.5 SBP</b>; arm unsupported +6.5. &nbsp; '
 '<b>3 Cause.</b> Pain &middot; retention &middot; nausea &middot; hypoxia &middot; withdrawal (EtOH, benzo, clonidine, BB) &middot; steroids &middot; NSAIDs &middot; sympathomimetics &middot; CNI &middot; VEGFi &middot; OSA &middot; NPO. &nbsp; '
 '<b>4 Wait.</b> Recheck after 30 min rest.'
)


DZ_NOTES = [
 {'warn': True,
  't': 'Two want it down in 20 min, three in 1h, three want it left alone.'},
]

NOTES = [
 {'t': '<b>Control</b> decides pump vs syringe. '
       '<span class="ctrlb t3">minutes</span> overshoot comes back at the pump &middot; '
       '<span class="ctrlb t2">tens of min</span> titratable, not reversible &middot; '
       '<span class="ctrlb t1">hours</span> the dose is a commitment &middot; '
       '<span class="ctrlb t0">unpredictable</span> &mdash; hydralazine, enalaprilat.'},
 {'warn': True,
  't': '<b>PRN antihypertensives.</b> 93% of PRN doses are IV. 2&times; risk of &gt;25% SBP drop '
       '&lt;1h, 24% more AKI. <b>84.5% of IV doses went to SBP &lt;180.</b> 2024 AHA advises '
       'against the orders outright.'},
 {'t': '<b>Not approved IV for HTN:</b> metoprolol (MI only), diltiazem (AF, PSVT), furosemide '
       '(edema). NTG ointment = angina only. Push IV metoprolol for 190/110 and the label&rsquo;s '
       'own data say the 110 does not move.'},
 {'t': '<b>Workup is small + sx-directed.</b> Routine: BMP, CBC, CXR, ECG, volume status, pulses, '
       '<b>fundi</b>. Not routine: trop, UA, smear, head CT. 5-sx screen (CP, dyspnea, HA, visual, '
       'neuro) <b>NPV ~99%</b>. Head CT is <em>insensitive</em> for HTN encephalopathy.'},
 {'warn': True,
  't': '<b>Off the gtt:</b> start PO <em>while it runs</em>, then wean. Nicardipine loses &frac12; '
       'its effect in 30 min and no PO agent peaks that fast. &nbsp; '
       '<b>ACEi/ARB the AM of surgery is unsettled</b> &mdash; 2024 ACC/AHA says hold 24h, the '
       '2026 anaesthetists say take it. Ask.'},
]
