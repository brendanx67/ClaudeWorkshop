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

> **One step at a time.** If you point Claude at this whole lesson, it can do
> every step in about a minute — and you'll have a correct repo and an empty hour.
> Ask it to stop and check in after each numbered step. The conversation *is* the
> lesson; the files are just where it lands.

**Seeing headings and links rather than `#` marks?** Then **Markdown Reader** is
working and you're set. If not, install it now (we did this together in the
opening talk): the
[Chrome Web Store](https://chromewebstore.google.com/detail/markdown-reader/medapdbncneneejhbgcjceippjlfkmkg),
then **Extensions** (puzzle-piece icon) → **Markdown Reader** → **Manage
extension** → turn **ON** "**Allow access to file URLs**" — the step everyone
misses. Every lesson this week is a `.md` file like this one.

*Windows asking which program to open `.md` files with? Pick Edge or Chrome — if
neither is listed, "Choose an app on your PC" and browse to
`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` or
`C:\Program Files\Google\Chrome\Application\chrome.exe`. Tick "Always use this
app" and you're done with that dialog.*

---

## 1. Create your ClaudeLab

- **Sign in to GitHub.** This is the one step Claude can't do for you — the
  sign-in asks questions, and Claude has no way to answer them. So you run it
  yourself, once.

  On **Windows**, open **PowerShell**: press the Start button, type `powershell`,
  and press Enter. On a **Mac**, open **Terminal** (⌘-Space, type `terminal`).
  Paste this in and press Enter:

  ```
  gh auth login --hostname github.com --git-protocol https --web
  ```

  It shows you a short code — copy it, press Enter, and paste it into the browser
  page that opens. Finish your two-factor step, so have your phone handy. When it
  says you're logged in, you're done with the terminal for the day.

  *(Grab an instructor if the browser sign-in is new to you — this is what the
  8:00 hour is for.)*
- **Then tell Claude who you are.** Signing in authenticates the GitHub *tool* —
  but Git itself still doesn't know your name and email, and your very first
  commit will stop with *"Please tell me who you are."* Ask Claude to set it up —
  your name, your email, and **`main` as the default branch for new repos.**
  Prefer your GitHub **no-reply** address over your real one: it still links
  commits to your account, but keeps your email out of every commit forever.
- Then ask Claude, in your words, to **create a repository called `ClaudeLab` in
  this folder and push it to your GitHub.** Ask for it to be **private** — you can
  open it up whenever you like, but you can't un-publish something. Watch each
  step and approve it.

Open your `ClaudeLab` on GitHub — empty for now; you'll fill it next.

Three words you'll hear all morning: a **repo** is a project folder that tracks
its own history; a **commit** is a saved snapshot; a **push** sends your commits
up to GitHub. You supply the intent; Claude does the Git.

**Then two folders and one file, once.** These live in `ws` itself, beside your
repos, and serve everything you do this week:

> *"In my `ws` folder, make a `.claude` folder for skills and commands, a `.tmp`
> folder for scratch work, and a short `CLAUDE.md` that points at my ClaudeLab's
> `CLAUDE.md` and `CRITICAL-RULES.md`. Put a one-line README in each folder."*

- `.claude/` — your skills and commands, starting in Session 2. It has to sit at
  `ws`; inside a repo folder it isn't picked up.
- `.tmp/` — scratch, outside every repo, so nothing lands in a commit by accident.
- `CLAUDE.md` — three lines pointing into your `ClaudeLab`, so Claude finds your
  rules from anywhere in `ws`. **Reference, don't embed**, applied to your setup.

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

Now open one of your own new files in the browser — say
`ClaudeLab/docs/about-my-work.md`. Rendered, like this page.

## Keep going (or if you have time)

- **Extra credit — build a skill.** Ask Claude for a small skill in
  `ws/.claude/skills/`: something you'd otherwise explain every time. Then
  `/reload-skills`, and run it by name — `/your-skill-name`. That's the ground
  Session 2 builds on.
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
- [ ] `ws` itself has `.claude/`, `.tmp/`, and a short `CLAUDE.md` — Session 2
      needs them.
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
