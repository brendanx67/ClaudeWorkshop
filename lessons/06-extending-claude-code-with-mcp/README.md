# Lesson 6 — Extending Claude Code with MCP (Python)

**Day 2 · 11:15–12:00 · Brendan**

The capstone. All week the message was one word: **explain.** This hour is the
next move — when an explanation is *settled* and you run it over and over, turn it
into a **tool** that just runs. Reliable, fewer steps, fewer tokens.

And fittingly, you won't write the Python. **You'll explain the tool you want, and
Claude will build it.** The tool is an automation of an explanation — which is the
whole point.

> **Where you should be:** Claude Code open on your `ws` folder, with
> `ClaudeWorkshop`, your `ClaudeLab`, and (from Session 2) `MyPublications` inside
> it. Python was installed during setup.

---

## What you'll build: a tiny MCP server

An **MCP** (Model Context Protocol) server is a small program that hands Claude a
list of **functions it can call** — your own tools, on tap. You'll write one in
Python, with two tools, and register it so Claude Code can use it.

## 1. A first tool — what time is it?

Start with the smallest possible tool, and a true story. Ask Claude, right now:

> *"What time is it?"*

It may guess — and guess wrong. Claude can't see your computer's clock. (Mine once
wrote `9:30 AM` in a file at `7:42`.) That's a job for a tool.

Ask Claude to build it, in your words:

> *"Make me a small Python MCP server in my ClaudeLab with one tool that returns
> the current local time. Then register it with Claude Code and tell me how to
> load it."*

Claude writes the file, installs the `mcp` package if needed, and registers it.
**Reload when it tells you to** (a new MCP shows up after a restart). Then ask the
time again — now it's exact. Look how little a tool is.

## 2. The tool you'll actually keep — status of all your repos

Now a tool worth having. Your `ws` holds several Git repos. Ask Claude:

> *"Orient yourself — what's the status of my repositories?"*

Watch what it does: it runs Git in **each folder, one at a time.** With three
repos that's slow and repetitive; in my own root it's eight. That's an explanation
you give every session — perfect to automate.

Ask Claude to add a second tool to your MCP:

> *"Add a tool to my MCP that scans the subfolders of my `ws` root and returns
> each repo's Git status — branch, changes, and whether it's ahead or behind — in
> one call."*

Reload, then ask again: *"What's the status of my repositories?"* **One tool call**
instead of one command per folder. Same answer, a fraction of the steps and tokens.
That's **explain → run**, on your own machine.

## 3. Make it automatic

The last mile: so you never have to ask. Add one line to your `ClaudeLab/CLAUDE.md`:

> *"At the start of a session, run my repo-status tool to orient yourself."*

Now every future session begins already knowing the state of your work — no prompt
needed. Commit and push your ClaudeLab; your tool travels with it.

## An MCP can go much further (so you've seen it)

You built two tools. My Status MCP has more — two worth knowing:

- **Images — screenshots and the clipboard.** A tool that hands Claude your recent
  Win+Shift+S screenshots or whatever image is on your clipboard. It changed how I
  work: instead of saving a file and pointing Claude at it, I just say *"I took two
  screenshots — the graph before and after"* and Claude sees them. (I once had it
  screenshot every slide of a deck like this one — before Claude Code had its own
  browser to do that itself.)
- **Context remaining.** Claude couldn't see how much context was left, so it kept
  guessing — *"that's been a long session, want a handoff?"* (the clock blind spot
  again). A tool that returns the real number let me add a **rule**: *don't suggest
  wrapping up until we're under 20%.* The tool supplies the fact; a rule in
  `CRITICAL-RULES.md` acts on it. (Fragile, though: it reads a file the Claude Code
  *statusline* writes — hidden plumbing that can vanish in a new setup.)

## You're on track when

- [ ] A Python MCP in your `ClaudeLab` with a **get-time** tool and a
      **repo-status** tool — registered and callable from Claude Code.
- [ ] Your `CLAUDE.md` tells Claude to run repo-status at session start.
- [ ] It's committed and pushed to your ClaudeLab.
- [ ] You can say *why* a tool beats re-explaining: reliable results, fewer steps,
      fewer tokens.

## What you take with you

- **Explanation vs. automation** — a skill is a great SOP; a tool runs the SOP for
  you. Explain by default; automate what you've explained enough times to trust.
- A tool you'll **actually use** — repo-status, in your own multi-repo root.
- The two-day arc, closed: Day 1 you *flushed what you explain* into docs. Today
  you *automated what you explain* into a tool.

---

*Instructor note (draft): verify that Claude Desktop's `</> Code` tab can register
a local MCP (`claude mcp add`) and reload it the way the console app does — the
whole hour depends on it. Keep each tool tiny; the point is the transition, not
the Python.*

*Snagged? A tool that won't load is almost always a "reload Claude Code" away. Ask
Claude to show you what it registered, or wave over an instructor.*
