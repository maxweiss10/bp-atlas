# BP Atlas — session handoff

**Live:** https://maxweiss10.github.io/bp-atlas · **Clone:** `~/bp-atlas` (not under Documents —
TCC blocks it) · **Repo:** maxweiss10/bp-atlas, branch `main`

Everything below shipped in one session (16 commits, `411cd57`..`7f9861c`). Working tree clean,
local and remote in sync, GitHub Pages serving the current build.

---

## What this session added

### 1. A fourth tab: Inpatient & emergency

Reproduces a White Book cardiology card (asymptomatic markedly elevated BP / hypertensive
emergency) with every line checked against primary sources.

**Deliberately a closed compartment.** The Wang efficacy model behind the other tabs is built from
chronic oral monotherapy trials and has no coefficient for a titrated infusion, so this tab has
**no mmHg column** and shares no data with the model. Ranking an esmolol drip beside amlodipine
5 mg would imply a comparison that does not exist.

| | Count |
|---|---|
| Agents | 31 — 2 unchanged from the card, 14 corrected, 15 added |
| Conditions | 17 — 8 corrected, 9 added |
| Individual corrections | 27 |
| Use tiers | 14 first reach, 14 specific, 3 know-only |

**Use tiers** exist because Max objected to scrolling past phentolamine to reach labetalol. The
table sorts on tier first, ties on onset, and each *specific* agent states its trigger in the same
cell. A segmented control filters to one tier. IV hydralazine is deliberately tier 2, not 1 — it is
the most-ordered PRN antihypertensive and should not read as a default.

**The four shaded rows at the top of the conditions table are the defaults**, including the two
where someone else wants the number lower: **pre-procedure** (the surgeon asks) and **discharge**
(the unit will not let an asymptomatic 180s patient leave). Those two carry the evidence to hold
the line, because "do not treat" is correct and useless when someone is standing there.

### 2. Styling: the MGH housestaff manual

Matched to the White Book treatment already used on **Pearl** (maxweiss10.github.io/pearls) so the
two sites read as one system. Arial Narrow in the data zone, `#D9D9D9` small-caps section bands,
black header rows, hairline grids, `#0432FF` underlined citations.

**Dark mode was removed on purpose** — the manual is paper.

When styling another of Max's sites to the White Book, **sample Pearl's live tokens first**; he
prefers its refined take over a literal photocopy of the PDF.

### 3. Register: ward shorthand

Arrows, standard abbreviations, no articles, no linking verbs. His own example of the target:

> "Extravasation causes necrosis and blistering — large vein, never a butterfly. A lot of volume at
> high body weights" → **"Extrav→necrosis/blisters; lg vein only. ↑wt=↑vol"**

He said the first version was "SOOOO verbose" and asked for cuts four separate times. **Assume he
wants it shorter than you think.** `data/abbrev.py` holds the substitution list applied to the
outpatient text. The **How it works** tab is deliberately exempt — it is the provenance record.

### 4. Table density

Every row in the drug, combination and inpatient agent tables is **exactly one line** (26px, was
~70 outpatient and ~77 inpatient). Body text is 17.5px on 2px side padding. Every column except the
two chip columns has `width:1%`, which a table clamps up to the content width, so the chip columns
(`max-width:0`, so their content cannot widen the table, with a 150px floor so a narrow window
scrolls sideways rather than starving them) split the slack; `fitChips()` then runs
after each render — one read pass, one write pass — and hides the chips that do not fit, with a
`+n` chip that lists them in its tooltip. On a phone the cards wrap instead and it is skipped.

**Δ SBP and Δ DBP are coloured on a seven-step muted cool-to-warm ramp** (`.r0`–`.r6`: blue, teal,
green, olive, bronze, rust, brick) with **fixed mmHg cuts**, not quantiles — Δ SBP at 4/6/8/10/12/15
— so a colour always means the same number and 10 sits two steps below 15. Every step clears 5:1 on
white; weight rises with the step. Inpatient onset and offset use the same ramp (five of the seven
steps). **Max asked for more contrast between 10 and 15, then said the first attempt — a saturated
rainbow on the time, cost and evidence columns too — "hurt my eyes".** Muted, and only where it
earns its place. The Intensity (low/moderate/high) column is gone: it restated Δ SBP.

**Two bugs found on the way, both older than this session.** The open detail row inherited the
one-line `nowrap` rule and rendered as overlapping text (fixed with id-specific `tr.detail > td`
rules). The column header was `position:sticky` inside a wrapper with `overflow-x:auto`, so it stuck
to the wrapper, never the window, and was never visible while scrolling — the wrapper no longer
scrolls (the page does, sideways, on a narrow window) and the header sticks under the control rail
at `top:var(--railH)`, which a ResizeObserver keeps current. That header sliding under the rail is
almost certainly what he called "the dropdown menus overlapping".

**Default dose rung is now the maximum dose** (`state.rung = 'max'`; the localStorage key moved to
`bpatlas.v2` so his saved `all` did not override it). Minutes print as `m` everywhere in the tables
via `shortMin()`, which leaves `/min` rates alone.

