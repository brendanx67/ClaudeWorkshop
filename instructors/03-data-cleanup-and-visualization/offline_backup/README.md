# Published reference cohort — Kumar et al., *Cell* 2026

`Kumar2026_Cell_TableS1_demographics.xlsx` — Supplementary Table S1, "Patient demographics
for both cohorts."

- **Paper:** Kumar M, Schlaffner CN, ... McKee AC, Hyman BT, Steen H, Steen JA.
  "Molecular features of human pathological tau distinguish tauopathy-associated dementias."
  *Cell*, Jan 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13075643/
- **License:** CC BY-NC-ND 4.0.

## Re-fetching it

PMC gates supplement downloads behind a proof-of-work challenge — a plain `curl` of the
PMC link returns an HTML stub, not the spreadsheet. Europe PMC serves the same files
ungated:

```
curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13075643/supplementaryFiles" -o suppl.zip
unzip suppl.zip NIHMS2150432-supplement-S1.xlsx
```

## What's in the workbook

Four sheets:

| Sheet | Shape | Notes |
|---|---|---|
| `Summary_Primary_Cohort` | 20 × 17 | Human-formatted. Mean on one row, `(SD)` on the row beneath. Header typo: `Age at deach (years)`. |
| `Summary_Secondary_Cohort` | 14 × 16 | Same layout. Title cell still says "Primary Cohort". |
| `Demographics_Primary_Cohort` | 203 donors | Case-level. |
| `Demographics_Secondary_Cohort` | 142 donors | Case-level. |

Case-level columns: `Group`, `SampleID`, `BrainBank`, `Age at Death`, `Sex`, `PMI [hours]`,
`Braak Stage`, `NPDX1`, `NPDX2`.

Primary cohort groups: AD 42, PSP 41, CBD 34, **CTE 24**, **CTRL 24**, PiD 20, DLB 14, fAD 4.

## Data quirks (all real — do not "fix" them before the workshop)

- `Age at Death` contains the string `>=90` — HIPAA de-identification cap. Non-numeric,
  and not honestly imputable.
- `PMI [hours]` contains `<24` and `<72` — censored values, also strings.
- `Braak Stage` is roman numerals with data-entry errors: alongside `I`–`VI` there are
  `IVV`, `VVI`, `IIIII`, `OI`, and `O` (letter O, meaning stage 0). 61/203 are blank.
- The two case-level sheets disagree on header capitalization: `Age at Death` vs
  `Age at death`. A naive concat produces two columns.
- PMI is `int` in the primary sheet, `float` in the secondary.

## The confound (the workshop's closing beat)

Among the 24 CTE donors:

- **All 24 are male.** Controls are 12F : 12M.
- **All 24 come from a single brain bank** (VA-BU-CLF). Controls come from MADRC, HBSFRC,
  and HBTRC.
- CTE post-mortem intervals run substantially longer than controls'.

So a naive CTE-vs-control contrast in this cohort is simultaneously a sex contrast, a
brain-bank contrast, and a PMI contrast. This is discoverable in a few lines and is the
intended "aha" for participants.
