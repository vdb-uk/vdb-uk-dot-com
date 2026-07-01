---
name: visual-verify
description: Build the site, serve it locally, and screenshot the changed page(s) in dark + light theme at desktop + mobile widths using dev-browser (headless browser) — so you can SEE a change is right before committing. Installs dev-browser automatically if missing.
user_invocable: true
arguments:
  - name: pages
    description: "Space-separated page paths to check, relative to the site root (e.g. `/ /about.html`). Default: the page(s) you just edited, else the home page."
    required: false
  - name: port
    description: "Port to serve dist/ on (default: 8123)"
    required: false
---

# Visually verify a change before committing

Push to `main` auto-deploys to production, and Hannah is not a developer — so
before committing a visual or content change, **look at it rendered in a real
browser**. This skill builds the site, serves it locally, screenshots the pages
you changed (dark + light theme, desktop + mobile), and shows you the images so
you can confirm the change landed and nothing else broke.

It drives [`dev-browser`](https://github.com/sawyerhood/dev-browser) — a headless
browser for agents. If it isn't installed, step 1 installs it for you. This is
pre-authorized (see `.claude/settings.json`), so it runs without permission
prompts.

## Steps

1. **Ensure dev-browser is installed** (idempotent — no-op once present):
   ```bash
   .claude/skills/visual-verify/ensure-dev-browser.sh
   ```
   If it reports Node.js is missing, tell the user to install Node
   (`brew install node` on macOS) — that's the one prerequisite.

2. **Build** `src/` → `dist/`:
   ```bash
   python3 build.py
   ```
   Expect `build.py completed ... (exit=0)`. A non-zero exit is a build error
   (usually a missing `@include`) — fix it before continuing.

3. **Serve `dist/`** locally in the background (default port 8123):
   ```bash
   python3 -m http.server 8123 --directory dist >/tmp/vdb-preview.log 2>&1 &
   ```

4. **Screenshot the page(s) you changed** — pass their paths (relative to the
   site root). Each page is captured in dark + light theme at desktop + mobile:
   ```bash
   .claude/skills/visual-verify/shoot.sh http://localhost:8123 / /about.html
   ```
   With no paths it shoots the home page. It prints each saved file as a
   `SAVED: <path>` line (files land in `~/.dev-browser/tmp/`).

5. **Look at the screenshots.** Read each `SAVED:` PNG and check, honestly:
   - the requested change is actually there and correct;
   - both **dark and light** themes look right (the site defaults to dark);
   - the **mobile** layout isn't broken (nav collapses, nothing overflows);
   - nothing else regressed on the page.

6. **Iterate or ship.** If something's off, edit `src/` / `styles.css` / `site.js`,
   re-run steps 2 & 4, and re-check. When it looks right, **stop the server**
   (`pkill -f "http.server 8123"`) and commit + push — `main` auto-deploys, then
   confirm live with the `verify-deploy` skill.

## Notes

- **Before/after against production:** `shoot.sh` takes any base URL, so you can
  capture the live site first for comparison:
  `shoot.sh https://vdb-uk.com/ /about.html`.
- **Truthful shots (handled for you):** the site defaults to a *dark* theme
  (`localStorage['vdb-theme']`), and `.reveal` sections are invisible until
  scrolled into view. `shoot.js` sets each theme explicitly and force-reveals
  those sections, so full-page captures aren't blank below the fold. See
  `docs/learnings/0003-truthful-screenshots.md` before editing `shoot.js`.
- **Never screenshot `dist/` files directly** — always go through the local
  server URL so paths, includes and assets resolve like production.
- Screenshots accumulate in `~/.dev-browser/tmp/`; dev-browser manages that dir.
