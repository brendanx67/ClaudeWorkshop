# Lesson 2 — Design with HTML and JavaScript

**Day 1 · 9:00–10:00 · Vagisha**

You build an **interactive HTML page of your own published papers, with charts of
how your citations have grown over time**, and put it on a live web address you can share.

In this session you will

- find your ORCID and pull your papers from OpenAlex, checking they are really yours
- design the page by describing what you want and letting Claude interview you
- build it, refine the look, and publish it live with GitHub Pages
- fold the whole workflow into a reusable tool you can run for anyone

**All you have to do is explain.** You bring the decisions, Claude does the fetching, the building, the
publishing.

Each step below lists **what to ask for**, and leaves the wording to you.
Turn the intent into a message for Claude. Do not aim for perfect wording. If you are unsure about something, **have Claude ask you questions so you can brainstorm**.

> **Where you should be.**
> - Signed in to GitHub.
> - Claude Desktop on its **Code** tab with a new session open on your `ws` folder.
> - Python installed, which Claude uses behind the scenes to fetch your papers.
> - Your folders from Lesson 1 look like the tree below.

```
ws/
├─ .claude/          shared rules and setup for all your projects
├─ ClaudeWorkshop/   the workshop guide, cloned during setup
└─ ClaudeLab/        your repo from Lesson 1
   ├─ CLAUDE.md
   ├─ CRITICAL-RULES.md
   ├─ docs/about-my-work.md
   └─ todos/         active, backlog, completed
```

**One thing before we start.** Paste this.

> *"For anything you do in this session, run Python with `-X utf8`."*

Claude uses Python to fetch your papers. Published work is full of accented names and Greek letters,
and by default Python on Windows crashes when it writes the first one out, partway through the fetch.

---

## OpenAlex and ORCID

Your page is built from real data, so two names to know.

