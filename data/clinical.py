"""Clinical layer: US dosing, notable adverse effects, dose-form preferences.

Dosing is grounded in current FDA prescribing information (DailyMed) with the
actual marketed strengths from RxNorm's prescribable set. Adverse effects are
deliberately short - "what you counsel and watch for", not a label dump.
"""

# ---------------------------------------------------------------- dosing
# Total mg per DAY used for hypertension in US practice, ascending.
DOSING = {
    'amiloride':           dict(doses=[5, 10], form='IR', freq='once daily',
                                note='Add-on to a thiazide to limit hypokalemia; minimally effective alone.'),
    'amlodipine':          dict(doses=[2.5, 5, 10], form='IR', freq='once daily',
                                note='Start 5 mg; 2.5 mg if frail, elderly, or hepatic impairment.'),
    'atenolol':            dict(doses=[25, 50, 100], form='IR', freq='once daily',
                                note='No added effect above 100 mg/d. Cap 50 mg/d if CrCl 15-35.'),
    'azilsartan':          dict(doses=[40, 80], form='IR', freq='once daily',
                                note='Target 80 mg; start 40 mg if on high-dose diuretics.'),
    'benazepril':          dict(doses=[5, 10, 20, 40], form='IR', freq='once daily',
                                note='Start 10 mg, or 5 mg on a diuretic or if GFR <30.'),
    'betaxolol':           dict(doses=[5, 10, 20], form='IR', freq='once daily',
                                note='Above 20 mg/d adds no significant BP effect. Thin US market.'),
    'bisoprolol':          dict(doses=[2.5, 5, 10, 20], form='IR', freq='once daily',
                                note='Start 2.5 mg if CrCl <40 or bronchospastic disease.'),
    'candesartan':         dict(doses=[4, 8, 16, 32], form='IR', freq='once daily',
                                note='Start 16 mg as monotherapy; full effect at 4-6 weeks.'),
    'captopril':           dict(doses=[25, 50, 100, 150, 300], form='IR', freq='2-3x daily',
                                note='Obsolete for chronic HTN - BID-TID dosing, take 1 h before meals.'),
    'carvedilol':          dict(doses=[12.5, 25, 50], form='IR', freq='twice daily',
                                note='HTN max is 50 mg/d - lower than the heart-failure target. Take with food.'),
    'chlorthalidone':      dict(doses=[12.5, 25, 50], form='IR', freq='once daily',
                                note='Practice starts at 12.5 mg; adverse effects are dose-related above 25.'),
    'diltiazem':           dict(doses=[120, 180, 240, 360, 480], form='ER', freq='once daily (ER)',
                                note='ER only - IR diltiazem is not indicated for hypertension.'),
    'enalapril':           dict(doses=[5, 10, 20, 40], form='IR', freq='once-twice daily',
                                note='Split to BID rather than exceeding 40 mg/d.'),
    'eplerenone':          dict(doses=[25, 50, 100], form='IR', freq='once-twice daily',
                                note='Halve the dose with verapamil or diltiazem (CYP3A4).'),
    'felodipine':          dict(doses=[2.5, 5, 10], form='ER', freq='once daily (ER)',
                                note='ER only. Swallow whole; grapefruit doubles levels.'),
    'fosinopril':          dict(doses=[10, 20, 40, 80], form='IR', freq='once daily',
                                note='Dual hepatic/renal clearance - the ACE inhibitor needing no renal adjustment.'),
    'furosemide':          dict(doses=[20, 40, 80, 160], form='IR', freq='twice daily',
                                note='Not first-line. Must be BID - about 6 h duration.'),
    'hydrochlorothiazide': dict(doses=[12.5, 25, 50], form='IR', freq='once daily',
                                note='Shorter-acting and less potent than chlorthalidone mg-for-mg.'),
    'indapamide':          dict(doses=[1.25, 2.5, 5], form='IR', freq='once daily (morning)',
                                note='Add a second agent rather than going to 5 mg.'),
    'irbesartan':          dict(doses=[75, 150, 300], form='IR', freq='once daily',
                                note='Start 75 mg if volume- or salt-depleted.'),
    'isradipine':          dict(doses=[5, 10, 20], form='IR', freq='twice daily',
                                note='IR capsules only - the once-daily CR tablet is discontinued.'),
    'lisinopril':          dict(doses=[5, 10, 20, 40], form='IR', freq='once daily',
                                note='Halve the starting dose if CrCl 10-30.'),
    'losartan':            dict(doses=[25, 50, 100], form='IR', freq='once-twice daily',
                                note='Shortest-acting ARB - 50 mg BID often beats 100 mg once daily at trough.'),
    'metoprolol':          dict(doses=[25, 50, 100, 200], form='ER', freq='once daily (succinate ER)',
                                note='Succinate ER once daily; tartrate must be BID for 24 h coverage.'),
    'nebivolol':           dict(doses=[2.5, 5, 10, 20, 40], form='IR', freq='once daily',
                                note='Start 2.5 mg if CrCl <30 or moderate hepatic impairment.'),
    'nicardipine':         dict(doses=[60, 90, 120], form='IR', freq='three times daily',
                                note='Oral IR only - Cardene SR discontinued. Impractical for chronic HTN.'),
    'nifedipine':          dict(doses=[30, 60, 90], form='ER', freq='once daily (ER only)',
                                note='ER only. IR nifedipine is not approved for hypertension.'),
    'nisoldipine':         dict(doses=[8.5, 17, 25.5, 34], form='ER', freq='once daily (ER)',
                                note='Geomatrix strengths are NOT interchangeable with the old 10/20/30/40 mg.'),
    'olmesartan':          dict(doses=[5, 20, 40], form='IR', freq='once daily',
                                note='Twice-daily dosing offers no advantage over the same total once daily.'),
    'perindopril':         dict(doses=[2, 4, 8, 16], form='IR', freq='once daily',
                                note='Levels roughly double over age 70 - start low. Sole-source in the US.'),
    'propranolol':         dict(doses=[80, 120, 160, 240], form='ER', freq='once daily (LA)',
                                note='Rarely first-line; chosen when tremor or migraine coexists.'),
    'ramipril':            dict(doses=[2.5, 5, 10, 20], form='IR', freq='once-twice daily',
                                note='Start 1.25 mg on a diuretic; cap 5 mg/d in renal impairment.'),
    'spironolactone':      dict(doses=[12.5, 25, 50, 100], form='IR', freq='once daily',
                                note='Fourth-line agent of choice for resistant HTN (PATHWAY-2).'),
    'telmisartan':         dict(doses=[20, 40, 80], form='IR', freq='once daily',
                                note='Longest ARB half-life (~24 h) - best trough coverage.'),
    'trandolapril':        dict(doses=[1, 2, 4, 8], form='IR', freq='once daily',
                                note='Start 2 mg in Black patients. Longest ACE inhibitor half-life.'),
    'valsartan':           dict(doses=[40, 80, 160, 320], form='IR', freq='once daily',
                                note='Once daily for HTN, unlike the BID dosing used in HF and post-MI.'),
    'verapamil':           dict(doses=[120, 180, 240, 360, 480], form='ER', freq='once daily (ER)',
                                note='ER only for HTN. Moderate CYP3A4 inhibitor.'),
}

