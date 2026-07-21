# 2025-07-09 — Plasma tryptic digest, TB-0402–0405

- **Operator:** LP
- **Date(s) performed:** 2025-07-09 (single day, no overnight step this round — rapid digest)
- **Sample IDs:** TB-0402, TB-0403, TB-0404, TB-0405
- **Project / run:** tf-scan atlas, pilot batch

## Objective
Four-sample plasma digest to check the rapid-digest protocol against our standard overnight
prep before committing the full batch.

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

## Observations
All four clear after resuspension. No precipitate.

## Results / output
- As-prepared 1000 ng/µL; diluted 1:5 in 0.1% FA to 200 ng/µL for injection.
- QC injection 2 µL on column. Raw files: `TB0402-0405_2025-07-09_QC.raw` on the instrument PC,
  copied to `s3://.../tf-scan/pilot/`.

## Open questions / to verify
- Rapid digest completeness vs overnight — compare missed-cleavage rates once searched.

## Next steps
Search QC runs, compare to overnight batch, decide on protocol for full set.
