# tf-scan batch 4 — CV analysis

| Field | Value |
|---|---|
| **Experiment ID** | EXP30 |
| **Project** | tf-scan atlas, batch 4 |
| **Author** | Lindsay Pino — lpino@talus.bio |
| **Collaborators** | — |
| **Reviewers** | — |
| **Date started** | 2025-07-23 |
| **Date completed** | 2025-07-22 |
| **Date reviewed** |  |

**Experiment type:** Analysis · **Experiment status:** Completed · **Review status:** In review

## Objectives
Same per-protein CV reproducibility check as batch 3, now for batch 4, to decide whether batch 4
can be folded into the atlas.

## Design
Three replicates (R1–R3) acquired and searched; per-protein CV of intensity computed across the
replicates. All three replicates were included.

## Experimental Summary
| Parameter | Description | This experiment |
|---|---|---|
| Sample type | what was measured | tf-scan atlas, batch 4 |
| Num. replication | biological/technical scheme | 3 (R1–R3) |
| Metric | reproducibility readout | per-protein CV of intensity |

## Analysis — file locations
| Data type | Location | What's there |
|---|---|---|
| Raw instrument data | Acquired 2025-07-25 on the Exploris | raw acquisitions |
| Intensity table | [tf-scan batch 4 data](../data/tf-scan-batch4/) | per-protein intensities, all replicates |

## Results
- Median per-protein CV was low, consistent with good reproducibility across replicates.
- No tubes flagged; all samples resuspended clear.

## Conclusions
Batch 4 reproducibility looks acceptable; proceed to fold into the atlas. *(LP)*

## Next steps
Merge batch 4 into the combined atlas table.