# Marketed in the US but not realistically prescribed for chronic hypertension:
# both lost their once-daily formulation, leaving BID/TID dosing.
RARE_IN_PRACTICE = {
    'isradipine',    # IR capsules twice daily; DynaCirc CR discontinued
    'nicardipine',   # IR capsules three times daily; Cardene SR discontinued
}

# In the efficacy model but not part of routine US hypertension practice.
NOT_US_PRACTICE = {
    'barnidipine', 'lercanidipine', 'manidipine', 'nitrendipine', 'cilazapril', 'delapril',
    'spirapril', 'fimasartan', 'bendrofluazide', 'cyclopenthiazide', 'celiprolol',
    'oxprenolol', 'eprosartan', 'penbutolol', 'moexipril',
    # Quinapril: FDA-listed shortage since 2023, effectively single-source, brand
    # discontinued, and zero NDCs in the current CMS NADAC file.
    'quinapril',
}

# ---------------------------------------------------------------- adverse effects
ACEI = dict(
    common=['Dry cough (~11% pooled; label rates 0.5-35% are not comparable)',
            'Hyperkalemia', 'Creatinine rise - up to 30% is acceptable'],
    important=['Angioedema, including fatal cases; higher risk in Black patients',
               'Boxed warning: fetal toxicity - stop as soon as pregnancy is detected'],
    monitoring='K+ and creatinine 1-2 weeks after start or titration', cls=True)
ARB = dict(
    common=['Hyperkalemia', 'Dizziness', 'Cough near placebo rate (2-3% vs ~11% for ACEi)'],
    important=['Boxed warning: fetal toxicity - stop as soon as pregnancy is detected',
               'Angioedema (postmarketing only); may start 6 wks after ACEi angioedema'],
    monitoring='K+ and creatinine 1-2 weeks after start or titration', cls=True)
BB_SEL = dict(
    common=['Bradycardia', 'Fatigue', 'Cold extremities'],
    important=['Never stop abruptly - rebound angina and MI (not a boxed warning)',
               'Masks hypoglycemia; beta-1 selectivity is lost at higher doses',
               'Not first-line unless coronary disease or heart failure'],
    monitoring='Heart rate', cls=True)
BB_NONSEL = dict(
    common=['Bradycardia', 'Fatigue'],
    important=['Nonselective - avoid in asthma and reactive airway disease',
               'Never stop abruptly - rebound angina and MI',
               'Not first-line unless coronary disease or heart failure'],
    monitoring='Heart rate', cls=True)
