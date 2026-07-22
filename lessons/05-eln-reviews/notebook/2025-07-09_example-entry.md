# Plasma tryptic digest, TB-0402–0405 (rapid-digest pilot)

| Field | Value |
|---|---|
| **Experiment ID** | EXP22 |
| **Project** | tf-scan atlas, pilot batch |
| **Author** | Lindsay Pino — lpino@talus.bio |
| **Collaborators** | — |
| **Reviewers** | R. Okafor |
| **Date started** | 2025-07-09 |
| **Date completed** | 2025-07-09 (single day, no overnight step this round — rapid digest) |
| **Date reviewed** | 2025-07-11 |

**Experiment type:** Method dev · **Experiment status:** Completed · **Review status:** Approved

## Objectives
Four-sample plasma digest to check the rapid-digest protocol against our standard overnight
prep before committing the full batch.

## Experimental Summary
| Parameter | Description | This experiment |
|---|---|---|
| Sample type | what was measured | Human plasma |
| Num. samples | total, including controls | 4 (TB-0402, TB-0403, TB-0404, TB-0405) |
| Conditions | perturbation tested | rapid 2 h digest vs standard overnight |
| Controls | positive and negative | n/a (protocol comparison) |

## Reagents & materials
- 100 mM TEAB + 1% SDC (lysis), made fresh same day
- DTT (Sigma, lot #SLCK4471), IAA (Thermo, lot #WH330621)
- Trypsin/LysC mix, sequencing grade (Promega, lot #0000539821, exp 2026-03)

## Procedure (as performed)
- Resuspended ~20 µg pellets in 40 µL lysis buffer → **500 ng/µL as prepared** (20 µg / 40 µL).
- Reduced 10 mM DTT, 56 °C, 30 min (block held 56 °C).
- Alkylated 20 mM IAA, RT dark, 30 min.
- Trypsin/LysC 1:25, 37 °C, 2 h (rapid protocol).
- Quenched FA to ~1%, spun 10 min, took supernatant.
- C18 StageTip, 3× wash, eluted 50% ACN.
- SpeedVac to dry (~35 min). Resuspended in 20 µL 0.1% FA → **1000 ng/µL as prepared**.

## Deviations from protocol
- Rapid 2 h digest instead of overnight (intentional — this is what the pilot is testing).
- Otherwise none.

## Analysis — file locations
| Data type | Location | What's there |
|---|---|---|
| Raw instrument data | `TB0402-0405_2025-07-09_QC.raw` (instrument PC) → s3://.../tf-scan/pilot/ | QC injections |

## Observations
All four clear after resuspension. No precipitate.

## Results / output
- As-prepared 1000 ng/µL; diluted 1:5 in 0.1% FA to 200 ng/µL for injection.
- QC injection 2 µL on column.

## Conclusions
Rapid-digest pilot prepped cleanly; arithmetic and dilutions check out. Recommend comparing
missed-cleavage rates to the overnight prep before adopting. *(LP)*

## Open questions / to verify
- Rapid digest completeness vs overnight — compare missed-cleavage rates once searched.

## Next steps
Search QC runs, compare to overnight batch, decide on protocol for full set.
