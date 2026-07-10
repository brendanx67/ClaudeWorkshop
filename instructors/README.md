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

## Adding your session

1. Copy `lessons/01-github-and-claudelab/` as a structural template.
2. Name it `lessons/NN-your-slug/`; write a participant `README.md`.
3. Add your row to `lessons/README.md` and the table in the top-level `README.md`.

## Writing standard

Write for a scientist who lives in Excel and PowerPoint and has never used a
terminal. No unexplained jargon (define *repo*, *commit*, *push* the first time).
Assume Claude does the mechanics; the participant supplies intent and judgment. The
bar: they succeed by **describing what they want to Claude**, not by typing
commands.

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

## Open questions (help us close these before July 21)

- **Mac clean-machine test** — no built-in disposable VM; needs a Mac owner among
  us (fresh user account or a UTM/Parallels VM).
- **Python install on a clean machine** — not yet verified; see setup.md.
- **Pre-event email:** exact wording, whether to include a tray-quit screenshot,
  and how much we ask people to finish at home vs. at 8:00.
- Sessions 2–6: owners to draft their lesson folders.