DHP = dict(
    common=['Dose-dependent peripheral edema', 'Headache, flushing, palpitations'],
    important=['Edema responds to adding an ACEi/ARB, not to a diuretic',
               'Gingival hyperplasia (under 1%)'],
    monitoring=None, cls=True)
NONDHP = dict(
    common=['Bradycardia', 'First-degree AV block'],
    important=['Do not use in HFrEF - negative inotrope',
               'Avoid routine use with a beta blocker (bradycardia, heart block)',
               'CYP3A4 inhibitor - limit simvastatin, watch digoxin'],
    monitoring='Heart rate; ECG if combined with other rate-slowing drugs', cls=True)
THIAZIDE = dict(
    common=['Hypokalemia', 'Hyperuricemia and gout', 'Hyperglycemia'],
    important=['Hyponatremia, especially in older women',
               'Sulfonamide-related rash and photosensitivity'],
    monitoring='Na+, K+, creatinine, uric acid, glucose, calcium', cls=True)
MRA = dict(
    common=['Hyperkalemia'],
    important=['Avoid if eGFR under 45 or K+ above 5.0',
               'Preferred fourth agent for resistant hypertension (PATHWAY-2)'],
    monitoring='K+ and creatinine at baseline, 1 week, and 1 month', cls=True)

AE = {d: dict(ACEI) for d in ['benazepril', 'captopril', 'enalapril', 'fosinopril',
                              'lisinopril', 'perindopril', 'ramipril', 'trandolapril']}
AE.update({d: dict(ARB) for d in ['azilsartan', 'candesartan', 'irbesartan', 'losartan',
                                  'olmesartan', 'telmisartan', 'valsartan']})
AE.update({d: dict(BB_SEL) for d in ['atenolol', 'betaxolol', 'bisoprolol', 'metoprolol', 'nebivolol']})
AE.update({d: dict(BB_NONSEL) for d in ['propranolol', 'carvedilol']})
AE.update({d: dict(DHP) for d in ['amlodipine', 'felodipine', 'isradipine', 'nicardipine',
                                  'nifedipine', 'nisoldipine']})
AE.update({d: dict(NONDHP) for d in ['diltiazem', 'verapamil']})
AE.update({d: dict(THIAZIDE) for d in ['hydrochlorothiazide', 'chlorthalidone', 'indapamide']})
AE.update({d: dict(MRA) for d in ['spironolactone', 'eplerenone', 'amiloride']})

