"""Plain-language content for the patient handout, and comorbidity rules.

Written at roughly a 6th-grade reading level. Every clinical fact traces to the
same audited sources as the clinician-facing strings in clinical.py; only the
wording changes.
"""

# ---- what the patient reads, by class -------------------------------------
CLASS_TEXT = {
    'ACEi': dict(
        what='Relaxes your blood vessels by blocking a hormone that tightens them.',
        common=['A dry, tickly cough that will not go away (about 1 in 9 people)',
                'Feeling lightheaded, especially standing up quickly'],
        call=['Swelling of the lips, tongue, or throat, or trouble breathing - '
              'go to an emergency room, do not wait'],
        rules=['Tell us straight away if you are pregnant or planning to be - '
               'this medicine can harm a baby.',
               'We will check a blood test 1 to 2 weeks after you start or change the dose.',
               'Avoid salt substitutes - most of them are potassium.']),
    'ARB': dict(
        what='Relaxes your blood vessels by blocking a hormone that tightens them. '
             'Works like an ACE inhibitor but rarely causes a cough.',
        common=['Feeling lightheaded, especially standing up quickly'],
        call=['Swelling of the lips, tongue, or throat, or trouble breathing - '
              'go to an emergency room, do not wait'],
        rules=['Tell us straight away if you are pregnant or planning to be - '
               'this medicine can harm a baby.',
               'We will check a blood test 1 to 2 weeks after you start or change the dose.',
               'Avoid salt substitutes - most of them are potassium.']),
    'BB': dict(
        what='Slows your heart down and eases how hard it has to work.',
        common=['Feeling tired, especially in the first few weeks',
                'A slower pulse', 'Cold hands and feet', 'Vivid dreams or trouble sleeping'],
        call=['A pulse under about 50, or feeling faint',
              'New wheezing or shortness of breath'],
        rules=['Never stop this suddenly. Stopping all at once can cause chest pain '
               'or a heart attack - if you want to come off it, we will lower the dose slowly.',
               'If you have diabetes, be aware this can hide the shaky, racing-heart '
               'warning signs of a low blood sugar.']),
    'CCB-DHP': dict(
        what='Relaxes your blood vessels so blood flows through them more easily.',
        common=['Puffy ankles or feet - the higher the dose, the more likely, '
                'and more common in women', 'Headache', 'Flushing or feeling warm'],
        call=['Swelling that makes your shoes tight, or swelling in only one leg'],
        rules=['If the ankle swelling bothers you, tell us. Adding a different blood '
               'pressure medicine helps more than a water pill does.']),
    'CCB-nonDHP': dict(
        what='Slows your heart down and relaxes your blood vessels.',
        common=['Constipation', 'Feeling tired', 'A slower pulse'],
        call=['A pulse under about 50, or feeling faint'],
        rules=['Do not drink grapefruit juice with this.']),
    'thiazide': dict(
        what='A water pill. It helps your body clear extra salt and water.',
        common=['Passing urine more often, mostly in the first couple of weeks',
                'Leg cramps or muscle weakness, which can mean low potassium',
                'A gout attack, if you are prone to them',
                'Sunburning more easily than usual'],
        call=['Bad muscle cramps or weakness', 'Feeling confused or very unsteady'],
        rules=['Take it in the morning, so it does not wake you up at night.',
               'Use sunscreen and cover up. Taken for many years, these slightly raise '
               'the risk of skin cancer.',
               'We will check your blood salts a few weeks after you start.']),
    'loop': dict(
        what='A strong water pill. It helps your body clear extra salt and water.',
        common=['Passing urine a lot, starting within an hour',
                'Leg cramps or muscle weakness', 'Feeling lightheaded or dehydrated'],
        call=['Ringing in your ears or hearing changes',
              'Feeling very dizzy, or passing much less urine'],
        rules=['Take doses in the morning and early afternoon, not at night.',
               'We will check your kidneys and blood salts after you start.']),
    'MRA': dict(
        what='A water pill that also keeps your body from losing potassium.',
        common=['Breast tenderness or swelling, including in men',
                'Passing urine more often'],
        call=['Muscle weakness, a slow or irregular heartbeat, or numb or tingly '
              'fingers - these can mean your potassium is too high'],
        rules=['Avoid salt substitutes - most of them are potassium.',
               'We will check your potassium and kidneys about a week after you start, '
               'and again at a month.']),
    'kSparing': dict(
        what='A water pill that keeps your body from losing potassium.',
        common=['Passing urine more often'],
        call=['Muscle weakness, a slow or irregular heartbeat, or numb or tingly '
              'fingers - these can mean your potassium is too high'],
        rules=['Avoid salt substitutes - most of them are potassium.',
               'We will check your potassium and kidneys after you start.']),
}

