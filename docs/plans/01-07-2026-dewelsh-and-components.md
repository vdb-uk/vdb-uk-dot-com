# De-Welsh + Shared Components Refactor

**Status:** Proposed (planning only — no site files changed by this document)
**Date:** 2026-07-01
**Branch for implementation:** `refactor/dewelsh-components` (all work on-branch, verified locally, merged to `main` only after sign-off)

---

## 1. Objectives

Two changes, done together on one branch:

1. **Remove ALL Welsh / i18n.** Strip every bilingual construct so the site is
   plain single-language English. English text becomes inline plain text (no
   `<span data-en>` wrappers), the language toggle disappears, and every piece of
   i18n plumbing (CSS rules, JS, `lang-config.js`, the `VDB_WELSH_ENABLED` kill
   switch) is deleted.

2. **Extract shared components** (header, footer, `<head>`, scripts, and the
   duplicated CSS) so a single edit propagates site-wide. Today the same header,
   footer, ~1,300-line CSS core, and ~150-line script block are copy-pasted into
   every page. This is the real maintenance tax.

**Success = one edit, one place.** After this, changing the nav means editing one
partial; changing a colour means editing one stylesheet; there is no Welsh left to
keep in sync.

## 2. Scope & non-goals

**In scope:** all 36 HTML files, the shared CSS/JS extraction, a small build step,
and the VPS deploy-workflow change to run that build.

**Non-goals (do NOT touch):**
- Content rewrites, redesigns, or copy changes beyond removing Welsh.
- The **dark/light theme toggle** — it is *separate* from the language toggle and
  must keep working (see §5).
- The rebrand token remap (`docs/plans/30-06-2026-rebrand/`) — colours/tokens stay.
- Legal-entity strings (see §5).

## 3. Current-state inventory

Static site, no build step, plain HTML/CSS/JS, hand/AI-edited, VPS auto-deploys
`main` (cron `git pull --ff-only` every minute; nginx serves the pulled dir).

**Files (36 total):**

| Class | Count | Notes |
|---|---|---|
| Full content pages (have inline `<style>`) | 26 | `index`, `about`, `contact`, `partnerships`, `accessibility`, `privacy`, `cookies`, 6× `capabilities/`, 11× `case-studies/` |
| Redirect stubs (`projects/*.html`) | 10 | 13-line `meta refresh` → `/case-studies/…`; contain bilingual "This page has moved / Mae'r dudalen…" text |

