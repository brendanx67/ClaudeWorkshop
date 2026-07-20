# Data for Lesson 4

## The study

Mice were exposed to X-ray doses ranging from **0 to 75 cGy** at dose rates of
either **30 or 300 cGy/min**. Skin punch samples were collected **6 days
post-exposure** and analyzed by DIA-MS (data-independent acquisition mass
spectrometry) to characterize dose-dependent proteomic responses. The study
comprises **80 samples** — **96 including reference/QC samples**, which are two
independent pooled reference sample types.

## The files

Real experimental data from that study — a protein abundance matrix and the
sample sheet that describes it. Treat both as **read-only** source data: read
and analyze them, but write your outputs (tables, figures, notebooks) into your
own `ClaudeLab`, never back here.

| File | What it is |
|------|------------|
| `proteins_unnormalized_wide.tsv` | Protein abundances, wide format: one row per protein (~9,600), one column per sample (96). |
| `metadata_wide.tsv` | The sample sheet: one row per sample (96), describing each one. |

The two files share the sample identifiers — that's how they connect. Beyond
that, go look for yourself.
