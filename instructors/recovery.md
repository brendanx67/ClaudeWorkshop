# Recovery — getting a straggler to the start line

**For instructors.** Someone arrived without doing the pre-work, or their setup
half-worked. You have about fifteen minutes before Lesson 1 needs them ready.

From a truly bare machine this takes **~11 minutes** of mostly waiting on
downloads, measured twice in a clean Windows Sandbox. It fits — but only if you
start now and don't diagnose anything you don't have to. When in doubt, reinstall
rather than investigate.

---

## First, two questions. Ask them before anything else.

### 1. "Do you have a paid Claude plan you can log into right now?"

### 2. "Do you have a GitHub account you can log into right now?"

**Both yes** → go to *The eleven-minute path* below.

**Either no** → stop. You cannot fix this in fifteen minutes, and trying will
cost them the session *and* your attention for the next hour.

Say so kindly and give them a real plan:

- **This hour, they watch.** Sit them beside someone with a working machine —
  paired is genuinely fine, and they'll follow Session 1 better as an observer
  than as someone fighting an installer.
- **They fix it during the coffee break**, not during a session. A paid plan is a
  few minutes at [claude.ai/upgrade](https://claude.ai/upgrade). A GitHub account
  is [github.com/signup](https://github.com/signup) — but if the blocker is
  **two-factor** (lost phone, dead authenticator, forgotten password), that is
  account recovery on GitHub's timetable, not ours. Nobody here can shortcut it.
- **Day 2 is a clean start.** Sessions 4–6 stand on their own. Tell them that
  plainly, so the morning doesn't feel like a write-off.

The one thing not to do is spend the hour trying. Two people fixing accounts is
two people; an instructor stuck with them is a third of the room's support.

---

## The eleven-minute path

Do these in order. Each step gates the next.

### 1. Claude Desktop — use this link

> **<https://claude.com/download?open_in_browser=1>**

Use this URL rather than any installer on a flash drive: it serves the current
build, so it skips the self-update prompt that costs several minutes.

Install, launch, sign in with their Claude account.

### 2. Set the working folder — and make `ws` from inside the picker

Claude Desktop → **`</> Code`** tab → set the working folder. A folder picker
opens. Go to **Documents**, **create a new folder called `ws` right there**, and
choose it. Don't send them to File Explorer first; the picker does both jobs.

Claude then asks whether the folder is trusted — **yes**.

### 3. Git — Claude offers it, and the quit everyone misses

Claude Desktop now says Git is needed and offers to open the download page. Click
**OK** and it lands on the right URL — nothing to search for.

Run the installer and **click Next through every screen, then Finish.** Every
default is correct. Don't read the options with them.

Then **fully quit Claude** — closing the window is not enough:

- **Windows:** system tray by the clock → click **^** to show hidden icons →
  right-click the Claude icon → **Quit**. Reopen from the Start menu.
- **Mac:** **⌘Q**, then reopen.

The Code tab will not see Git until you do this. If someone says "I installed Git
and it still says Git is required," this is why, every time.

### 4. One paste

```
Set up this computer for the workshop from here. Install the GitHub CLI and Python 3 if they aren't already installed — but don't sign me in to GitHub, I'll do that at the workshop. Then clone https://github.com/brendanx67/ClaudeWorkshop into this folder, and tell me what you installed. This completes the pre-workshop setup.
```

Approve each step as Claude asks. This installs the GitHub CLI and Python and
clones the repo — no sign-in needed, it's public.

**Python version doesn't matter.** Runs land on 3.13 or 3.14; both work for
everything this week. Don't spend a minute on it.

### 5. Markdown Reader — do this *while* Claude is working

Don't wait for the paste to finish. Claude will be several minutes on `gh`,
Python, and the clone, and this is the free minute in the whole recovery. Move to
the browser and install the extension now.

1. [Chrome Web Store — Markdown Reader](https://chromewebstore.google.com/detail/markdown-reader/medapdbncneneejhbgcjceippjlfkmkg)
2. **Extensions** (puzzle-piece icon) → **Markdown Reader** → **Manage
   extension** → turn **ON** "**Allow access to file URLs**."

Step 2 is the one everyone misses. Without it, nothing on their own disk renders.

### 6. The start line

Open in their browser:

```
ws / ClaudeWorkshop / lessons / 01-github-and-claudelab / README.md
```

If Windows asks which program to open `.md` files with, pick Edge or Chrome — if
neither is listed, *"Choose an app on your PC"* and browse to
`C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` or
`C:\Program Files\Google\Chrome\Application\chrome.exe`.

**Headings and links, not `#` marks** — that's the finish line. They're now where
everyone else started, and Lesson 1 takes it from there.

---

## While you're helping

- **GitHub sign-in is in Lesson 1, not here.** Don't get ahead of it; they'll do
  it with the room.
- **Never watch a progress bar together.** Downloads are most of these eleven
  minutes. Markdown Reader is deliberately parked on top of the longest wait —
  look for other overlaps like it, and talk them through what's coming next.
- **Don't debug — reinstall.** Anything odd in a half-finished setup is faster to
  replace than to understand, and you don't have the time.
- **Hand them off when they hit the start line.** Say who to wave at next, and
  get back to the room.
