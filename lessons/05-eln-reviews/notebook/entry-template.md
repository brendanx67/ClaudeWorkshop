# <Experiment title>

| Field | Value |
|---|---|
| **Experiment ID** | EXP&lt;nn&gt; |
| **Project** | <e.g. tf-scan atlas> |
| **Author** | <name — name@talus.bio> |
| **Collaborators** | <names, or —> |
| **Reviewers** | <name — assigned reviewer> |
| **Date started** | <YYYY-MM-DD> |
| **Date completed** | <YYYY-MM-DD — note if a step ran overnight / across days> |
| **Date reviewed** | <YYYY-MM-DD, or blank until reviewed> |

**Experiment type:** <e.g. Method dev / Analysis> · **Experiment status:** <In progress / Completed> · **Review status:** <In review / Approved>

## Objectives
One or two sentences: what this experiment was for and what "done" looks like.

## Design
How the experiment or analysis was laid out. Link the metadata sheets, plate maps, or per-run
records this entry draws on — and make the **link text match where the link actually goes.**

## Experimental Summary
| Parameter | Description | This experiment |
|---|---|---|
| Sample type / cell line(s) | what was measured | ... |
| Num. samples | total, including controls | ... |
| Treatment / conditions | doses, perturbations | ... |
| Time point(s) | when assayed | ... |
| Num. replication | biological or technical scheme | ... |
| Controls | positive and negative | ... |

## Reagents & materials
Anything where identity matters later — buffers, enzymes, **lot numbers and expiry**,
substitutions. If a lot or expiry is uncertain, say so; don't clean it up. *(Prep entries.)*

## Procedure (as performed)
What actually happened, in order. Record the values you actually used, not the values the
protocol calls for. Mark approximate values as approximate (e.g. "~16 h", not "16 h") — the
uncertainty is information. *(Prep entries.)*

## Deviations from protocol
Every place the run departed from the standard protocol, with the reason if known. Skipped
steps, substituted reagents, out-of-spec temperatures, shortened washes. **If nothing deviated,
write "none."** A blank here should never mean "I didn't check."

## Analysis — file locations
| Data type | Location | What's there |
|---|---|---|
| Metadata sheets | <link> | plate maps / sample metadata |
| Raw instrument data | s3://... | raw acquisitions |
| Processed data | s3://... | searched / quantified tables |
| Figures | <link> | figures for this entry |
| Analysis steps | <notebook.ipynb> | the code that produced the results |

## Results
Concentrations as prepared (show the arithmetic), figures, and what the numbers say. If an
as-prepared value doesn't match the target, flag it here.

## Conclusions
The call, in one or two lines — and who is making it. Sign with your initials, e.g. *(LKP)*.

## Open questions / to verify
Things to follow up before trusting this. Missing timings, uncertain lots, values to double-check.

## Next steps
What happens to these samples or this analysis next.
