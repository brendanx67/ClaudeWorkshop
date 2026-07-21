# For the teaching team (and any Ambassador reading along)

These notes are open on purpose. Six of us are building this workshop, and we'd be
glad if other Claude Community Ambassadors borrowed from it — so this folder
records not just *what* the workshop is but *why* we made the calls we did.

## The mental model

Two repositories, side by side under a single root folder (`ws`) that Claude Code
opens:

- **ClaudeWorkshop** (this repo) — the **textbook**: lessons, setup, these notes.
  Shared and cloned by everyone. It has no `claude/` folder, no `CLAUDE.md` — it's
  reference material, not a working environment.
- **ClaudeLab** — the participant's **lab**: a repo *they* create and own on
  *their* GitHub, where they run experiments and build a knowledge base. Created
  in Lesson 1.

We deliberately did **not** call the participant repo "lab-notebook" — too
grandiose, and it sounds like we're replacing their real one. "ClaudeLab" is a
place to experiment, not a system of record.

**Three `CLAUDE.md` cases, resolved differently** (a common point of confusion):

- `ws`-root `CLAUDE.md` (multi-repo root) — **deferred.** In pwiz-ai it was a long
  time before this earned its place; we don't start with one.
- `ClaudeWorkshop/CLAUDE.md` — **none.** The textbook is reference material.
- `ClaudeLab/CLAUDE.md` — **yes.** The participant's standing instructions, which
  Claude auto-reads whenever it works inside their lab. It's the **hub** of their
  knowledge base: thin, and pointing into `docs/`, `todos/`, and later files.

## Decisions we've settled

- **Setup is minimal before the event; auth happens in the room.** Pre-event, a
  participant installs Git + GitHub CLI + Python and clones the (public)
  ClaudeWorkshop repo — none of which can fail on a browser sign-in. GitHub
  `gh auth login` is the *first* thing Lesson 1 does, with instructors circulating.
  Rationale: sign-in is the single most confusing step; do it with help, and don't
  send anyone home feeling they flunked the homework.
- **Hour one teaches a habit, not plumbing.** No slash command, no `claude/`
  folder, no junction to start. The lesson is: talk to Claude, and flush what you
  explained into files you own (`docs/`, `todos/` first). Commands, skills, and the
  `.claude` junction come later, once there's a reason for them.
- **Reference, don't embed.** A principle we teach explicitly: `ClaudeLab/CLAUDE.md`
  is the thin hub Claude reads every time; it points into `docs/` (and `todos/`,
  and standing files) rather than embedding everything. The knowledge base grows
  `CLAUDE.md` + `docs/` + `todos/` → root `CRITICAL-RULES.md` / `STYLEGUIDE.md` /
  `TOC.md` → `claude/` commands + skills.
- **Setup by natural language, not a command.** Participants point Claude at
  `setup/setup.md` in plain English rather than running a wired-up command — which
  is itself their first taste of pointing Claude at a doc.

## Workflow on this repo

- **Branch per piece of work** (e.g. `vagisha/design-lesson`). Don't commit
  straight to `main`.
- **Open a PR** for anything beyond a typo, so the rest of us see the thinking.
- **Keep `main` runnable** — someone should always be able to clone `main` and get
  a working setup → Lesson 1.

## Slides in HTML, not PowerPoint

We'd like instructors to build their talks as HTML with Claude Code — it models
the exact skill participants learn, lives in Git, and prints to a clean 16:9 PDF.
Start from [`presentation-template/`](presentation-template/) (UW-branded,
single file, no build step). Copy it into your session's
`lessons/NN-.../slides/` folder and make it yours. Not mandatory — but if you
try it, you'll have a better sense of what we're asking participants to do.

**The template lives in `instructors/`, but finished decks live in `lessons/`.**
That's on purpose: the template is an instructor tool an attendee never needs,
but a finished deck is *for* attendees — they may refer back to it during the
hands-on. See "Adding your session" for exactly where things go.

## Adding your session

1. Copy `lessons/01-github-and-claudelab/` as a structural template.
2. Name it `lessons/NN-your-slug/`; write a participant `README.md`.
3. Add your row to `lessons/README.md` and the table in the top-level `README.md`.

**Where each file goes** — the test is "does an attendee need this?":

- **Slide deck** → `lessons/NN-your-slug/slides/index.html` (for attendees; built
  from the template).
- **Data / files participants use** → in `lessons/NN-your-slug/`.
- **Instructor-only material** (answer keys, offline backups, host notes) →
  `instructors/NN-your-slug/`.

## Writing standard

Write for a scientist who lives in Excel and PowerPoint and has never used a
terminal. No unexplained jargon (define *repo*, *commit*, *push* the first time).
Assume Claude does the mechanics; the participant supplies intent and judgment. The
bar: they succeed by **describing what they want to Claude**, not by typing
commands.

