# Stage 1 — Brand Foundation

**Edits covered:** 01 (logo + palette), 02 (fonts), 21 (brand kit ingest).
**Touches:** every HTML file (~24 with the design system). **Must land before Stages 3–6.**

This is the keystone. The site has **no build step** — design tokens are duplicated into a
`:root` block in every page (`index.html:22–55`, `partnerships.html:20–72`, etc.), so a
rebrand is a *repeated, mechanical* edit applied identically across files. Get the token
recipe right once, apply everywhere, then verify with grep.

---

## Pre-requisite: the brand kit is not in the repo

The brief says the kit lives in `work/vdb-brand/` (logo SVGs, `design-tokens.css`,
`design-tokens.json`, the Outfit + DM Sans font files, the written style guide).
**That folder does not exist locally.** Two paths:

- **Preferred:** Hannah supplies `work/vdb-brand/` (see Stage 7). Use the real
  `vdb-wordmark.svg` / `vdb-reversed.svg` and the kit's exact token scale.
- **Best-effort (unblock now):** the brief gives the core hexes and font names (below),
  which is enough to build the palette/type. The only true blocker is the **logo SVGs** —
  the current header logo is an *inline hand-built SVG monogram* (`index.html:1810–1824`),
  so we either drop in the supplied SVG or rebuild the wordmark inline. Do not guess the
  logo geometry; if the SVG is delayed, set the header to a clean text wordmark
  "VDB" in Outfit as a temporary stand-in and flag it.

---

## 1.1 — Palette: "Welsh Slate" red → VDB purple (edit 01)

### Target token values (from the brief's brand kit)

| Role | New value | Replaces |
|------|-----------|----------|
| **Primary** purple | `#5E1A8E` | the red `#c8283f` |
| **CTA / hero accent** orange | `#E89A3C` | — (see open Q below) |
| **Secondary** teal | `#1C9C8E` | — |
| Ink (text) | `#1E1A29` | `--slate-800/900` text roles |
| Slate (muted text) | `#5B5566` | `--slate-400/600` |
| Mist (faint text) | `#9A93A8` | lighter slate |
| Line (borders) | `#E7E3EE` | `--stone-300` / slate lines |
| Surface | `#FAF8FC` | `--stone-50/100` |
| White | `#FFFFFF` | — |

### How the current tokens are structured (what you're replacing)

Each page's `:root` defines four scales (sample from `index.html:22–55`):
- `--slate-950 … --slate-50` (10 steps) — dark UI / backgrounds / text
- `--red-700 --red-600 --red-500(#c8283f) --red-400 --red-100` — primary accent
- `--gold-600 … --gold-100` — stat figures / "gold" labels
- `--stone-300 --stone-200 --stone-100 --stone-50` — cream light-mode backgrounds

`#c8283f` appears **72× across 24 files**; the `--red-*`, `--gold-*`, `--stone-*` and
`--slate-*` custom properties are referenced hundreds of times via `var(--red-500)` etc.

### Recommended approach: remap, don't rename

Renaming `--red-*` → `--purple-*` across hundreds of `var()` call-sites is high-risk in a
no-build, per-file-duplicated codebase. Instead, **keep the token names, change their
values** in each `:root`. One careful edit to the `:root` block per file recolours the
whole page:

```css
/* OLD (index.html:34–38) */            /* NEW — same names, brand values */
--red-700: #8b1a2b;                      --red-700: #4a1370;   /* purple 700 */
--red-600: #a82135;                      --red-600: #5E1A8E;   /* purple primary */
--red-500: #c8283f;                      --red-500: #6d2aa0;   /* purple 500 */
--red-400: #d94a5e;                      --red-400: #8a4fbf;   /* purple 400 */
--red-100: #fce8eb;                      --red-100: #efe6f6;   /* purple wash */
```

Then introduce the **orange CTA** and **teal secondary** as new tokens (add to every
`:root`):

```css
--orange-500: #E89A3C;  /* CTA / hero accent */
--teal-500:   #1C9C8E;  /* secondary accent */
```

- **Gold:** the hero stat figures and `.label--gold` use `--gold-*`. The new kit has no
  "gold" — decide per Stage 7 whether stat figures become **orange** (`--orange-500`) or
  stay a warm accent. Default recommendation: retire gold → orange for figures, keeping one
  warm accent in the system. _(Confirm with Hannah.)_
