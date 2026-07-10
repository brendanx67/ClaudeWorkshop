# Presentation template (HTML, not PowerPoint)

A single-file HTML slide deck you build and edit with Claude Code — the same
skill the workshop teaches. No PowerPoint, no build step, no dependencies. It
lives in Git, and it prints to a clean 16:9 PDF for sharing.

Instructors: **copy this folder** into your own working area (or your ClaudeLab)
and make it yours. Start from [`index.html`](index.html).

## Present it

Double-click `index.html` (or open it in any browser). **Validate full-screen** —
press **F** — before you trust how it looks; a narrow side-panel/preview browser
distorts a deck sized for a 16:9 screen.

Controls:

| Key / action | Does |
|---|---|
| → / Space / click | next slide |
| ← / ↑ | previous slide |
| Home / End | first / last slide |
| **F** | toggle full-screen |

## Edit it

Each `<section class="slide">` is one slide. Duplicate a slide, change the words.
Built-in layouts: title, bullets, dark section-opener, two-column, big statement,
and a figure/embed slide. Or just ask Claude Code:

- *"Add a two-column slide comparing X and Y."*
- *"Turn these three bullets into a simple diagram."*
- *"Make a slide with my figure `assets/result.png` and a caption."*

**Colors:** edit the four `--brand` / `--accent` variables at the top of the
`<style>` block. They default to **UW purple/gold**; swap them for any palette.

**Images/video:** drop files in an `assets/` folder next to `index.html` and
reference them (`<img src="assets/…">`).

## Print to a 16:9 PDF

1. **Ctrl/Cmd-P** in the browser.
2. Destination: **Save as PDF**.
3. **Margins: None** (or Default), and turn **ON "Background graphics"** so dark
   slides keep their color.

You get one slide per page at true 16:9. The `@page { size: 13.333in 7.5in }`
rule in the print CSS is what makes that work.

## The one non-obvious trick: embeds in a printed deck

An `<iframe>` or `<video>` can't render into a PDF. So for live/interactive
content, show the live thing on screen and a **static picture** in print:

```html
<div class="figure-wrap">
  <iframe class="screen-only" src="assets/demo.html"></iframe>
  <img class="print-only" src="assets/demo-still.png"
       alt="demo" style="width:100%;height:100%;object-fit:contain">
</div>
```

`.screen-only` is hidden when printing; `.print-only` appears only when printing.
Take a screenshot of the live embed, save it as the still, and your PDF looks
right. (See the commented example on the figure slide in `index.html`.)
