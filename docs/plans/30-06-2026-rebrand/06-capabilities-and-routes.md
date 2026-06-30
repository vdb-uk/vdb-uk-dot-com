# Stage 6 — Capabilities Pages & Routes

**Edits covered:** 05 (route side of the new capability set), 09 (footer capabilities list).
**Touches:** `capabilities/*.html`, the homepage capability cards (links), and the footer on
**every** page. Do after Stages 1–2; pairs with Stage 3.3 / 3.8.

The new homepage capability set (Stage 3.3) changes which capability subpages exist and what
they're called. This stage resolves the routing so nothing 404s and nav/footer/cards stay
consistent.

---

## 6.1 — The capability set transition

| New capability (homepage order) | Current page | Plan |
|---|---|---|
| 1. Research and innovation | `capabilities/research.html` | **Keep file**, relabel title/H1/nav to "Research and innovation" |
| 2. Product and system development | — (none) | **Create** `capabilities/product-and-system-development.html` |
| 3. Fundraising and scale-up | `capabilities/funding.html` | **Keep file**, relabel to "Fundraising and scale-up" |
| 4. Science and engineering | `capabilities/science.html` | **Keep file**, relabel to "Science and engineering" |
| 5. Sustainability | `capabilities/esg.html` | **Keep file**, relabel to "Sustainability" |
| 6. Partnership building | — (none) | **Create** `capabilities/partnership-building.html` |
| _(dropped)_ Secretariat & Programme Mgmt | `capabilities/secretariat.html` | **Retire** (see 6.3) |
| _(dropped)_ Translation & Language Services | `capabilities/translation.html` | **Retire** (see 6.3) |

### Why keep existing slugs rather than rename
The site has **no build step** and links are hard-coded across ~24 files. Renaming
`funding.html`→`fundraising-and-scale-up.html` and `esg.html`→`sustainability.html` would
require chasing every internal link and risks external/indexed links breaking. **Lowest-risk
path: keep the existing filenames, change only the on-page title, H1, `<title>`/meta, and the
nav/footer/card *labels*.** If Hannah wants clean URLs, do the rename as a follow-up with
redirects (nginx or meta-refresh) from the old slugs.

> Decision flag for Hannah: keep short legacy slugs (recommended, fast, safe) **or** adopt
> descriptive slugs with redirects (cleaner URLs, more work). Default to keep-and-relabel.

---

## 6.2 — Create the two new capability subpages

`product-and-system-development.html` and `partnership-building.html`. Clone the structure of
an existing capability page (e.g. `research.html`) so they inherit the (now rebranded, post
Stage 1) shared header/footer/tokens, breadcrumb, hero, content blocks, and i18n scaffolding.

**Seed content** from the Stage 3.3 card copy plus public site material:
- **Product and system development** — lead with app development (web/mobile, secure portals,
  dashboards, data pipelines), the HLS technical-delivery partnership, and proof points
  (GripAble/SqueezAble, BlakBear sensors, the new NPK app from edit 27). Connects to Stage 5
  (HLS) and Stage 3.7.
- **Partnership building** — multi-stakeholder consortia (universities, public bodies,
  enterprises, spin-outs), operational leadership, examples (Imperial College → Arts Council
  of Wales), and the HLS delivery partnership.

Each page: full EN + CY, hero + 2–4 content sections + CTA, matching the existing capability
template. This is the largest *content-authoring* sub-task in the stage — budget time for it,
or ship minimal v1 pages and expand later. Welsh = machine translation acceptable initially,
flag for review.

---

## 6.3 — Retire Secretariat & Translation pages

The pages still exist but are dropped from the capability set, the homepage cards (Stage 3.3)
and the featured block (Stage 3.5). Options:
- **A (recommended):** unlink them everywhere (nav, footer, cards, sitemap) **and** add a
  redirect to the homepage `/#capabilities` so any external/indexed link doesn't dead-end.
  Implement via a `<meta http-equiv="refresh">` + canonical, or an nginx rule.
- **B:** leave them live but orphaned (no inbound links). Simpler, but stale content stays
  crawlable and still shows old branding unless Stage 1 is applied to them too.

Either way, **apply Stage 1 (rebrand) + Stage 2 (copy) to these files** while they remain
served, so a stray visitor doesn't hit red/serif/"VDB UK" content. Confirm A vs B with Hannah.
_(Note: `case-studies/` and the legacy `projects/` redirects are unaffected by the capability
set; they're handled only by the global Stages 1–2.)_

---

## 6.4 — Footer capabilities list (edit 09) · 🟡 applies to every page

**Location:** the footer `CAPABILITIES` column, duplicated on every page (e.g.
`index.html:2410–2423`). Current list: Secretariat / Research / Funding / Science / ESG /
Translation.

**New list (homepage order) + links:**
1. Research and innovation → `capabilities/research.html`
2. Product and system development → `capabilities/product-and-system-development.html`
3. Fundraising and scale-up → `capabilities/funding.html`
4. Science and engineering → `capabilities/science.html`
5. Sustainability → `capabilities/esg.html`
6. Partnership building → `capabilities/partnership-building.html`

Apply the identical updated footer column to **all ~24 pages** (find/replace the list block).
Update EN + CY labels. Drop Secretariat + Translation links.

---

## 6.5 — Homepage capability-card links (pairs with Stage 3.3)

After the routes are settled, wire each homepage `cap-card__link` (`index.html` grid
1975–2077) to the matching filename above. Verify each "Learn more →" resolves (no 404).

---

## Verification (Stage 6)
- Every nav/footer/card capability link resolves to a real file (crawl or click-through).
- `grep -rn 'secretariat.html\|translation.html' --include='*.html' .` → only redirect stubs
  (option A) or zero inbound links (option B); no live nav/footer/card references.
- The two new pages render with the rebranded shell, breadcrumb, EN + CY.
- Footer capabilities list is identical and correct on a sample of pages across the site.
