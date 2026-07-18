# Lesson 1 — GitHub and your ClaudeLab

**Day 1 · 8:00–9:00 · Brendan**

This hour is mostly *conversation*. You'll create your own repository on GitHub —
your **ClaudeLab** — and let Claude interview you to fill it. The whole trick of
the workshop: **all you have to do is explain to Claude.** You bring the ideas;
Claude builds. And when you're not sure how to explain, **have Claude ask you.**

There's deliberately more room here than instruction. The prompts below are
**examples, in your own words** — not things to copy exactly. Finish early? Keep
talking to Claude. That's the assignment.

> **Where you should be:** Claude Code open on your `ws` folder, with
> `ClaudeWorkshop` already cloned inside it. Not there? Grab an instructor — that's
> what the 8:00 hour is for.

---

## 1. Create your ClaudeLab

- **Sign in to GitHub** (the one step we saved for the room — an instructor will
  help if the browser sign-in is new).
- Then ask Claude, in your words, to **create a repository called `ClaudeLab` in
  this folder and push it to your GitHub.** Watch each step and approve it.

Open your `ClaudeLab` on GitHub — empty for now; you'll fill it next.

Three words you'll hear all morning: a **repo** is a project folder that tracks
its own history; a **commit** is a saved snapshot; a **push** sends your commits
up to GitHub. You supply the intent; Claude does the Git.

## 2. Let Claude set it up — and interview you

Rather than list folders yourself, point Claude at a recipe we've written for you:

> *"Set up the folders and files described in
> `ClaudeWorkshop/lessons/01-github-and-claudelab/skeleton.txt` in my ClaudeLab.
> Keep every file thin, and interview me wherever it says to."*

Claude makes the structure and then **asks you questions** — about your work
(→ `docs/about-my-work.md`), any rule you want it to always follow
(→ `CRITICAL-RULES.md`), and one thing you'd like to achieve (→ your first
`todos/` item). Answer freely.

That's two ideas at once: **have Claude ask you**, and — as your answers land in
files — **flush what you explain** into a knowledge base you own. Notice
`CLAUDE.md` stays short: it *points* to the other files instead of repeating them.
That's **reference, don't embed.**

## 3. Look it over, then save

Skim what Claude made — open a file or two. When it looks right:

> *"Save everything to my ClaudeLab and push it to GitHub."*

Refresh the GitHub page — your notes, rules, and first todo are there,
timestamped. A real first commit. 🎉

## 4. See it rendered

Open one of your new files — say `ClaudeLab/docs/about-my-work.md`. That's
**Markdown**: plain text with light formatting. Readable — but it can look a lot
nicer, and you'll be reading `.md` files all week.

Install **Markdown Reader** (free; Chrome or Edge; Mac or Windows):

1. Get it from the Chrome Web Store:
   [chromewebstore.google.com/…/markdown-reader](https://chromewebstore.google.com/detail/markdown-reader/medapdbncneneejhbgcjceippjlfkmkg)
2. Browser **Extensions** (puzzle-piece icon) → **Markdown Reader** → **Manage
   extension** → turn **ON** "**Allow access to file URLs**." *(The step everyone
   misses — without it, it won't render files on your computer.)*

Now open that same file in Chrome or Edge — headings, links, and lists, rendered. 🎉

## Keep going (or if you have time)

- Add a rule to `CRITICAL-RULES.md` the moment you notice a preference.
- Once you have a few files, ask Claude to **read your repo and write a `TOC.md`**
  — a map of your ClaudeLab.
- Or just keep talking to Claude about your work, and save anything worth keeping.
  That's the real skill.

## Up next

You just did the first half of a pattern you'll see all workshop: **interview →
spec → demo.** You had Claude *ask* you, then *flushed* your answers into files in
`docs/`. In **Session 2** you'll flush the same kind of idea a different way —
asking Claude to turn it into a working HTML page you can see and click. A spec
and a demo are both ways of capturing what you explained: one reads, one runs.

## You're on track when

- [ ] `ClaudeLab/` sits next to `ClaudeWorkshop/` in `ws`, and is on your GitHub.
- [ ] It has `CLAUDE.md`, `CRITICAL-RULES.md`, `docs/about-my-work.md`, and
      `todos/{active,backlog,completed}`, with a first commit from today.
- [ ] One todo in `active/` or `backlog/`, named the workshop way
      (`TODO-YYYYMMDD-...` if you started it today).
- [ ] You can say what *commit* and *push* mean — and what *"reference, don't
      embed"* is protecting you from.
- [ ] **Markdown Reader** installed — your `.md` files render in the browser.

## What you take with you

- A repo you own and keep using — this workshop and beyond.
- The **multi-repo root**: `ws` now holds two repos; add a third anytime with
  *"clone it into this folder."*
- The habit at the heart of the week: **explain to Claude, let it ask you, and
  flush what you explain into a knowledge base you own — keeping the hub thin.**

---

*Snagged? Nothing here is fragile. Ask Claude to explain the current state, or wave
over an instructor.*
