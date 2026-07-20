# STATUS — Session 4 (Scientific data analysis)

**Handoff document.** Hand this to a new agent to resume work on this session.
Last updated: **2026-07-20**. Session is taught **Wed 2026-07-22, 8:00–10:00**
(Day 2, first block) by **Mike Riffle**.

---

## Orientation — read these first

- **Repo:** `ClaudeWorkshop` — the *textbook* (reference material, shared). The
  participant's own repo is `ClaudeLab`, which they create in Lesson 1. Both sit
  side by side under a root folder called `ws`.
- **Writing standard & workflow:** [`instructors/README.md`](../README.md). Write
  for a scientist who lives in Excel and has never used a terminal. Small nudges,
  wide-open space — *not* a copy-paste script. Example prompts are always marked
  "in your own words."
- **This session's spine:** the participant
  [README](../../lessons/04-scientific-data-analysis/README.md) and the example
  [`CLAUDE.example.md`](../../lessons/04-scientific-data-analysis/CLAUDE.example.md).

## Where things stand

| Artifact | Path | State |
|---|---|---|
| Participant lesson | `lessons/04-.../README.md` | **Done** — goal, 8-step arc, checkpoints, takeaways |
| Example CLAUDE.md | `lessons/04-.../CLAUDE.example.md` | **Done** — project map, 6-step workflow, statistics rules, code rules |
| Data + study blurb | `lessons/04-.../data/` | **Done** — 2 TSVs + `README.md` |
| Slide deck | `lessons/04-.../slides/index.html` | **First draft** — 16 slides, needs a full-screen review |
| Slides outline | `instructors/04-.../SLIDES_OUTLINE.md` | **Done** — 13-section content spine for the deck |
| Pitfalls / traps | `instructors/04-.../NOTES.md` | **Done** — plus a pre-teaching verify list |

**The dataset** (real, from a TRX-Phase2a low-dose X-ray study):
`proteins_unnormalized_wide.tsv` (~9,562 proteins × 96 sample columns) and
`metadata_wide.tsv` (96 samples × 25 fields). They join on the metadata
`replicate` column ↔ the matrix's sample-column headers. 80 biological samples +
16 pooled reference/QC.

## Decisions already made — do not undo these

1. **`CLAUDE.example.md` must NOT be named `CLAUDE.md`.** Claude Code auto-loads
   any file literally named `CLAUDE.md`; the workshop repo deliberately has none
   (see `instructors/README.md`), so naming it that would inject instructions into
   live sessions. Students copy it into *their* ClaudeLab as `CLAUDE.md`.
2. **That file is an ADDITIVE nested layer.** It composes with the student's
   ClaudeLab root `CLAUDE.md` (built in Lesson 1). It must never restate what the
   root already owns — `CRITICAL-RULES.md`, `docs/`, `todos/`. Keep it thin and
   analysis-specific.
3. **Pitfalls stay out of the participant README.** They live in `NOTES.md` and as
   HTML speaker-note comments in the deck, to be delivered live — so participants
   discover them rather than reading them.
4. **Delivery is interleaved**: present a step slide → jump into Claude Code → come
   back for the next step. That's why the deck has no closing "now go build it"
   slide; it ends on the GitHub push. Don't re-add a sendoff close.
5. **Data files are `.tsv`**, not `.csv`.
6. **No `limma`** in the statistics rules — it's R/Bioconductor and conflicts with
   the Python-venv coding rule. Replaced with OLS.
7. **Deck is built from `instructors/presentation-template/`** with its `<style>`
   and `<script>` copied verbatim. Keep the print CSS intact (16:9 PDF).
8. **Branch per piece of work, open a PR, never commit to `main`.**

## Open items

- [ ] **Verify before teaching** (from [`NOTES.md`](NOTES.md)):
  - [ ] Confirm the abundance matrix is already **log2**. Values sit ~17–24, which
        strongly implies it — but this is **inferred, not verified**, and it now
        appears as a speaker note on the data slide. Confirm before saying it aloud.
  - [ ] Confirm the **two reference-pool types**, and what the `pool` rows'
        `IR Type` / `Strain` values mean (do the pools come from another experiment?).
  - [ ] Confirm **per-mouse row counts** — is there repeated-measures structure to
        make the cross-validation-by-subject point real?
- [ ] **Full-screen review of the deck** (open `slides/index.html`, press **F**).
      The metadata slide (5 bullets) and QC slide (5 bullets + sub) are the two
      most at risk of overflow at 16:9. Never verified by an agent — needs a human.
- [ ] **Rehearse each step live**, and capture **known-good fallback outputs**
      (finished findings / screenshots) so a stalled live demo doesn't derail the
      room. Nothing built for this yet. Cf. Lesson 3's `offline_backup/`.
- [x] **PR opened & merged** — PRs #7 and #8 (`mike/analysis-lesson`) are merged to `main`.
- [ ] *Optional:* make the `CLAUDE.example.md` project map name `METADATA.md` and
      `DATA.md` explicitly. The deck's steps 2–3 tell Claude to write those files,
      but the map still uses generic labels. Offered, deferred by Mike.
- [ ] *Optional:* the deck has **no figure slides / `assets/`** yet. The template's
      `figure-slide` layout is ready for a real QC or PCA plot.
- [ ] *Open question in the outline:* report output — HTML or Markdown → PDF?

## Known inconsistency (deliberate)

The **deck numbers the process steps 1–7** (science = 1), while the **README numbers
the arc 1–8** with *setup* as step 1. The deck treats setup as pre-work. Harmless,
but renumber if it bothers anyone.

## Git

- **Branch:** `mike/analysis-lesson` — merged to `main` (PRs #7 and #8) and no
  longer the working branch. Start new work from a fresh branch off `main`.
- **Commits so far:** lesson + data + CLAUDE example + NOTES → self-maintaining
  project map → slides outline + deck → this STATUS doc.
- **PR:** #7 and #8 (`mike/analysis-lesson`) opened and **merged**. All Session 4
  work above — including this file (`f72c7aa`) — is committed and pushed to `main`.
