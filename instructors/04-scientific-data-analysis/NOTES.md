# Instructor notes — Lesson 4 (Scientific data analysis)

Private notes for building the lesson plan and slides: the pitfalls this dataset
can surface and where they fit the arc. **Kept out of the participant README on
purpose** — the lesson is a guided-but-open analysis, not a scripted reveal, so we
seed these in the *slides and live patter*, not the handout.

Unlike Lesson 3, there's no single "wrench." The teaching payload is the *habit* —
rigorous, honest analysis — and these pitfalls are the concrete places that habit
pays off. Surface the ones that fit the room; you won't hit all four in two hours.

---

## The dataset (quick reference)

- **`proteins_unnormalized_wide.tsv`** — ~9,562 proteins × 96 sample columns, wide.
  Join key is the column header (the `replicate` value in the metadata).
- **`metadata_wide.tsv`** — 96 rows × 25 columns, one row per sample.
- **80 biological samples + 16 reference/QC** (two pooled reference types). On QC
  rows, `GroupName = Batch QC` and the biological fields read `pool` / `na`.
- **Design columns worth knowing:** `Target Dose_cGy` (0–75), `Dose Rate` /
  `Dose Rate_cGy_per_min` (30 vs 300), `Sack Day`, `Sex`, `Strain`, `WellPosition`,
  `acquiredRank`, `IR Order`, `Platform Placement`, `EarTag`, `TEI-REX mouse number`.
- **Likely already log2.** Values sit in ~17–24, i.e. log2 intensities — the
  filename's "unnormalized" refers to *cross-sample normalization*, not the log
  transform. A clean hook for step 4 ("raw or transformed?") and a small trap:
  don't log already-logged data. *(Confirm before teaching.)*

---

## Pitfalls to surface (the teaching payload)

### 1. Pooled QC/reference samples aren't biological replicates
- **Where it lives:** the 16 reference/QC samples — `GroupName = Batch QC`,
  biological fields `pool`/`na`.
- **The trap:** dropping all 96 columns into a dose-vs-response comparison. The
  pools have no dose; they're process controls.
- **Where it surfaces in the arc:** step 6 (QC) — the pools are *for* QC (batch
  drift, CV), then get excluded from biological analysis. Good place to teach
  "know what each sample is before you compare it."

### 2. Hidden confounding
- **Where it lives:** `Dose Rate`, `Sack Day`, `WellPosition`, `acquiredRank` /
  `IR Order`, `Platform Placement` — all present, all potential confounders of a
  dose effect.
- **The trap:** attributing a proteomic shift to dose when it tracks plate
  position, acquisition order, or sack day just as well.
- **Where it surfaces:** step 6–7. Have them crosstab dose against the suspects
  *before* believing a hit. The Lesson 3 lesson (confounded design) in a new key.

### 3. Multiple testing
- **Where it lives:** ~9,562 proteins tested at once.
- **The trap:** a raw p < 0.05 per-protein screen returns hundreds of "hits" by
  chance. The CLAUDE.md already forbids ignoring this — this is where it bites.
- **Where it surfaces:** step 7. FDR / Benjamini–Hochberg, and a gut-check on how
  many hits you'd expect under the null.

### 4. Cross-validation leakage
- **Where it lives:** `EarTag` / `TEI-REX mouse number` — subject identity.
- **The trap:** if any subject contributes more than one row, a random by-sample
  split leaks the subject across train/test and inflates measured performance.
- **Where it surfaces:** step 7, whenever they build a predictor. Match the split
  to the claim — new unseen *sample* vs new unseen *subject*. *(Confirm the
  subject structure — how many rows per mouse — before leaning on this one.)*

---

## To verify before teaching

- [ ] Confirm the matrix is log2 (and the base), so the "raw or transformed?" beat
      is correct.
- [ ] Confirm the two reference-pool types, and what the `pool` rows' `IR Type` /
      `Strain` values mean (whether the pools come from a different experiment).
- [ ] Confirm per-mouse row counts — is there repeated-measures structure to make
      the CV-by-subject point real, or is it one sample per mouse?