**i18n constructs to remove** (live `grep` counts, 2026-07-01 — reproduce with the
commands in Appendix A; the execution plan's gates require these to reach **0**):

| Construct | Occurrences | What it is | Removal action |
|---|---|---|---|
| `data-en` / `data-cy` span pairs | 2,033 each | Inline content wrappers `<span data-en>X</span><span data-cy>Y</span>` | Replace whole pair with the English text `X`, inline |
| `data-en-block`/`-flex`/`-grid` (+ `cy`) | 152 / 52 / 52 | Layout-preserving variants of the above | Same: keep English element, drop Welsh, drop the `data-*` attr |
| `data-aria-label-en` / `-cy` | 205 | Localised `aria-label` | Keep English value as a plain `aria-label`, drop both data-attrs |
| `data-alt-en` / `-cy` | 37 | Localised image `alt` | Keep English value as plain `alt`, drop data-attrs |
| `data-title-en` / `-cy` on `<title>` | 23 | Localised page title | Keep English title text, drop data-attrs |
| `data-content-en` / `-cy` on meta description | 23 | Localised meta description | Keep English `content`, drop data-attrs |
| `.lang-toggle` markup + CSS | 312 refs | EN/CY button group + its styles | Delete markup and CSS |
| `data-set-lang` buttons | 78 | Toggle buttons | Delete |
| `[data-lang="en"] [data-cy]` … CSS rules | ~10 blocks/page | Show/hide rules for the span pattern | Delete entire rule group |
| `data-lang` attr on `<html>` | 26 | Drives the CSS above | Delete (keep static `lang="en"`) |
| Language-toggle JS | 23–26 pages | `setLang`, `applyLocalizedMetadata`, `applyLocalizedAttributes`, browser-lang detect, `vdb-lang` storage, langBtns | Delete from shared `site.js` |
| `lang-config.js` | 1 file | `VDB_WELSH_ENABLED` kill switch + Shift+W + `?cymraeg` unlock | Delete file + its `<script>` tags |
| Redirect-stub Welsh | 10 files | "Mae'r dudalen hon wedi symud" etc. | Reduce to English-only |

**Duplication (the components problem):**

- Every content page inlines a `<style>` block of **1,280–1,794 lines**. Diffing
  pages shows a large **shared core** (design tokens, reset, typography, `.header`,
  `.footer`, `.header__nav`, buttons, `.theme-toggle`, `.lang-toggle`, i18n rules,
  reveal/utility classes) **interleaved with** genuinely page-specific rules. It is
  *not* a clean "shared prefix + unique suffix" — extraction requires separating the
  common ruleset from per-page rules (see §6, Phase 2).
- Every content page inlines a **~50-line `<header>`** and **~60-line `<footer>`**
  that are effectively identical across pages (absolute nav links, no per-page active
  state) — prime partial candidates. *Precondition check:* confirm byte-identity
  across all 26 before extracting (Phase 1, step 1).
- Every content page inlines a **~150-line `<script>`** block: language toggle
  (remove) **plus** mobile nav, header-scroll, theme toggle, scroll-reveal, and
  smooth-scroll (all **keep**, all identical) → consolidate into one `site.js`.
- Shared external assets today: exactly one JS file, `lang-config.js` (to be deleted).

## 4. What must be preserved

- **All English copy, verbatim.** Removing a `data-en/data-cy` pair must keep the
  exact English string.
- **The theme (dark/light) toggle** — `.theme-toggle`, `data-set-theme`, `setTheme`,
  `vdb-theme` storage, `prefers-color-scheme` handling. Only the *language* toggle
  goes.
- **Legal-entity strings, unchanged:** footer `© 2026 VandenberghUK Ltd (company
  no. 12296613).` and the privacy-page data-controller "VandenberghUK Ltd".
- **No framework, source stays directly AI-editable** (Hannah's agent must be able to
  edit a page's content and the shared partials by hand).
- **Redirect behaviour** of `projects/*.html` (still `meta refresh` to the matching
  `/case-studies/…`).

## 5. Architecture decision — how to share header/footer/CSS

A build step is now permitted (fast + VPS deploy updated to run it). Options:

| Option | How | SEO / FOUC | A11y | Speed | AI-editability | Verdict |
|---|---|---|---|---|---|---|
| **A. Build-time partials + shared `styles.css` + `site.js`** | Single `build.py` inlines `_partials/*` into `src/*` → `dist/*.html`; pages link one stylesheet + one script | Full static HTML in output → **best** (no client render, no flash) | Best | Build ~ms; page load unchanged/faster (cached CSS/JS) | Edit `src/` + `_partials/`; one build command | **Recommended** |
| B. JS-injected header/footer | `fetch()`/`innerHTML` or `<vdb-header>` custom element renders chrome at runtime | Header/footer absent from initial HTML → weaker SEO, **FOUC** | Focus/landmark timing issues | No build, but runtime cost every page | Simple partials, but content not in source view | Rejected (SEO/FOUC) |
| C. Custom element w/ declarative shadow DOM | Web component per chunk | Better than B, still hydration nuance | Shadow-DOM landmark caveats | No build | More concept overhead for a hand-edited site | Rejected (complexity) |
| D. No build, keep chrome inline; only externalise CSS/JS | Move shared CSS→`styles.css`, JS→`site.js`; header/footer stay copy-pasted | Fine | Fine | No build | Header/footer edits still 26× | Partial win only |

**Recommendation: Option A.** It fully solves the "one edit, site-wide" goal
(including header/footer), keeps the deployed output as plain static HTML (no SEO or
FOUC regression), and stays trivially AI-editable. Option D is the fallback if the
build step is ever unwanted — it still captures the biggest win (CSS/JS dedup) but
leaves header/footer duplicated.

### 5.1 Proposed layout (Option A)

```
/                      # repo root
├── src/               # editable page sources (one per page)
│   ├── index.html         # <head include> + page body + <footer include> …
│   ├── about.html
│   ├── capabilities/…, case-studies/…, projects/…  (stubs stay tiny)
├── _partials/
│   ├── head.html          # meta, fonts, favicons, <link rel=stylesheet href=/styles.css>
│   ├── header.html        # nav + theme toggle (NO lang toggle)
│   ├── footer.html        # footer (legal strings verbatim)
│   └── scripts.html       # <script src=/site.js>
├── styles.css         # the shared CSS core (tokens, reset, header, footer, nav, buttons, theme, utilities)
├── site.js            # theme toggle, mobile nav, scroll-reveal, header-scroll, smooth-scroll
├── images/ favicon.* CNAME   # static assets, copied to dist as-is
├── build.py           # the build
└── dist/              # BUILD OUTPUT — what nginx serves (gitignored)
```

- Page-specific CSS stays in a small per-page `<style>` inside each `src/*.html`
  (simplest; avoids a per-page CSS-file explosion). Only the *shared core* moves to
  `styles.css`.
- Include mechanism: an explicit HTML comment marker, e.g.
  `<!-- @include _partials/header.html -->`. `build.py` (Python 3 **stdlib only** —
  no npm, no deps) reads each `src/**/*.html`, expands markers (one pass), copies
  static assets, and writes to `dist/`. For safety it builds into `dist.tmp/` then
  atomically renames over `dist/`, so a failed build never serves partial output.
  Expected runtime: **milliseconds** for 36 files.

### 5.2 Deploy-workflow change (required)

Current: nginx mounts the repo dir read-only and serves it; cron does `git pull
--ff-only`, and the pull *is* the deploy.

Change to:
1. **`docker-compose.yml`** — repoint the volume from the repo root to the build
   output: `…/vdb-uk-dot-com/dist:/usr/share/nginx/html:ro`.
2. **`/usr/local/bin/vdb-autodeploy.sh`** (on the VPS) — after a successful `git pull
   --ff-only` that advanced `HEAD`, run `cd <repo> && python3 build.py` (atomic swap),
   logging to `/var/log/vdb-autodeploy.log`. On build failure: log and keep the
   previous `dist/` (do not serve a broken build).
3. **`dist/` gitignored** — the VPS builds on pull; git stays DRY (source only).
   *Tradeoff:* direct-on-VPS edits (the old fallback) now require running `build.py`
   afterwards; the canonical workflow remains "commit to `main` & push". *Alternative
   if zero-server-build is ever wanted:* commit `dist/` and have the build run in CI
   — not recommended (noisy diffs).
4. **Pre-req check:** confirm `python3` exists on the VPS **host** (the cron/bash
   layer, not the alpine nginx container). If absent, fall back to Option D for
   header/footer, or install python3.
5. **CLAUDE.md update** — document the new `src/` + `_partials/` + `build.py` layout
   and the "edit source, not `dist/`" rule so Hannah's agent edits the right files.

## 6. Phased execution plan

All phases run on `refactor/dewelsh-components`. Each phase has a **gate** (must pass
before proceeding) and a **rollback**. Order is chosen to de-risk: build the
component machinery first (behaviour-preserving), then remove Welsh once (in single
locations), then rewire deploy, then verify + merge.

### Phase 0 — Branch & scaffold
- Create branch. Add `build.py`, `_partials/`, `src/`, gitignore `dist/`.
- Stand up a no-op/identity build that reproduces current output, to prove the
  pipeline before moving content.
- **Gate:** `python3 build.py` runs clean and fast; `dist/` populated.
- **Rollback:** delete branch.

### Phase 1 — Extract head/header/footer/scripts partials (Welsh still present)
- **Step 1 (precondition):** confirm `<header>` and `<footer>` are byte-identical
  across all 26 content pages; reconcile any drift before extracting.
- Move each page into `src/`, replacing the head/header/footer/scripts blocks with
  `@include` markers pointing at `_partials/*`. Partials still contain the Welsh
  markup at this stage.
- **Gate:** built `dist/*.html` is DOM-equivalent to the pre-refactor pages
  (visual-parity screenshots on every page + normalised HTML diff); build < 1s.
- **Rollback:** `git restore` to Phase 0.

### Phase 2 — Extract shared CSS → `styles.css`, shared JS → `site.js`
- Identify the common CSS core (tokens, reset, typography, header, footer, nav,
  buttons, theme, lang-toggle-for-now, i18n rules, utilities) and move it to
  `styles.css`, linked from `_partials/head.html`. Leave page-unique rules in each
  page's small `<style>`.
- Consolidate the shared `<script>` into `site.js` (keep theme/nav/reveal/scroll,
  keep lang JS for now), referenced by `_partials/scripts.html`. Delete the inline
  duplicates.
- **Gate:** full visual + behaviour parity (theme toggle, mobile nav, reveal,
  language toggle all still work) across all pages; `styles.css`/`site.js` exist;
  per-page `<style>` now holds only page-specific rules.
- **Rollback:** `git restore` to Phase 1.

### Phase 3 — Remove ALL Welsh / i18n
Now that chrome/CSS/JS are centralised, remove i18n in single locations plus a
per-page content sweep:
- **Shared (one edit each):** delete `.lang-toggle` markup from `_partials/header.html`;
  delete `.lang-toggle` + `[data-lang]` i18n CSS rules from `styles.css`; delete the
  language-toggle JS from `site.js`; delete `lang-config.js` + its `<script>` tags;
  remove `data-lang` from `<html>` (keep `lang="en"`).
- **Per page (content sweep):** unwrap every `data-en/data-cy` pair (and
  `-block/-flex/-grid` variants) to inline English; convert `data-aria-label-en` →
  `aria-label`, `data-alt-en` → `alt`, `data-title-en` → title text,
  `data-content-en` → meta `content`; drop all `-cy` attrs.
- **Redirect stubs:** rewrite the 10 `projects/*.html` "moved" text to English-only.
- **Gate:** every i18n `grep` in Appendix A returns **0**; visual parity holds; theme
  toggle still works; no console errors; no dangling `data-cy*`, `lang-toggle`,
  `VDB_WELSH_ENABLED`, or `lang-config.js` references.
- **Rollback:** `git restore` to Phase 2.

### Phase 4 — Deploy workflow + docs
- Update `docker-compose.yml` mount → `dist/`. Update `vdb-autodeploy.sh` to build
  after pull (atomic, logged, fail-safe). Confirm `python3` on the VPS host. Update
  CLAUDE.md (§5.2).
- **Gate:** dry-run the modified deploy script locally / in a scratch checkout
  (pull → build → serve `dist/`) and confirm a fresh clone builds a correct site;
  document the rollback command.
- **Rollback:** revert compose/script changes (they are not live until merged).

### Phase 5 — Local verification & merge
- Full-site local verification pass (§7): serve `dist/`, screenshot every page,
  confirm parity, run link/redirect checks, confirm build timing, confirm all i18n
  greps are 0.
- Complete the sign-off checklist, then merge `refactor/dewelsh-components` → `main`
  and watch the first auto-deploy + rebuild on the VPS.
- **Rollback (post-merge):** `git revert` the merge commit and push; the VPS re-pulls
  and rebuilds the previous good state. The atomic build swap means a bad build keeps
  serving the last good `dist/`.

## 7. Verification strategy

- **i18n-zero gates:** the Appendix A greps must all return 0 after Phase 3.
- **Visual parity:** serve locally (`python3 -m http.server` over `dist/`), capture a
  before (current `main`) and after screenshot of **all 26 content pages** at desktop
  + mobile widths using the browser automation tools; compare for regressions.
  Confirm the 10 redirects still land on the right `/case-studies/` page.
- **Behaviour:** theme toggle switches and persists; mobile nav opens/closes;
  scroll-reveal fires; no JS console errors on any page.
- **Build health:** `build.py` completes in well under a second; a deliberately
  broken partial fails the build **without** replacing `dist/` (atomic-swap test).
- **Legal strings:** grep confirms "VandenberghUK Ltd (company no. 12296613)" and the
  privacy data-controller are byte-unchanged.

## 8. Rollback plan (summary)

Everything lives on a branch until the final merge, so pre-merge rollback is `git
restore`/branch-delete. Post-merge rollback is `git revert <merge>` + push → VPS
re-pulls and rebuilds. The build's temp-dir + atomic rename guarantees a failed VPS
build never serves partial/broken output. The Welsh kill switch is already off, so
there is no live bilingual behaviour to lose.

## 9. Risks & open questions

- **Python3 on the VPS host** — must confirm before committing to Option A (else
  Option D). *Blocking check in Phase 4.*
- **Header/footer drift** — if any of the 26 pages has a subtly different
  header/footer, partial extraction must reconcile it first (Phase 1, step 1).
- **CSS core vs page-specific split** — the boundary is a judgement call; err toward
  moving a rule to `styles.css` only if it is truly shared, to avoid per-page
  breakage.
- **Metadata-localisation asymmetry** — 23 pages localise `<title>`/description, 26
  have the theme toggle; the shared `site.js` must not assume every element exists
  (null-guard, as the current code already does).
- **`dist/` gitignored vs committed** — recommendation is gitignore + build-on-VPS;
  revisit if a zero-server-build guarantee is later required.

## Appendix A — i18n grep reference (gates must return 0 after Phase 3)

Run from repo root against the built/`src` HTML:

```bash
grep -rlE 'data-(en|cy)\b'            --include='*.html' .   # content spans
grep -rlE 'data-(en|cy)-(block|flex|grid)' --include='*.html' .
grep -rlE 'data-aria-label-(en|cy)'   --include='*.html' .
grep -rlE 'data-alt-(en|cy)'          --include='*.html' .
grep -rlE 'data-(title|content)-(en|cy)' --include='*.html' .
grep -rl  'lang-toggle'               --include='*.html' .
grep -rl  'data-set-lang'             --include='*.html' .
grep -rlE '\[data-lang'               --include='*.html' .
grep -rl  'VDB_WELSH_ENABLED'         --include='*.html' .
grep -rl  'lang-config.js'            --include='*.html' .
grep -rliE 'cymraeg|welsh'            --include='*.html' .   # residual copy (review, not blind-delete)
```

Baseline (2026-07-01): `data-en`/`data-cy` 2,033 each; `-block` 152, `-flex` 52,
`-grid` 52; `data-aria-label-en` 205; `data-alt-en` 37; `data-title-cy` 23;
`data-content-cy` 23; `lang-toggle` 312 refs; `data-set-lang` 78. Files: 26 content
pages + 10 redirect stubs.
