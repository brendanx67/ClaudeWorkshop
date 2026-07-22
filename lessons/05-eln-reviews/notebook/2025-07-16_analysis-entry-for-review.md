# tf-scan batch 3 — CV analysis

| Field | Value |
|---|---|
| **Experiment ID** | EXP27 |
| **Project** |  |
| **Author** | Lindsay Pino — lpino@talus.bio |
| **Collaborators** | — |
| **Reviewers** | — |
| **Date started** | 2025-07-16 |
| **Date completed** |  |
| **Date reviewed** |  |

**Experiment type:** Analysis · **Experiment status:** Completed · **Review status:** In review

## Objectives
Assess reproducibility of per-protein intensities across replicates for tf-scan atlas batch 3,
to decide whether batch 3 is clean enough to fold into the atlas.

## Design
Three replicates (R1–R3) of the batch-3 samples were acquired and searched. For each protein we
compute the coefficient of variation (CV) of intensity across the replicates, then look at the
distribution of per-protein CVs. Inputs and code are linked below.

## Experimental Summary
| Parameter | Description | This experiment |
|---|---|---|
| Sample type | what was measured | tf-scan atlas, batch 3 |
| Num. replication | biological/technical scheme | 3 (R1–R3) |
| Metric | reproducibility readout | per-protein CV of intensity |

## Analysis — file locations
| Data type | Location | What's there |
|---|---|---|
| Raw & processed intensity tables | [tf-scan batch 3 data](../data/kinase-panel-batch2/) | per-protein intensities, all replicates |
| Analysis steps | [tf-scan_batch3_cv.ipynb](../analysis/tf-scan_batch3_cv.ipynb) | CV computation and Figure 1 |

## Results
- Computed the CV of intensity for each protein across all three replicates, then looked at the
  distribution of per-protein CVs.
- Median per-protein CV was low, consistent with good reproducibility across replicates.
- See Figure 1 (in the notebook): distribution of per-protein CV across replicates.

## Conclusions
Batch 3 reproducibility looks acceptable; proceed to fold into the atlas. *(LP)*

## Next steps
Merge batch 3 into the combined atlas table.
