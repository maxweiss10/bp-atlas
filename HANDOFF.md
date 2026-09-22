# BP Atlas — session handoff

**Live:** https://maxweiss10.github.io/bp-atlas · **Clone:** `~/bp-atlas` (not under Documents —
TCC blocks it) · **Repo:** maxweiss10/bp-atlas, branch `main`

Current as of 2026-09-22. Two sessions of work are on `main`: the first (`411cd57`..`7f9861c`)
added the inpatient tab, the White Book styling and the ward-shorthand register; the second
(`6470b81`..HEAD) rebuilt the tables. Working tree clean, remote in sync, Pages serving the build.
If he says something is not showing, it is almost always the ten-minute Pages cache:
`open "https://maxweiss10.github.io/bp-atlas/?v=$(date +%s)"`.

---

## What the site is now

Five tabs in one `index.html`. **Single drugs** — 38 US-marketed drugs, 136 real dose rows, from
the Wang 2025 efficacy model; opens on each drug's maximum dose. **Combinations** — pairs and
triples through the paper's permutation equations. **Build a regimen** — builder, next-step
ranking, ladders, counselling. **Inpatient & emergency** — a White Book cardiology card checked
line by line: 17 situations with targets, 31 agents. **How it works** — the provenance record.

Every table is one 26px line per row. Everything that does not fit the line is in the tooltip and
in the open row.

---

## Decisions in force, with the reason

1. **No mmHg column inpatient.** The Wang model is chronic oral monotherapy; it has no coefficient
   for a titrated infusion. The tab shares no data with the model (`INPATIENT` is its own constant).
   Ranking an esmolol drip beside amlodipine 5 mg would imply a comparison that does not exist.

2. **One line per row, and the chip columns absorb the slack.** Every column except
   Contraindications/Indications (inpatient: Indications/Avoid in) has `width:1%`, which a table
   clamps up to the content width; the chip columns are `max-width:0; width:auto` so their content
   cannot widen the table, with a floor of 150px (120px under 1500px). After every render
   `fitChips()` measures each chip cell — one read pass, one write pass — and hides what does not
   fit behind a `+n` chip whose tooltip lists the rest. On a phone the cards wrap and it is skipped.
   Verified at 375, 1000, 1280, 1440, 1512 and 1720px: the tables fit at 1440 and above.

3. **Colour is rationed.** Δ SBP and Δ DBP are coloured on a seven-step **muted** cool-to-warm
   ramp (`.r0`–`.r6`: blue, teal, green, olive, bronze, rust, brick) with **fixed mmHg cuts** —
   Δ SBP at 4/6/8/10/12/15, Δ DBP at 3–8 — so a colour always means the same number and 10 sits two
   steps below 15. Every step clears 5:1 on white; weight rises with the step. Inpatient onset and
   offset use five of the seven steps. Nothing else is coloured. **He asked for more contrast
   between 10 and 15, then said the first attempt — a saturated rainbow on the time, cost and
   evidence columns too — "hurt my eyes."** The Intensity (low/moderate/high) column is gone: it
   restated Δ SBP.

4. **Max dose is the default rung** (`state.rung = 'max'`, Reset returns to it, and the storage key
   moved to `bpatlas.v2` so his saved "every dose" did not override it). Minutes print as `m`
   everywhere in the tables via `shortMin()`, which leaves `/min` rates alone.

5. **A formulation gets its own row only when it changes the order.** The test: different dose,
   schedule, indication or route. Passes: metoprolol tartrate vs succinate ER (both tables),
   nifedipine IR vs ER, diltiazem IV vs ER, labetalol IV vs PO, hydralazine IV/IM vs PO,
   nitroglycerin drip vs ointment, clonidine tablet vs patch (inpatient). Considered and rejected,
   with him agreeing: carvedilol CR, verapamil and propranolol IR, spironolactone suspension,
   isosorbide mononitrate (its IR-vs-ER schedule point sits inside the ISDN row's correction note).
   - In `model.json`, `metoprolol` became `metoprolol succinate` (the old row: ER, once daily,
     HF-approved, tag "HF-approved form") and `metoprolol tartrate` (IR, BID, 50/100/200/400 mg,
     no HFrEF indication — it is a *caution* chip there — tag "No HF indication; BID"). Both carry
     `base: 'metoprolol'`, `fdisp` and `mform: 'shared'`, rendered as one dashed **shared model**
     tag: the Wang appendix (p. 18) lists metoprolol once with no formulation and its trials used
     both. `fdisp` alone tags nifedipine/diltiazem/verapamil (ER) and propranolol (LA).
   - Tartrate kinetics are the tartrate label's own sentences (effect within 1 h; half the
     maximum effect gone at 3.3/5.0/6.4 h after 20/50/100 mg; weekly titration; 1–2 wk taper).
     Tartrate costs are the 2026 NADAC file via the CMS API (dataset
     `fbb83258-11c7-47f5-8b18-5f8e79f7e704`, effective 2026-08-19; the rest of the page is the
     2026-08-26 file): median unit price × whole tablets, $0.96 / $1.11 / $1.65 / $3.30.
   - Two forms of one drug are never paired (`comboAllowed` and `comboFlags` check `base`), and
     the HF-proven beta-blocker list in `renderAdvice` names `metoprolol succinate`, not tartrate.
   - The only single pill is `hydrochlorothiazide|metoprolol tartrate` — NADAC has no succinate
     combination.

