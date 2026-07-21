# Instructor answer key — Lesson 5 (ELN reviews)

Hi, it's me (Lindsay) writing to future-me and whoever's co-piloting the room. These files
are hand-built fixtures, not generated from a seed — every "mistake" in them is on purpose,
and the entries are *supposed* to look clean. So keep this page to yourself: the participant
README points here, but the fun is when the room finds the problems, not when they read the
spoilers.

---

## The arc (the interview is the lesson)

Interview → build the skill from *their* answers → try it on a sample entry → capstone.
The big change from a normal "spot the planted bug" session: **the planted bugs aren't the
point anymore — the participant's own review criteria are.** My sample entries are the
proving ground, not the curriculum.

**Beat 1 — Claude interviews them.** They ask Claude to interview them (one question at a
time, `AskUserQuestion` buttons) about their field, their analyses and measurements, and
the mistakes they've been burned by. This is where the hour's real value is; protect it and
don't rush it. A biologist, a chemist, a clinical-assay person, and a field ecologist will
walk out with four genuinely different skills — that's success, not drift.

**Beat 2 — flush answers into a `review-entry` skill** in their ClaudeLab. Likely their
*first slash-command skill* — see NOTES.md, coordinate with Brendan/Lesson 6.

**Beat 3 — run it on the sample entry.** It catches some of what's planted and misses some,
because it's tuned to *their* mistakes, not mine. Two teachable things surface here: (a) an
ELN entry is a **hub** — most of what needs checking is in what it links to, so a good skill
follows links / opens the analysis / recomputes rather than trusting prose; (b) every skill
has holes, which sets up the capstone.

**Beat 4 — capstone: find a miss, teach the skill to remember it.** They find a problem the
skill didn't flag (the batch-4 dilution trap is the reliable one; their own entry works too)
and add a check. Loop closed.

**If someone freezes at the interview** (the main failure mode): that's what the question
bank below is for. Feed them a couple of concrete prompts and they'll be off.

## The canary — an *engagement* tell (keep this one to yourself)

What I actually want to know, walking the room, is simple: **is this person really doing the
"interview me" thing the whole workshop is built on, or are they mindlessly pasting prompts
into their own Claude and nodding along?** The mascot is how I find out without asking.

Here's the mechanism, and why it works. During the interview we have Claude ask for a **lab
mascot** and sign every review off with it — but **the mascot is never printed anywhere in the
participant guide.** There's no word for them to copy. It can only exist if a real
back-and-forth actually happened and they answered a question *out loud, in their own head.*
So when they run their skill on the practice entry, the sign-off is the tell:

- **A real, specific mascot they clearly chose** (their postdoc's cat, the department's haunted
  centrifuge, whatever) → they engaged. Someone was home for the interview. Green light, move on.
- **No sign-off, or a limp generic one** ("🦉 owl," "the lab") they obviously didn't pick →
  autopilot. Either the interview never really happened or they clicked through it without
  engaging. That's your cue to wander over and get them actually talking to Claude.

