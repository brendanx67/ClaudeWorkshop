# Lesson 1 — GitHub and your ClaudeLab

**Day 1 · 8:00–9:00 · Brendan**

The real skill this hour: **talk to Claude, then flush what you explained into
files you own.** You'll create your **ClaudeLab** — your own repository on GitHub
— and start filling it the way you'll fill it all week: by explaining things to
Claude and letting Claude write them down where you'll find them again.

No commands, no setup files to wire up. Just conversation, and a place to keep it.

> **Where you should be:** Claude Code open on your `ws` folder, with
> `ClaudeWorkshop` already cloned inside it (from the pre-workshop setup — see
> [`../../setup/`](../../setup/)). Not there yet? Grab an instructor — that's what
> the 8:00 hour is for.

---

## Why put your work in a repository?

A **Git repository** ("repo") is a project folder that remembers its own history.
Each saved snapshot (a **commit**) is kept, so you can see what changed and go
back. Sending those commits to **GitHub** (a **push**) copies your work safely to
the cloud, to share or to pick up from any machine.

Three words you'll hear all morning:

- **repo** — a project folder that tracks its own history.
- **commit** — a saved snapshot, with a short note about what changed.
- **push** — send your commits up to GitHub.

You supply the intent; Claude does the Git. Watching it work and confirming each
step *is* the skill: **ask → review → confirm.**

## What we'll do

1. **Sign in to GitHub.** We connect Claude to your GitHub account — the one step
   we saved for the room. An instructor will help if the browser sign-in is new
   to you.

2. **Create your ClaudeLab.** Ask Claude in your own words, for example:

   > Create a new repository called `ClaudeLab` in this folder, connect it to my
   > GitHub, and push it. This is where I'll run experiments with Claude.

   Claude makes a `ClaudeLab/` folder next to `ClaudeWorkshop/`, starts a repo,
   creates it on your GitHub, and pushes an empty first version. **Approve each
   step and watch what it does.** See it appear on your GitHub profile. 🎉

3. **Flush your first explanation into `docs/`.** This is the habit. Tell Claude
   about your work and let it write the notes:

   > I want a `docs/` folder in ClaudeLab. Interview me for a few minutes about my
   > research and what I'm hoping to do with Claude, and write it up as
   > `docs/about-my-work.md`.

   Now Claude — today and in every future session — can read `docs/about-my-work.md`
   instead of you re-explaining yourself. That's the payoff of writing it down.

4. **Capture what you want to do next in `todos/`.** Same move, different drawer:

   > Make a `todos/` folder and start a note there for the first thing I'd like to
   > try this week: <say it in a sentence>.

   `docs/` is what you want Claude to *know*; `todos/` is the work you want to
   *track*.

5. **Save it (commit + push).** When it looks right:

   > Save everything to my ClaudeLab and push it to GitHub.

   Refresh the GitHub page — your `docs/` and `todos/` notes are there,
   timestamped. A real first commit.

## Checkpoints

You're on track when:

- [ ] `ClaudeLab/` sits next to `ClaudeWorkshop/` in your `ws` folder.
- [ ] You can open your `ClaudeLab` repo in a browser on GitHub.
- [ ] It has `docs/` and `todos/` with at least one note each, committed today.
- [ ] You can say, in your own words, what *commit* and *push* mean — and why
      writing things into `docs/` beats re-explaining them.

## What you're taking with you

- A GitHub repo you own and keep using — this workshop and beyond.
- The **multi-repo root** habit: `ws` now holds two repos; adding a third project
  later is just *"clone it into this folder."*
- The core loop: **ask → review → confirm**, and the habit of **flushing what you
  explain into your knowledge base.**

Your knowledge base grows from here. Over the week `docs/` and `todos/` are joined
by standing files at the root of ClaudeLab — a `CRITICAL-RULES.md` for things
Claude must always do, a `STYLEGUIDE.md` for how you like work done, a `TOC.md`
to keep it all findable — and, later, your own commands and skills that just
*point* into these docs. One principle underneath all of it: **reference, don't
embed.**

---

### Stuck? Quick fixes

- **"I don't see my repo on GitHub."** Ask Claude: *"Did the push succeed? Show
  me the repo URL."*
- **Asked for a password when pushing.** GitHub sign-in didn't finish — wave over
  an instructor, or ask Claude to *"sign me in to GitHub again."*
- **Made a mess.** Nothing here is fragile. Ask Claude to explain the current
  state, or grab an instructor.