- **Neutrals:** map `--slate-*`/`--stone-*` toward the kit's ink/slate/mist/line/surface.
  This is the fiddliest part because dark-mode backgrounds lean on `--slate-950/900`. Keep
  the dark hero (`#0f1118`-ish) but retune toward `#1E1A29` ink so dark sections read as
  "deep purple-black" not "blue-black". Verify both themes (there's a light/dark toggle).

> **⚠️ partnerships.html has a second token block** at `1236–1266` defining `--hls-purple`,
> `--hls-purple-soft`, `--hls-purple-line` (a restrained purple accent for the HLS
> partnership UI). Now that the **primary brand is purple**, the HLS-purple may visually
> merge with the brand colour. Reconcile in Stage 5: either keep HLS-purple as a distinct
> shade or fold it into the new palette. Do not leave two unrelated purples fighting.

### Open question → Stage 7
**CTA buttons: orange `#E89A3C` or purple?** The brief recommends orange CTAs with purple
as primary. Until confirmed, build with **orange CTAs** (the brief's recommendation) and
note it as provisional.

---

## 1.2 — Type: Crimson Pro + Outfit → Outfit + DM Sans (edit 02)

### Current state
- Tokens (`index.html:54–55`): `--font-display: 'Crimson Pro', Georgia, …, serif` and
  `--font-body: 'Outfit', …, sans-serif`.
- Headings get the display font via a **global element rule** `h1,h2,h3,h4 { font-family:
  var(--font-display) }` (`index.html:126–127`) — there is **no per-element font class**,
  so changing the two tokens reskins all headings automatically. 
- The italic-serif hero accent ("*drive UK innovation*", `index.html:1879–1882`) uses
  `<em>` inside a Crimson Pro heading — it will become Outfit italic; the brief explicitly
  wants the mixed serif/italic-serif look gone, so flatten the `<em>` styling.
- Google Fonts loaded identically on every page:
  `fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600;700&display=swap`

### Target
```css
--font-display: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;  /* headings, 600 */
--font-body:    'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif; /* body/UI, 400/500/600 */
```
Brief body spec: **16px / 1.65 line-height / 60–75 chars per line**.

### Steps (apply to every page)
1. Swap the **Google Fonts `<link>`** to load Outfit + DM Sans, drop Crimson Pro:
   `…/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@300;400;500;600;700&display=swap`
   _(If the kit ships `Outfit.ttf` + `DMSans.ttf`, optionally self-host via `@font-face`
   for performance/offline; Google Fonts is fine for v1.)_
2. Set `--font-display: 'Outfit'` and `--font-body: 'DM Sans'` in each `:root`.
3. Review heading sizes — Outfit at heading sizes is heavier than Crimson Pro; the kit
   gives **h1 52px, h2 36px, eyebrow 13px/uppercase/0.16em**. Retune `.hero h1`
   (`index.html:398`), `.featured__text h2` (938), `.cta-banner h2` (1200) etc. for the
   new face. Screenshot-check headline wrapping.
4. Flatten the hero `<em>` italic-serif accent so the headline reads as one Outfit weight
   (optionally keep `<em>` as a colour accent in orange/purple, not italic-serif).

---

## 1.3 — Logo (edit 01 + 21)

- **Header** (`index.html:1810–1824` and the equivalent inline SVG on every page): replace
  the hand-built red "V-chevron + D + B + 'UK'" monogram with **`vdb-wordmark.svg`** (purple
  wordmark, no "UK"). On the dark hero/header use **`vdb-reversed.svg`** (white on purple).
- **Footer** brand block (`index.html:2398–2409`) also has an inline SVG logo — swap to the
  reversed mark (footer is dark).
- **Favicon:** `favicon.png` / `apple-touch-icon.png` → regenerate from `vdb-favicon.svg`.
- Remove the SVG `<text>"UK"</text>` element regardless (the brand is now "VDB" only).
- The logo lives in the shared header/footer markup repeated across **all ~24 pages** —
  change must be applied everywhere, not just the homepage. (See the propagation recipe.)

---

## 1.4 — Propagation recipe (no build step)

Because every page carries its own copy of the tokens + header + footer, apply Stage 1 to
**all** of: `index.html`, `about.html`, `contact.html`, `accessibility.html`, `cookies.html`,
`privacy.html`, `partnerships.html`, `capabilities/*.html` (6), `case-studies/*.html` (10).
Decide on `projects/*.html` (legacy redirects — Stage 6) — recommend applying tokens there
too in case they're hit directly.

Suggested execution:
1. Define the canonical new `:root` block once (in this doc / a snippet file).
2. Apply to `index.html` first; screenshot-verify EN + CY, light + dark.
3. Roll the identical block to the rest. Where a page has page-specific extra tokens
   (partnerships' `--hls-*`), merge rather than overwrite.
4. Swap the Google Fonts link and the inline logo SVG on every page.

### Verification (must pass before Stage 3+)
```bash
# zero old red, zero serif font, zero "UK" in logo text — across the site
grep -rn 'c8283f' --include='*.html' .            # expect: 0
grep -rn 'Crimson Pro' --include='*.html' .        # expect: 0
grep -rn '>UK<' --include='*.html' .               # expect: 0 (logo 'UK' text removed)
# new tokens present everywhere
grep -rL '#5E1A8E\|--orange-500' --include='*.html' . # expect: only files without a :root
```
Plus: load homepage + 3 sample pages in the browser, toggle light/dark and EN/CY, confirm
no red survives and headings render in Outfit.

---

## 1.5 — Keep the repo self-documenting (CLAUDE.md)

`CLAUDE.md` → **Design System** currently reads:
> Palette: "Welsh Slate" … Welsh red CTAs (#c8283f) … Fonts: Crimson Pro (serif headings),
> Outfit (sans body)

Update it to the VDB brand: purple `#5E1A8E` primary, orange `#E89A3C` CTA, teal `#1C9C8E`
secondary, **Outfit** headings + **DM Sans** body. Note that tokens are remapped in-place
(the `--red-*` names now hold purple values) so future editors aren't confused. Also update
the i18n note if heading markup changed.

---

## Definition of done (Stage 1)
- New `:root` applied to every page; grep verification passes (0 red, 0 Crimson Pro).
- Logo swapped in header + footer on all pages; favicon regenerated; no "UK" in logo.
- Outfit + DM Sans loading; headings reflowed and screenshot-checked.
- partnerships' `--hls-*` purple reconciled with the new primary.
- `CLAUDE.md` design-system section updated.
- Open: CTA colour (orange vs purple) confirmed — Stage 7.
