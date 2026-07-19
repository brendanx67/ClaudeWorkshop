# Lesson 6 — Extending Claude Code with MCP (Python)

**Day 2 · 11:15–12:00 · Brendan**

The capstone. All week the message was one word: **explain.** This hour is the
next move. When an explanation is settled and you run it over and over, turn it
into a **tool** that just runs: reliable, fewer steps, fewer tokens.

And you won't write the Python. **You'll explain the tool you want, and Claude
will build it.** The tool is an automation of an explanation, which is the whole
point.

> **Where you should be:** Claude Code open on your `ws` folder, with
> `ClaudeWorkshop`, your `ClaudeLab`, and (from Session 2) `MyPublications` inside
> it. Python was installed during setup.

---

## What you'll build

A small MCP server called **Status**, living in your `ClaudeLab`, with two tools
you build by explaining what you want. (It's a tiny echo of the Status MCP behind
the workshop.)

## 1. A home for your tools

Ask Claude to set up a place for tools in your ClaudeLab:

> *"In my ClaudeLab, make an `mcp/` folder with a short README that says this is
> where my MCP servers live. Inside it, start a new MCP server called `Status`."*

Now your ClaudeLab has `mcp/Status/`: an empty server, ready for its first tool.

## 2. First tool: what time is it?

A true story first. Ask Claude:

> *"What time is it?"*

It may guess, and guess wrong. Claude can't see your clock. (Mine once wrote
`9:30 AM` at `7:42`.) That's a job for a tool.

> *"Add a tool to my Status server called `GetLocalTime` that returns my
> computer's local time. Install anything it needs, and register the server with
> Claude Code."*

Claude writes the tool, installs the `mcp` package if needed, and registers the
server.

### The one manual step: restart Claude

**A new or changed MCP won't show up until you fully restart Claude** — the same
quit-and-reopen you did during setup. Claude can't do this for you; it's running
*inside* the app you have to restart.

- **Windows:** find the Claude icon in the system tray by the clock (click the
  **^** to show hidden icons), right-click it, choose **Quit**, then reopen.
- **Mac:** press **⌘Q**, then reopen.

*(In the Claude Code console app this is just `/exit` then `claude --resume`.
Claude Desktop makes you do the two-click quit instead.)*

Reopen on your `ws` folder and ask again: *"What time is it?"* Now it's exact.
Claude called your tool.

## 3. Second tool: status of all your repos

Back in your `ws` folder, ask Claude:

> *"Orient yourself. What's the status of my repositories?"*

Watch it run Git in **each folder, one at a time.** That's an explanation you give
every session, and a perfect thing to automate:

> *"Add a `GetRepoStatus` tool to my Status server that scans the subfolders of my
> `ws` root and reports each repo's Git status: branch, changes, and whether it's
> ahead or behind, all in one call."*

**Restart Claude again** (the same quit-and-reopen). Then ask once more:
*"What's the status of my repositories?"* **One tool call** replaces one command
per folder. Same answer, a fraction of the steps and tokens. That's **explain then
run**, on your own machine.

## 4. Make it automatic

The last mile, so you never have to ask. Add one line to your
`ClaudeLab/CLAUDE.md`:

> *"At the start of a session, run my repo-status tool to orient yourself."*

Now every future session begins already knowing the state of your work. Commit and
push your ClaudeLab. Your Status server travels with it.

## An MCP can go much further (so you've seen it)

You built two tools. My Status MCP has more, and two are worth knowing, both the
same tiny shape:

- **Images: screenshots and the clipboard.** A tool that hands Claude your recent
  Win+Shift+S screenshots or whatever image is on your clipboard. It changed how I
  work: instead of saving a file and pointing Claude at it, I just say *"I took two
  screenshots, the graph before and after,"* and Claude sees them. (I once had it
  screenshot every slide of a deck like this one, before Claude Code had its own
  browser to do that itself.)
- **Context remaining.** Claude couldn't see how much context was left, so it kept
  guessing *"that's been a long session, want a handoff?"* (the clock blind spot
  again). A tool that returns the real number let me add a **rule**: *don't suggest
  wrapping up until we're under 20%.* The tool supplies the fact; a rule in
  `CRITICAL-RULES.md` acts on it. (Fragile, though: it reads a file the statusline
  writes, so it can vanish in a new setup.)

## You're on track when

- [ ] A **Status** MCP server in `ClaudeLab/mcp/Status/` with a **GetLocalTime**
      tool and a **repo-status** tool, registered and callable from Claude Code.
- [ ] You **restarted Claude** to load each new tool (the quit-and-reopen).
- [ ] Your `CLAUDE.md` tells Claude to run repo-status at session start.
- [ ] It's committed and pushed to your ClaudeLab.
- [ ] You can say *why* a tool beats re-explaining: reliable results, fewer steps,
      fewer tokens.

## What you take with you

- **Explanation vs. automation** — a skill is a great SOP; a tool runs the SOP for
  you. Explain by default; automate what you've explained enough times to trust.
- **You don't write the tool. You explain it.** Spot where a tool would beat the
  steps, ask Claude to build it, ask Claude to keep improving it.
- The two-day arc, closed: Day 1 you *flushed what you explain* into docs. Today
  you *automated what you explain* into a tool.

---

*Instructor note (draft): the load-bearing unknowns are (1) that Claude Desktop's
`</> Code` tab can register a local MCP (`claude mcp add`) at all, and (2) that the
tray-quit reload actually loads new tools. Rehearse both before the day. The
restart is the friction that will trip people; keep each tool tiny so a restart is
the hardest part, not the Python.*

*Snagged? A tool that won't appear is almost always a "restart Claude" away. Ask
Claude to show you what it registered, or wave over an instructor.*
