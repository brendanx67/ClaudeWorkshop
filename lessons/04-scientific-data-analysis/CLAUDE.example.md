<!--
  Example CLAUDE.md for a proteomics analysis folder. It LAYERS on top of the
  student's ClaudeLab root CLAUDE.md (from Lesson 1), which Claude Code also reads.
  Keep it ADDITIVE: only analysis-specific guidance belongs here — the root hub
  already points to CRITICAL-RULES.md, docs/, and todos/, so don't restate them.

  Named CLAUDE.example.md (not CLAUDE.md) so the workshop repo never auto-loads it;
  students place it as `CLAUDE.md` beside the data in their own working space.
-->

# Proteomics analysis

This project focuses on proteomics scientific data analysis. These notes
**supplement** the standing instructions in the ClaudeLab root `CLAUDE.md` — they
don't replace them. What follows is only what's specific to the analysis itself.

## Project map — keep it current

This file is the project's **map**, and it must stay accurate. When any document,
script, figure, or result is **created, moved, or renamed**, update its pointer
below in the same step; when the underlying work changes, update the document it
points to as well (e.g. revise `PROJECT.md` when the hypotheses change). A stale
pointer is worse than none.

Point to where each of these lives, and fill them in as they appear:

- **Science** — study, questions, hypotheses, goals — e.g. `PROJECT.md`
- **Metadata description** — what the sample sheet's columns mean
- **Data description** — shape, units, raw vs. transformed
- **Scripts** — the analysis code and how to run it
- **Figures** — where plots are written
- **Findings** — the running index of results — `findings/FINDINGS.md`
- **Results** — tables and the report
- **Project status** — where things stand and what's next

## How to work through an analysis

Work through these steps **one at a time, in order**, and **stay inside the
current step** — do only its work, nothing from a later one. When you're
understanding the metadata, don't open the data; before the QC step, run no QC;
and so on. Understand each step before the next. When a step is done, **stop and
check with me before moving on** — never advance to the next step, or jump ahead
to results, on your own.

0. **Scaffold the project.** Before any analysis, stand up a working
   environment: confirm Python is available, create the project-local `venv`, and
   install the tooling — all per **How the code should be written** below. Don't
   open the data or start the interview yet; this step is only the sandbox
   everything else runs in.
1. **Understand the project.** The science and domain, the questions and
   hypotheses, and the purpose of the analysis — before touching the data.
2. **Understand the metadata.** What each column is, its data type, and whether
   it is internally consistent.
3. **Understand the data.** Its shape, and whether the values are raw or
   transformed (e.g. log-scaled).
4. **Match the data to the metadata**, unambiguously — every sample mapped, with
   no guessing — and sanity-check that join before trusting any result.
5. **QC the data.** Assess outliers, missingness, batch structure, and the pooled
   controls, and **decide what processing is needed** — normalization, batch
   correction, imputation (or filtering).
6. **Build tested data loaders.** Encode the join and the QC decisions in a robust,
   well-tested, well-documented loader that every downstream script uses.
7. **Explore the data.** Ask the scientific questions and pursue those lines of
   thought.
8. **Report the findings** in a clear, shareable report.

## Save findings as you go

Don't wait until the end to write things down — capture each result the moment you
have it.

- Keep findings in a **`findings/` directory**, one file per finding, named for
  what it shows.
- Each finding is **self-contained**: its status, the discussion, and the figures,
  tables, or lists it produced.
- Record **full provenance** — the data and the script behind each finding, so it
  can be retraced. A finding you can't retrace is a rumor.
- Maintain a manifest, **`findings/FINDINGS.md`**, that indexes every finding;
  update it in the same step you add or change one, and keep the project map above
  pointed at it.

## How the statistics should be done

- **Rigor is essential**, and always **correct for multiple hypothesis testing**.
- **Prefer well-established, canonical, simpler tests** — Mann–Whitney U, t-tests,
  OLS (ordinary least squares) for linear models, logistic and linear regression
  (both with regularization). Reach for
  well-established non-linear models (XGBoost, random forests) only when the
  simpler ones genuinely won't do.
- **Never p-hack.**
- **Match cross-validation to what you're estimating** — performance on a new
  unseen sample vs. a new unseen subject calls for different data splits.
- Use **well-established statistical libraries** wherever possible.

## How the code should be written

- Write the analysis in **Python**. **Don't assume Python is installed** — check
  first (`python3 --version`, or `python --version` on Windows). If it isn't
  available, install it with [`uv`](https://docs.astral.sh/uv/) **into this project**
  so the folder is self-contained: point `UV_PYTHON_INSTALL_DIR` at a local
  `.python` directory, then run `uv python install` (e.g. `uv python install 3.12`).
  Don't install Python system-wide.
- Work inside a **virtual environment (`venv`) in this folder** — create it with
  `uv venv` and install every library into it. **Never install packages outside the
  venv** (no global or system installs).
- Install **only established, widely trusted libraries** — e.g. `numpy`,
  `pandas`, `scikit-learn`. Nothing obscure or unvetted.
- **Test, lint, and type-check** all code: `pytest` for unit tests, `ruff` for
  linting, `mypy` for type checking.
