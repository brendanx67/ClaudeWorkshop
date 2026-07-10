# Lesson 1 — GitHub and your ClaudeLab

**Day 1 · 8:00–9:00 · Brendan**

This hour is mostly *conversation*. You'll talk to Claude about your own work,
and along the way you'll learn to keep what's worth keeping — in your own
repository on GitHub, your **ClaudeLab**. Claude does the mechanics; you bring the
ideas.

There's deliberately more room here than instruction. The prompts below are
**examples, in your own words** — not things to copy exactly. Finish a step early?
Keep talking to Claude and see where it goes. That's the assignment.

> **Where you should be:** Claude Code open on your `ws` folder, with
> `ClaudeWorkshop` already cloned inside it. Not there? Grab an instructor — that's
> what the 8:00 hour is for.

---

## 1. Just start talking

Before any setup, tell Claude what you do and let it interview you. Something like:

> *"I'm a [what you do]. Ask me a dozen questions about my work and what I'd like
> help with."*

Answer however you like — there are no wrong answers. This "ask me N questions"
move is one you'll reuse all week: it turns a blank page into a conversation.

## 2. Give it a home

That conversation was worth keeping. Let's put it somewhere permanent — which is
the whole reason to learn Git and GitHub.

- **Sign in to GitHub** (the one step we saved for the room — an instructor will
  help if the browser sign-in is new).
- Then ask Claude, in your words, to **create a repository called `ClaudeLab`,
  save a summary of your interview as `docs/about-my-work.md`, and push it to your
  GitHub.** Watch each step and approve it.

Open your `ClaudeLab` on GitHub — your work is online. 🎉

Three words you'll hear all morning: a **repo** is a project folder that tracks
its own history; a **commit** is a saved snapshot; a **push** sends your commits
up to GitHub. You supply the intent; Claude does the Git.

## 3. Set up your drawers

Ask Claude to make the folders you'll fill all week — **`docs/`, `scripts/`, and
`todos/` with `active/`, `backlog/`, and `completed/`** — and to leave a one-line
note in each saying what it's for. (Git only tracks files, so those little notes
are also what make the folders "real.")

Then drop the first thing you'd like to try into `todos/active/`. Think of it this
way: **`docs/` is what you want Claude to know; `todos/` is the work you want to
track** (it flows `backlog → active → completed`).

## 4. Teach Claude your rules — "reference, don't embed"

This is the habit that keeps a knowledge base from turning to mush. Ask Claude to
create two files:

- **`CRITICAL-RULES.md`** — start it with one rule: *reference, don't embed* —
  keep your always-on files short, put knowledge in `docs/`, and point to it.
- **`CLAUDE.md`** — a short **hub** Claude reads every time it works in your lab,
  that *points to* your rules and docs instead of repeating them.

Notice what just happened: your `CLAUDE.md` follows the very rule it points at.
That's the whole idea — and why it stays short. Save and push.

## If you have time (or want to keep going)

- **`STYLEGUIDE.md`** — tell Claude one or two ways you like work done.
- Once you have a few files, ask Claude to **read your repo and write a `TOC.md`**
  — a map of your ClaudeLab. A nice way to watch Claude survey what you've built.
- Or just keep talking to Claude about your work, and save anything worth keeping.
  That's the real skill.

## You're on track when

- [ ] `ClaudeLab/` sits next to `ClaudeWorkshop/` in `ws`, and is on your GitHub.
- [ ] It has `docs/`, `scripts/`, and `todos/{active,backlog,completed}`, with a
      first commit from today.
- [ ] A thin `CLAUDE.md` that *references* `CRITICAL-RULES.md`.
- [ ] You can say what *commit* and *push* mean — and what *"reference, don't
      embed"* is protecting you from.

## What you take with you

- A repo you own and keep using — this workshop and beyond.
- The **multi-repo root**: `ws` now holds two repos; add a third anytime with
  *"clone it into this folder."*
- The habit at the heart of the week: **talk to Claude, then flush what you
  explained into your knowledge base — and keep the hub thin.**

---

*Snagged? Nothing here is fragile. Ask Claude to explain the current state, or wave
over an instructor.*
