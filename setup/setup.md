# Setup — from "Claude Desktop installed" to ready for Lesson 1

> **Validated on a clean Windows machine (Windows Sandbox), July 2026.** The
> Windows path below reflects what actually happened on bare metal. The **Mac
> path is still untested** — flagged inline where it differs.

The goal: arrive at the workshop with the tools installed and `ClaudeWorkshop`
cloned, having done nothing that can fail on a GitHub sign-in. Sign-in happens in
the room, in Lesson 1, with instructors on hand.

## Prerequisites you install by hand

The `</> Code` tab **will not run without Git** — so Claude can't install Git for
you; you do these first, yourself.

1. **A paid Claude plan** (Pro or Max). Claude Code isn't on the free plan.
2. **Claude Desktop** — install from [claude.com/download](https://claude.com/download)
   and **let it update itself** on first launch (the download can be a version
   behind; just accept the upgrade).
3. **Git** — required before Claude Code will accept any prompt.
   - Open Claude Desktop → the **`</> Code`** tab. If it shows a red "Git is
     required" message, click through to the download page and install Git with
     the **default options** (Windows: "Git for Windows"; Mac: it will prompt for
     the Xcode command-line tools, or use [git-scm.com](https://git-scm.com)).
   - **⚠️ The gotcha:** after Git installs, the Code tab still won't see it until
     you **fully quit Claude** — not just close the window. On **Windows**,
     right-click the Claude icon in the **system tray** (the hidden-icons area by
     the clock) → **Quit**, then reopen from the Start menu. On **Mac**, **Cmd-Q**
     (or Claude menu → Quit), then reopen. *Now* the Code tab detects Git.
4. **A free GitHub account** — [github.com/signup](https://github.com/signup).
   Remember your username and the email you used. (You'll sign in at the workshop,
   not now.)

## Make your workspace and open Claude Code

1. Make an empty folder **`ws`** inside your **Documents** (Windows:
   `Documents\ws`; Mac: Finder → Documents → New Folder → `ws`).
2. Claude Desktop → **`</> Code`** tab → open the `ws` folder.

## Paste this once (after the Code tab has detected Git)

```
Set up this computer to use GitHub from here. Install the GitHub CLI if it isn't already installed — but don't sign me in to GitHub, I'll do that at the workshop. Then clone https://github.com/brendanx67/ClaudeWorkshop into this folder, and tell me what you installed. This completes the pre-workshop setup.
```

Approve the steps as Claude asks. On a clean machine this is exactly what happens:

- Claude checks for Git (present — it's a prerequisite) and the GitHub CLI.
- If the GitHub CLI is missing and there's **no package manager** (winget/choco),
  Claude downloads the **official `gh` installer directly** and installs it
  silently — verified on a machine with no winget.
- Claude clones `ClaudeWorkshop` into `ws`. **No sign-in required** — it's a
  public repo.

You're ready when Claude reports Git ✓, GitHub CLI ✓, and `ClaudeWorkshop`
cloned. GitHub sign-in is the first thing Lesson 1 does.

> A newly installed `gh` is on the PATH for **new** Claude Code sessions. If a
> follow-up command can't find `gh`, reopen the `ws` folder and try again.

## Python (needed for the Day-1 data session)

Python 3 is used later in the workshop. Plan: install it as part of pre-event
setup so it's ready. **Clean-machine Python install is not yet verified** — until
it is, treat Python as a "we'll make sure it's installed at the 8:00 hour" item
rather than a promised pre-event step.

## Notes for the teaching team

Findings from the Windows Sandbox dry run (July 2026):

- **Git must be pre-installed**; the Code tab is inert without it. This is the
  biggest change from our first draft — Claude cannot bootstrap Git.
- **The tray-quit step is the top support risk.** Expect to walk beginners
  through it; consider a screenshot in the email.
- **No package manager is fine** — Claude installed `gh` from the official MSI on
  its own. We don't need to prescribe winget.
- The bundled installer self-updated; tell people to expect the upgrade prompt.
- Still open: **Mac clean-machine test**, and **verifying Python install** on a
  clean machine.