**Small instructions, wide-open space — not a copy-paste script.** Don't write a
session as a chain of prompts to paste. Give a small nudge, then leave room for
the participant to talk to their own Claude and go their own way. When you show a
prompt, mark it clearly as *an example, in your own words* — never "paste this."
Favor the **interview opener**: the standout session at Code with Claude SF began
with just *"I want to build a check-splitting app. Ask me 12 questions,"* then
*"write a spec,"* then *"make a demo"* — three tiny instructions, a full hour of
open exploration, everyone in a different place. Aim for that shape. A participant
who finishes early should have somewhere to keep going, not a wall.

**Recurring named concepts** (reinforce them by name across sessions):

- **All you have to do is explain (to Claude).** The master idea: the participant
  brings the intent and explains it; Claude does the building. Everything below
  serves this. Two techniques sit under it:
  - *Have Claude ask you* — when they don't know where to start, let Claude
    interview them instead of straining to explain everything up front. The most
    unlocking move for a beginner.
  - *Flush what you explain* — capture the explanation in a durable artifact. A
    Markdown **spec** and a **DHTML demo** are both flushes — the same move in
    different media (one reads, one runs) — alongside `docs/` and `todos/`.
- **Reference, don't embed** — keep the always-on hub (`CLAUDE.md`) thin; put
  knowledge in `docs/` and `CRITICAL-RULES.md` and point to it. **Deeper cut
  (worth teaching): the wrapper is tool-specific, the knowledge is not.**
  `CLAUDE.md` is the thin, *Claude Code-specific* layer; the files it points to
  hold *tool-agnostic* know-how that works just as well pasted into ChatGPT,
  Cursor, or Copilot. Swap the wrapper, keep the knowledge — **no lock-in.** So a
  tool-specific instruction ("use the question interface") belongs in `CLAUDE.md`;
  a general one ("pace your questions") belongs in `CRITICAL-RULES.md`.
- **Interview → spec → demo** — the check-splitting arc, Day 1 in miniature:
  Lesson 1 does the interview and the spec; Lesson 2 does the demo.

## What the Windows clean-machine test settled (July 2026)

Ran the full flow in Windows Sandbox. Key findings, now baked into
[`../setup/setup.md`](../setup/setup.md):

- **Git is a hard prerequisite.** The `</> Code` tab won't accept *any* prompt
  until Git is installed, so "Claude installs Git for you" is impossible — Git is
  now a manual pre-req.
- **The tray-quit gotcha is our #1 support risk.** After installing Git you must
  fully **Quit Claude from the system tray** (not just close the window) before
  the Code tab detects it. Beginners will not guess this; a screenshot in the
  email is warranted.
- **No package manager is fine.** With no winget in the Sandbox, Claude Code found
  the official `gh` MSI and installed it silently. We don't prescribe a method.
- **Bundled installers go stale** and self-update on first launch — expected.
- **Option B held up:** install `gh` + clone the public repo, zero sign-in.
- **Python installs cleanly too:** no package manager, so Claude Code pulled
  Python 3.14 from python.org and installed it silently (PATH + `py` launcher).
  We can promise Python as a pre-event step.

## What the Session-1 dry run settled (July 20, Windows Sandbox)

Ran Session 1 end to end from the pre-event email prompt, as a participant would.

- **The question picker works — but Claude won't reach for it unaided.** The
  selectable-options interface renders correctly in the Code tab and handles
  multi-select and free-text "Other" cleanly. But through the first two INTERVIEW
  beats the session asked in prose anyway, and only switched when told to. The old
  skeleton line sat inside the `CLAUDE.md` *template body* — text being written
  into a file, not an instruction aimed at the session doing the writing. Fixed by
  adding a `HOW TO INTERVIEW` block at the top of `skeleton.txt`, addressed to
  Claude. **Closes the "question-interaction behavior" open question.**
- **Pacing held.** One question at a time, no wall of questions — rule #2 works as
  written.
- **Empty `todos/` folders need `.gitkeep`.** Git won't track an empty directory,
  so `active/` and `completed/` vanish on clone without one. Now stated in the
  skeleton rather than left to luck.
- **Session 1 runs ~15 minutes** for an experienced participant working straight
  through, from a machine already set up. Marks from the July 21 run: empty
  `ClaudeLab` at 6:30, interview starting at 8:00, "Keep going" at 15:00. An
  earlier run took ~30 minutes, but that one stopped throughout to take notes and
  discuss changes. Setup from a bare machine adds ~11 minutes before any of it —
  see [recovery.md](recovery.md).
- **Writing the `gh auth login` line into Lesson 1 is what made the difference.**
  With the command and "open PowerShell" written down, sign-in stopped being a
  conversation with Claude about how to sign in. Arriving already authenticated,
  a single sentence — *"I'm authenticated and working on Lesson 1; I need to
  create ClaudeLab"* — is enough for Claude to start.
- **There is real headroom in the hour.** Don't trim the interview to save time;
  the interview is the lesson. Spend the slack there.

## Open questions (help us close these before July 21)

- **Mac clean-machine test** — no built-in disposable VM; needs a Mac owner among
  us (fresh user account or a UTM/Parallels VM). The whole **Windows** path is
  validated.
- **Pre-event email:** exact wording, whether to include a tray-quit screenshot,
  and how much we ask people to finish at home vs. at 8:00.
- Sessions 2–6: owners to draft their lesson folders.
