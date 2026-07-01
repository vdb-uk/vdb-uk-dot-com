# 0003 — Truthful full-page screenshots need theme seeding + force-reveal

- **Date:** 2026-07-01
- **Area:** build / css / tooling (visual-verify skill)

## Problem
When screenshotting a page for visual verification, a naive `page.screenshot({
fullPage: true })` lies in two ways on this site:

1. **Everything looks dark (or wrong).** The theme isn't a CSS default — `site.js`
   reads `localStorage['vdb-theme']` and applies it as `data-theme` on `<html>`,
   defaulting to **dark**. A fresh headless context has no saved theme, so you
   only ever capture the default and never see the other mode.
2. **Sections below the fold come out blank.** `.reveal` elements start at
   `opacity: 0; translateY(20px)` (class `.reveal--hidden`) and only animate in
   (`.reveal--visible`) when an `IntersectionObserver` sees them scroll into view.
   A full-page shot captures the tall page in one frame, so anything that never
   entered the viewport stays invisible.

## What we learned
To get a truthful capture you must drive the page's own state, not just point a
camera at it:

- **Set the theme explicitly** per shot: `localStorage.setItem('vdb-theme', t)`
  **and** `document.documentElement.setAttribute('data-theme', t)` for
  `t ∈ {dark, light}`.
- **Force-reveal before shooting:** for every `.reveal`, remove `reveal--hidden`
  and add `reveal--visible` so the whole page is painted.

## How to apply
This is baked into `.claude/skills/visual-verify/shoot.js` (via the `visual-verify`
skill). If you change the theme mechanism in `site.js` (the `vdb-theme` key, the
`data-theme` attribute, or the `.reveal--hidden/--visible` classes), update
`shoot.js` to match — otherwise screenshots will quietly go back to lying. The
same two rules apply to any future browser-automation check (e.g. Playwright,
`dev-browser --connect`).
