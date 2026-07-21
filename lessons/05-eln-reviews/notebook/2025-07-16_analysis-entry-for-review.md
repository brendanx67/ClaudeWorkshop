# tf-scan batch 3 — CV analysis

- **Operator:** LP
- **Date performed:** 2025-07-16
- **Date of completion:**
- **Project / run:**

## Objective
Assess reproducibility of per-protein intensities across replicates for tf-scan atlas batch 3,
to decide whether batch 3 is clean enough to fold into the atlas.

## Data
Raw and processed intensity tables: [tf-scan batch 3 data](../data/kinase-panel-batch2/)

## Analysis
Full analysis in the linked notebook: [tf-scan_batch3_cv.ipynb](../analysis/tf-scan_batch3_cv.ipynb)

Computed the coefficient of variation (CV) of intensity for each protein across all three
replicates, then looked at the distribution of per-protein CVs.

## Results
- Median per-protein CV was low, consistent with good reproducibility across replicates.
- See Figure 1 (in the notebook): distribution of per-protein CV across replicates.

## Conclusion
Batch 3 reproducibility looks acceptable; proceed to fold into the atlas.

## Next steps
Merge batch 3 into the combined atlas table.
