"""Onset and offset layer: how fast each drug turns on and off.

Three separate questions the mmHg column cannot answer:

  on    how long after a single dose before blood pressure starts to move
  pk    when that single dose has its largest effect (the peak/trough problem)
  full  how long a fixed dose needs before the effect plateaus - the interval
        to wait before judging the dose or titrating
  off   how long the effect persists once the drug is stopped or missed

The efficacy model this page is built on reports plateau effects (mean trial
follow-up 8.6 weeks), so every mmHg figure in the table is a `full` figure.
This layer says how long you wait to get there.

Provenance per field:
  L  stated in this drug's own FDA prescribing information
  K  derived from this drug's labelled pharmacokinetics (effective half-life,
     Tmax, time to steady state) - no published BP time-course
  C  class-typical, carried from the labelled members of the same class -
     either the agent has no US label at all, or its label is silent on this
     particular field

`off` is only rarely measured. Where a label reports an actual withdrawal
study it is marked L and quoted; otherwise it is K - roughly four to five
effective half-lives, which is when the drug is gone, not when the blood
pressure has finished drifting back. Treat K offsets as the earliest the
effect fades, not the latest.

`taper` marks the agents that must not be stopped abruptly.
"""

# hours; used for sorting and for nothing else
H, D, W = 1, 24, 168


def _(t, h, s):
    return {'t': t, 'h': h, 's': s}


# ------------------------------------------------------------------ classes
# Carried to the non-US agents only, and always marked C in the output.
CLASS_KIN = {
    'ACEi':    dict(on=_('~1 h', 1, 'C'), pk=_('2-6 h', 4, 'C'), full=_('1-2 wk', 2 * W, 'C'),
                    off=_('~2-3 d', 60, 'C'), hl='effective half-life 10-13 h'),
    'ARB':     dict(on=_('~2 h', 2, 'C'), pk=_('3-6 h', 5, 'C'), full=_('2-4 wk', 4 * W, 'C'),
                    off=_('~2-4 d', 72, 'C'), hl='half-life 6-15 h'),
    'BB':      dict(on=_('2-4 h', 3, 'C'), pk=_('2-4 h', 3, 'C'), full=_('1-2 wk', 2 * W, 'C'),
                    off=_('~2-3 d', 60, 'C'), hl='half-life 6-12 h', taper=True),
    'DHP':     dict(on=_('2-5 h', 3, 'C'), pk=_('2-8 h', 5, 'C'), full=_('1-2 wk', 2 * W, 'C'),
                    off=_('~2-3 d', 60, 'C'), hl='half-life 8-16 h'),
    'thiazide': dict(on=_('~2 h', 2, 'C'), pk=_('~4 h', 4, 'C'), full=_('2-4 wk', 4 * W, 'C'),
                     off=_('~2-3 d', 60, 'C'), hl='half-life 6-15 h'),
}

