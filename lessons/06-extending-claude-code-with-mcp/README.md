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

> *"Add **just this one tool** to my Status server that returns my computer's local
> time. Install anything it needs, and register the server with Claude Code. Don't
> build any other tools yet — I want to test the restart with this one first."*

Claude writes the tool, installs the `mcp` package if needed, and registers the
server. Notice you described *what you want*, not what to name it — Claude will
call it something like `get_local_time` on its own. That's the whole week in one
line.

**Stop here — one tool only.** It's tempting to let Claude build both tools now.
Don't. The next step is a restart, and the *first* thing you want to prove is that
the restart flow works — and the local-time tool is the simplest possible thing to
prove it with. A one-line tool that either says the right time or doesn't. Get that
easy win before anything more moving can go wrong.

### The one manual step: restart Claude

**A new or changed MCP won't show up until you fully restart Claude** — the same
quit-and-reopen you did during setup. Claude can't do this for you; it's running
*inside* the app you have to restart.

- **Windows:** find the Claude icon in the system tray by the clock (click the
  **^** to show hidden icons), right-click it, choose **Quit**, then reopen.
- **Mac:** press **⌘Q**, then reopen.

*(In the Claude Code console app this is just `/exit` then `claude --resume`.
Claude Desktop makes you do the two-click quit instead.)*

**Reopen on your `ws` folder** — the same folder you registered from. Your Status
server belongs to that folder; open a different one and the tool won't be there.
Ask again: *"What time is it?"* Now it's exact. Claude called your tool.

**This is the checkpoint.** Don't move on until the time comes back right. If it
does, you've proven the whole pipeline — a tool you described, built, registered,
and loaded through a restart — on the simplest possible tool. That's the easy win.
Everything after this is just more tools through the same door. (If it *doesn't*
come back, it's almost always the restart: a window close instead of a full quit,
or reopening a different folder. Fix that here, where there's only one tiny tool in
the way.)

## 3. Second tool: status of all your repos

Only now that the time tool round-trips, add the second one. Back in your `ws`
folder, ask Claude:

> *"Orient yourself. What's the status of my repositories?"*

Watch it run Git in **each folder, one at a time.** That's an explanation you give
every session, and a perfect thing to automate:

> *"Add a tool to my Status server that scans the subfolders of my `ws` root and
> reports each repo's Git status: branch, changes, and whether it's ahead or
> behind, all in one call. This tool shells out to Git, so pass
> `stdin=subprocess.DEVNULL` on every subprocess call — otherwise it hangs."*

### The one gotcha worth knowing before it bites (Windows)

That last clause saves real pain. A subprocess launched from *inside* an MCP
server inherits the server's **stdin** — the very channel Claude talks to it over.
On Windows that makes each Git call hang for **minutes**, even though the identical
command runs in a fraction of a second in a terminal. The symptom is unmistakable:
the clock tool answers instantly, but repo-status just sits there and eventually
you give up and kill it.

The fix is one argument — `stdin=subprocess.DEVNULL` on every `subprocess` call —
so the Git commands don't inherit that pipe. If you hit the hang before adding it,
tell Claude exactly that:

> *"The repo-status tool hangs for minutes but the clock is instant. Pass
> `stdin=subprocess.DEVNULL` to every subprocess call in the server."*

With it, the same scan comes back in about a quarter-second.

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

## Keep going, and show us

Finished both tools with time left? Don't stop there.

- Add one of the two above: **images**, or **context remaining**.
- Better: build a tool for a friction **you** hit this week.
- We'll spend the last few minutes **demoing anything anyone built** beyond the
  two required tools. Bring what you made, working or not.

## You're on track when

- [ ] A **Status** MCP server in `ClaudeLab/mcp/Status/` with a **local-time**
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

*Instructor note: both pieces this hour rests on were verified on 2026-07-21 in a
clean run. (1) Claude Desktop's `</> Code` tab registers a local MCP with
`claude mcp add` — it lands at project scope, keyed to the open folder. (2) The
tray-quit reload loads the new tool: a fresh `ws`-rooted session answered the time
exactly via the tool. Two things to say from the front: the restart is a **full
quit**, not a window close (same as the Git step in setup), and a tool is scoped
to the folder it was registered from — everyone stays on `ws` all hour, so it
won't bite, but name it before someone panics that their tool "disappeared."
Keep each tool tiny so the restart stays the hardest part, not the Python.*

*One-tool-first is deliberate, from a real run: building both tools before the
restart meant the first post-restart tool call was the heavier repo-status, and a
slow round-trip there became someone's first impression of MCP. Have them register
**only** the local-time tool, restart, and confirm the clock before touching the
second tool — the first thing through the door should be the one that can't be slow
or wrong in an interesting way.*

*The slow round-trip in that run had one root cause, and it's worth knowing cold
because it presents as a mystery: on Windows, a Git subprocess spawned inside the
MCP server **inherits the server's stdin** (the JSON-RPC pipe) and hangs for
minutes — while the same command is instant in a terminal, so nobody suspects the
code. Diagnosed by driving the server over stdio: `initialize` returned in 0.74s,
the tool call never did; adding `stdin=subprocess.DEVNULL` to the subprocess calls
dropped it to 0.27s. If someone's repo-status hangs but their clock is instant,
that's the fix — every subprocess in the tool needs `stdin=subprocess.DEVNULL`. The
lesson now bakes it into the build request, but call it out live if you see a hang.*

*Snagged? A tool that won't appear is almost always a "restart Claude" away. Ask
Claude to show you what it registered, or wave over an instructor.*
