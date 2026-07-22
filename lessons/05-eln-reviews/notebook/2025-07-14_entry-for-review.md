# Plasma tryptic digest, TB-0417–0420

| Field | Value |
|---|---|
| **Experiment ID** | EXP24 |
| **Project** | tf-scan atlas |
| **Author** | Lindsay Pino — lpino@talus.bio |
| **Collaborators** | — |
| **Reviewers** | — |
| **Date started** | 2025-07-14 |
| **Date completed** | 2025-07-14 |
| **Date reviewed** |  |

**Experiment type:** Sample prep · **Experiment status:** Completed · **Review status:** In review

## Objectives
Four-sample plasma digest for the tf-scan atlas runs, following the standard SDC protocol
([PR — SDC plasma digest](../protocols/SDC-plasma-digest.md)).

## Experimental Summary
| Parameter | Description | This experiment |
|---|---|---|
| Sample type | what was measured | Human plasma |
| Num. samples | total, including controls | 4 (TB-0417, TB-0418, TB-0419, TB-0420) |
| Time point(s) | when assayed | n/a (prep only) |
| Controls | positive and negative | n/a |

## Reagents & materials
- 100 mM TEAB + 1% SDC (lysis)
- DTT, IAA
- LysC; sequencing-grade trypsin

## Procedure (as performed)
- Resuspended pellets (~20 µg each) in 50 µL lysis buffer → 200 ng/µL.
- Reduced with 10 mM DTT, 56 °C, 30 min.
- Alkylated with 20 mM IAA, RT in the dark, 30 min.
- LysC digestion 1:100, 37 °C, 2 h.
- Trypsin digestion 1:50, 37 °C, 16 h.
- Quenched with FA to ~1%, centrifuged 10 min, retained supernatant.
- C18 StageTip cleanup, 3× wash per protocol, eluted 50% ACN.
- Dried by SpeedVac and resuspended in 20 µL 0.1% FA.
- QC injection: 1:10 dilution, 2 µL on column.

## Deviations from protocol
None.

## Analysis — file locations
| Data type | Location | What's there |
|---|---|---|
| Bench notes | [2025-07-14 bench notes](../raw-notes/2025-07-14_bench-notes.txt) | what actually happened at the bench |
| Raw instrument data | s3://data-pipeline-raw-bucket/250714_TFscan_plasma_QC/ | QC injections |

## Observations
All samples processed normally.

## Results / output
- Digests prepared at 200 ng/µL, ready for LC-MS.
- QC injections acquired.

## Conclusions
Four plasma digests prepared to spec, no deviations; ready for acquisition. *(LP)*

## Next steps
Acquire full runs and search.
