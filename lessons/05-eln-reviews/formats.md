# Real ELNs aren't markdown (a quick reality check)

Let's be honest about something the tidy version of this lesson glosses over: almost
nobody's lab notebook is a nice markdown file in a repo. It's a Google Doc, or Benchling,
or a Word doc, or Notion, or that one Evernote you swear you'll migrate someday. So how
does Claude review *that*? Two ways, and both are worth knowing.

## The two ways in

**1 · Export it, then review the file.** Download the entry as a `.docx`, `.pdf`, or
`.html`, drop it next to your analysis, and review that. It works offline, needs no
sign-in, and won't fall over when twenty of us do it at once. Bonus: a Word doc (or an
exported Google Doc) *keeps its hyperlinks* — the visible text and the actual destination
travel separately — which is exactly the thing a good review needs to see. This is the
path we use today.

**2 · Connect to it live over MCP.** Point Claude straight at the source — Google Drive,
Notion, Benchling's API. More like how you'd really work day to day, and honestly the
better long-term answer — but live auth for a whole room is asking for trouble mid-session.
Good news: that's literally the next hour (Lesson 6, MCP servers), so we let that lesson
show the live path and keep our own hands clean here.

## Getting each flavor into reviewable shape

| Your ELN | Export path | Live path |
|---|---|---|
| Google Docs | File → Download → **Word (.docx)** or **PDF** | Google Drive connector / MCP |
| Word / OneDrive | already a `.docx` — just use it | OneDrive / SharePoint MCP |
| Benchling | export the entry to **PDF**, or pull it via the API | Benchling API / MCP |
| Notion | Export → **Markdown & HTML** or **PDF** | Notion connector / MCP |
| Evernote | export as **.enex** (it's XML) or **HTML** | — |
| OneNote | export the page to **Word / PDF** | Microsoft Graph MCP |

## The one thing to get right when reading a .docx

Pull the *hyperlink targets*, not just the words you can see. A lazy text dump hands you
the link's label ("tf-scan batch 3 data") and quietly drops where it actually points — so
a mislabeled link becomes invisible, which is the whole trap in today's entry. Any of
these surfaces the target:

```bash
pandoc -t markdown entry.docx        # renders links as [text](destination)
python tools/read_eln.py entry.docx  # stdlib only, no install; prints 'text' -> destination
```

Or just ask Claude, in plain English: *"pull the full text and every hyperlink's display
text and target out of this .docx."* (The `review-entry` skill does this as step zero, so
you mostly won't have to think about it.)

## Why none of this waters the lesson down

Everything a real review has to catch survives the export: the blank header fields, the
link whose text and destination disagree, and — because the analysis notebook is its own
separate thing no matter what your ELN is — the mislabeled figure and the quietly dropped
replicate. The format changes how you *read* the entry. It doesn't change what a good
review has to go check. Which, in the end, is the whole point of the lesson.