**[OpenAlex](https://openalex.org)** is a free, open catalog of the world's published research. For almost
every paper it knows the authors, the venue, and how many times it has been cited, year by year.
That yearly breakdown is what provides the data for your citation charts. One limit is worth knowing. OpenAlex only breaks citations out by year from about 2012 on. Citations your older papers earned before 2012 still count in the lifetime total, but they are not broken down by year.

**[ORCID](https://orcid.org)** is a free, permanent 16-digit ID that tells you apart from every
other researcher, for example `0000-0002-1825-0097`. We will use your ORCID, not your name, to pull your papers, because names
are not unique. Do not know your ORCID? Give Claude your name and institution and have it look you up in
the **ORCID registry**, which is the place ORCIDs come from.

No ORCID, or too few papers for an interesting page? Follow along with your PI's. Michael MacCoss
at the University of Washington works well for today.

## Get set up

You are already on `ws` from Lesson 1, so the rules set up there apply to everything you do. Two
short setup steps come first.

**First, make a folder for the work.** A new repository next to your `ClaudeLab`, so everything for
this project lives in one place, ready to publish at the end and to re-run later.

> *"Make a folder called MyPublications here, make it a git repository, and keep everything for this
> project inside it. Save any code you write as reusable scripts I can run again."*

Now `ws` has a new folder next to `ClaudeLab`.

```
ws/
├─ .claude/
├─ ClaudeWorkshop/
├─ ClaudeLab/          your repo from Lesson 1
└─ MyPublications/     new, everything for this project lives here
```

**Second, set the ground rules for committing.** You will commit and push several times this session,
so it is worth telling Claude once how you want it done.

> *"In the MyPublications folder, add a rule that you never commit without first
> showing me the files you will include and a short commit message of no more than five bullet
> points, then waiting for my okay."*

From now on, **"commit it"** is all you need, and Claude shows you what it will save, displays a commit message for you to approve, and waits.
Commit whenever a piece is done. It costs nothing, and every checkpoint is easy to return to.

## Your ORCID

Skip this if you know your ORCID. If not, have Claude find it from your name and institution, and
**give you the link to the ORCID record so you can open it and confirm the name and institution are
yours** before going on. A wrong ID means a page full of someone else's work.

## Your papers from OpenAlex, and check they are yours

Have Claude pull your full publications list from OpenAlex, then do the part that matters, **check it.** Even the
right ORCID is not foolproof. When we searched Michael MacCoss's, OpenAlex handed back two papers by
a different researcher, Malcolm MacCoss. Someone who shares your last name can turn up in your
results, so this is where you catch it, before anything is built on top.

Do this in two steps.

**First, fetch.** Tell Claude what you are building, a page of your papers with charts of your
citations over time, so it knows what to pull. **Ask Claude to**

- fetch all your works from OpenAlex by your ORCID, with the details that page needs — the venue, the year, the work type, and how often each was cited each year — and save them
- ask you questions if anything is unclear
- show you a short summary once it is done — how many works, and a breakdown by type (article, review, preprint, and so on)
- **wait for you before moving on, and not build the page until you tell it to**

Skim the breakdown and tell Claude which kinds to keep. Dropping **preprints** is usually a good call,
since the published version of the same paper is already in your list, so it tidies things and clears
out the duplicate pairs in one move. Keep them if your preprints matter to you — it is your page.

**Then, check. Ask Claude to**

- review what is left and flag anything that might not be yours — for example, a paper with no co-authors in common with the rest
- show you the list, most suspicious first, with the reason, and tell you how many it flagged
- remember the ones you reject, so a re-run drops them automatically

Read the flagged ones first, then skim the rest, a paper Claude did not flag can still be wrong.
Tell Claude which are not yours. Claude should clean up the list and save a list of flagged publications.
At this point you might want to peek in the directory to see which scripts and files Claude has added. Tell Claude to **commit it**. 

## Design the page

Do not spell out the design, unless you really want to. Start the other way and let Claude interview you. **Ask Claude to**

- ask you at least 12 things it needs to know before it builds anything

Claude asks about the look, the accent color, the numbers to feature, the charts. **"You decide" is a
fine answer**, and you can change anything later.

When the questions run out, have Claude write a short spec (**todo**), the plan for building your page. **Ask Claude to**

- write a short todo that describes the page from your answers
- say how the data was fetched and cleaned up, so the whole thing can be re-run
- save it in your `ClaudeLab` under `todos/active`, since it is the plan for a piece of ongoing work
- name the todo `TODO-YYYYMMDD-...` per the convention introduced in Lesson 1.
- wait for you to approve the todo before building anything.

Review the plan. Fixing a plan is quick. When it looks right, say **"commit it."**

**NOTE**: The todo lives in `ClaudeLab`, a different repo from `MyPublications`, and Claude commits it there.
Your session is open on `ws` so Claude can reach both.

Now tell Claude to build `index.html`. The todo and the page are **the demo**, your explanation made
real. **Open the file in your own browser and review it.** Claude may attempt to show you a preview but it can be hit or miss.
**Commit** this first version. The commit lands in `MyPublications`.

## Make it yours

This is the design heart of the hour. Look at the page, tell Claude what to change, refresh, review
again. Color, headings, a dark-mode toggle, another chart, a link from each title to its DOI,
whatever you want. It is a conversation, not a form. Say what looks wrong and what you want instead. Want a chart but are not sure
which kind? Have Claude suggest a few and pick one. If something looks empty or off, say so.
**Commit** when it looks right.

## Put it online

**GitHub Pages** turns a public repository into a live website, for free. Your page is a single
`index.html` in `MyPublications`, so two facts are all that matter. Pages needs the repository to be
**public**, which is fine here, it is public research, and it can serve straight from the
**repository root**, where your file already sits.

**Ask Claude to**

- create a public GitHub repository called MyPublications from this folder
- push everything to it
- publish the page to GitHub Pages and tell you the live URL
- ask questions if anything is unclear

Claude runs the git commands one step at a time, and you approve each one. If it cannot turn on GitHub Pages for some reason, 
ask it to outline the steps so that you can do it manually. After GitHub Pages is turned on, a minute later your page is live at
`https://<your-username>.github.io/MyPublications/`. Share the link with anyone.


Your page is live, so the todo is done. Tell Claude to move it from `todos/active` to
`todos/completed` in your `ClaudeLab` and **commit it** there. That closes the todo the workshop way,
and it is the same cross-repo commit you made when you saved the todo. Claude should be able to handle it seamlessly. 

## Turn it into a tool

The payoff. You did not just make a page, you made all the parts of a page-maker — a fetch script, an
exclusions list, and a page design template you can reuse. Fold them into a **skill** you can run for
anyone, your PI, a labmate. **Ask Claude to**

- package this into a publications-page skill that takes a name or ORCID and an organization
- reuse your fetch script, and turn your page into a template, keeping both in the skill folder so it stands alone
- not re-interview you, but always confirm the ORCID first and show you any flagged papers before
  building
  
Your prompt could simply be:

> *"Turn the work we did in this session into a publications-page skill that takes as input a name or
> ORCID and an organization, and produces a standalone HTML page."*


The rule is **bake in the design, re-check the facts.** The slow parts, the interview and the look,
get frozen into the template. The two things it must never skip, the ORCID and the flagged papers,
stay as quick checks, because skipping them publishes a page from unchecked data.

To try it now, run `/reload-skills` and ask Claude in words to run it, for example *"run the
publications-page skill for my PI."* You will see a warning that the command is not recognized yet.
Ignore it. That only means it is not in the type-ahead menu until you next restart Claude. Asked in
words, it still runs. Refreshing your own page is then seconds. Building one for your PI is a couple
of minutes, the flag check still happens, but the design work is gone.

## Keep going (or if you have time)

- A search box, more stat cards, or a papers-per-year chart.
- A one-line intro about you or the lab under the title.
- Re-fetch from OpenAlex later to refresh the numbers, your `publications-page` skill makes it a one-liner. Ask Claude how to
  automate it with GitHub Actions.

## You're on track when

- [ ] You checked your fetched papers and dropped any that were not yours.
- [ ] A page of your papers with at least one chart is open in your browser.
- [ ] It is live at a `github.io` address you can share.
- [ ] You packaged the workflow into a `/publications-page` skill.

## What you take with you

- A live, shareable page you built by describing it, not by coding it.
- The reflex to **check what Claude did**, especially when it tells you it succeeded.
- The design loop, look, ask, look again.
- A `/publications-page` skill that turns your one-off page into a tool, **a page-maker you can use for anyone.**

---

*Snagged? Nothing here is fragile. Ask Claude to explain the current state, or wave over an
instructor.*
