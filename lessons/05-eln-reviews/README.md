# Lesson 5 — ELN reviews

**Day 2 · 10:30–11:15 · Lindsay**

Okay — you just spent two hours with Mike building an analysis you're proud of. Here's
the slightly uncomfortable question I want us to sit with: six months from now, when you
(or, worse, someone who *isn't* you) opens the **ELN** entry — that's your *electronic
lab notebook* write-up of what you did — is it actually trustworthy? A notebook entry is
where an analysis goes to be believed, and it's only ever as good as the review it
survives.

Think of it like a recipe card you handed a friend. It reads beautifully. But whether
the cake comes out has almost nothing to do with how tidy the card is — it's whether the
card matches what you actually did in the kitchen. So this hour we're going to hand
Claude an entry that reads beautifully and is quietly wrong, learn the difference between
a review that pats you on the head and one that actually opens the oven, and then — the
part I love — **build a review skill that checks for *your* mistakes**, the specific ones
that bite in *your* work, and keep it.

Because here's the thing: I can show you the stuff *I'd* catch — I'm a proteomics person,
so I'm paranoid about dropped replicates and dilution math. But a good ELN review is
deeply personal. The things a crystallographer double-checks, an ecologist double-checks,
someone running clinical assays double-checks — totally different lists. **The point of
this hour isn't to learn my checklist. It's to teach Claude yours.** So we're going to
let Claude *interview you* to find out what yours even is.

> **Where you should be:** Claude open on your `ws` folder, with `ClaudeWorkshop` and
> your `ClaudeLab` sitting inside it. Nothing to install — the entry you'll review is
> already in this lesson's folder.

The whole lesson in one line: **a review is only as good as what you make Claude check it
against — and what to check is a thing only you know.**

## Goal

Let Claude interview you about how *you'd* review a notebook entry, turn your answers into
a reusable **skill** — a saved instruction you run with a slash command like
`/review-entry` — in your ClaudeLab, then sharpen it against a real (flawed) entry.

## Where you should be

- Claude open on your `ws` root, `ClaudeLab` sitting next to `ClaudeWorkshop`.
- You've done at least one analysis (hi, Lesson 4) — so this kind of entry looks familiar.
- A sample entry to practice on is a Word doc (basically an exported Google Doc), here:
  `ClaudeWorkshop/lessons/05-eln-reviews/notebook/2025-07-16_analysis-entry-for-review.docx`

## What we'll do

You bring the judgment; Claude does the interviewing, the reading, and the math. The
prompts below are **examples — say them however you'd say them.**

> **Pace it — one entry at a time.** This lesson works best slow: do a single entry, then
> *stop and talk it through together* before moving on. Don't let Claude sprint ahead and
> hand you finished reviews for every entry at once — if it does, just say *"one at a time,
> wait for me."* Two habits make it click:
> - **You first, if you like.** Before Claude runs the skill on an entry, take a pass
>   yourself — say what you'd check, or what smells off — then run it and compare. It's
>   *your* review instinct we're here to exercise, not Claude's.
> - **You decide the depth.** Say *"just run it"* and discuss the output, or ask Claude to
>   walk the entry section by section (metadata → design → the data link → the results
>   claim), pausing at each so you can react.

We build one skill, then put it to work across a few entries with a little less hand-holding
each time — **watch me take one, then we take one together, then you take one on your own.**
Working through this on your own? Same entries — you just drive all three passes yourself.

**1 · Warm-up: read one by hand.** Before Claude touches it, open the batch-3 sample entry
(the Word doc above) and review it yourself — the way you would a labmate's entry you'd been
asked to sign off on. Get a feel for the format, the numbers, what it links to, and jot down
what you'd want to check. No hunting for anything in particular; just get the lay of the land.
We'll come back to this exact entry.

**2 · Let Claude interview you.** Now get Claude to pull *your*
review checklist out of your head. Start it off, roughly:

> *"I want to build a skill that reviews my lab notebook entries. Before you write
> anything, interview me — one question at a time — about what I'd actually check in an
> entry from my own work. Ask about my field, the kinds of analyses and measurements I
> do, the mistakes I've been burned by before, and what a trustworthy entry has to
> include. Ask me a couple of lighter questions too — a lab mascot, say — and give the
> skill some character by having it sign off each review with mine. Then we'll turn my
> answers into the skill."*

Answer honestly and specifically — this is the actual work of the hour. Think about the
thing you'd be embarrassed to get caught not checking: the unit you always fat-finger,
the control that has to be there, the calibration that expires, the sample-ID scheme that
drifts, the step you *always* forget to write down. Letting Claude ask you is the whole
point; you'll get somewhere you wouldn't have reached by staring at a blank prompt. *(If
your Claude launches into prose questions, nudge it: "ask me with the question buttons,
a few options each, one at a time.")*

**3 · Turn your answers into a skill.** Once Claude's got your list, flush it into *your*
lab so you never have to re-explain it:

> *"Great — save that as a skill called `review-entry` in my ClaudeLab, so I can run
> `/review-entry` on any entry and have you check for exactly these things."*

That's the week's refrain again: **all you have to do is explain.** Claude writes the
skill; you brought the expertise about what "reviewed" means *in your world*.

**4 · Run it — one entry at a time.** Now put the skill to work, taking the training wheels
off as you go. Pause and talk after each entry before starting the next.

- **The batch-3 entry you just read by hand.** Run the skill on it and compare — what did it
  catch that you didn't, and did you spot anything it missed?
  > *"Run `/review-entry` on the batch-3 analysis entry in this lesson's folder."*

  (It signs off in your lab's voice at the end — small thing, never gets old.) A lot of what
  needs checking lives in what the entry *links to*, not in its words — an ELN entry is a
  **hub**. If your skill didn't already say so, tell it to follow links, open any linked
  analysis, and recompute the numbers rather than trusting the write-up. *(That sample is a
  Word doc; if reading it is fiddly, there's a helper — `python .../tools/read_eln.py <file>`
  prints every link as `text -> destination`. Ask Claude first, though.)*
- **A second entry — the wet-lab digest.** Point the skill at
  `notebook/2025-07-14_entry-for-review.md` and see how your checklist holds up on a different
  kind of entry (a bench prep, with its own linked notes). Compare again.

Your skill will catch some things and miss others — it's tuned to *your* mistakes, and even
those aren't all captured yet. That's exactly the setup for the last pass.

**5 · On your own — the capstone: catch something your skill missed, and teach it to
remember.** Every review skill has holes — the test is what you do when you find one. Find a problem in an entry
that your skill *didn't* flag (there's a subtle one waiting in the batch-4 injection-prep
entry — the arithmetic looks fine, so ask where a number actually *came from*; or use one
of your own entries and a mistake from your own life). Then close the loop:

> *"You missed this. Add a check for it to my `review-entry` skill so it catches this
> kind of thing every time from now on."*

Commit and push your ClaudeLab. Your reviewer just learned something permanent — for you,
and for anyone you share it with. That's the good stuff.

## Keep going

Done early? Amazing — there's no wall here:

- Run your skill on one of your *own* real entries, or a labmate's. (This is the moment it
  stops being a workshop toy and starts being useful.)
- Interview Claude in reverse: ask *it* what a careful reviewer in your field would check
  that you *didn't* mention — then keep what's actually right for you.
- Trade skills with the person next to you. Their checklist will have a check yours is
  missing, guaranteed.

## You're on track when

- [ ] You read an entry by hand first — before Claude — and formed your own take.
- [ ] Claude interviewed *you* — one question at a time — and your answers, not my
      checklist, shaped the skill.
- [ ] A `review-entry` skill lives in your ClaudeLab, runs as `/review-entry`, and checks
      for things that are specific to *your* work.
- [ ] You ran it on more than one entry, one at a time, and saw it both catch and miss things.
- [ ] You found something it missed and taught it a new check.
- [ ] ClaudeLab committed and pushed.

## What you take with you

- **A good review is personal.** The mistakes worth catching are the ones from *your*
  bench and *your* pipeline; the skill is where that hard-won paranoia gets written down.
- **Don't trust the write-up — trust the review, then review the review.** A tidy entry is
  a *claim*, not a fact. (Same instinct that makes you run a control, honestly — just
  pointed at your own notebook.)
- **Your skill is a living SOP.** Every time it misses something, you add a check — caught
  forever after, for everyone who runs it. Next hour, in Lesson 6, you'll turn an
  explanation into an actual MCP tool; a skill is the same idea in a smaller pot.

---

*Instructor materials — the interview beats, the planted-problem key, the reference skill
— live in [`../../instructors/05-eln-reviews/`](../../instructors/05-eln-reviews/), kept
out of this guide on purpose. (No peeking, participants.)*
