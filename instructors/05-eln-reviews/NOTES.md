# Instructor notes — Lesson 5 (ELN reviews)

Me talking to me (and my co-pilot) about building and running this one. **On purpose, this
stays out of the participant README** — the reveals land way harder felt than read, so the
planted stuff lives here and in the live patter, not the handout.

Solo session, 45 minutes, Day 2 · 10:30–11:15. It runs straight into Lesson 6 (MCP), so
whatever else happens, protect the 11:15 handoff.

---

## Where this sits in the two days

The schedule does most of my setup for me, which is lovely:

- **Lesson 1 (Brendan)** already gave everyone Claude Code on their `ws` root and a
  `ClaudeLab`. I teach zero setup — thank you, Brendan.
- **Lesson 4 (Mike), the slot right before me,** just had them *run an analysis and make
  plots.* That's my cold open: "you just did an analysis — would your notebook entry of it
  survive review?" The primary target is a CV-analysis entry with a linked notebook, which
  is basically a mirror of what Mike just walked them through. Use that.
- **Lesson 6 (Brendan), right after me,** turns an explanation into an MCP tool. My handoff:
  today we reviewed an *exported* entry; MCP is how you'd point the same skill at a *live*
  Google Doc or Benchling. Say it as I close so it feels like a baton pass, not a full stop.

The one-liner I want running through it: **do an analysis (4) → check whether the record of
it is trustworthy (5) → connect to your live ELN (6).**

## Run-of-show (45 min, solo)

- **10:30–10:36 Frame.** ELN = electronic lab notebook. The pitch: a good review is
  *personal* — I can show what I'd catch, but the skill has to check for *your* mistakes. So
  we're going to let Claude interview each of you to find out what those are.
- **10:36–10:52 The interview (the heart of it).** They get Claude to interview them, one
  question at a time, about their field and the mistakes they've been burned by. Circulate
  hard — this is where people freeze. Have the question bank (ANSWER_KEY.md) ready to unstick
  anyone staring at a blank answer. Don't rush this; the interview *is* the lesson. (The mascot they pick here is your quiet tell
  later for who really engaged — see ANSWER_KEY.md. Never announce it.)
- **10:52–11:00 Flush into a skill.** "Save that as a `/review-entry` skill in your ClaudeLab."
- **11:00–11:10 Try it on the sample entry + capstone.** Run it on the batch-3 entry. As you circulate,
  use the **canary** — the live-chosen mascot signing each review — to spot who actually did
  the interview vs. who's on autopilot (ANSWER_KEY.md; keep it to yourself). Then watch it
  catch some things and miss others. Then find a miss (batch-4 dilution trap, or one of their
  own) and add a check. Commit/push.
- **11:10–11:15 Close + hand to Lesson 6.**

Solo means I can't work the room and present at once — so the interview and the capstone are
where I spend my legs. The framing (6 min) and the skill-save (fast) can run from the front.

**Keep it paced — don't let it steamroll.** This is a one-at-a-time lesson: a single entry,
then pause and talk before the next. In a test run a driving Claude dumped a finished review
for the sample entry *and* pre-empted the batch-4 capstone in one go — which flattens the
whole point (it's *their* review instinct we're exercising, not the model's). If you see it —
in the demo or on someone's screen — rein it in: *"one at a time, wait for me,"* and offer the
participant the first pass before the skill runs. The README's **"Pace it"** callout now says
this to participants directly.

## Stuff to confirm before July 22 (the load-bearing unknowns)

- [ ] **The interview actually interviews.** Lesson 1's dry run found Claude won't reach for
      the `AskUserQuestion` button interface unaided — it asks in prose until told. The README
      tells participants to nudge it ("ask me with the question buttons, one at a time"), but
      rehearse it, and be ready to hand people that nudge fast. The pacing rule (one question
      at a time) is the other half — a wall of questions kills the beat.
- [ ] **Is this the room's first slash-command skill?** The knowledge-base path in
      `instructors/README.md` puts `claude/` skills + commands *late*, and Lesson 1 dodges
      `.claude/` entirely. If nobody's made a skill yet, I define it plainly here (done in the
      README) — **and I need to check with Brendan** whether Lesson 6 assumes skills already
      exist, so we introduce the idea in the right spot and don't step on each other.
- [ ] **Reading a `.docx` in the `</> Code` tab.** Confirm Claude pulls text *and* hyperlink
      targets. If it only grabs visible text, trap #2 (the mislabeled link) vanishes — which
      is what `tools/read_eln.py` is for (stdlib only, no pandoc needed). Rehearse on a clean
      machine, because this is the bit most likely to bite.
- [ ] **ClaudeLab exists and pushes.** The skill and the capstone commit land in their
      ClaudeLab — confirm Lesson-1 auth survived overnight to Day 2.
- [ ] **Don't assume pandoc.** The prompts lean on asking Claude directly; `read_eln.py` is
      the fallback. Fine if there's no pandoc anywhere.

## Real ELNs aren't markdown (and that's the point, not a problem)

Actual notebooks are Google Docs, Benchling, Word, Notion. Two ways in: **export** (review a
downloaded `.docx`/`.pdf`) or **live over MCP**. We export — robust with a full room, and a
`.docx` keeps the hyperlink text/target split that carries trap #2. The live-MCP path is
Lesson 6, so it's a handoff, not my problem to solve. `formats.md` is the participant-facing
version of this, and it quietly reinforces the workshop's "sharing: GitHub vs Drive/OneDrive"
thread while it's at it.

## Windows / OneDrive / WSL (my machine, specifically)

The workshop path lives under OneDrive
(`…\OneDrive\Documents\ws\ClaudeWorkshop\lessons\05-eln-reviews`). Things to watch:

- **OneDrive vs an active working dir** — file locks, "conflicted copy" duplicates, `.git`
  churn. For the live session I'll copy `ws` somewhere unsynced (`C:\ws`) or just pause
  OneDrive while teaching. Learned this one the hard way; not doing it live.
- **WSL** — reaching the OneDrive path through `/mnt/c/...` works but is slow and adds
  locking weirdness. For the demo I'd rather run from the Linux side (`~/projects/`), and I
  will *not* be editing the same files from Windows and WSL at once.
- **CRLF** — cosmetic here; ignore it, or `git config core.autocrlf true` and move on.

## Slides

Built: `lessons/05-eln-reviews/slides/index.html` (off `instructors/presentation-template/`) —
a 20-slide deck: title / who-I-am, the AI-as-leverage framing, a "read one by hand first"
warm-up, the hands-on as three gradual-release passes (**watch me → together → on your own**),
takeaways, and the Lesson-6 handoff. Print to a 16:9 PDF from the browser (Ctrl/Cmd-P,
"Background graphics" on). Note the deck's three-pass framing is more structured than the
README's four-step flow — same beats, just paced explicitly; reconcile the two if you tighten
either.
