# -*- coding: utf-8 -*-
"""Prose blocks for the inpatient view: definitions, the triage comparison, and
the notes under each table.

The card this reproduces is a UCSF/MGH-style Cardiology reference card.  Where a
figure on it was checked against the primary source and moved, the move is
stated in the text rather than quietly applied, because a reader carrying the
paper card needs to know which line changed.
"""

LEDE = (
 'The card this reproduces is the fastest way to triage a pressure of 212/118 at two in the '
 'morning, and most of it holds up. What follows is that card, checked line by line against '
 'the primary sources, with the figures that moved marked and the originals kept. Two documents '
 'published after it change several answers: the <b>2025 AHA/ACC hypertension guideline</b>, which '
 'retired the 2017 one in August 2025, and the <b>2026 AHA/ASA acute ischemic stroke guideline</b> '
 'from February 2026. Where they disagree with the card, the card is out of date rather than wrong '
 '&mdash; it was right when it was printed.'
)

DEFS = [
 {'k': 'mild', 'title': 'Asymptomatic elevated BP',
  'thr': '&ge;130/80 and &lt;180/110&ndash;120 &middot; no acute organ damage',
  'body': 'The ordinary inpatient elevated pressure. <b>Corrected:</b> the card gives this as '
          '&ldquo;SBP&nbsp;&le;180 <em>and</em> DBP&nbsp;&le;110&rdquo;, which has no lower bound '
          'and overlaps the row below it &mdash; a diastolic of 115 satisfies both definitions at '
          'once.'},
 {'k': 'marked', 'title': 'Severe hypertension',
  'old': 'was &ldquo;hypertensive urgency&rdquo;',
  'thr': '&gt;180/120 &middot; no acute organ damage',
  'body': 'The 2025 guideline’s term. The 2024 AHA acute-care statement calls the same thing '
          '<b>asymptomatic markedly elevated BP</b> and uses &gt;180/110&ndash;120. Both are '
          'current; the card’s &ldquo;formerly hypertensive urgency&rdquo; is right, and there '
          'are now two replacement names rather than one.'},
 {'k': 'crisis', 'title': 'Hypertensive emergency',
  'thr': '&gt;180/120 <em>with</em> acute target-organ damage',
  'body': 'The organ damage makes the diagnosis, not the number. This is the only one of the three '
          'that earns an intravenous drug.'},
]

EOD = [
 {'sys': 'Brain', 'items': [
   {'t': 'hypertensive encephalopathy and PRES'}, {'t': 'intracerebral hemorrhage'},
   {'t': 'subarachnoid hemorrhage'}, {'t': 'acute ischemic stroke'}]},
 {'sys': 'Eye', 'items': [
   {'t': 'grade III&ndash;IV retinopathy'}, {'t': 'hemorrhages'},
   {'t': 'exudates', 'add': True}, {'t': 'papilledema'}]},
 {'sys': 'Heart and lungs', 'items': [
   {'t': 'acute coronary syndrome'}, {'t': 'acute heart failure', 'add': True},
   {'t': 'pulmonary edema'}, {'t': 'aortic dissection'}]},
 {'sys': 'Kidney', 'items': [
   {'t': 'acute kidney injury'}, {'t': 'thrombotic microangiopathy', 'add': True}]},
 {'sys': 'Blood', 'items': [
   {'t': 'microangiopathic hemolysis'}, {'t': 'with thrombocytopenia', 'add': True}]},
 {'sys': 'Pregnancy', 'items': [
   {'t': 'pre-eclampsia with severe features', 'add': True}, {'t': 'HELLP', 'add': True},
   {'t': 'eclampsia', 'add': True}]},
 {'sys': 'Sympathetic', 'items': [
   {'t': 'catecholamine crisis &mdash; pheochromocytoma, stimulants, clonidine withdrawal',
    'add': True}]},
]

