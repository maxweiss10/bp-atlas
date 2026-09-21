# -*- coding: utf-8 -*-
"""The inpatient / hypertensive-emergency layer, assembled.

A closed compartment.  Nothing here is read by the efficacy model and nothing
in model.json is read by this, because the Wang meta-analysis describes chronic
oral monotherapy and has no coefficient for a titrated infusion: putting an
esmolol drip in the same ranking as amlodipine 5 mg would imply a comparison
that does not exist.

Provenance marks, carried by every agent and every condition row:

  wb   on the White Book card, checked against the primary source, unchanged
  fix  on the card, but at least one figure is corrected here; `fix` holds the
       original, the replacement, and the source that settles it
  add  not on the card, added here

Run `python3 build_inpatient.py` to embed the result in index.html.
"""
from ip_text import LEDE, DEFS, EOD, EOD_NOTE, ASSESS, TOP_NOTES, DZ_NOTES, NOTES
from ip_conds import CONDS
from ip_agents import AGENTS

INPATIENT = {
    'lede': LEDE,
    'defs': DEFS,
    'eod': EOD,
    'eodNote': EOD_NOTE,
    'assess': ASSESS,
    'topNotes': TOP_NOTES,
    'conds': CONDS,
    'dzNotes': DZ_NOTES,
    'agents': AGENTS,
    'notes': NOTES,
}
