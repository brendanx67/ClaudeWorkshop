# Lesson 3 — Data cleanup and visualization

**Day 1 · 10:30–12:00 · Lauren & Chris**

Projects rarely fail at the instrument. They fail at the **metadata** — the
sample sheet, the case list, the spreadsheet a collaborator emailed you in
March. Two labs both say "age," and mean different things by it. That's the hour.

Same trick as Lesson 1: **all you have to do is explain.** You bring the
judgment; Claude does the merging, the plotting, the writing-down. The prompts
below are **examples, in your own words** — never things to copy exactly.

> **Where you should be:** Claude Code open on your `ws` folder, with both
> `ClaudeWorkshop` and your own `ClaudeLab` inside it. The data you'll need is in
> [`cohorts/`](cohorts/), in this folder.

---

## 1. Meet the three labs

Your lab prepares clinical samples. Three independent **CTE** groups — chronic
traumatic encephalopathy, the tauopathy associated with repetitive head impacts
— have each shipped you samples plus their metadata, and each has asked you to
analyze their cohort and compare it with the others.

Nobody coordinated. In [`cohorts/`](cohorts/):

| | Lab | What they sent |
|---|---|---|
| **1** | Whitfield Institute (neuropathology) | `BINC_case_manifest.pdf` — post-mortem brain |
| **2** | Universiteit van Rijndal (biomarkers) | `rijndal_cohort_export.csv` — living cohort, CSF and plasma |
| **3** | Cascade Athletic Health Center (sports medicine) | `cascade_biobank_inventory.xlsx` — mixed sample types |

The institutions are fictional and their data is synthetic — invented for this
workshop. The paper in the next section is real.

## 2. Add the published cohort

You also want to compare against the literature. Kumar et al., *Cell* 2026
([doi:10.1016/j.cell.2025.12.036](https://doi.org/10.1016/j.cell.2025.12.036))
has a **Supplementary Table S1** with case-level demographics — one row per brain
donor, CTE and control. That's a fourth cohort, free.

Ask Claude, in your own words, to go get it.

Then do the thing that matters: **ask Claude what it actually downloaded.** Open
the file. Publisher sites don't always hand a robot the spreadsheet it asked for,
and Claude will cheerfully report success either way. If what landed isn't a
table, say so and ask whether there's another route to the same file — a
supplement usually lives in more than one place. Push until you have real rows.

That's the whole *review what Claude did* habit, in ninety seconds. It never
stops being worth it.

## 3. Look at the files. Just look.

Open all three cohort files yourself — PDF viewer, Excel, whatever you like. No
Claude. Two minutes.

Don't fix anything. Don't take notes. Just notice how differently three competent
labs describe the same kind of thing.

## 4. Plan it on paper — **without Claude**

Pair up. Five minutes, on paper or in a scratch file: **what steps would you take
to merge these into one table?** What has to be decided? What would you have to
look up, guess, or ask someone about?

Do not skip this, and do not open Claude for it. In a minute you're going to read
a plan Claude wrote, and the only way to judge a plan is to already have one.
People who skip this step approve whatever they're shown.

## 5. Hand it to Claude

Now switch on **planning mode** (Shift+Tab — Claude proposes a plan and waits for
you instead of charging ahead) and describe the job. Roughly:

> *"Merge the four cohorts into one Excel workbook: a sheet per cohort, plus a
> combined sheet. Ask me before you decide anything you're unsure about."*

Read its plan against yours. Where they differ, one of you is wrong — find out
which.

One thing to insist on: a **decisions log** sheet in the workbook. Every time
Claude maps one lab's column onto another's, converts something, guesses, or
drops a field, it gets a row: what it did, and why. You'll want this later. It's
the Lesson 1 habit — **flush what you explain** — pointed at the choices instead
of at you.

When the workbook exists:

- **Get it reviewed.** Ask Claude to launch a **code-review agent** — a second,
  fresh Claude with no memory of building the thing, reading the work cold. A
  fresh reader catches what an author can't.
- **Commit and push it to your ClaudeLab** (your repo from Lesson 1). Same words
  as yesterday: *"save this to my ClaudeLab and push it."*

## 6. Let Claude interview you, then plot

Don't specify figures. Start the other way — **have Claude ask you**:

> *"I want to visualize these cohorts. Ask me the questions you need answered
> before you make a single plot."*

Answer honestly, including "I don't know yet." Then have it produce **around ten
plots** representing the data — and look at every one. Some will be wrong. Say so,
and ask for another. This is a conversation, not a render.

## 7. Put your plots on the shared board

Everyone posts to one board so we can look at all of them side by side:

> **[tinyurl.com/claude-plots](https://tinyurl.com/claude-plots)**

No account, no sign-in. Drag a plot straight from the folder onto the board, or
snip what's on your screen (`Win + Shift + S`, or `Cmd + Shift + 4` on a Mac) and
paste it.

Then look at everyone else's. Do the numbers make sense? Anything too big, too
clean, or missing entirely is worth saying out loud.

Posting to a public board is fine here — every one of these cohorts is synthetic.

## 8. Your favorites, as a report

Pick the plots that actually say something, and ask Claude to assemble them into
a single **HTML report** on the cohort demographics — one page, opens in a
browser. Sections, captions, the figures. Something you'd send a collaborator.

Push it to your ClaudeLab too. Your partner can pull it down and open it, which
is a cheap and pleasant demonstration of why the Git hour was worth it.

## 9. The wrench

Each PI sent a **cover letter** along with their shipment. They're in
[`cover-letters/`](cover-letters/), in this folder. Nobody has read them yet.

Read them now — then hand them to Claude:

> *"Review my merged workbook and my decisions log against these three letters.
> Where do they disagree?"*

Sit with what comes back. Then ask the question that actually matters: how would
you have found this out *without* the letters?

## Keep going

- **Fix it.** Correct what the letters overturned — and write the correction into
  the decisions log rather than quietly editing a cell. That's the difference
  between a spreadsheet and a record.
- Ask Claude for **a checklist you'd send a collaborator** before they ship you
  metadata: the questions you now wish you'd asked. Save it in your ClaudeLab.
  You will use it in real life.
- Anything the letters taught you that you never want to repeat? That's a line in
  `CRITICAL-RULES.md`.

## Up next

Lesson 4 is real scientific data analysis — bigger files, actual statistics. The
habit you built this hour is what keeps that honest: **an analysis is only as
good as its metadata, and metadata is only as good as the questions you asked
about it.**

## You're on track when

- [ ] One Excel workbook: a sheet per cohort, a combined sheet, and a decisions
      log a stranger could follow.
- [ ] The published cohort is genuinely in it — you opened the file and saw rows,
      instead of trusting the word "downloaded."
- [ ] A review agent read the merge cold, and you read what it said.
- [ ] Workbook and HTML report are committed and pushed to your ClaudeLab.
- [ ] You can name something the cover letters overturned — and say what would
      have caught it earlier.

## What you take with you

- A merge you can defend, because the decisions log says what you decided.
- The reflex to **check what Claude actually did** — especially when it tells you
  it succeeded.
- The uncomfortable, useful lesson of section 9: **data does not carry its own
  context.** Somebody has to ask. That somebody is you — and you now have a tool
  that will ask twelve questions the moment you tell it to.

---

*Snagged? Nothing here is fragile — the source files are read-only, and the
workbook can be rebuilt from scratch in a minute. Ask Claude to explain the
current state, or wave over an instructor.*