EOD_NOTE = (
 'Items in <span class="add" style="color:var(--accent-ink)">green</span> are on the 2024 AHA '
 'statement’s list but not the card’s. Two items on the card appear in none of the '
 'source lists: <b>TIA</b>, which is not acute organ damage the way a completed stroke is, and '
 '<b>hematuria</b>, which is a useful clue to glomerulonephritis or microangiopathy but is not a '
 'criterion &mdash; acute kidney injury is. And the thresholds are not a wall: the 2024 statement '
 'says organ damage can appear below 180/110&ndash;120, so a patient with the findings and a lower '
 'pressure still has an emergency.'
)

ASSESS = (
 '<b>Open the medication list first.</b> The commonest cause of a markedly elevated inpatient '
 'pressure is the home regimen nobody restarted &mdash; 41% of patients ordered as-needed '
 'antihypertensives were not receiving their own. Then the <b>measurement</b>: cuff size, arm '
 'supported at heart level, back and feet supported, no talking, no full bladder. Then the '
 '<b>reversible cause</b> &mdash; pain, anxiety, urinary retention, nausea, hypoxia or hypercapnia, '
 'alcohol, benzodiazepine, clonidine or beta-blocker withdrawal, steroids, NSAIDs, '
 'sympathomimetics, decongestants, calcineurin inhibitors, VEGF inhibitors, obstructive sleep '
 'apnea, and simply being NPO. Then <b>rest the patient half an hour and measure again</b>. '
 'In a 12,825-patient cohort, <b>44% of severe inpatient readings came down on their own within '
 'three hours</b> with no treatment at all, and treated patients were no more likely than '
 'untreated ones to fall 20 mmHg by the next check.'
)

TRIAGE = {
 'cols': [
   {'title': 'Severe hypertension', 'sub': 'no acute organ damage'},
   {'title': 'Hypertensive emergency', 'sub': 'organ damage present'},
 ],
 'rows': [
  {'label': 'Where',
   'a': 'Floor, or outpatient management with close follow-up. The 2025 guideline is explicit that '
        'an asymptomatic severe reading is <b>not</b> a reason to send someone to the emergency '
        'department.',
   'b': '<b>ICU.</b> <em>Corrected:</em> the card offers &ldquo;floor vs ICU&rdquo; as equals. '
        'ICU admission for continuous monitoring is now a <b>Class 1</b> recommendation, so the '
        'floor is the exception, not the alternative.'},
  {'label': 'How fast',
   'a': 'Days to weeks, through the long-acting regimen, with outpatient follow-up. '
        '<em>Corrected:</em> the card’s &ldquo;no more than 25&ndash;30% over hours to '
        'days&rdquo; has no source behind it.',
   'b': 'No more than <b>25%</b> in the first hour, then to <b>&lt;160/100</b> over the next '
        '2&ndash;6 hours, then cautiously to <b>130&ndash;140</b> over 24&ndash;48 hours. '
        '<em>Two corrections:</em> the card’s &ldquo;no lower than 160/100&rdquo; reverses '
        'the guideline, which makes 160/100 the target you descend to rather than a floor you stay '
        'above; and the 24&ndash;48 hour endpoint is 130&ndash;140, not &ldquo;normal&rdquo;, since '
        '2025. The card’s other line &mdash; MAP down 10&ndash;20% in the first hour, then '
        '5&ndash;15% &mdash; is a textbook convention and appears in no guideline.'},
  {'label': 'Route',
   'a': 'Oral, long-acting. Not intravenous, and not immediate-acting oral either.',
   'b': 'Short-acting titratable intravenous agents, then convert to oral before the floor or '
        'discharge.'},
  {'label': 'What to give',
   'a': '<b>Nothing, for the number alone.</b> <em>This is where the card has been overtaken.</em> '
        'It suggests captopril or labetalol; the 2025 guideline makes intermittent intravenous '
        '<em>or oral</em> dosing to acutely lower an asymptomatic pressure a <b>Class 3: '
        'Harm</b> recommendation, and the hospital-medicine paper the card itself cites says not to '
        'give immediate-acting oral agents and names captopril’s class among those implicated '
        'in harm. What is reasonable is restarting or adjusting the <b>long-acting</b> regimen in '
        'someone with a genuine history of uncontrolled hypertension.',
   'b': 'Match the drip to the organ. Labetalol and nicardipine cover most of it; clevidipine when '
        'volume matters; esmolol when the heart rate matters. Hydralazine remains a poor choice '
        'here for the same reason it always was.'},
  {'label': 'What the evidence shows',
   'a': 'There is still <b>not one randomised trial</b> of treating asymptomatic elevated inpatient '
        'blood pressure. Every number below is observational. Treated patients had more acute '
        'kidney injury (10.3% vs 7.9%) and more myocardial injury (1.2% vs 0.6%) than matched '
        'untreated ones, and there was no blood-pressure band in which treatment looked better. '
        'Intensifying in hospital raised a composite of death, ICU transfer, stroke and kidney '
        'injury to 8.7% from 6.9%, worst with intravenous agents. Intensifying at discharge raised '
        '30-day readmission with a number needed to harm of 27, and bought no blood-pressure '
        'difference at one year.',
   'b': 'The evidence here is about <em>how</em>, not whether. Overcorrection is the recurring '
        'harm: 57% of patients given nicardipine or nitroprusside for an emergency dropped their '
        'mean pressure more than 25% within the first thirty minutes.'},
 ],
}

