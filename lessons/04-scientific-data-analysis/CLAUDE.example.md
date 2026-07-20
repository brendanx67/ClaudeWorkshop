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

## How to work through an analysis

Follow these steps in order. Understand each one before moving to the next, and
don't jump ahead to results.

1. **Understand the project.** The science and domain, the questions and
   hypotheses, and the purpose of the analysis — before touching the data.
2. **Understand the metadata.** What each column is, its data type, and whether
   it is internally consistent.
3. **Understand the data.** Its shape, and whether the values are raw or
   transformed (e.g. log-scaled).
4. **Match the data to the metadata**, unambiguously — every sample mapped, with
   no guessing.
5. **Explore the data.** Ask the scientific questions and pursue those lines of
   thought.
6. **Report the findings** in a clear, shareable report.

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

- Write the analysis in **Python** (already installed).
- Work inside a **virtual environment (`venv`) in this folder** — create one and
  install every library into it. **Never install packages outside the venv** (no
  global or system installs).
- Install **only established, widely trusted libraries** — e.g. `numpy`,
  `pandas`, `scikit-learn`. Nothing obscure or unvetted.
- **Test, lint, and type-check** all code: `pytest` for unit tests, `ruff` for
  linting, `mypy` for type checking.