6. **Inpatient rows.** Use tiers (1 first reach / 2 specific / 3 know-only; 14/14/3) exist because
   he objected to scrolling past phentolamine to reach labetalol; the table sorts on tier, ties on
   onset. IV hydralazine is deliberately tier 2. The trigger of a specific agent rides in the tier
   chip's tooltip and is spelled out in the open row. Dosing lives only in the open row, which
   leads with it. Subclass prints `IP_SUB_SHORT` shorthand (β1-sel, NO donor venous, arteriolar
   dilator) with the full name in the tooltip. Route chips say `IV/IM` where the label allows IM.
   Every block above the tables goes through `linkDrugs()`; `nitro`, `metoprolol`, `clonidine
   patch` are aliases. Atenolol and nimodipine are named in the conditions table but are not
   agents, so they do not link — he knows and is fine with it.

7. **The four shaded rows at the top of the conditions table are the defaults**, including the two
   where someone else wants the number lower: pre-procedure and discharge. They carry the evidence
   to hold the line.

8. **Register: ward shorthand.** Arrows, standard abbreviations, no articles, no linking verbs. His
   own example: "Extravasation causes necrosis and blistering — large vein, never a butterfly. A
   lot of volume at high body weights" → **"Extrav→necrosis/blisters; lg vein only. ↑wt=↑vol"**.
   He called the first version "SOOOO verbose" and asked for cuts four times. `data/abbrev.py`
   holds the substitution list for the outpatient text. **How it works** is deliberately exempt.

9. **Styling is the MGH housestaff manual**, matched to the White Book treatment on Pearl
   (maxweiss10.github.io/pearls): Arial Narrow in the data zone, `#D9D9D9` small-caps bands, black
   header rows, hairline grids, `#0432FF` underlined citations. **Dark mode was removed on
   purpose.** When styling another of his sites, sample Pearl's live tokens first.

---

## Build pipeline — read this before editing anything

| Script | Run it when |
|---|---|
| `data/build_inpatient.py` | after editing any `ip_*.py` — embeds `INPATIENT` |
| `data/embed_model.py` | **after editing `model.json`** — embeds `PAYLOAD` only |
| `data/add_kinetics.py` | only when regenerating the kinetics layer from `kinetics.py` |

`merge_data.py` cannot be run: its inputs (`nadac_prices.json`, `embed_data.json`,
`single_pill.json`, `formulations.json`, `drugs.json`) were never committed. Edit `model.json`
directly and re-embed. New costs come from the NADAC API (see decision 5).

**Traps, each of which cost time:**

- `model.json` edits reach the page only through `embed_model.py`. `add_kinetics.py` regenerates
  kinetics from source first and would overwrite them.
- `s.index('NOTES = [')` matches inside `DZ_NOTES = [`. Anchor on line starts in `data/ip_text.py`.
- The desktop shrink rule is `#drugtable tbody td:not(.ci)` and its `:not()` counts as a class, so
  any phone override must match that specificity (`td:not(.ci), td.ci`) or the cards collapse to a
  pixel. It happened once and shipped for a few minutes.
- The table wrapper must **not** be a scroll container (`overflow:visible`). With `overflow-x:auto`
  the sticky header sticks to the wrapper, not the window, and is never visible while scrolling —
  which is how it had always been until this session. The header sticks at `top:var(--railH)`,
  kept current by a ResizeObserver on the control rail and on every tab switch. That header sliding
  under the rail is almost certainly what he called "the dropdown menus overlapping".
- The one-line `nowrap` rule reaches the open detail row unless the override carries the table id
  (`#drugtable tbody tr.detail > td`). Without it the open row renders as overlapping text — also
  an old bug.
- `fitChips()` measures after render; anything that changes a chip cell's width without a render
  (a window resize) has to re-render. A debounced resize handler does. Do not measure hidden
  chips: `offsetWidth` is 0.
- Line numbers in `index.html` shift with every CSS edit. Find the embedded lines by prefix
  (`const PAYLOAD = `, `const INPATIENT = `), never by number.

---

## Verification record

`data/verification/` holds seven research passes with per-claim sources, plus a README naming what
could not be verified. Highlights:

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
- **Added this session, each from the label on DailyMed:** metoprolol tartrate tablets
  (`63d45147-…`), metoprolol succinate ER (`151079c5-…`), clonidine tablets (`58772b44-…`),
  Catapres-TTS (`39e1d35e-…`: therapeutic levels 2–3 days after first application; after removal
  levels hold ~8 h then fall over days; remove before MRI and before cardioversion; excessive rise
  on discontinuation reversed with oral clonidine or IV phentolamine; above two TTS-3 adds nothing).
  MERIT-HF is PMID 10376614, POISE 18479744. All links checked to resolve on 2026-09-22.

**Open verification debt:** ahajournals.org, JACC and NEJM block automated access, so the 2025
AHA/ACC hypertension guideline's exact class-of-recommendation wording came from concordant
secondary sources rather than the PDF. Worth a check through the UCSF library before quoting a
COR/LOE designation where the distinction matters. Smaller: the "46% of figures are label-stated"
sentence in How it works predates the tartrate row (four more label figures); recompute if that
paragraph is touched.

---

## Working preferences observed

- **Cheat-sheet register, always.** Assume a physician reader; use acronyms freely.
- **He pushes back on verbosity repeatedly.** Cut harder than feels right.
- **"Push intermittently."** Commit and push at each checkpoint; he watches the live site and the
  browser pane while the work is going on, and reacts mid-task.
- **Colour is rationed.** Magnitude at a glance, yes; a saturated ramp on every column, no.
- **Sources must actually resolve.** Search URLs are not acceptable; use direct, verified links.
  DailyMed over a subscription reference: the real label, free, and the link survives sharing.
- **He asks "push" even when things are already pushed** — usually the Pages cache.
- **When he asks for an audit, he means fix what it finds and then update this file.**