# Drug-specific facts layered on the class defaults. Every figure here was read
# from a current FDA label or the cited trial.
SPECIFIC = {
    'captopril':      dict(add_common=['Rash 4-7%, metallic taste 2-4%'],
                           add_important=['Neutropenia 3.7% with connective tissue disease plus renal impairment']),
    'enalapril':      dict(add_important=['Intestinal angioedema - abdominal pain without swelling']),
    'fosinopril':     dict(add_common=['No renal dose adjustment needed']),
    'perindopril':    dict(add_common=['Levels roughly double over age 70']),
    'trandolapril':   dict(add_common=['Longest half-life of the ACE inhibitors (22.5 h)']),
    'losartan':       dict(add_common=['Mild uricosuric effect - lowers urate (Hyzaar label)']),
    'olmesartan':     dict(add_important=['Sprue-like enteropathy - chronic diarrhea and weight loss, months to years in']),
    'telmisartan':    dict(add_important=['Raises digoxin peak ~49% - monitor levels']),
    'irbesartan':     dict(add_important=['K+ above 6 in 18.6% in the diabetic nephropathy trial']),
    'atenolol':       dict(add_important=['Renally cleared - cap 50 mg/d if CrCl 15-35',
                                          'Avoid in pregnancy - fetal growth restriction']),
    'bisoprolol':     dict(add_common=['Beta-2 blockade appears at 20 mg and above']),
    'metoprolol':     dict(add_common=['CYP2D6 poor metabolizers lose cardioselectivity']),
    'nebivolol':      dict(add_common=['Vasodilatory; the nitric-oxide mechanism is not in the FDA label']),
    'betaxolol':      dict(add_common=['Use 5-10 mg if bronchospastic disease is unavoidable']),
    'propranolol':    dict(add_common=['Vivid dreams and insomnia - crosses the blood-brain barrier'],
                           add_important=['Asthma is an outright contraindication']),
    'carvedilol':     dict(add_common=['Postural hypotension 9.7%, syncope 3.4% during titration'],
                           add_important=['Worsens hyperglycemia in heart failure with diabetes',
                                          'Intraoperative floppy iris - do NOT stop before cataract surgery']),
    'amlodipine':     dict(add_common=['Edema 1.8% at 2.5 mg rising to 10.8% at 10 mg',
                                       'Edema 14.6% in women vs 5.6% in men']),
    'felodipine':     dict(add_common=['Edema 10% (under 50 y, 5 mg) to 30% (over 60 y, 20 mg)'],
                           add_important=['Grapefruit roughly doubles bioavailability']),
    'nisoldipine':    dict(add_common=['Edema 7% at 8.5 mg rising to 27% at 34 mg'],
                           add_important=['Do not take with grapefruit; take on an empty stomach']),
    'nifedipine':     dict(add_important=['Extended-release only - IR is not approved for hypertension',
                                          'Avoid IR within 1-2 weeks of MI or in acute coronary syndrome']),
    'isradipine':     dict(add_important=['IR capsules twice daily only - the CR tablet is discontinued']),
    'nicardipine':    dict(add_important=['Increased angina in 7% vs 4% on placebo',
                                          'Oral IR three times daily only - SR discontinued']),
    'verapamil':      dict(add_common=['Constipation 7.3% - the usual dose-limiting effect'],
                           add_important=['Contraindicated if EF under 30%', 'Raises digoxin 50-75%']),
    'diltiazem':      dict(add_common=['Peripheral edema; less constipation than verapamil'],
                           add_important=['Raises carbamazepine 40-72%']),
    'hydrochlorothiazide': dict(add_important=['Squamous cell skin cancer with cumulative dose (FDA 2020) - counsel sun protection',
                                               'Acute myopia and angle-closure glaucoma']),
    'chlorthalidone': dict(add_common=['More hypokalemia than HCTZ (6.0% vs 4.4%)'],
                           add_important=['The 2025 guideline dropped its preference - no MACE benefit over HCTZ']),
    'indapamide':     dict(add_common=['Hypokalemia 20% at 1.25 mg rising to 61% at 5 mg'],
                           add_important=['Start at 1.25 mg - hyponatremia and hypokalemia are dose-related']),
    'spironolactone': dict(add_common=['Gynecomastia ~9% of men in RALES (mean 26 mg/d)',
                                       'Menstrual irregularity, breast tenderness'],
                           add_important=['Hypocalcemia - the opposite direction from thiazides']),
    'eplerenone':     dict(add_common=['Gynecomastia reported, but no rate in the label and no head-to-head with spironolactone'],
                           add_important=['Contraindicated if K+ above 5.5 or CrCl 30 or less',
                                          'Often needs twice-daily dosing for adequate BP lowering']),
    'amiloride':      dict(add_common=['Hyperkalemia ~10% alone, 1-2% combined with a thiazide'],
                           add_important=['Boxed warning: hyperkalemia, which can be fatal',
                                          'Minimally effective alone - an add-on to a thiazide']),
    'furosemide':     dict(common=['Hypokalemia', 'Volume depletion and orthostasis', 'Hypomagnesemia'],
                           important=['Boxed warning: profound diuresis with electrolyte depletion',
                                      'Ototoxicity with rapid IV, high dose, CKD, or aminoglycosides',
                                      'Not first-line unless eGFR under 30 or heart failure'],
                           monitoring='K+, Na+, Mg, creatinine, volume status', cls=False),
}
AE['furosemide'] = dict(common=[], important=[], monitoring=None, cls=False)

for name, spec in SPECIFIC.items():
    rec = AE.setdefault(name, dict(common=[], important=[], monitoring=None, cls=True))
    for k in ('common', 'important', 'monitoring'):
        if k in spec:
            rec[k] = spec[k]
    rec['common'] = list(rec.get('common', [])) + spec.get('add_common', [])
    rec['important'] = list(rec.get('important', [])) + spec.get('add_important', [])
    if 'cls' in spec:
        rec['cls'] = spec['cls']
    elif spec.get('add_common') or spec.get('add_important'):
        rec['cls'] = False

SOURCES = {
    'dosing': ('FDA prescribing information via DailyMed, with marketed strengths from the '
               'RxNorm prescribable set. Total daily dose for hypertension.'),
    'ae': ('FDA prescribing information via DailyMed, plus the 2017 and 2025 ACC/AHA '
           'hypertension guideline drug tables. Incidence figures are label figures except: '
           'ACE inhibitor cough (Bangalore, Am J Med 2010, pooled ~11%), chlorthalidone vs '
           'hydrochlorothiazide hypokalemia (Diuretic Comparison Project, NEJM 2022), and '
           'olmesartan enteropathy (FDA Drug Safety Communication, July 2013, and the Benicar '
           'label section 5.5). Amiloride and furosemide boxed warnings were read from the SPL XML.'),
    'cost': ('CMS National Average Drug Acquisition Cost (NADAC), file dated 26 August 2026. '
             'Median generic price per unit, cheapest whole-tablet regimen delivering the '
             'daily dose, times 30 days.'),
}