**Formulation rows.** `metoprolol` in `model.json` became two entries, `metoprolol succinate` (the
old row: ER, once daily, HF-approved) and `metoprolol tartrate` (IR, BID, 50/100/200/400 mg, costed
from the 2026 NADAC API — dataset `fbb83258-11c7-47f5-8b18-5f8e79f7e704`, effective 2026-08-19,
median unit price × whole tablets: $0.96/$1.11/$1.65/$3.30 — and no HFrEF indication). Both carry
`base: 'metoprolol'`, `fdisp` (ER/IR) and `mform: 'shared'`, rendered as a dashed `model: metoprolol`
tag: the Wang appendix (p. 18) lists metoprolol once with no formulation, and its trials used both.
`fdisp` alone tags nifedipine/diltiazem/verapamil (ER) and propranolol (LA). The single-pill key is
`hydrochlorothiazide|metoprolol tartrate` only — NADAC has no succinate combination. The renderAdvice
list of HF-proven beta blockers names `metoprolol succinate`, not tartrate, on purpose.

**Inpatient rows split the same way**: `Metoprolol tartrate` and `Metoprolol succinate ER` (both PO,
tier 1), `Clonidine` and `Clonidine patch` (route `top`, tier 3), each from its own label. Hydralazine,
phentolamine and furosemide show `IV/IM` on the route chip. The Dosing column left the row for the
open row; the Subclass column prints `IP_SUB_SHORT` shorthand with the full name in the tooltip; the
notes above the tables are full width in a two-column grid; every block above the tables now goes
through `linkDrugs()` and `nitro`/`metoprolol`/`clonidine patch` are aliases. Atenolol and
nimodipine are named in the conditions table but are not agents, so they do not link.

The **Difference** column is now a short label ("More ↓K", "Sprue-like enteropathy") with a count
chip; sentences live in the open row. **Peak** and **Stopping** are their own columns — Stopping
has three states (taper / no rebound / dash), and the dash matters: a label saying nothing is not a
label saying it is safe.

---

## Build pipeline — read this before editing data

| Script | Run it when |
|---|---|
| `data/build_inpatient.py` | after editing any `ip_*.py` — embeds `INPATIENT` |
| `data/embed_model.py` | **after editing `model.json`** — embeds `PAYLOAD` only |
| `data/add_kinetics.py` | only when regenerating the kinetics layer from `kinetics.py` |

**The trap that bit once:** `model.json` edits reach the page only through an embed step. The old
`add_kinetics.py` regenerates kinetics from source first, so it would overwrite direct edits —
which is why `embed_model.py` exists. An outpatient shorthand pass was silently unused for a whole
commit before this was noticed.

**A second trap, hit three times:** `s.index('NOTES = [')` matches inside `DZ_NOTES = [`. Anchor on
line starts when editing `data/ip_text.py`.

---

## Verification record

`data/verification/` holds seven research passes with per-claim sources, plus a README naming what
could not be verified. Highlights of what changed and why:

- **ICH** was the most out-of-date row: entry band 150–220 (not 180–220), target 130 to <140 held
  ≥7 days, and SBP <130 is Class 3 Harm — the card had no floor.
- **Ischemic stroke**: 220/120 is a treatment *threshold*, not a target. The post-thrombolysis
  window and the post-thrombectomy harm rule were both absent.
- **Aortic dissection**: HR 60–80 is the 2022 target; <60 is the 2010 one.
- **A recurring pattern**: three timing figures on the card are the label's *peak* or *recheck
  interval* relabelled as onset — captopril, oral labetalol, nifedipine.
- **A retraction worth knowing about.** An earlier version of this page "corrected" nitroprusside's
  ten-minute maximum-rate limit as legacy labelling. That was wrong and is retracted. Two labels
  are currently marketed and they differ; the card quotes the one that carries it.

**Open verification debt:** ahajournals.org, JACC and NEJM all block automated access, so the 2025
AHA/ACC hypertension guideline's exact class-of-recommendation wording came from concordant
secondary sources rather than the PDF. Worth a check through the UCSF library before quoting a
COR/LOE designation in a setting where the distinction matters.

---

## Working preferences observed

- **Cheat-sheet register, always.** Assume a physician reader; use acronyms freely.
- **He pushes back on verbosity repeatedly.** Cut harder than feels right.
- **He asks "push" even when things are already pushed** — usually a stale browser cache, since
  Pages sends a ten-minute cache header. `open "…/bp-atlas/?v=$(date +%s)"` bypasses it.
- **Sources must actually resolve.** Search URLs are not acceptable; use direct, verified links.
  DailyMed over a subscription reference, because it is the real label, it is free, and the link
  survives being shared.
- **"Push intermittently."** Commit and push at each checkpoint rather than at the end; he watches
  the live site while the work is going on.
- **Colour is rationed.** He wants magnitude visible at a glance but the first saturated version
  hurt his eyes. Muted tones, and only on the columns that are ranked on.