DZ_NOTES = [
 {'t': '<b>Every one of the card’s six condition rows needed something changed, and seven '
       'more conditions were missing.</b> That is less an indictment of the card than of how fast '
       'this particular corner moves: the intracerebral hemorrhage target, the aortic dissection '
       'heart rate, and the whole of the ischemic stroke row were all rewritten by guidelines '
       'published after it went to print.'},
 {'t': '<b>The default is slow; this table is the list of exceptions.</b> Everywhere else, '
       'no more than a quarter off in the first hour. Here, three conditions want the pressure '
       'down inside an hour, two want it down inside twenty minutes, and three want you to leave '
       'it almost entirely alone. Reading the row is how you find out which kind you have.',
  'warn': True},
]

NOTES = [
 {'t': '<b>The Control column is the one the card implies but never states.</b> Everything else '
       'here can be looked up; this is the property that decides whether an agent belongs on a '
       'pump or in a syringe. <span class="ctrlb t3">minutes</span> means an overshoot comes back '
       'at the pump. <span class="ctrlb t2">tens of min</span> means titratable but not instantly '
       'reversible. <span class="ctrlb t1">hours</span> means the dose you just gave is a '
       'commitment. <span class="ctrlb t0">unpredictable</span> means you cannot know in advance '
       'how far it will go or when &mdash; which is the entire case against hydralazine and '
       'enalaprilat for titration.'},
 {'t': '<b>Three of the agents interns reach for on the floor are not approved intravenously for '
       'hypertension at all.</b> Metoprolol\u2019s intravenous label covers acute myocardial '
       'infarction; diltiazem\u2019s covers rate control in atrial fibrillation and conversion of '
       'supraventricular tachycardia; furosemide\u2019s covers edema, and its own label reserves '
       'the hypertension indication for the <em>oral</em> form. Nitroglycerin ointment is approved '
       'only for preventing angina. That is not an argument against ever using them. It is an '
       'argument for knowing that when you push intravenous metoprolol for a pressure of 190/110, '
       'you are using a rate drug, off-label, on a patient whose problem is vasoconstriction '
       '&mdash; and the label\u2019s own data show the diastolic does not move.'},
 {'warn': True,
  't': '<b>The as-needed antihypertensive order is the single most consequential habit on this '
       'page.</b> In the largest series, 93% of as-needed doses were intravenous; they carried a '
       'doubled risk of a greater-than-25% systolic drop within the hour, a quarter more acute '
       'kidney injury, and a dose-response relationship out to four or more doses. In another, '
       '<b>84.5% of intravenous doses were given for a systolic below 180</b>, and a third of '
       'patients dropped more than a quarter of their pressure within six hours. The 2024 AHA '
       'statement advises against the orders outright, and describes the loop they create: a '
       'night-time as-needed dose, a morning scheduled dose held for the resulting low pressure, '
       'a higher evening pressure, another as-needed dose.'},
 {'t': '<b>The workup is smaller than you expect, and most of it is directed rather than routine.</b> '
       'The 2024 AHA statement asks for a basic metabolic panel, a complete blood count, a chest '
       'radiograph, a 12-lead electrocardiogram, an assessment of volume status, and an examination '
       'that includes bilateral pulses and the <b>fundi</b>. Troponin, urinalysis, a blood smear and '
       'a head CT are not on that list &mdash; they are ordered when a symptom points at them. A '
       'five-symptom screen (chest pain, breathlessness, headache, visual change, other neurologic '
       'change) has a negative predictive value of about 99% for acute organ damage. One trap: a '
       'head CT is <b>insensitive</b> for hypertensive encephalopathy and cannot be used to rule it '
       'out.'},
 {'t': '<b>Measurement error is larger than most of the drugs on this page.</b> A regular cuff on an '
       'extra-large arm reads <b>19.5 mmHg too high</b>; one size too small reads 9.6 too high. An '
       'arm left unsupported at the side adds 6.5 systolic, a hand resting in the lap adds 3.9. The '
       'direction is worth memorising: <b>too small reads high, too large reads low</b>. Roughly a '
       'third of inpatient cuffs are the wrong size. The trap runs the other way in the unit: above '
       '180/100 an oscillometric cuff can <em>under</em>read an arterial line by as much as 50/30, '
       'which is one of the reasons a true emergency gets a line.'},
 {'t': '<b>Coming off the drip is where the pressure runs away.</b> Nicardipine loses half its '
       'effect in about thirty minutes, and no oral agent reaches peak effect that fast. So start '
       'the oral agent <em>while the infusion is still running</em>, then wean the infusion in '
       'steps rather than stopping it; longer overlap produces lower systolic variability. This is '
       'also where the money is. A UCSF weaning protocol cut mean nicardipine infusion time from '
       '118 hours to 30 and saved about $18,000 per patient &mdash; and drifted back to 96 hours '
       'once the protocol stopped being enforced.'},
 {'t': '<b>Cost is real here, and it is about duration rather than choice of agent.</b> Clevidipine '
       'runs roughly $199 a vial against about $25 for a bag of nicardipine, a 682% difference for '
       'the same time to goal, which is why formularies restrict it. Nitroprusside is the cautionary '
       'tale: its list price went from $27.46 to $880.88 per 50 mg between 2012 and 2015, and use '
       'across 47 hospitals fell 53%. But a drip that runs four days instead of one costs more than '
       'any of these choices.'},
 {'warn': True,
  't': '<b>Two situations where the high pressure is the compensation and lowering it causes the '
       'harm.</b> The <b>Cushing reflex</b> &mdash; hypertension with bradycardia and irregular '
       'breathing &mdash; is raised intracranial pressure maintaining cerebral perfusion; the '
       'treatment is directed at the pressure inside the skull, not the one in the arm. And in '
       '<b>autonomic dysreflexia</b> after spinal cord injury at or above T6, the fix is to sit the '
       'patient up and find the noxious stimulus. Neither appears on the card.'},
 {'t': '<b>Fenoldopam is in the guideline tables and not in the pharmacy.</b> It still appears in '
       'the 2017 and 2025 hypertensive-emergency drug tables, but it was discontinued in the United '
       'States in 2023 and returns no current labels, and its renal-protection claim failed on hard '
       'outcomes. It has no row here for that reason. Neither does intravenous clonidine or '
       'urapidil, which have never been marketed in the United States.'},
]