Read it alongside the skill's *checks*: an engaged person's skill is full of their own domain
language (their units, their controls, their field's greatest hits); an autopilot skill is
generic boilerplate. Mascot + specificity together give you a five-second read on any
participant's screen.

**Keep it covert.** To participants this is just a bit of character — the skill signs off in
their lab's voice, cute, moving on. Nobody's told it's a check. If you announce it, it stops
measuring engagement and starts measuring who read the footnote. So don't put it on a slide,
and if someone asks, it's "just for fun."

(It also happens to model a good habit — a cheap tripwire that makes a silent failure, here
"nobody actually engaged," impossible to miss — but that's a bonus, not the pitch.)

## Interview question bank (for stuck participants)

Seed these in your patter — Claude will ask its own, but you'll want these ready for anyone
staring at a blank answer. The goal is to surface *the thing they'd be embarrassed to get
caught not checking.*

- **Field & units:** "What units do you fat-finger or mix up? (nM vs µM, mg vs mL, per-cell
  vs per-well.)"
- **The mandatory control:** "What has to be present for a result to mean anything — a
  blank, a negative control, a standard curve, a reference sample?"
- **Expiry & provenance:** "What goes stale — reagents, calibrations, antibody lots,
  standards — that an entry should record the age/lot of?"
- **The step everyone forgets to write down:** "What did you *do* that never makes it into
  the write-up? Filtering, outlier removal, normalization, a re-run, a dilution?"
- **Identity drift:** "How do samples/subjects get mislabeled or swapped in your workflow?"
- **The link that lies:** "Where do your entries point — data dirs, notebooks, dashboards —
  and how often does the link say one thing and go somewhere else?"
- **The claim that outruns the data:** "What conclusion do people in your field state too
  strongly for what the numbers actually support?"
- **Field-specific greatest hits** to offer by discipline: batch effects & multiple testing
  (omics); well-position/plate effects (screening); gating & compensation (flow); RT / m/z /
  missed cleavages (MS); primer/contamination controls (molecular); detection limits &
  blanks (analytical chem); site/PMI/sex confounds (clinical cohorts, cf. Lesson 3).

Their skill doesn't need all of these — it needs the three or four that are *theirs*.

---

## Practice entry — the batch-3 analysis entry (the proving ground)

This is the sample they run their *own* skill against — not a checklist to teach. It's here so
everyone has a concrete, messy entry to point at, and so you can see whether their skill catches
what it should. `notebook/2025-07-16_analysis-entry-for-review.docx` (a Word doc = an exported Google Doc;
there's a markdown twin `…-review.md` for anyone who'd rather skip the extraction). Its
conclusion — *"batch 3 is reproducible, fold it into the atlas"* — is confident and flat wrong.
It links to `analysis/tf-scan_batch3_cv.ipynb` and the dirs under `data/`.

| # | The entry shows | What's actually true | Caught by |
|---|---|---|---|
| 1 | Header **Date of completion** and **Project/run** left blank | fields just… empty | reading the header |
| 2 | Data link text **"tf-scan batch 3 data"** | target is `data/kinase-panel-batch2/` — a *different project* | pulling the link **target**, not the text (this is why round 1 whiffs) |
| 3 | "Figure 1: distribution of per-protein CV" | plot code hard-codes **"Retention time (min)" / "Peak area" / "RT alignment — kinase panel"**, copy-pasted from another analysis | open the `.ipynb`, read the plot cell |
| 4 | "CV computed across **all three** replicates … median CV low" | notebook quietly runs `df[df.replicate != 'R3']` first. Median CV is **~0.017 without R3**, **~0.99 with all three** | open the `.ipynb`, read the filter cell; compare to the entry's method |

The three tells are really one story: somebody reused an old kinase-panel notebook, repointed
the data path but not the link text, and never fixed the plot labels. Say that out loud —
it's *exactly* how this happens at 6pm on a Friday, and naming it lands better than moralizing.

**Land #4 hard.** The "good reproducibility" that justifies folding batch 3 into the atlas
exists *only* because a replicate got quietly dropped. Sign off on this and you've folded bad
data into the atlas — and none of it is visible from the entry text. A lazy "review this"
literally cannot reach it. That's the money moment.

---

## Capstone — the batch-4 injection-prep entry (a dilution error that survives a recompute)

`notebook/2025-07-18_batch4-injection-prep.md`. On purpose, it's **clean on every check the
skill already has** — header filled, no bad links, no linked code, dates sane. It even passes
the arithmetic check, which is the whole trick.

**The error.** TB-0432's peptide concentration (0.20 µg/µL) was read on a **1:10 dilution**
(the neat stock was over the assay's linear range), and the ×10 never got applied back to the
stock:

- Reported stock **0.20 µg/µL**; true stock **2.0 µg/µL**.
- "Inject 2 µL to load 400 ng" → actually **4000 ng on column**, a 10× overload (fried column,
  carryover, saturated signal — pick your nightmare).
- That reassuring `0.20 µg/µL × 2 µL = 0.4 µg` in the entry is a **decoy** — perfectly correct
  math *on the wrong input*, so anyone (or any skill) that just recomputes the stated numbers
  signs off feeling great.

Why it's a genuinely new class and not just the arithmetic check again: the arithmetic check
recomputes *stated* values and matches them to targets — and here they match! The bug is
upstream, in the *provenance* of the number — what reference frame it was measured in, whether
the dilution factor ever propagated. Same family as the batch-3 "400 vs 200 ng/µL" gotcha in
Entry B, but the mean cousin: that one fails a recompute, this one sails through it.

**Getting them there.** Run `/review-entry` first (it passes — that's the gap, made visible).
Then the open prompt: *"trace where that reported concentration actually came from — is the
on-column amount right?"* Nudges, in order if they stall: (1) *"the assay was read on a
dilution — so then what?"* (2) *"what's the true stock, and what does 2 µL of it load?"*

**If Claude back-calculates it unprompted** (a sharp model might): that's the teaching moment,
not a miss — smile and use it. The point was never "can Claude catch it once." It's that you
don't want to depend on luck: bake it into the skill and it's caught *every* run, by *every*
labmate, in the same format. Reliability and sharing, not raw cleverness.

**The fix (answer key).** They add a check to their `review-entry` skill. Anything in this
neighborhood is right:

> **Measurement provenance / dilution-factor propagation.** For every reported concentration
> or amount, trace it back to the measurement it actually came from. If a value was read on a
> diluted (or concentrated) aliquot, confirm the dilution factor was applied back to the stock.
> Check the reference frame of each number (stock vs diluted, per-µL vs per-injection) and
> re-derive anything downstream that depends on it (e.g. on-column load). Flag values that are
> internally self-consistent but rest on a factor that never propagated.

Re-run → the 10× lands in the review. Commit and push ClaudeLab. Loop closed, and honestly
that closing move is the whole workshop in miniature.

### Easier alternative capstone
Less technical room? Swap in `notebook/2025-07-23_batch4-cv-analysis.md`, which plants an
impossible **timeline** (data acquired 2025-07-25 but analysis "performed" 2025-07-23;
completion 07-22 before start 07-23) — same "add a new check" exercise, way easier to spot.
Answer-key check: *"Chronological plausibility — every date could've happened in the order
given: completion ≥ performed; analysis ≥ data acquisition; nothing dated in the future."*

---

## Alternative target (Entry B) — the wet-lab digest

For a benchier crowd, `notebook/2025-07-14_entry-for-review.md` runs the same arc against raw
notes + an SOP instead of a notebook. Sources: `raw-notes/2025-07-14_bench-notes.txt`,
`protocols/SDC-plasma-digest.md`. Planted: wrong sample count (the 0418 tube cracked and got
tossed), 20 µg/50 µL = **400** ng/µL against a stated 200 target, C18 washed **2×** not 3×, an
**expired substituted trypsin** lot, reduction at **54–55 °C** not 56, an approximate "~16 h"
written as a crisp "16 h", and — my favorite — "Deviations: none" sitting on top of all of it.
Headline: an entry that swears there were no deviations while the notes show three.

---

## The reference skill (what a finished `/review-entry` looks like)

They build their own by explaining it to Claude, so theirs won't match word for word — use this
to judge whether they covered the ground. Full text in
[`review-entry_SKILL_complete.md`](review-entry_SKILL_complete.md): seven checks — link
integrity, faithfulness to source notes, arithmetic, linked-code-vs-description, protocol
compliance, header/completeness, and (the capstone add) measurement provenance / dilution-factor
propagation. Note the **Step 0**: pull text *and hyperlink targets* out of `.docx`/`.pdf`/
exported entries, because a plain-text read drops the targets and hides trap #2.

---

## If you're short on time

Protect these, in order: the **interview** (that's the lesson — a personalized skill is the whole
deliverable), the **capstone loop** (find a miss → add a check), and *then* the sample entry as a
proving ground if there's time. If you have to cut, cut the sample-entry walkthrough before you
cut the interview — someone who leaves with a thin skill built from their own answers got more out
of the hour than someone who watched me demo my dropped-replicate trap.
