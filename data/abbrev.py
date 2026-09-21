# -*- coding: utf-8 -*-
"""The abbreviation pass applied to the outpatient text (ward shorthand).

Kept in the repo so the substitution list is reviewable and the pass is
repeatable. Deliberately NOT applied to the How it works tab, which is the
provenance record and needs to stay readable.

A conservative, reviewable abbreviation pass.

Only substitutions whose meaning cannot change with context. Nothing here
touches a number, a drug name, or anything inside an HTML tag.
"""
import re

SUBS = [
 (r'\bblood pressure\b', 'BP'), (r'\bBlood pressure\b', 'BP'),
 (r'\bhypertension\b', 'HTN'), (r'\bHypertension\b', 'HTN'),
 (r'\bheart failure\b', 'HF'), (r'\bHeart failure\b', 'HF'),
 (r'\bchronic kidney disease\b', 'CKD'),
 (r'\bmyocardial infarction\b', 'MI'),
 (r'\bacute coronary syndrome\b', 'ACS'),
 (r'\bcoronary artery disease\b', 'CAD'),
 (r'\bejection fraction\b', 'EF'),
 (r'\bpatients\b', 'pts'), (r'\bPatients\b', 'Pts'),
 (r'\bpatient\b', 'pt'),
 (r'\bcompared with\b', 'vs'), (r'\bcompared to\b', 'vs'), (r'\bversus\b', 'vs'),
 (r'\bis associated with\b', 'a/w'), (r'\bare associated with\b', 'a/w'),
 (r'\bassociated with\b', 'a/w'),
 (r'\bdiscontinuation\b', 'd/c'), (r'\bdiscontinued\b', 'd/c'),
 (r'\bapproximately\b', '~'), (r'\bAbout\b', '~'), (r'\babout\b', '~'),
 (r'\bgreater than\b', '&gt;'), (r'\bless than\b', '&lt;'),
 (r'\btwice daily\b', 'BID'), (r'\bthree times daily\b', 'TID'),
 (r'\bfour times daily\b', 'QID'), (r'\bonce daily\b', 'daily'),
 (r'\badverse effects\b', 'AEs'), (r'\badverse effect\b', 'AE'),
 (r'\bBoxed warning\b', 'BOXED'), (r'\bboxed warning\b', 'BOXED'),
 (r'\bwithout\b', 'w/o'), (r' with ', ' w/ '),
 (r'\bbecause of\b', '2/2'), (r'\bbecause\b', 'b/c'),
 (r'\bhistory of\b', 'h/o'),
 (r'\bweeks\b', 'wk'), (r'\bweek\b', 'wk'),
 (r'\bmonths\b', 'mo'), (r'\bmonth\b', 'mo'),
 (r'\bhours\b', 'h'), (r'\bhour\b', 'h'),
 (r'\bminutes\b', 'min'), (r'\bminute\b', 'min'),
 (r'\bmilligram\b', 'mg'), (r'\bmilligrams\b', 'mg'),
 (r'\bintravenous\b', 'IV'), (r'\bintravenously\b', 'IV'),
 (r'\bcontraindicated\b', 'contraindic'),
 (r'\bhyperkalemia\b', '↑K'), (r'\bHyperkalemia\b', '↑K'),
 (r'\bhypokalemia\b', '↓K'), (r'\bHypokalemia\b', '↓K'),
 (r'\bhyponatremia\b', '↓Na'), (r'\bhyperuricemia\b', '↑urate'),
 (r'\bpregnancy\b', 'preg'),
]


# repeated boilerplate that appears dozens of times verbatim
PHRASES = [
 (r'Fetal toxicity - stop before or as soon as pregnancy is confirmed', 'Fetal tox — stop once preg confirmed'),
 (r'Fetal toxicity – stop before or as soon as pregnancy is confirmed', 'Fetal tox — stop once preg confirmed'),
 (r'Efferent arteriolar dilation causes acute kidney injury', 'Efferent dilation → AKI'),
 (r'\bacute kidney injury\b', 'AKI'),
 (r'\bHyperkalaemia\b', '↑K'), (r'\bhyperkalaemia\b', '↑K'),
 (r'\bHypokalaemia\b', '↓K'), (r'\bhypokalaemia\b', '↓K'),
 (r'\bHyponatraemia\b', '↓Na'), (r'\bhyponatraemia\b', '↓Na'),
 (r'\bhyperuricaemia\b', '↑urate'),
 (r'\bbradycardia\b', 'brady'), (r'\btachycardia\b', 'tachy'),
 (r'\bhypotension\b', 'hypoTN'), (r'\bHypotension\b', 'HypoTN'),
 (r'\bdose-related\b', 'dose-rel'),
 (r'\bcontraindication\b', 'contraindic'),
 (r'\brenal impairment\b', 'renal impair'),
 (r'\bhepatic impairment\b', 'hepatic impair'),
 (r'\bin combination with\b', 'w/'),
 (r'\bat the same time as\b', 'w/'),
 (r'\bthere is no\b', 'no'),
 (r'\bthere are no\b', 'no'),
 (r'\bin order to\b', 'to'),
 (r'\bas well as\b', '+'),
 (r'\bmore likely to\b', 'more likely'),
 (r'\bshould be\b', ''),
 (r'\bhas been shown to\b', ''),
]
SUBS = SUBS + PHRASES

def shorten(text):
    """Substitute only in text nodes, never inside a tag."""
    if not isinstance(text, str) or not text.strip():
        return text
    out = []
    for part in re.split(r'(<[^>]+>)', text):
        if part.startswith('<'):
            out.append(part); continue
        for pat, rep in SUBS:
            part = re.sub(pat, rep, part)
        part = re.sub(r'\s{2,}', ' ', part)
        out.append(part)
    return ''.join(out)