# ---- drug-specific lines layered on top ------------------------------------
DRUG_TEXT = {
    'amlodipine':      dict(add_common=['Ankle swelling affects about 1 in 9 people at 10 mg, '
                                        'and about 1 in 50 at 2.5 mg']),
    'verapamil':       dict(add_common=['Constipation is common - about 7 in 100 people'],
                            add_rules=['Ask us before taking any new medicine; this one changes '
                                       'how many other drugs are handled.']),
    'losartan':        dict(add_rules=['This one also lowers uric acid, so it is a good choice '
                                       'if you get gout.']),
    'spironolactone':  dict(add_common=['About 1 in 11 men get breast tenderness or swelling; '
                                        'it usually settles if we stop or switch']),
    'hydrochlorothiazide': dict(add_rules=['Sun protection matters with this one.']),
    'chlorthalidone':  dict(add_rules=['This is longer-acting than similar water pills, so take '
                                       'it in the morning.']),
    'furosemide':      dict(add_rules=['This works fast - plan to be near a toilet for a few '
                                       'hours after each dose.']),
    'carvedilol':      dict(add_rules=['Take with food. Tell your eye surgeon you take this '
                                       'before any cataract operation.']),
    'metoprolol':      dict(add_rules=['Take with or just after food.']),
    'nisoldipine':     dict(add_rules=['Take on an empty stomach. Avoid grapefruit.']),
    'moexipril':       dict(add_rules=['Take it an hour before a meal.']),
    'propranolol':     dict(add_rules=['If you have asthma, this is not the right medicine - '
                                       'tell us.']),
    'quinapril':       dict(add_rules=['This one is hard to get at the moment. If your pharmacy '
                                       'cannot fill it, call us rather than going without.']),
}

