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
     you **fully quit Claude** — not just close the window. On **Windows**, find
     the Claude icon in the **system tray** by the clock — click the **^** (show
     hidden icons) if you don't see it — then right-click it → **Quit**, and
     reopen from the Start menu. On **Mac**, **Cmd-Q** (or Claude menu → Quit),
     then reopen. *Now* the Code tab detects Git.
4. **A free GitHub account you can actually log into** —
   [github.com/signup](https://github.com/signup). We connect Claude to GitHub
   together at the workshop, but **you** have to complete that sign-in, and it
   almost always needs **two-factor authentication** (a code from your phone or an
   authenticator app). This is the one step no instructor can do for you, so
   **before Tuesday:** log in to github.com in a browser, confirm your password
   and your second factor work, and **bring your phone** both mornings. Staying
   logged in on github.com makes the workshop sign-in quicker.

## Make your workspace and open Claude Code

1. Make an empty folder **`ws`** inside your **Documents** (Windows:
   `Documents\ws`; Mac: Finder → Documents → New Folder → `ws`).
2. Claude Desktop → **`</> Code`** tab → open the `ws` folder.

## Paste this once (after the Code tab has detected Git)

```
Set up this computer for the workshop from here. Install the GitHub CLI and Python 3 if they aren't already installed — but don't sign me in to GitHub, I'll do that at the workshop. Then clone https://github.com/brendanx67/ClaudeWorkshop into this folder, and tell me what you installed. This completes the pre-workshop setup.
```

Approve the steps as Claude asks. On a clean machine this is exactly what happens:

- Claude checks for Git (present — it's a prerequisite) and the GitHub CLI.
- If the GitHub CLI is missing and there's **no package manager** (winget/choco),
  Claude downloads the **official `gh` installer directly** and installs it
  silently — verified on a machine with no winget.
- Same for **Python 3** — Claude installs it from the official python.org
  installer (PATH enabled, `py` launcher included) — verified on a clean machine.
- Claude clones `ClaudeWorkshop` into `ws`. **No sign-in required** — it's a
  public repo.

You're ready when Claude reports Git ✓, GitHub CLI ✓, and `ClaudeWorkshop`
cloned. GitHub sign-in is the first thing Lesson 1 does.

> A newly installed `gh` is on the PATH for **new** Claude Code sessions. If a
> follow-up command can't find `gh`, reopen the `ws` folder and try again.

## Python (needed for the Day-1 data session)

Python 3 is used later in the workshop, and the pre-event prompt above installs
it. **Verified on clean Windows machines:** with no package manager present,
Claude Code installed Python from the official python.org installer (silent, PATH
enabled, `py` launcher) and confirmed it runs. Nothing extra to do — same "works
in new sessions" PATH note applies.

> **Any Python 3.13 or later is fine** for everything in this workshop. Dry runs
> landed on 3.13 and 3.14 and both worked. If someone's `python --version` shows
> 3.12 or older, have Claude install a current one; otherwise move on.

## Notes for the teaching team

Findings from the Windows Sandbox dry run (July 2026):

- **Git must be pre-installed**; the Code tab is inert without it. This is the
  biggest change from our first draft — Claude cannot bootstrap Git.
- **The tray-quit step is the top *software* support risk.** Expect to walk
  beginners through it; consider a screenshot in the email.
- **GitHub 2FA is the top risk we CANNOT fix onsite.** A participant who can't
  pass their own two-factor sign-in (wrong device, lost authenticator, forgotten
  password) is locked out and no instructor can rescue them. The pre-event email
  asks everyone to verify github.com login + 2FA at home and bring their phone.
  Treat "can you log into GitHub right now?" as a triage question at 8:00.
- **No package manager is fine** — Claude installed `gh` from the official MSI on
  its own. We don't need to prescribe winget.
- **`gh auth login` does NOT set the Git identity.** Signing in authenticates the
  GitHub *CLI*; Git still has no `user.name` / `user.email`, so the first commit
  stops with *"Please tell me who you are."* Every participant hits this at the
  same moment in Lesson 1. It can't move into pre-work — it has to follow sign-in,
  which we deliberately saved for the room — so Lesson 1 now covers it explicitly,
  with the GitHub **no-reply** address as the default (a real address ends up in
  commit metadata permanently).
- **Set `init.defaultBranch=main`.** Otherwise Git 2.5x prints a yellow paragraph
  about `master` on every `git init`. Harmless, but it reads as an error to a
  beginner and will generate hands.
- **Don't chase the Python version.** Runs landed on 3.13 and on 3.14, sometimes
  by reading python.org's version list and sometimes by writing a version straight
  into the download URL. Every one of them works for this workshop. 3.13 or later
  is the only bar; don't spend 8:00 triage on it.
- **Skills must live in `ws/.claude`, not inside a repo.** Tested July 20: a
  `.claude` folder inside `ClaudeLab` is *not* discovered by a session rooted at
  `ws` — only the session root and the user-level `~/.claude` are. Session 2's
  tree already assumed `ws/.claude` existed but nothing created it, so Lesson 1
  now does. Good news: `/reload-skills` is enough to pick up a new skill, and it
  appears in the type-ahead menu immediately — no restart.
- **No junctions or symlinks anywhere in the participant path.** Root-level
  `CLAUDE.md` is a thin file pointing into `ClaudeLab` instead. The real content
  stays versioned in the repo, it needs no admin rights or Developer Mode, and it
  demonstrates "reference, don't embed" in the setup itself. (Hard-linking a file
  into a repo is actively unsafe: `git checkout` writes a new inode, so the link
  silently detaches and the root copy serves stale content forever with no error.)
- The bundled installer self-updated; tell people to expect the upgrade prompt.
- Still open: **Mac clean-machine test**. (Windows path — Git prereq, `gh`,
  Python, clone — is fully validated.)
