# Session 4 — Scientific Data Analysis · Slides Outline

Instructor working draft for the deck. The spine follows the participant
[README](../../lessons/04-scientific-data-analysis/README.md) and the workflow in
the example [`CLAUDE.md`](../../lessons/04-scientific-data-analysis/CLAUDE.example.md);
the traps to seed live are in [`NOTES.md`](NOTES.md).

**Arc:** who I am → what we'll do → setup → how to work → the analysis, step by
step (science → metadata → data → QC → loaders → analysis → report) → push it.
**Time:** keep 1–8 brisk; the bulk of the two hours is 9–11 (QC, loaders,
analysis). Everything downstream rests on 7–10 being done right.

---

## 1. Who I am

- Research scientist — computer science background (data science / statistics) and
  biology.
- Long track record doing scientific data analysis; this is the workflow I use.
- *Point: I'm not showing you a toy — this is how the work actually goes.*

## 2. What we'll do today

- The **whole process, end to end**: from scaffolding a project to a final report.
- One real dataset: mouse low-dose X-ray study, skin-punch DIA-MS proteomics.
- Claude writes the code; **you supply the science and the judgment.**

## 3. What I hope you learn — and take home

- Primarily the **process** (the steps coming up). Heavy emphasis on the
  **beginning** — metadata, data, QC. *Everything downstream depends on it; get it
  wrong and the fanciest analysis is built on sand.*
- The **confidence to tackle this yourself.**
- **Take home**, in your ClaudeLab: Python scripts, figures, tables, protein
  lists, and a final report from this analysis.

## 4. Set up the project in your ClaudeLab

- Copy the `data/` folder and `CLAUDE.example.md` (renamed to `CLAUDE.md`) into a
  new folder in your ClaudeLab — e.g. `proteomics-analysis/`.
- Have Claude create a **venv** (isolated Python sandbox).
- That `CLAUDE.md` carries the workflow, the statistics and code rules, and the
  **project map** it keeps up to date.

## 5. General tips — how to work with Claude efficiently

- **Save everything to Markdown; don't restate it.** Point `CLAUDE.md` at those
  files instead. This is what lets you start a new session cold and pick up exactly
  where you stopped.
- Tell Claude to **automatically save important findings** to findings Markdown
  files as it goes.
- **Name findings descriptively**, and make each one self-contained: verification
  status, discussion, links to related findings, the figures / tables / protein
  lists, and references to the data and scripts that produced them —
  **complete provenance.** A finding you can't retrace is a rumor.

## 6. State the science and objectives

- Have Claude **interview you** about the project: domain, the experiment,
  hypotheses and questions, the goal of the study.
- **One question at a time** — no walls of questions.
- Save the result to **`PROJECT.md`** so it carries into future sessions.

## 7. Review the metadata

- Have Claude open the metadata file and report back: the **columns**, and the
  **types of values** in each.
- Let Claude ask questions; **correct any mistakes it makes** — you're the domain
  expert here.
- **Visualize** the important variables (callback to Lesson 3, the day before).
- Mark which samples are **controls** vs. **experimental**.
- ⚠ *Seed the trap:* the pooled **reference/QC samples aren't biological
  replicates** — they have no dose and don't belong in group comparisons.

## 8. Review the data

- Have Claude open the data file. **What's the shape** — are rows samples or
  proteins? What kind of values are stored? What's the **missingness** situation?
- **Pin down the join:** map every sample column to exactly one metadata row, and
  sanity-check it before any plot relies on it — a bad join is the error that hides.
- ⚠ *Values sit ~17–24 → almost certainly already log2* despite "unnormalized" in
  the name. Good "raw or transformed?" beat; don't let anyone log it twice.

## 9. QC

- Generate and review QC plots; **save the good ones as findings.**
- **CV (coefficient of variation) plots** — *compute on linear-scale intensities,
  not logged data* — especially among controls.
- **PCA (principal component analysis) plots** colored by metadata variables.
- How does **normalization** change CV (especially among controls)? How does it
  change the PCA (especially among controls)?
- **Distribution** of protein abundances across runs. **Correlation** plots.
- **This is where the processing decisions get made:** normalization, batch
  correction, imputation (or filter on missingness) — the loaders encode them next.
- ⚠ *Batch correction ties to confounding:* dose can be entangled with batch,
  plate/well position, or acquisition order — all present as columns.

## 10. Build the data loaders — *the foundation everything rests on*

- Now that QC has decided the processing, build the reusable loader that **encodes
  the join and those decisions** (normalization, batch correction, imputation).
- **Every downstream analysis script uses it** to get its input.
- Tell Claude that **thoroughly testing and validating this code is essential** —
  generate it with unit tests, lint, and type-check, and **well documented** (it may
  ship with the paper).

## 11. Data exploration and analysis — *the bulk of the time*

- Now start answering the **real questions.**
- **Univariate:** proteins correlated with **exposure, dose, dose rate** — plots
  and protein lists, saved as findings.
  - ⚠ *~9,600 proteins → correct for multiple testing (FDR).*
- **Build a model to predict dose from the proteome.** Do it however you like;
  recommend **linear regression with regularization.** Claude talks you through the
  choices and makes suggestions.
  - ⚠ *Cross-validate against the right unit — split by subject/mouse, not by
    sample, or you leak.*
- **GO (Gene Ontology) enrichment** of the significant proteins.
- **Can Claude build a story** from the significant proteins?

## 12. Generate the report

- Have Claude assemble a **report of findings and methods** from the saved
  findings files.
- Output as **HTML or Markdown** (convert to PDF?). Something you'd hand a
  collaborator — or your future self.

## 13. Push everything to GitHub

- GitHub is **essential to this process**, not an afterthought:
  - It **backs up your work.**
  - It **never overwrites** the findings from previous sessions.
  - It lets you **pick up later, from anywhere.**
- *Close the loop: this is why Day 1 was about Git.*