# ---- comorbidities that should change the shortlist ------------------------
# sel: 'cls:X' matches a display class, 'sub:X' a finer subclass, plain text a drug
PROFILES = [
    # ---- cardiac ----------------------------------------------------------
    dict(id='hfref', label='Heart failure, reduced EF (\u226440%)', group='Cardiac',
         exclude=[('sub:nonDHP', 'Negative inotropes - avoid in HFrEF')],
         promote=[('carvedilol', 'One of the three beta blockers with mortality benefit'),
                  ('metoprolol', 'Succinate ER has mortality benefit in HFrEF'),
                  ('bisoprolol', 'One of the three beta blockers with mortality benefit'),
                  ('sub:MRA', 'Class 1: spironolactone or eplerenone, mortality benefit (RALES, EMPHASIS-HF)')],
         note='Treat this as heart-failure therapy, not blood-pressure therapy - the regimen is '
              'driven by mortality benefit, not mmHg.'),
    dict(id='hfpef', label='Heart failure, EF \u226540%', group='Cardiac',
         promote=[('sub:MRA', 'MRA benefit at EF \u226540% is finerenone-led (FINEARTS-HF); spironolactone cut '
                              'HF admissions in TOPCAT but its primary endpoints were neutral')],
         note='The agents that move outcomes at EF \u226540% - SGLT2 inhibitors and finerenone (FDA-approved '
              'for EF \u226540%, 2025) - are not in this model. Unlike HFrEF, verapamil and diltiazem are not '
              'contraindicated here. Decongest with a diuretic; treat the pressure to goal.'),
    dict(id='cad', label='Coronary disease or prior MI', group='Cardiac',
         promote=[('cls:BB', 'The setting where a beta blocker is genuinely first-line'),
                  ('cls:ACEi', 'Mortality benefit after MI'),
                  ('cls:ARB', 'Alternative when an ACEi is not tolerated')]),
    dict(id='afib', label='AF needing rate control', group='Cardiac',
         promote=[('cls:BB', 'Rate control and blood pressure in one drug'),
                  ('sub:nonDHP', 'Rate control and blood pressure in one drug')]),
    dict(id='brady', label='Bradycardia or AV block', group='Cardiac',
         exclude=[('cls:BB', 'Further slows the sinus node and AV conduction'),
                  ('sub:nonDHP', 'Slows AV conduction - can complete the block')],
         note='Applies to resting heart rate under about 55, or second- or third-degree block '
              'without a pacemaker.'),
    dict(id='as', label='Severe aortic stenosis', group='Cardiac',
         demote=[('sub:DHP', 'Afterload reduction against a fixed obstruction can drop cardiac output'),
                 ('sub:loop', 'Preload-dependent - aggressive diuresis causes hypotension')],
         note='Lower pressure cautiously and avoid abrupt afterload or preload reduction.'),

    # ---- renal ------------------------------------------------------------
    dict(id='ckd', label='CKD with albuminuria', group='Renal',
         promote=[('cls:ACEi', 'Slows progression - the mandatory component'),
                  ('cls:ARB', 'Slows progression - the mandatory component')],
         note='Use one RAS blocker, never two. Expect a creatinine rise of up to 30%.'),
    dict(id='hyperk', label='High potassium or advanced CKD', group='Renal',
         exclude=[('sub:MRA', 'Hyperkalaemia risk'), ('sub:kSparing', 'Hyperkalaemia risk')],
         demote=[('cls:ACEi', 'Raises potassium - monitor closely'),
                 ('cls:ARB', 'Raises potassium - monitor closely')]),
    dict(id='ras', label='Bilateral renal artery stenosis', group='Renal',
         exclude=[('cls:ACEi', 'Efferent arteriolar dilation causes acute kidney injury'),
                  ('cls:ARB', 'Efferent arteriolar dilation causes acute kidney injury')],
         note='Suspect it when creatinine jumps more than 30% after starting a RAS blocker, or with '
              'flash pulmonary oedema.'),
    dict(id='stones', label='Calcium kidney stones', group='Renal',
         promote=[('sub:thiazide', 'Reduces urinary calcium excretion and stone recurrence')]),

    # ---- metabolic --------------------------------------------------------
    dict(id='diabetes', label='Diabetes with albuminuria', group='Metabolic',
         promote=[('cls:ACEi', 'Slows nephropathy'), ('cls:ARB', 'Slows nephropathy')],
         demote=[('sub:thiazide', 'Raises glucose - a real but usually minor effect'),
                 ('cls:BB', 'Raises glucose and masks hypoglycaemia')]),
    dict(id='gout', label='Gout', group='Metabolic',
         demote=[('sub:thiazide', 'Raises urate and can trigger a flare'),
                 ('sub:loop', 'Raises urate')],
         promote=[('losartan', 'Mildly uricosuric - lowers urate')]),
    dict(id='osteoporosis', label='Osteoporosis', group='Metabolic',
         promote=[('sub:thiazide', 'Reduces urinary calcium loss')]),

    # ---- respiratory ------------------------------------------------------
    dict(id='asthma', label='Asthma', group='Respiratory',
         exclude=[('propranolol', 'Non-selective - asthma is a contraindication'),
                  ('carvedilol', 'Non-selective - avoid in reactive airways')],
         demote=[('cls:BB', 'Even beta-1 selective agents lose selectivity as the dose rises')],
         note='Propranolol and carvedilol are the only non-selective beta blockers in this model, so '
              'the exclusion list is complete.'),
    dict(id='copd', label='COPD', group='Respiratory',
         exclude=[('propranolol', 'Non-selective - avoid in obstructive airway disease'),
                  ('carvedilol', 'Non-selective - avoid in obstructive airway disease')],
         note='Unlike asthma, beta-1 selective blockers are NOT demoted here: the Cochrane review '
              'found no change in FEV1 or symptoms even in severe airflow limitation, and they '
              'should not be withheld when there is a cardiac indication.'),

    # ---- pregnancy --------------------------------------------------------
    dict(id='pregnancy', label='Pregnant or planning', group='Pregnancy',
         exclude=[('cls:ACEi', 'Fetal toxicity - stop before or as soon as pregnancy is confirmed'),
                  ('cls:ARB', 'Fetal toxicity - stop before or as soon as pregnancy is confirmed'),
                  ('spironolactone', 'Anti-androgen effects on a male fetus'),
                  ('eplerenone', 'Insufficient pregnancy data - not an anti-androgen concern'),
                  ('atenolol', 'Fetal growth restriction - the signal is atenolol-specific')],
         promote=[('nifedipine', 'ACOG first-line for chronic hypertension in pregnancy - use the ER form')],
         note='Labetalol and methyldopa are the other first-line choices but are not in this model. '
              'No class-wide beta blocker demote applies: the growth-restriction signal is specific '
              'to atenolol, and metoprolol is the usual in-model alternative.'),

    # ---- neurologic -------------------------------------------------------
    dict(id='migraine', label='Migraine', group='Neurologic',
         promote=[('propranolol', 'AAN/AHS Level A for episodic migraine prevention, and labelled for it'),
                  ('metoprolol', 'AAN/AHS Level A - the same evidence tier as propranolol'),
                  ('candesartan', 'Three positive prevention RCTs; non-inferior to propranolol 160 mg')],
         note='Verapamil is Level U for migraine - its prophylactic role is cluster headache, not '
              'migraine.'),
    dict(id='cluster', label='Cluster headache', group='Neurologic',
         promote=[('verapamil', 'First-line prophylaxis for episodic cluster headache')],
         note='High doses are usual; get an ECG before and during escalation for heart block.'),
    dict(id='tremor', label='Essential tremor', group='Neurologic',
         promote=[('propranolol', 'AAN Level A and the only one labelled for essential tremor'),
                  ('atenolol', 'AAN Level B - an option when propranolol is contraindicated')]),

    # ---- other ------------------------------------------------------------
    dict(id='angioedema', label='Prior ACEi angioedema', group='Other',
         exclude=[('cls:ACEi', 'Recurrence risk - never rechallenge')],
         note='An ARB may be started, but only about 6 weeks later, and with counselling.'),
    dict(id='raynaud', label='Raynaud phenomenon', group='Other',
         demote=[('cls:BB', 'Peripheral vasoconstriction worsens attacks')],
         promote=[('sub:DHP', 'Vasodilators; nifedipine is used to treat Raynaud itself')]),
    dict(id='cirrhosis', label='Cirrhosis with ascites', group='Other',
         promote=[('spironolactone', 'The diuretic of choice in ascites')],
         note='Hepatic clearance matters here - avoid drugs needing hepatic activation where you can.'),
    dict(id='lithium', label='On lithium', group='Other',
         demote=[('sub:thiazide', 'Raises lithium levels - toxicity risk'),
                 ('sub:loop', 'Raises lithium levels'),
                 ('cls:ACEi', 'Raises lithium levels'), ('cls:ARB', 'Raises lithium levels')],
         note='If unavoidable, check a lithium level within a week and after any dose change.'),
    dict(id='bph', label='BPH', group='Other',
         note='An alpha blocker treats both the prostate and the pressure, but no alpha blocker is '
              'in this model, so none can be ranked here.'),
    dict(id='black', label='Black adult, no CKD or HF', group='Other',
         promote=[('cls:CCB', 'More effective as initial monotherapy'),
                  ('sub:thiazide', 'More effective as initial monotherapy')],
         note='The gap largely disappears once a RAS blocker is combined with either of these.'),
]