# ------------------------------------------------------------------ per drug
KIN = {
# ---------------------------------------------------------------- ACE inhibitors
'benazepril': dict(
    on=_('<1 h', 1, 'L'), pk=_('2-4 h', 3, 'L'), full=_('1-2 wk', 2 * W, 'C'),
    off=_('~2 d', 48, 'K'), hl='effective half-life 10-11 h; steady state after 2-3 doses',
    q=['Label: lowered blood pressure within 1 hour, with peak reductions achieved between 2 and 4 hours after dosing; the effect of a single dose persisted for 24 hours.']),
'captopril': dict(
    on=_('15-30 min', 0.4, 'K'), pk=_('1-1.5 h', 1.2, 'L'), full=_('several wk', 3 * W, 'L'),
    off=_('~1 d', 24, 'K'), hl='half-life under 2 h - the shortest-acting agent here', reb='ok',
    q=['Label: reductions of blood pressure are usually maximal 60 to 90 minutes after an individual dose.',
       'Label: the reduction in blood pressure may be progressive, so to achieve maximal therapeutic effects, several weeks of therapy may be required.',
       'Label: abrupt withdrawal has not been associated with a rapid increase in blood pressure.']),
'enalapril': dict(
    on=_('1 h', 1, 'L'), pk=_('4-6 h', 5, 'L'), full=_('1-2 wk', 2 * W, 'C'),
    off=_('~2-3 d', 60, 'K'), hl='effective half-life 11-14 h', reb='ok',
    q=['Label: onset of antihypertensive activity was seen at one hour with peak reduction of blood pressure achieved by four to six hours.',
       'Label: in some patients achievement of optimal blood pressure reduction may require several weeks of therapy.',
       'Label: abrupt withdrawal has not been associated with a rapid increase in blood pressure.']),
'fosinopril': dict(
    on=_('<1 h', 1, 'L'), pk=_('2-6 h', 4, 'L'), full=_('several wk', 3 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life ~12 h', reb='ok',
    q=['Label: lowered blood pressure within 1 hour, with peak reductions achieved 2 to 6 hours after dosing.',
       'Label: in most trials the antihypertensive effect increased during the first several weeks of repeated measurements.',
       'Label: abrupt withdrawal has not resulted in a rapid increase in blood pressure.']),
'lisinopril': dict(
    on=_('1 h', 1, 'L'), pk=_('6 h', 6, 'L'), full=_('1-2 wk', 2 * W, 'C'),
    off=_('~2-3 d', 60, 'K'), hl='effective half-life 12 h', reb='ok',
    q=['Label: onset of antihypertensive activity was seen at one hour, with peak reduction of blood pressure achieved by 6 hours.',
       'Label: the effect at 24 hours was substantially smaller than the effect six hours after dosing.',
       'Label: abrupt withdrawal has not been associated with a rapid increase in blood pressure.']),
'moexipril': dict(
    on=_('~1 h', 1, 'L'), pk=_('3-6 h', 4.5, 'L'), full=_('4 wk', 4 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='half-life 2-9 h',
    q=['Label: antihypertensive effects were first detectable about 1 hour after dosing, with a peak effect between 3 and 6 hours.',
       'Label: during chronic therapy the antihypertensive effect is generally evident within 2 weeks of treatment, with maximal reduction after 4 weeks.']),
'perindopril': dict(
    on=_('~1 h', 1, 'C'), pk=_('~4 h', 4, 'L'), full=_('several wk', 3 * W, 'L'),
    off=_('~3-6 d', 108, 'K'), hl='perindoprilat accumulates to steady state over 3-6 days; terminal half-life 30-120 h from slow ACE dissociation',
    q=['Label: the effect of perindopril occurred promptly, with effects increasing slightly over several weeks.',
       'Label: perindoprilat attains steady state plasma levels in 3 to 6 days.']),
'quinapril': dict(
    on=_('<1 h', 1, 'L'), pk=_('2-4 h', 3, 'L'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='effective accumulation half-life ~3 h, terminal 25 h',
    q=['Label: antihypertensive activity commences within 1 hour with peak effects usually achieved by 2 to 4 hours after dosing.',
       'Label: during chronic therapy, most of the blood pressure lowering effect of a given dose is obtained in 1 to 2 weeks.',
       'Label: the trough effect represents about 50% of the peak effect.']),
'ramipril': dict(
    on=_('1-2 h', 1.5, 'L'), pk=_('3-6 h', 4.5, 'L'), full=_('2-4 wk', 4 * W, 'L'),
    off=_('~3 d', 72, 'K'), hl='half-life 13-17 h in the therapeutic range', reb='ok',
    q=['Label: lowered blood pressure within 1 to 2 hours, with peak reductions achieved 3 to 6 hours after dosing.',
       'Label: adjust dosage according to blood pressure response after 2 to 4 weeks of treatment.',
       'Label: abrupt withdrawal has not resulted in a rapid increase in blood pressure.']),
'trandolapril': dict(
    on=_('~1 h', 1, 'C'), pk=_('4-10 h', 6, 'L'), full=_('1 wk', W, 'L'),
    off=_('~4-8 d', 144, 'K'), hl='effective half-life 22.5 h', reb='ok',
    q=['Label: during chronic therapy, the maximum reduction in blood pressure with any dose is achieved within one week.',
       'Label: a single 2 mg dose produces 70 to 85% inhibition of plasma ACE at 4 hours, with about half the effect still manifest at 8 days.',
       'Label: abrupt withdrawal has not been associated with a rapid increase in blood pressure.']),
# ---------------------------------------------------------------- ARBs
'azilsartan': dict(
    on=_('~2 h', 2, 'C'), pk=_('~3 h', 3, 'K'), full=_('2 wk', 2 * W, 'L'),
    off=_('~2 d', 48, 'K'), hl='half-life ~11 h; steady state within 5 days', reb='ok',
    q=['Label: most of the antihypertensive effect occurs within the first two weeks of dosing.',
       'Label: no rebound effect was observed following abrupt cessation.']),
'candesartan': dict(
    on=_('~2 h', 2, 'C'), pk=_('3-4 h', 3.5, 'K'), full=_('4-6 wk', 5 * W, 'L'),
    off=_('~2 d', 48, 'K'), hl='half-life ~9 h', reb='ok',
    q=['Label: most of the antihypertensive effect is present within 2 weeks, and maximal blood pressure reduction is generally obtained within 4 to 6 weeks.',
       'Label: in studies of up to 1 year there was no rebound after abrupt withdrawal.']),
'irbesartan': dict(
    on=_('1st dose', 2, 'L'), pk=_('3-6 h', 4.5, 'L'), full=_('2 wk', 2 * W, 'L'),
    off=_('>1 wk', 8 * D, 'L'), hl='half-life 11-15 h; steady state within 3 days', reb='ok',
    q=['Label: the effect is apparent after the first dose, and it is close to its full observed effect at 2 weeks.',
       'Label: at the end of an 8-week exposure, about 2/3 of the antihypertensive effect was still present one week after the last dose. Rebound hypertension was not observed.',
       'The only agent here with a measured, quantified offset - and it is unusually long.']),
'losartan': dict(
    on=_('~2 h', 2, 'C'), pk=_('6 h', 6, 'L'), full=_('3-6 wk', 4.5 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='losartan half-life ~2 h, active metabolite 6-9 h', reb='ok',
    q=['Label: the effect is substantially present within one week but in some studies the maximal effect occurred in 3 to 6 weeks.',
       'Label: there is no apparent rebound effect after abrupt withdrawal.',
       'Label: peak (6 hour) effects were uniformly, but moderately, larger than trough effects.']),
'olmesartan': dict(
    on=_('~2 h', 2, 'C'), pk=_('~2 h', 2, 'K'), full=_('2-4 wk', 3 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life ~13 h; steady state within 3-5 days', reb='ok',
    q=['Label: the onset of the antihypertensive effect occurred within 1 week and was largely manifest after 2 weeks (near maximal at 4 weeks).',
       'Label: no rebound effect following abrupt withdrawal after 1 year of treatment.']),
'telmisartan': dict(
    on=_('1st dose', 2, 'L'), pk=_('~3 h', 3, 'K'), full=_('4 wk', 4 * W, 'L'),
    off=_('3-7 d', 6 * D, 'L'), hl='half-life ~24 h', reb='ok',
    q=['Label: blood pressure was reduced after the first dose, with a maximal reduction by about 4 weeks.',
       'Label: with cessation of treatment, blood pressure gradually returned to baseline values over a period of several days to one week.']),
'valsartan': dict(
    on=_('2 h', 2, 'L'), pk=_('6 h', 6, 'L'), full=_('4 wk', 4 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='half-life ~6 h', reb='ok',
    q=['Label: onset of antihypertensive activity occurs at approximately 2 hours, and maximum reduction of blood pressure is achieved within 6 hours.',
       'Label: the reduction is substantially present within 2 weeks, and maximal reduction is generally attained after 4 weeks.',
       'Label: abrupt withdrawal has not been associated with a rapid increase in blood pressure.']),
# ---------------------------------------------------------------- beta blockers
'atenolol': dict(
    on=_('2-4 h', 3, 'K'), pk=_('2-4 h', 3, 'K'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='half-life 6-7 h, much longer in the elderly and in renal failure', taper=True,
    q=['Label: the full effect of this dose will usually be seen within one to two weeks.',
       'Label: both beta-blocking and antihypertensive effects persist for at least 24 hours.',
       'Label: patients with coronary artery disease should be advised against abrupt discontinuation; because coronary disease is common and may be unrecognized, it may be prudent not to stop abruptly even when treating hypertension alone.']),
'betaxolol': dict(
    on=_('3-4 h', 3.5, 'K'), pk=_('3-4 h', 3.5, 'L'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~3-4 d', 84, 'K'), hl='half-life 14-22 h; steady state in 5-7 days', taper=True,
    q=['Label: the full antihypertensive effect is usually seen within 7 to 14 days.',
       'Label: the antihypertensive response was similar at peak blood levels (3 to 4 hours) and at trough (24 hours).',
       'Label: consider gradual withdrawal of beta-adrenergic receptor inhibitors.']),
'bisoprolol': dict(
    on=_('2-4 h', 3, 'K'), pk=_('2-4 h', 3, 'K'), full=_('1 wk', W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life 9-12 h; steady state within 5 days', taper=True,
    q=['Label: blood pressure responses were seen within one week of treatment and changed little thereafter.',
       'Label: abrupt withdrawal of beta-blockade may be followed by an exacerbation of the symptoms of hyperthyroidism or may precipitate thyroid storm.']),
'carvedilol': dict(
    on=_('1-2 h', 1.5, 'L'), pk=_('1-2 h', 1.5, 'L'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~2 d', 48, 'K'), hl='half-life 7-10 h', taper=True,
    q=['Label: the peak antihypertensive effect occurred 1 to 2 hours after a dose.',
       'Label: the full antihypertensive effect is seen within 7 to 14 days.',
       'Label: acute exacerbation of coronary artery disease upon cessation of therapy - do not abruptly discontinue.']),
'metoprolol': dict(
    on=_('~6-7 h', 6.5, 'K'), pk=_('~7 h', 7, 'K'), full=_('1 wk', W, 'L'),
    off=_('~1 d', 24, 'K'), hl='plasma half-life 3-7 h, extended by the succinate ER matrix', taper=True,
    q=['Label: in general, the maximum effect of any given dosage level will be apparent after 1 week of therapy. Titrate at weekly or longer intervals.',
       'Label: when discontinuing, gradually reduce the dosage over a period of 1 to 2 weeks and monitor the patient.']),
'nebivolol': dict(
    on=_('~2-4 h', 3, 'K'), pk=_('~2-4 h', 3, 'K'), full=_('2 wk', 2 * W, 'L'),
    off=_('~2-4 d', 72, 'K'), hl='effective half-life ~12 h (19 h in CYP2D6 poor metabolizers)', taper=True,
    q=['Label: the blood pressure lowering effect was seen within two weeks of treatment and was maintained over the 24-hour dosing interval.',
       'Label: the dose can be increased at 2-week intervals.',
       'Label: do not abruptly discontinue in patients with coronary artery disease.']),
'propranolol': dict(
    on=_('~6 h', 6, 'K'), pk=_('~6 h', 6, 'K'), full=_('days to wk', 3 * W, 'L'),
    off=_('~2 d', 48, 'K'), hl='half-life ~10 h for the long-acting capsule', taper=True,
    q=['Label: the time needed for full antihypertensive response to a given dosage is variable and may range from a few days to several weeks.',
       'Label: it may be advisable to withdraw the drug gradually over a period of several weeks - the longest taper of any agent here.']),
# ---------------------------------------------------------------- calcium channel blockers
'amlodipine': dict(
    on=_('~2-6 h', 4, 'K'), pk=_('6-12 h', 9, 'K'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~1 wk', 7 * D, 'K'), hl='half-life 30-50 h; steady state only after 7-8 days - the slowest on and off',
    q=['Label: because of the gradual onset of action, acute hypotension is unlikely.',
       'Label: in general, wait 7 to 14 days between titration steps.',
       'Label: steady-state plasma levels are reached after 7 to 8 days of consecutive daily dosing.',
       'The practical consequence: a single missed dose barely registers, and a dose change takes two weeks to judge.']),
'diltiazem': dict(
    on=_('~2-3 h', 2.5, 'K'), pk=_('3-6 h', 4.5, 'L'), full=_('2 wk', 2 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='steady-state half-life 5-10 h for the once-daily ER capsule',
    q=['Label: maximum antihypertensive effect is usually observed by 14 days of chronic therapy; schedule dosage adjustments accordingly.',
       'Label: the trough (24 hour) effect retained more than one-half of the response seen at peak (3 to 6 hours).']),
'felodipine': dict(
    on=_('2-5 h', 2, 'L'), pk=_('2-5 h', 3.5, 'L'), full=_('2 wk', 2 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life 11-16 h for the ER tablet',
    q=['Label: following administration of the extended-release tablet, a reduction in blood pressure generally occurs within 2 to 5 hours.',
       'Label: dosage adjustments should occur generally at intervals of not less than 2 weeks.',
       'Label: trough reductions in diastolic pressure are approximately 40 to 50% of peak reductions.']),
'isradipine': dict(
    on=_('2-3 h', 2, 'L'), pk=_('2-3 h', 2.5, 'L'), full=_('2-4 wk', 3 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='early half-life 1.5-2 h, terminal ~8 h',
    q=['Label: dose-related reductions in blood pressure are achieved within 2 to 3 hours following a single oral dose.',
       'Label: maximal response may require 2 to 4 weeks.',
       'Label: duration of action (at least 50% of peak response) of more than 12 hours.']),
'nicardipine': dict(
    on=_('~30 min', 0.5, 'K'), pk=_('1-2 h', 1.5, 'L'), full=_('~3 d', 3 * D, 'K'),
    off=_('~1 d', 24, 'K'), hl='fast early half-life 2-4 h, terminal 8.6 h',
    q=['Label: the maximum blood pressure lowering effect occurs approximately 1 to 2 hours after dosing.',
       'Label: well over half of the antihypertensive effect is lost by the end of the 8-hour dosing interval.',
       'Label: at least 3 days should be allowed before increasing the dose.',
       'The sharpest peak-to-trough swing of any oral agent here - the reason it is impractical for chronic hypertension.']),
'nifedipine': dict(
    on=_('~2-6 h', 4, 'K'), pk=_('~6 h', 6, 'K'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~1-2 d', 36, 'K'), hl='half-life ~7 h as the ER tablet (2 h for the immediate-release capsule)', reb='ok',
    q=['Label: titration should proceed over a 7 to 14 day period so that the response to each dose level can be fully assessed.',
       'Label: no rebound effect has been observed upon discontinuation.',
       'Label: trough/peak ratios ranged from 41-78% diastolic and 46-91% systolic.']),
'nisoldipine': dict(
    on=_('~4-6 h', 5, 'K'), pk=_('6-12 h', 9, 'K'), full=_('1-2 wk', 2 * W, 'C'),
    off=_('~2-3 d', 60, 'K'), hl='half-life ~14 h',
    q=['Label: the sustained antihypertensive effect was demonstrated by 24 hour monitoring, with trough/peak ratios of 70 to 100%.',
       'One of the flattest 24-hour profiles here - very little peak-to-trough swing.']),
'verapamil': dict(
    on=_('~4-7 h', 5, 'K'), pk=_('7-9 h', 8, 'K'), full=_('1-2 wk', 2 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life ~12 h for the ER capsule, and it lengthens during chronic dosing',
    q=['Label: the antihypertensive effects of verapamil are evident within the first week of therapy.',
       'Label: since the half-life of verapamil increases during chronic dosing, maximum response may be delayed.']),
# ---------------------------------------------------------------- diuretics
'hydrochlorothiazide': dict(
    on=_('2 h', 2, 'L'), pk=_('4 h', 4, 'L'), full=_('2-4 wk', 3 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='half-life 6-15 h; a single dose diureses for 6-12 h',
    q=['Label: after oral administration, diuresis begins within 2 hours, peaks in about 4 hours, and lasts about 6 to 12 hours.',
       'Label: the antihypertensive effect had onset within 1 week and was near maximal at 4 weeks.',
       'Label: the hydrochlorothiazide dose should generally not be increased until 2 to 3 weeks have elapsed.',
       'The brisk diuresis in the first hours is not the antihypertensive effect - that takes weeks, and arrives after the diuresis has largely resolved.']),
'chlorthalidone': dict(
    on=_('~2-3 h', 2.5, 'K'), pk=_('~4-6 h', 5, 'K'), full=_('2-4 wk', 4 * W, 'L'),
    off=_('~1-2 wk', 10 * D, 'K'), hl='half-life 40-60 h - by far the longest of the thiazide-type agents',
    q=['Label: double the dosage every 2 to 4 weeks as needed based on individual patient response.',
       'Label: the mean plasma half-life is about 40 to 60 hours.',
       'The long half-life is why it covers a missed dose better than hydrochlorothiazide - and why hyponatraemia and hypokalaemia take longer to resolve after stopping.']),
'indapamide': dict(
    on=_('1-2 h', 1.5, 'K'), pk=_('~2 h', 2, 'K'), full=_('4 wk', 4 * W, 'L'),
    off=_('~3-4 d', 84, 'K'), hl='half-life ~14 h in whole blood, 26 h terminal',
    q=['Label: if the response to 1.25 mg is not satisfactory after 4 weeks, the daily dose may be increased to 2.5 mg.',
       'The slowest diuretic to judge - the label sets a four-week interval between steps.']),
'furosemide': dict(
    on=_('<1 h', 1, 'L'), pk=_('1-2 h', 1.5, 'K'), full=_('days', 3 * D, 'K'),
    off=_('<1 d', 12, 'K'), hl='half-life ~2 h; a single oral dose diureses for 6-8 h',
    q=['Label: the onset of diuresis following oral administration is within 1 hour. The duration of diuretic effect is 6 to 8 hours.',
       'Fastest on and fastest off of anything here, which is exactly why it is a poor chronic antihypertensive: twice-daily dosing leaves the blood pressure unprotected for much of the day.']),
'spironolactone': dict(
    on=_('~1-2 d', 36, 'K'), pk=_('~1-2 d', 36, 'K'), full=_('2 wk', 2 * W, 'L'),
    off=_('~2-3 d', 60, 'K'), hl='spironolactone half-life 1-2 h, but the active metabolites run 10-35 h',
    q=['Label: treatment should be continued for at least 2 weeks, since the maximum response may not occur before this time.',
       'The delay is pharmacodynamic, not pharmacokinetic - the effect depends on turning over aldosterone-driven sodium transport, so nothing useful happens on day one.']),
'eplerenone': dict(
    on=_('~1-2 d', 36, 'K'), pk=_('~1-2 d', 36, 'K'), full=_('4 wk', 4 * W, 'L'),
    off=_('~1 wk', 7 * D, 'L'), hl='half-life 3-6 h; steady state within 2 days', reb='ok',
    q=['Label: blood pressure lowering was apparent within 2 weeks from the start of therapy, with maximal antihypertensive effects achieved within 4 weeks.',
       'Label: blood pressures in patients not taking other antihypertensives rose 1 week after withdrawal by about 6/3 mmHg - one of the few directly measured offsets on this page.']),
'amiloride': dict(
    on=_('~2 h', 2, 'K'), pk=_('6-10 h', 8, 'L'), full=_('~2 wk', 2 * W, 'C'),
    off=_('~1-2 d', 36, 'K'), hl='half-life 6-9 h; the effect on electrolyte excretion lasts about 24 h',
    q=['Label: the effect on electrolyte excretion reaches a peak between 6 and 10 hours and lasts about 24 hours.']),
}

# Agents in the efficacy model with no US label - carry the class profile.
CLASS_FOR = {
    'barnidipine': 'DHP', 'lercanidipine': 'DHP', 'manidipine': 'DHP', 'nitrendipine': 'DHP',
    'cilazapril': 'ACEi', 'delapril': 'ACEi', 'spirapril': 'ACEi',
    'eprosartan': 'ARB', 'fimasartan': 'ARB',
    'bendrofluazide': 'thiazide', 'cyclopenthiazide': 'thiazide',
    'celiprolol': 'BB', 'oxprenolol': 'BB', 'penbutolol': 'BB',
}

SOURCE = ('FDA prescribing information via openFDA/DailyMed, read directly from the '
          'Clinical Pharmacology, Clinical Studies and Dosage sections of each '
          "drug's own single-ingredient label.")


def kin_for(name, sub):
    """Return the packed kinetics record for one drug, or None."""
    rec = KIN.get(name)
    if rec is None:
        key = CLASS_FOR.get(name)
        if key is None:
            return None
        rec = dict(CLASS_KIN[key])
        rec['q'] = [f'No US label for this agent - shown as the {key} class profile, '
                    f'carried from the labelled members of the class.']
    out = {k: rec[k] for k in ('on', 'pk', 'full', 'off')}
    out['hl'] = rec.get('hl')
    if rec.get('taper'):
        out['tap'] = 1
    if rec.get('taper'):
        out['reb'] = 'taper'
    elif rec.get('reb'):
        out['reb'] = rec['reb']
    out['q'] = rec.get('q', [])
    return out
