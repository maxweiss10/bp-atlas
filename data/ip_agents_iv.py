# -*- coding: utf-8 -*-
"""Parenteral and topical agents.

Dosing, onset and offset are from the FDA prescribing information on DailyMed
unless a note says otherwise.  `on.v` and `off.v` are the sort values, in
minutes; the string beside them is what the column prints.

`ctrl` is how finely the agent can be steered - 3 you can take an overshoot
back in minutes, 0 you cannot take it back at all.  It is the property that
decides drip versus push, and it is the one thing the card's layout implies
but never states.
"""

DM = 'https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query='

IV_AGENTS = [
# ---------------------------------------------------------------- drips ----
{
 'n': 'Clevidipine', 'brand': 'Cleviprex', 'route': 'gtt', 'routeAbbr': 'gtt',
 'cls': 'CCB', 'abbr': 'CCB', 'clsf': 'Dihydropyridine calcium blocker',
 'setting': 'icu', 'aline': True,
 'dose': {'start': '1&ndash;2 mg/h',
          'titr': 'double q90 s at first, then smaller steps q5&ndash;10 min; most respond at '
                  '4&ndash;6 mg/h',
          'max': '16 mg/h at any moment; 21 mg/h <i>averaged</i> over 24 h',
          'was': 'max 21 mg/h'},
 'on': {'v': 3, 's': '2&ndash;4 min', 's2': '4&ndash;5% drop by then'},
 'off': {'v': 10, 's': '5&ndash;15 min', 's2': 'no accumulation'},
 'ctrl': 3,
 'ctrlNote': 'Broken down by blood and tissue esterases, so offset is organ-independent and does '
             'not lengthen with a long infusion. The most controllable agent available.',
 'ind': [{'t': 'ICH', 'full': 'Intracerebral hemorrhage - smooth control without ICP rise'},
         {'t': 'SAH', 'full': 'Subarachnoid hemorrhage'},
         {'t': 'Stroke', 'full': 'Acute ischemic stroke'},
         {'t': 'Ao dissection', 'full': 'Aortic dissection, after beta blockade'},
         {'t': 'Flash pulm edema', 'full': 'Arterial-selective, so it does not add volume'},
         {'t': 'Post-op', 'full': 'Perioperative hypertension'}],
 'avoid': [{'t': 'Soy or egg allergy', 'full': 'Label contraindication - the vehicle is a soybean '
                                               'oil emulsion with egg yolk phospholipid'},
           {'t': 'Defective lipid metabolism', 'full': 'Label contraindication - pathologic '
                 'hyperlipidemia, lipoid nephrosis, acute pancreatitis with hyperlipidemia'},
           {'t': 'Severe AS', 'full': 'Label contraindication - afterload reduction without '
                                      'contractile reserve'}],
 'watch': 'Triglycerides and total lipid volume. Rebound hypertension for <b>8 h</b> after stopping '
          'if nothing oral has taken over.',
 'mech': 'Third-generation dihydropyridine in a lipid emulsion. Arterial-selective, with no '
         'venodilation and no effect on filling pressures.',
 'practical': 'Carries <b>0.2 g of lipid per mL</b>, which is what sets the 1000 mL and 21 mg/h '
              'daily caps. Once the stopper is punctured, use within 12 hours &mdash; a lipid '
              'emulsion grows bacteria. Roughly <b>three times the price of nicardipine</b>, and '
              'one price comparison put a vial 682% above a nicardipine bag, so formularies '
              'restrict it. Its real advantage is volume, not potency.',
 'src': 'fix',
 'fix': [{'field': 'Maximum rate', 'was': 'max 21 mg/h', 'now': '16 mg/h instantaneously, with '
          '21 mg/h as a 24-hour average',
          'why': 'The label’s 21 mg/h is a <b>lipid-volume cap</b> &mdash; “no more than '
                 '1000 mL or an average of 21 mg/hour&hellip; per 24 hour period” &mdash; not '
                 'a ceiling on the pump. Reading it as an instantaneous maximum both under-doses a '
                 'patient who needs 16 and ignores the volume limit that actually binds.',
          'cite': {'t': 'Clevidipine prescribing information', 'u': DM + 'clevidipine'}}],
 'cites': [{'k': 'label', 't': 'Clevidipine butyrate injectable emulsion', 'u': DM + 'clevidipine'}],
},
{
 'n': 'Nicardipine', 'brand': 'Cardene IV', 'route': 'gtt', 'routeAbbr': 'gtt',
 'cls': 'CCB', 'abbr': 'CCB', 'clsf': 'Dihydropyridine calcium blocker',
 'setting': 'icu', 'aline': True,
 'dose': {'start': '5 mg/h',
          'titr': '+2.5 mg/h q5 min if pushing, q15 min if not',
          'max': '15 mg/h; drop back to 3 mg/h once at goal'},
 'on': {'v': 7, 's': '5&ndash;10 min', 's2': 'half the effect by ~45 min'},
 'off': {'v': 30, 's': '~30 min to half', 's2': 'full 2&ndash;6 h', 'soft': True,
         'note': 'The label times the 50% offset at about 30 minutes; full offset is 2-6 hours and '
                 'lengthens after a long infusion, because the slow terminal half-life is 14.4 h.'},
 'ctrl': 2,
 'ctrlNote': 'Half the effect is gone in about half an hour, but the rest takes hours, and a long '
             'infusion loads a deep compartment that empties slowly. Titratable, not instantly '
             'reversible.',
 'ind': [{'t': 'ICH', 'full': 'Intracerebral hemorrhage - the best blood-pressure variability '
                              'profile of the available agents'},
         {'t': 'SAH', 'full': 'Subarachnoid hemorrhage'},
         {'t': 'Stroke', 'full': 'Acute ischemic stroke'},
         {'t': 'Ao dissection', 'full': 'Aortic dissection, after beta blockade'},
         {'t': 'Flash pulm edema', 'full': 'Acute pulmonary edema'},
         {'t': 'AKI', 'full': 'No renal dose adjustment and no toxic metabolite'}],
 'avoid': [{'t': 'Advanced AS', 'full': 'Label contraindication'},
           {'t': 'HFrEF', 'full': 'Titrate slowly, especially alongside a beta blocker'},
           {'t': 'Hepatic impairment', 'full': 'CYP-metabolised; effects are prolonged'}],
 'watch': 'Infusion site &mdash; rotate it <b>every 12 h</b> to avoid phlebitis. Volume: 15 mg/h of '
          'the 0.1 mg/mL bag is 150 mL/h.',
 'mech': 'Dihydropyridine calcium blocker; a peripherally selective arterial vasodilator with '
         'essentially no negative inotropy, and it does not raise intracranial pressure. That last '
         'property is why it is the neuro-ICU workhorse.',
 'practical': 'Head to head against labetalol in a mixed ICU population it reached goal more often '
              '(83% vs 67%), needed fewer added agents and caused fewer hypotensive episodes. Use '
              'the 0.2 mg/mL bag when volume matters. Large peripheral vein or central line.',
 'src': 'fix',
 'fix': [{'field': 'Offset', 'was': '15 min - 4 h', 'now': '~30 min to half the effect, 2-6 h to '
          'full, longer after a prolonged infusion',
          'why': 'The 15-minute floor is not in the label, which states a “50% offset of '
                 'action in about 30 minutes”. The distinction matters at the bedside: if you '
                 'stop the drip expecting the pressure back in fifteen minutes, you will stop it '
                 'too late.',
          'cite': {'t': 'Nicardipine prescribing information', 'u': DM + 'nicardipine'}}],
 'cites': [{'k': 'label', 't': 'Nicardipine hydrochloride injection', 'u': DM + 'nicardipine'}],
},
{
 'n': 'Nitroglycerin', 'route': 'gtt', 'routeAbbr': 'gtt',
 'cls': 'Nitro', 'abbr': 'NITRO', 'clsf': 'Nitric oxide donor, mainly venous',
 'setting': 'both', 'aline': False,
 'dose': {'start': '5 mcg/min',
          'titr': '+5 mcg/min q3&ndash;5 min; above 20 mcg/min, steps of 10&ndash;20',
          'max': 'no label maximum. ~200 mcg/min in ordinary use; 400&ndash;800 in flash pulmonary '
                 'edema',
          'was': 'start 10&ndash;30, max 400, non-responder at 200'},
 'on': {'v': 3, 's': '2&ndash;5 min'},
 'off': {'v': 7, 's': '5&ndash;10 min', 's2': 'half-life ~3 min'},
 'ctrl': 3,
 'ctrlNote': 'On and off within minutes. The limit is not control but tachyphylaxis.',
 'ind': [{'t': 'ACS', 'full': 'Dilates coronaries without the steal that nitroprusside causes'},
         {'t': 'Flash pulm edema', 'full': 'The first-line agent, at doses far above the usual '
                                           'heart-failure range'},
         {'t': 'Acute HF', 'full': 'Preload reduction'}],
 'avoid': [{'t': 'PDE5 inhibitor', 'full': 'Label contraindication. Wait 12 h after avanafil, 24 h '
                  'after sildenafil or vardenafil, 48 h after tadalafil'},
           {'t': 'RV infarction', 'full': 'An infarcted right ventricle is preload-dependent'},
           {'t': 'Raised ICP', 'full': 'Label contraindication'},
           {'t': 'Tamponade', 'full': 'Label contraindication - any state where output depends on '
                  'venous return'}],
 'watch': '<b>Tachyphylaxis over the first 24&ndash;48 h.</b> Headache is dose-limiting. Use '
          'non-PVC tubing &mdash; PVC adsorbs 20&ndash;60% of the dose.',
 'mech': 'Nitric oxide donor. Predominantly a venodilator, with arterial effect appearing at higher '
         'rates &mdash; which is why the flash-pulmonary-edema doses are so much larger.',
 'practical': 'In sympathetic crashing acute pulmonary edema the published approach is a bolus of '
              '1000&ndash;2000 mcg over two minutes, then 100&ndash;300 mcg/min, titrating down as '
              'it resolves. That is an order of magnitude above the ordinary heart-failure drip and '
              'sits outside anything the card describes.',
 'src': 'fix',
 'fix': [{'field': 'Starting rate', 'was': '10-30 mcg/min', 'now': '5 mcg/min',
          'why': 'The label starts at 5 mcg/min and titrates in 5 mcg steps every 3-5 minutes.',
          'cite': {'t': 'Nitroglycerin in 5% dextrose injection', 'u': DM + 'nitroglycerin+injection'}},
         {'field': 'Maximum', 'was': 'max 400 mcg/min', 'now': 'no label maximum; ~200 in ordinary '
          'use and 400-800 in flash pulmonary edema',
          'why': 'Printing 400 as the ceiling is wrong in both directions - too high for a routine '
                 'drip and too low for the one situation that needs the big doses.',
          'cite': {'t': 'Nitroglycerin in 5% dextrose injection', 'u': DM + 'nitroglycerin+injection'}},
         {'field': 'Non-responder threshold', 'was': 'no response by 200 mcg/min = non-responder',
          'now': 'deleted',
          'why': 'No source carries this. The label’s only non-response landmark is at '
                 '<b>20</b> mcg/min, where it says to switch to larger increments - an instruction '
                 'to keep going, not to stop.',
          'cite': {'t': 'Nitroglycerin in 5% dextrose injection', 'u': DM + 'nitroglycerin+injection'}}],
 'cites': [{'k': 'label', 't': 'Nitroglycerin in 5% dextrose injection',
            'u': DM + 'nitroglycerin+injection'}],
},
{
 'n': 'Esmolol', 'brand': 'Brevibloc', 'route': 'gtt', 'routeAbbr': 'gtt',
 'cls': 'BB', 'abbr': 'BB', 'clsf': 'Beta-1 selective blocker',
 'setting': 'icu', 'aline': False,
 'dose': {'start': '500 mcg/kg over 1 min, then 25&ndash;50 mcg/kg/min',
          'titr': '+25 mcg/kg/min q5&ndash;10 min',
          'max': '300 mcg/kg/min &mdash; above that is unstudied',
          'was': 'titrate q10&ndash;20 min'},
 'on': {'v': 1.5, 's': '1&ndash;2 min', 's2': 'steady state ~5 min', 'soft': True,
        'note': 'The label states no onset figure; it gives steady-state beta blockade at about '
                '5 minutes with a loading dose. The 1-2 minute figure is from the critical-care '
                'literature.'},
 'off': {'v': 15, 's': '10&ndash;20 min', 's2': 'half-life ~9 min'},
 'ctrl': 3,
 'ctrlNote': 'Cleared by red-cell esterases, so neither liver nor kidney failure changes it. Turn '
             'it off and beta blockade is substantially gone in 10-20 minutes.',
 'ind': [{'t': 'Ao dissection', 'full': 'Rate and dP/dt control - the first agent, before any '
                                        'vasodilator'},
         {'t': 'ACS', 'full': 'Coronary ischemia with tachycardia'},
         {'t': 'Peri-op', 'full': 'Perioperative hypertension'},
         {'t': 'Tachyarrhythmia', 'full': 'Where rate and pressure need the same drug'}],
 'avoid': [{'t': 'Decompensated HF', 'full': 'Label contraindication'},
           {'t': 'Cardiogenic shock', 'full': 'Label contraindication'},
           {'t': 'Heart block &gt;1&deg;', 'full': 'Label contraindication, as is sick sinus '
                  'syndrome and severe sinus bradycardia'},
           {'t': 'With IV non-DHP CCB', 'full': 'Label contraindication - IV cardiodepressant '
                  'calcium blockers'},
           {'t': 'Pulmonary HTN', 'full': 'Label contraindication'}],
 'watch': 'Extravasation causes necrosis and blistering &mdash; large vein, never a butterfly. A '
          'lot of volume at high body weights.',
 'mech': 'Beta-1 selective, with <b>no vasodilator activity at all</b>: pressure falls only through '
         'reduced rate and contractility. In an emergency driven by vasoconstriction that is the '
         'wrong lever on its own, which is why in dissection it is paired with a vasodilator.',
 'practical': 'The label and the guideline disagree about the ceiling, and the card follows the '
              'label. The label allows 250&ndash;300 mcg/kg/min for hypertension specifically and '
              'says above 300 is unstudied; the hypertension guideline\u2019s own emergency drug '
              'table stops at 200. Either is defensible &mdash; know which one the person '
              'questioning you is holding.',
 'src': 'fix',
 'fix': [{'field': 'Titration interval', 'was': 'adjust q10-20 min', 'now': 'q5-10 min',
          'why': 'Slower than every source: the label titrates at intervals of four minutes or '
                 'more, and the critical-care references say every 3-5 or every 10 minutes. On a '
                 'drug whose whole point is speed, a 20-minute step wastes it.',
          'cite': {'t': 'Esmolol hydrochloride injection', 'u': DM + 'esmolol'}},
         {'field': 'Onset', 'was': '&lt;1 min', 'now': '1-2 min', 'why': 'Minor, but nothing in the '
          'label or the reviews supports sub-minute onset.',
          'cite': {'t': 'Esmolol hydrochloride injection', 'u': DM + 'esmolol'}}],
 'cites': [{'k': 'label', 't': 'Esmolol hydrochloride injection', 'u': DM + 'esmolol'}],
},
{
 'n': 'Nitroprusside', 'brand': 'Nipride RTU', 'route': 'gtt', 'routeAbbr': 'gtt',
 'cls': 'Nitro', 'abbr': 'NITRO', 'clsf': 'Nitric oxide donor, arterial and venous',
 'setting': 'icu', 'aline': True,
 'dose': {'start': '0.3 mcg/kg/min',
          'titr': 'reassess at least 5 min between steps; usual working range 0.25&ndash;2',
          'max': '10 mcg/kg/min, for as short a time as possible. eGFR &lt;30: mean rate under 3. '
                 'Anuric: 1',
          'was': 'up to 10 mcg/kg/min for &lt;10 min'},
 'on': {'v': 1, 's': '&lt;1&ndash;2 min'},
 'off': {'v': 2, 's': '1&ndash;10 min', 's2': 'half-life ~2 min'},
 'ctrl': 3,
 'ctrlNote': 'The fastest on and off of any of them, which is exactly why it needs an arterial line '
             'and a volumetric pump - small rate changes move the pressure a long way.',
 'ind': [{'t': 'Severe LV dysfunction', 'full': 'Balanced arterial and venous dilation unloads both '
                  'sides'},
         {'t': 'Refractory HTN', 'full': 'Named as the fallback in acute ischemic stroke when '
                  'pressure stays uncontrolled or DBP exceeds 140'}],
 'avoid': [{'t': 'ACS or CAD', 'full': 'Coronary steal - it redistributes flow away from ischemic '
                  'myocardium. A randomised trial found higher mortality when started within 9 h of '
                  'infarction'},
           {'t': 'Raised ICP', 'full': 'Label states it can raise intracranial pressure'},
           {'t': 'Renal impairment', 'full': 'Thiocyanate accumulates; its half-life doubles or '
                  'triples in renal failure'},
           {'t': 'Hepatic impairment', 'full': 'Label - more susceptible to cyanide toxicity'},
           {'t': 'PDE5i or riociguat', 'full': 'Label contraindication'},
           {'t': 'Compensatory HTN', 'full': 'Label contraindication - coarctation, AV shunt'}],
 'watch': '<b>Cyanide.</b> Above 2 mcg/kg/min it is generated faster than the body clears it. The '
          'earliest sign is <b>needing more drug to hold the same pressure</b>. Check thiocyanate '
          'if the cumulative dose passes 7 mg/kg/day.',
 'mech': 'Releases nitric oxide directly, dilating arteries and veins equally. Each molecule also '
         'releases five cyanide ions, which is the whole problem.',
 'practical': 'A 70 kg adult can buffer roughly <b>35 mg</b> of cumulative nitroprusside before the '
              'cyanide defence is exhausted. Suspicion alone is grounds to treat; hydroxocobalamin '
              'with sodium thiosulfate is what is actually used, and it is not in the label. In '
              'intracerebral hemorrhage, nitroprusside carried higher adjusted mortality than '
              'nicardipine in a 1,426-patient database.',
 'monitor': 'The boxed warning requires <b>continuous blood-pressure monitoring</b>, and the label '
            'requires a volumetric pump. Protect from light; discard if the solution turns blue, '
            'green or bright red.',
 'src': 'fix',
 'fix': [{'field': 'Maximum-rate duration', 'was': 'up to 10 mcg/kg/min temporarily, under 10 min',
          'now': 'buffering is exceeded in <b>under an hour</b> at 10 mcg/kg/min; limit max-rate '
                 'infusion to as short a time as possible',
          'why': 'The current label contains no ten-minute rule. That figure is legacy '
                 'Nitropress-era labelling. The real constraint is the cumulative cyanide load, '
                 'not a stopwatch.',
          'cite': {'t': 'Sodium nitroprusside boxed warning',
                   'u': DM + 'nitroprusside'}}],
 'cites': [{'k': 'label', 't': 'Sodium nitroprusside injection', 'u': DM + 'nitroprusside'}],
},
# ------------------------------------------------------------- IV pushes ----
{
 'n': 'Labetalol', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'BB', 'abbr': 'BB', 'clsf': 'Alpha-1 and non-selective beta blocker',
 'setting': 'both', 'aline': False,
 'dose': {'start': '10&ndash;20 mg over 2 min (0.25 mg/kg)',
          'titr': '20&ndash;80 mg q10 min. Infusion possible at 0.5&ndash;2 mg/min, though the '
                  'kinetics suit boluses better',
          'max': '300 mg cumulative &mdash; above that is unstudied'},
 'on': {'v': 4, 's': '2&ndash;5 min', 's2': 'peak 5&ndash;15 min'},
 'off': {'v': 240, 's': '2&ndash;6 h', 's2': 'tail to 16&ndash;18 h', 'soft': True,
         'note': 'The label describes blood pressure approaching pretreatment values only after an '
                 'average of 16 to 18 hours. Half-life is about 5.5 hours.'},
 'ctrl': 1,
 'ctrlNote': 'Each dose is a commitment for hours. This is the drug people overshoot with, because '
             'the next dose is given before the previous one has finished arriving.',
 'ind': [{'t': 'Stroke', 'full': 'Ischemic and hemorrhagic - the standard floor agent'},
         {'t': 'Pre-eclampsia', 'full': 'One of the three ACOG first-line agents'},
         {'t': 'Ao dissection', 'full': 'Can serve as the beta blocker alone, since it also blocks '
                  'alpha'},
         {'t': 'ACS', 'full': 'Acute coronary syndrome'}],
 'avoid': [{'t': 'Asthma or COPD', 'full': 'Label contraindication - bronchial asthma or '
                  'obstructive airway disease'},
           {'t': 'Overt HF', 'full': 'Label says avoid in overt congestive heart failure'},
           {'t': 'Bradycardia or block', 'full': 'Label contraindication - severe sinus bradycardia '
                  'or block beyond first degree'},
           {'t': 'Cardiogenic shock', 'full': 'Label contraindication'},
           {'t': 'With IV non-DHP CCB', 'full': 'Label contraindication'}],
 'watch': 'Keep the patient supine and mobilise gradually for up to 3 hours. Rare but real '
          'hepatocellular injury.',
 'mech': 'Blocks alpha-1 and beta together, but <b>given intravenously the ratio is about 1 to 7</b> '
         '&mdash; so it behaves mostly as a beta blocker, while the problem in most hypertensive '
         'emergencies is arterial vasoconstriction. Orally the ratio is about 1 to 3.',
 'src': 'fix',
 'fix': [{'field': 'Duration', 'was': '3-6 h', 'now': '2-6 h of useful effect, with a tail running '
          'to 16-18 h',
          'why': 'The label times the return toward baseline at an average of 16 to 18 hours. '
                 'Understating this is precisely what produces the overcorrection labetalol is '
                 'known for &mdash; the dose you give at hour three is landing on top of the one '
                 'from hour one.',
          'cite': {'t': 'Labetalol hydrochloride injection', 'u': DM + 'labetalol+injection'}}],
 'cites': [{'k': 'label', 't': 'Labetalol hydrochloride injection', 'u': DM + 'labetalol+injection'}],
},
{
 'n': 'Hydralazine', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'Vasodil', 'abbr': 'VASO', 'clsf': 'Direct arteriolar vasodilator',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '5&ndash;20 mg q15&ndash;30 min until something happens',
          'titr': '10&ndash;40 mg IM if there is no access. In pregnancy, 5&ndash;10 mg then 10 mg '
                  'q20 min',
          'max': 'label says 20&ndash;40 mg repeated as needed, which is more than current practice'},
 'on': {'v': 15, 's': '10&ndash;20 min', 's2': 'peak 10&ndash;80 min', 'soft': True,
        'note': 'The label gives the average maximal decrease as occurring between 10 and 80 '
                'minutes - an eight-fold spread, and the real reason this drug cannot be titrated.'},
 'off': {'v': 180, 's': '1&ndash;4 h', 's2': 'can run 8&ndash;12 h', 'soft': True,
         'note': 'The injection label states no duration at all. 1-4 hours is the fair central '
                 'estimate; tissue sequestration in arterial walls prolongs the vascular effect, '
                 'and slow acetylators and renal impairment prolong it further.'},
 'ctrl': 0,
 'ctrlNote': 'You give a dose, nothing happens for anywhere between ten and eighty minutes, someone '
             'gives another, and both land together. There is no way to take it back.',
 'ind': [{'t': 'Pre-eclampsia', 'full': 'One of the three ACOG first-line agents, and the one place '
                  'it is genuinely preferred'}],
 'avoid': [{'t': 'CAD', 'full': 'Label contraindication - reflex tachycardia raises myocardial '
                  'oxygen demand and can provoke angina'},
           {'t': 'Ao dissection', 'full': 'Reflex tachycardia raises dP/dt and wall shear stress'},
           {'t': 'Rheumatic MV disease', 'full': 'Label contraindication'},
           {'t': 'As a titration agent', 'full': 'The unpredictability is the point - use something '
                  'else whenever you have the choice'}],
 'watch': 'Reflex tachycardia. Drug-induced lupus with prolonged use.',
 'mech': 'Dilates arterioles directly and leaves venous capacitance alone, so afterload drops while '
         'the baroreflex fires back.',
 'practical': 'In one hospital series 94 patients received 201 doses of intravenous hydralazine and '
              '<b>only 4 of them had an urgent hypertensive condition</b>. Keeping it off the drip '
              'table, as the card does, is the right call.',
 'src': 'fix',
 'fix': [{'field': 'Duration', 'was': '1-4 h', 'now': '1-4 h typically, but up to 8-12 h',
          'why': 'Defensible as a median, but the tail is the clinically dangerous part and the '
                 'label states no duration at all.',
          'cite': {'t': 'Hydralazine hydrochloride injection', 'u': DM + 'hydralazine+injection'}},
         {'field': 'Peak', 'was': 'not stated', 'now': '10 to 80 minutes',
          'why': 'The card gives an onset but not a peak, and the peak is where the danger lives: '
                 'an eight-fold spread means the same dose in two patients does two different '
                 'things at two different times.',
          'cite': {'t': 'Hydralazine hydrochloride injection', 'u': DM + 'hydralazine+injection'}}],
 'cites': [{'k': 'label', 't': 'Hydralazine hydrochloride injection', 'u': DM + 'hydralazine+injection'},
           {'k': 'trial', 't': 'Campbell 2011, IV hydralazine use is often unjustified',
            'u': 'https://pubmed.ncbi.nlm.nih.gov/21890447/'}],
},
{
 'n': 'Phentolamine', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'Alpha', 'abbr': 'ALPHA', 'clsf': 'Non-selective alpha blocker',
 'setting': 'both', 'aline': False,
 'dose': {'start': '5 mg IV (1&ndash;5 mg boluses)',
          'titr': 'repeat q10&ndash;15 min as needed',
          'max': '~15 mg. Extravasation: 5&ndash;10 mg in 10 mL saline infiltrated into the site '
                 'within 12 h'},
 'on': {'v': 0.5, 's': 'seconds', 's2': 'peak ~2 min'},
 'off': {'v': 15, 's': '~15 min', 's2': 'half-life 19 min'},
 'ctrl': 3,
 'ind': [{'t': 'Pheochromocytoma', 'full': 'The labelled indication, and the crisis drug during '
                  'tumour manipulation'},
         {'t': 'Stimulant toxicity', 'full': 'Cocaine or methamphetamine - after benzodiazepines, '
                  'which are first-line'},
         {'t': 'MAOI reaction', 'full': 'The tyramine or sympathomimetic pressor crisis'},
         {'t': 'Clonidine withdrawal', 'full': 'Though the definitive fix is restarting the '
                  'clonidine'},
         {'t': 'Vasopressor extravasation', 'full': 'The labelled dermal-necrosis indication'}],
 'avoid': [{'t': 'CAD or prior MI', 'full': 'Label contraindication - angina, coronary '
                  'insufficiency or any evidence of coronary disease'}],
 'watch': 'Rebound tachycardia, flushing, headache. Myocardial infarction and cerebrovascular spasm '
          'are in the label’s warnings.',
 'mech': 'Competitive blockade of alpha-1 and alpha-2, producing direct arterial vasodilation. It '
         'is the only agent here that addresses the actual mechanism of a catecholamine surge.',
 'fits': '<b>The card has no agent at all for catecholamine excess.</b> That is the gap this row '
         'fills. In pheochromocytoma the rule is firm: <b>alpha blockade before beta blockade</b>, '
         'because blocking beta-2 vasodilation while alpha-1 runs unopposed can send the pressure '
         'higher.',
 'src': 'add',
 'cites': [{'k': 'label', 't': 'Phentolamine mesylate for injection', 'u': DM + 'phentolamine'}],
},
{
 'n': 'Diltiazem', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'CCB', 'abbr': 'CCB', 'clsf': 'Non-dihydropyridine calcium blocker',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '0.25 mg/kg over 2 min (~20 mg)',
          'titr': '0.35 mg/kg (~25 mg) after 15 min; then 5&ndash;15 mg/h infusion',
          'max': '15 mg/h, and no longer than 24 h'},
 'on': {'v': 3, 's': '~3 min', 's2': 'peak 2&ndash;7 min'},
 'off': {'v': 420, 's': 'bolus 1&ndash;3 h', 's2': 'after a drip, median 7 h'},
 'ctrl': 1,
 'ctrlNote': 'Not a quick-off drip, whatever it looks like. After an infusion the rate effect can '
             'persist anywhere from 30 minutes to more than 10 hours, median 7.',
 'ind': [{'t': 'AF or flutter with RVR', 'full': 'The right choice when hypertension travels with a '
                  'fast rate and the ejection fraction is preserved'},
         {'t': 'Ao dissection', 'full': 'The accepted fallback for rate control when beta blockade '
                  'is contraindicated'}],
 'avoid': [{'t': 'With IV beta blockers', 'full': 'A label CONTRAINDICATION, not a caution - not '
                  'together or within a few hours'},
           {'t': 'WPW with AF', 'full': 'Label contraindication - accessory pathway'},
           {'t': 'VT or wide-complex tachycardia', 'full': 'Label contraindication - has caused '
                  'hemodynamic collapse and ventricular fibrillation'},
           {'t': 'Block or sick sinus', 'full': 'Label contraindication without a pacemaker'},
           {'t': 'Cardiogenic shock', 'full': 'Label contraindication'},
           {'t': 'Decompensated HFrEF', 'full': 'The label is softer than common teaching - caution '
                  'rather than contraindication - but the practical advice stands'}],
 'watch': 'Symptomatic hypotension in about 3% of trial patients. Hypotension, if it happens, can '
          'last as long as the rate effect.',
 'mech': 'Calcium blockade weighted toward the AV node and myocardium as well as the vasculature, '
         'so it slows the rate and lowers the pressure with one drug and no reflex tachycardia.',
 'fits': '<b>Not approved intravenously for hypertension</b> &mdash; only for rate control in '
         'atrial fibrillation and flutter, and for converting supraventricular tachycardia. Reach '
         'for it when the rate is the problem too, not for pressure alone.',
 'src': 'add',
 'cites': [{'k': 'label', 't': 'Diltiazem hydrochloride injection',
            'u': 'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=bba03666-ff4f-4bf6-fa92-78e1ec2d9073'}],
},
{
 'n': 'Metoprolol tartrate', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'BB', 'abbr': 'BB', 'clsf': 'Beta-1 selective blocker',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '5 mg over 2 min',
          'titr': 'repeat at 2 min intervals in the labelled infarct regimen; 5&ndash;15 mg '
                  'q5&ndash;15 min is what is used for pressure',
          'max': '15 mg in the labelled regimen; no stated ceiling for hypertension, because '
                 'hypertension is not an approved intravenous indication'},
 'on': {'v': 12, 's': '5&ndash;20 min', 's2': 'max blockade ~20 min', 'soft': True,
        'note': 'The label states no onset of action, only that maximum beta blockade came at about '
                '20 minutes when infused over 10 minutes. The 5-20 minute figure is from the '
                'critical-care literature.'},
 'off': {'v': 240, 's': '2&ndash;6 h', 's2': 'half-life 3&ndash;7 h', 'soft': True,
         'note': 'The label states no duration of effect.'},
 'ctrl': 1,
 'ctrlNote': 'Slower on, slower off and less selective control than esmolol at the same job. '
             'Critical-care references say it is often avoided for blood pressure for exactly this '
             'reason.',
 'ind': [{'t': 'Rate control', 'full': 'Where the tachycardia is the real target'},
         {'t': 'ACS', 'full': 'The labelled indication is acute myocardial infarction in a '
                  'hemodynamically stable patient'}],
 'avoid': [{'t': 'Decompensated HF', 'full': 'COMMIT found early IV metoprolol caused more '
                  'cardiogenic shock, concentrated in Killip II-III and hypotensive patients'},
           {'t': 'Bradycardia or block', 'full': 'Label contraindication'},
           {'t': 'Cardiogenic shock', 'full': 'Label contraindication'},
           {'t': 'With IV diltiazem', 'full': 'The diltiazem label contraindicates the combination'}],
 'watch': 'It is the reflex drug on every floor and it is <b>off-label for pressure</b>.',
 'mech': 'Beta-1 selective, so no vasodilation at all &mdash; pressure falls only through reduced '
         'cardiac output.',
 'fits': 'The label’s own pharmacodynamic data are the argument against it: intravenous then '
         'oral metoprolol reduced heart rate, systolic pressure and cardiac output, while '
         '<b>diastolic pressure and stroke volume stayed unchanged</b>. When you push it for a '
         'pressure of 190/110, the 110 is the part it does not move.',
 'practical': '<b>Be precise about what the guidelines actually say.</b> No guideline states that '
              'intravenous metoprolol should not be used for blood pressure. The case against it is '
              '<em>omission</em>: it appears in none of the hypertensive-emergency drug tables in '
              'the 2017 or 2025 hypertension guidelines, and the word does not appear once in the '
              '2024 acute-care statement. Those tables have listed esmolol and labetalol as the beta '
              'blockers since 2017. The one affirmative prohibition that exists is narrower: the '
              '2014 NSTE-ACS guideline makes intravenous beta blockade <b>Class III: Harm</b> in '
              'patients with risk factors for shock &mdash; over 70, heart rate above 110, systolic '
              'under 120, or late presentation.',
 'src': 'add',
 'cites': [{'k': 'label', 't': 'Metoprolol tartrate injection',
            'u': 'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=7c1f998a-233d-4feb-6ea2-457702abd0d2'},
           {'k': 'trial', 't': 'COMMIT/CCS-2, Lancet 2005 - 11 more cardiogenic shocks per 1000, concentrated in the first 24-48 h', 'u': 'https://pubmed.ncbi.nlm.nih.gov/16271643/'},
           {'k': 'source', 't': '2014 AHA/ACC NSTE-ACS guideline - Class III: Harm for IV beta blockade with risk factors for shock', 'u': 'https://www.ahajournals.org/doi/10.1161/CIR.0000000000000134'}],
},
{
 'n': 'Enalaprilat', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'ACEi', 'abbr': 'ACEI', 'clsf': 'ACE inhibitor, the only intravenous one',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '1.25 mg over 5 min q6h',
          'titr': '0.625 mg if on a diuretic or CrCl &le;30, may repeat after 1 h',
          'max': '5 mg q6h'},
 'on': {'v': 15, 's': '~15 min', 's2': 'peak up to 4 h'},
 'off': {'v': 720, 's': '6 h labelled', 's2': '12&ndash;24 h in practice', 'soft': True,
         'note': 'The label says about six hours and that duration is dose-related; the '
                 'critical-care literature puts a single bolus at 12-24 hours.'},
 'ctrl': 0,
 'ctrlNote': 'Onset at 15 minutes but a peak up to four hours away, so you cannot see what a dose '
             'did before the next decision. And the size of the response depends on the '
             'patient’s renin state, which you do not know.',
 'ind': [{'t': 'Listed to be recognised', 'full': 'It appears in stroke guidelines as an option, but '
                  'it is not a titration agent'}],
 'avoid': [{'t': 'Pregnancy', 'full': 'BOXED WARNING - fetal injury and death in the second and '
                  'third trimesters'},
           {'t': 'AKI', 'full': 'Efferent arteriolar dilation drops filtration pressure further'},
           {'t': 'Volume depletion', 'full': 'A high-renin patient can drop precipitously'},
           {'t': 'Hyperkalemia', 'full': 'As for any ACE inhibitor'},
           {'t': 'As a titration agent', 'full': 'The combination of a four-hour peak and a '
                  'half-day duration means there is no way to walk a dose back'}],
 'watch': 'Potassium and creatinine.',
 'src': 'add',
 'fits': 'Included so it can be recognised and declined. The card omits it, which is defensible; '
         'knowing <em>why</em> it is omitted is more useful than not knowing it exists.',
 'cites': [{'k': 'label', 't': 'Enalaprilat injection', 'u': DM + 'enalaprilat'}],
},
{
 'n': 'Furosemide', 'route': 'iv', 'routeAbbr': 'IV',
 'cls': 'Diuretic', 'abbr': 'DIUR', 'clsf': 'Loop diuretic',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '40 mg IV over 1&ndash;2 min in acute pulmonary edema',
          'titr': '80 mg if nothing happens within an hour',
          'max': 'no adult ceiling stated; high-dose therapy at no more than 4 mg/min'},
 'on': {'v': 5, 's': '&lt;5 min', 's2': 'peak within 30 min'},
 'off': {'v': 120, 's': '~2 h'},
 'ctrl': 1,
 'ind': [{'t': 'Volume overload', 'full': 'Genuinely fluid-overloaded acute pulmonary edema'},
         {'t': 'CKD with volume', 'full': 'Where a thiazide has stopped working'}],
 'avoid': [{'t': 'SCAPE', 'full': 'Sympathetic crashing acute pulmonary edema is volume '
                  'REDISTRIBUTED, not volume overloaded - diuresis is not the primary move and '
                  'must not delay nitrates and positive pressure'},
           {'t': 'Anuria', 'full': 'Label contraindication'},
           {'t': 'Same line as labetalol', 'full': 'Furosemide is alkaline at pH 9 and precipitates '
                  'with acidic drugs - the label names labetalol specifically'}],
 'watch': 'Electrolytes. Ototoxicity with rapid injection, high doses, or alongside aminoglycosides.',
 'src': 'add',
 'fits': 'An <b>adjunct</b>, not a hypertensive-emergency agent, and included mainly so the SCAPE '
         'caveat has somewhere to live. Like metoprolol and diltiazem, it is <b>not approved '
         'intravenously for hypertension</b> &mdash; its own label reserves that indication for the '
         'oral form.',
 'cites': [{'k': 'label', 't': 'Furosemide injection',
            'u': 'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=aaced7a8-c3d7-4d66-8c07-aa407b8b3f35'}],
},
# ---------------------------------------------------------------- topical ----
{
 'n': 'Nitroglycerin ointment', 'brand': '2% paste', 'route': 'top', 'routeAbbr': 'TOP',
 'cls': 'Nitro', 'abbr': 'NITRO', 'clsf': 'Nitric oxide donor, mainly venous',
 'setting': 'floor', 'aline': False,
 'dose': {'start': '&frac12; inch (7.5 mg)',
          'titr': 'may double to 1 inch and again to 2 inches',
          'max': 'two doses a day, with a 10&ndash;12 h nitrate-free interval'},
 'on': {'v': 30, 's': '~30 min', 'soft': True,
        'note': 'The label states no onset figure and says explicitly that transdermal onset is not '
                'rapid enough to abort an acute anginal attack. Treat ~30 minutes as practice, not '
                'as a labelled number.'},
 'off': {'v': 420, 's': 'up to 7 h'},
 'ctrl': 1,
 'ctrlNote': 'Its one real virtue on a floor: if the pressure falls too far you can <b>wipe it '
             'off</b>. Nothing else here can be withdrawn by hand.',
 'ind': [{'t': 'Floor bridge', 'full': 'The card lists nitro paste or patch as usable on the floor '
                  'while an oral agent is arranged'},
         {'t': 'Autonomic dysreflexia', 'full': 'Applied above the level of injury, precisely '
                  'because it can be removed'}],
 'avoid': [{'t': 'PDE5 inhibitor', 'full': 'Same windows as any nitrate - 12 h avanafil, 24 h '
                  'sildenafil or vardenafil, 48 h tadalafil'},
           {'t': 'RV infarction', 'full': 'Preload-dependent'},
           {'t': 'Poor perfusion', 'full': 'Absorption through cold, clamped-down or oedematous '
                  'skin is unreliable'}],
 'watch': 'Headache. Tolerance without the nitrate-free interval.',
 'src': 'wb',
 'fits': 'Off-label for hypertension &mdash; the ointment is approved only for preventing angina. '
         'The card names it without a dose; these are the label’s.',
 'cites': [{'k': 'label', 't': 'Nitroglycerin ointment 2%',
            'u': 'https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=e464e9bb-48e8-4b9f-9fff-e220cfbac0c5'}],
},
]
