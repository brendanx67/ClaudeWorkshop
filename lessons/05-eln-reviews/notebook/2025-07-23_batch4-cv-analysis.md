# tf-scan batch 4 — CV analysis

- **Operator:** LP
- **Date performed:** 2025-07-23
- **Date of completion:** 2025-07-22
- **Sample IDs:** TB-0431, TB-0432, TB-0433
- **Project / run:** tf-scan atlas, batch 4

## Objective
Same per-protein CV reproducibility check as batch 3, now for batch 4, to decide whether batch 4
can be folded into the atlas.

## Data
Raw files acquired 2025-07-25 on the Exploris. Intensity table:
[tf-scan batch 4 data](../data/tf-scan-batch4/)

## Analysis
Computed the coefficient of variation (CV) of intensity for each protein across the three
replicates, then looked at the distribution of per-protein CVs. All three replicates were included.

## Results
- Median per-protein CV was low, consistent with good reproducibility across replicates.
- No tubes flagged; all samples resuspended clear.

## Conclusion
Batch 4 reproducibility looks acceptable; proceed to fold into the atlas.

## Next steps
Merge batch 4 into the combined atlas table.
