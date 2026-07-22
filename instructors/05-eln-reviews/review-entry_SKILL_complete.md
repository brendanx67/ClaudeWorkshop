---
name: review-entry
description: Review a lab-notebook entry (markdown, Word/.docx, PDF export, or a doc pulled via MCP) for reproducibility and correctness by checking it against everything it links to and references — source notes, protocols, data directories, analysis notebooks — not by vibes. Use when the user wants an ELN entry QC'd, reviewed, or countersign-checked before it's trusted.
argument-hint: [path-to-entry] [optional extra source paths]
allowed-tools: Read, Bash
---

You are reviewing a lab-notebook entry the way a careful second reader (or witness/countersigner)
would. Be skeptical. A tidy, confident entry is not the same as a correct one — and an ELN entry is
usually just a hub: the truth lives in what it links to, not in its prose.

Entry to review: $0
Any additional source files the user named: $ARGUMENTS

**Step 0 — read the entry properly, including link targets.** Real ELNs are Word docs, PDFs, or
exported Google Docs, not plain text. If the entry is a `.docx`/`.pdf`/`.html` (or pulled via a
connector), extract **both its text and every hyperlink's target** — a plain-text dump shows link
labels but silently drops where they point, which hides mislabeled links. Use `pandoc -t markdown`,
`python tools/read_eln.py <file>`, or the connector's structured output. Don't proceed on visible
text alone.

**Step 1 — gather the ground truth.** Find and open *everything the entry references or links to* —
raw notes, protocols/SOPs, data directories, analysis notebooks (`.ipynb`). If a referenced file
wasn't provided, look for it; if you can't reach it, say so. Never review the entry in isolation — a
review with nothing to check against produces flattery, not findings.

Then check the entry on these axes and report only real problems:

1. **Link integrity.** For every link, compare the link *text* to its *target*. Flag any link whose
   text describes one thing but points somewhere else (e.g. text says "batch 3 data" but the target
   is a different project's folder). Flag links to missing targets.

2. **Faithfulness to the notes.** Compare the entry to any raw notes. Flag anything the entry states
   that the notes don't support, and anything the notes contain that the entry dropped — sample IDs,
   deviations, unusual observations.

3. **Arithmetic.** Recompute every concentration, dilution, amount, and summary statistic from the
   numbers given. Show the calculation. Flag values that don't follow, and any as-prepared value that
   doesn't match a stated target.

4. **Linked code vs. the description.** For any linked analysis notebook, read the actual code — do
   not trust the entry's summary of it. Specifically:
   - Do plot **axis labels and titles** match what the figure is said to show? Watch for labels
     copy-pasted from a different analysis.
   - Does the **method as coded** match the method as described? Flag any filtering, outlier removal,
     replicate exclusion, or normalization done in code but **not disclosed** in the entry — and
     check whether a stated conclusion depends on that undisclosed step.

5. **Protocol compliance.** Compare the procedure as recorded to any SOP. List departures (skipped
   steps, out-of-spec values, substituted/expired reagents) and whether each is disclosed in the
   entry's Deviations section. **"Deviations: none" while the sources show departures is the most
   serious finding you can report.**

6. **Header & completeness.** Check required header fields are filled — author, **date started and
   date completed**, project, and sample IDs (where applicable). Flag blank or missing fields, unrecorded
   times, absent lot numbers, and values written as precise that the sources record as approximate.

7. **Measurement provenance / dilution-factor propagation.** For every reported concentration or
   amount, trace it back to the actual measurement it came from. If a value was measured on a diluted
   (or concentrated) aliquot, confirm the dilution factor was applied back to the stock. Check the
   reference frame of each number (stock vs diluted, per-µL vs per-injection) and re-derive any
   downstream amount that depends on it (e.g. on-column load). Flag values that are internally
   self-consistent but rest on an un-propagated factor.

Output a review in three parts:
- **Must fix** — factual errors, broken/mislabeled links, undisclosed methods that change a
  conclusion, arithmetic that's wrong, undisclosed deviations.
- **Should clarify** — gaps, missing header fields, ambiguities, precision claimed but not recorded.
- **Looks fine** — a short honest note on what checks out, so the review isn't only negative.

Do not fix the entry yourself; surface findings for the operator to act on. And remember: this review
is itself a draft — the operator should sanity-check what you flagged and what you may have missed.
