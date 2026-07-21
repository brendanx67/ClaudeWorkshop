# Lesson 4 — Scientific data analysis

**Day 2 · 8:00–10:00 · Mike Riffle**

This is the long session, and the real one: you take a genuine scientific dataset
the whole way — from *"what is this study even asking?"* to a report you'd hand a
collaborator. One proteomics dataset, two hours, Claude writing the code while you
supply the science and the judgment.

Same trick as every session: **all you have to do is explain.** When you're not
sure how to start, **have Claude ask you.** The prompts below are **examples, in
your own words** — never things to paste.

## Goal

By the end, you can take a real, messy dataset from first contact to a shareable
report — understanding the study, loading the data and metadata with *tested*
code, doing honest QC and statistics, and writing up what you found — with Claude
doing the coding and you supplying the science.

## Where you should be

- Claude Code open on your `ws` folder, with `ClaudeWorkshop` and your own
  `ClaudeLab` inside it.
- **From Day 1:** your `ClaudeLab` exists and is on your GitHub, and you're
  comfortable committing and pushing.
- **From setup:** Python is installed.
- Lesson 3 helps but isn't required — this is the same *review what Claude did*
  reflex, now pointed at statistics.
- The dataset is in [`data/`](data/) in this folder: a protein abundance matrix
  and its sample sheet. Read [`data/README.md`](data/README.md) for the
  one-paragraph study description.

## What we'll do

Roughly this arc — **open at every step**, but in this order. Each step is a small
nudge; where you go inside it is up to you and your Claude.

1. **Set up the analysis in your ClaudeLab.** Copy this folder's `data/` and the
   example `CLAUDE.example.md` (renamed to `CLAUDE.md`) into a new folder in your
   `ClaudeLab` — say `proteomics-analysis/` — and have Claude create a **venv** (a
   virtual environment: an isolated Python sandbox, so installs never touch your
   system). That `CLAUDE.md` carries the analysis workflow and the rules for the
   rest of the session.
2. **Interview yourself about the science.** Before any code:
   > *"Ask me what you need to know about this study — the question, the
   > hypotheses, the design, the purpose — before we touch the data."*

   Flush your answers into a short doc. You can't analyze what you can't state.
3. **Understand the metadata.** What is each column? Its data type? Is it
   internally consistent? Walk the sample sheet with Claude before trusting it.
4. **Understand the data — and pin down the join.** What shape is it? Is a value
   raw or already transformed (log-scaled)? What is a row, what is a column? Then
   map the data to the metadata **unambiguously — every sample column to exactly one
   metadata row, no guessing** — and sanity-check that mapping before you trust any
   plot. A bad join is the error that hides.
5. **QC — quality control.** Look before you leap: outliers, missingness, batch
   structure, the pooled reference samples. This is where you **decide what
   processing the data needs** — normalization, batch correction, imputation (or
   filtering) — by watching how each changes CVs and PCA. Decide what's signal and
   what's artifact.
6. **Write tested data loaders.** Now that QC has told you what's needed, have
   Claude build the robust, reusable loader every downstream script will use — the
   verified join plus the normalization, batch correction, and imputation you
   settled on — with unit tests, linting, and type-checking. It's the foundation of
   everything downstream (and likely shared at publication), so don't trust a loader
   you haven't tested.
7. **Explore and analyze — the bulk of your time.** Now ask the real questions and
   chase them. Keep the statistics honest: correct for multiple testing, pick
   models that fit the question, and match cross-validation to what you're actually
   predicting. This is a conversation, not one render.
8. **Write the report.** Assemble your findings, figures, and tables into a
   Markdown or PDF report you'd send a collaborator — or your future self. Commit
   and push it to your `ClaudeLab`.

## Checkpoints

- [ ] The analysis lives in your `ClaudeLab`: `data/` plus a `CLAUDE.md`, in its
      own folder, with a working venv.
- [ ] You can state the study's question and hypotheses in a sentence — because you
      wrote them down, not because you guessed.
- [ ] Every sample column maps to exactly one metadata row — you checked the join
      before trusting a plot.
- [ ] You ran real QC and can name one thing it caught (or confirmed clean) — and
      what it told you to normalize, batch-correct, or impute.
- [ ] Data and metadata are loaded by **tested** code that encodes those QC
      decisions.
- [ ] Your statistics are honest — multiple-testing corrected, model appropriate,
      cross-validation matched to the question.
- [ ] A report (Markdown or PDF) with figures and tables, committed and pushed to
      your `ClaudeLab`.

## What you take with you

- **A real analysis you own** — scripts, tested loaders, figures, tables, a
  findings doc, and a shareable report — sitting in your `ClaudeLab`, ready to
  rerun and extend.
- **A reusable workflow.** The `CLAUDE.md` you carried in — understand → metadata →
  data → QC → load → explore → report — travels to your next dataset unchanged.
- **The habit at the center of the week, made rigorous:** you supply the science,
  Claude supplies the code, and neither of you trusts an untested loader or an
  uncorrected p-value.

---

*Snagged? Nothing here is fragile — the source data is read-only and every script
can be rebuilt from a prompt. Ask Claude to explain the current state, or wave over
an instructor.*
