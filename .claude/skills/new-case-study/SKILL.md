---
name: new-case-study
description: Scaffold a new case-study page from the shared template, add its card to the index, and create the legacy /projects redirect stub
user_invocable: true
arguments:
  - name: slug
    description: URL slug, kebab-case (e.g. wales-nutrient-recovery) — becomes case-studies/<slug>.html
    required: true
  - name: title
    description: Human title of the case study (e.g. "Wales Nutrient Recovery")
    required: true
---

# Scaffold a new case study

Create a new case-study page that matches the established template, list it on the
index, and keep the legacy `/projects/<slug>` URL redirecting. Work only in `src/`;
`build.py` emits everything to `dist/`.

Don't invent the markup — **copy an existing case study** and adapt it, so the new
page inherits the current structure and classes.

## Steps

1. **Pick the closest existing case study as the template** and copy it:
   ```bash
   cp src/case-studies/npk-recovery.html src/case-studies/<SLUG>.html
   ```
   (Browse `src/case-studies/` for the nearest match in shape/sector.)

2. **Adapt the new page** (`src/case-studies/<SLUG>.html`). Keep the shared
   includes (`<!-- @include _partials/head.html -->`, `header.html`, `footer.html`,
   `scripts.html`) untouched. Update:
   - `<title>` → `<TITLE>: <short descriptor> | Case Study | VDB`
   - the `<meta name="description">` to a 1–2 sentence summary
   - the `.cs-hero` heading, badge, subtitle, and the four `.cs-meta`
     (Venture/Client, Sector, Capabilities, Timeline) values
   - the body sections in place: `.cs-context`, `.cs-objective`,
     `.cs-deliverables` (numbered `.cs-deliverable` items), and any results/CTA
     sections the template carries. Replace copy; don't restructure the classes.
   - any hero/background image references to real assets in `images/` (optimised
     JPG < 200KB — use the `generate-image` skill if you need one).

3. **Add a card to the index** `src/case-studies/index.html`: duplicate an existing
   `<a href="/case-studies/<other>.html" class="cs-card"> … </a>` block, then set
   its `href` to `/case-studies/<SLUG>.html`, and update `.cs-card__image`,
   `.cs-card__badge`, `.cs-card__tag`s, `.cs-card__title`, `.cs-card__excerpt`, and
   the `.cs-card__meta` (Client/Sector) values. Place it in the intended order.

4. **Create the legacy redirect stub** so old `/projects/<slug>` links still work.
   Copy the shape of `src/projects/npk-recovery.html` (a meta-refresh + canonical):
   ```bash
   cp src/projects/npk-recovery.html src/projects/<SLUG>.html
   ```
   Then swap both `<SLUG>` references (the `meta http-equiv="refresh"` URL and the
   `link rel="canonical"`) to point at `/case-studies/<SLUG>.html`.

5. **Build and preview** (see the `preview` skill):
   ```bash
   python3 build.py            # expect exit=0
   ```
   Open the new page, the index (confirm the new card links correctly), and
   `/projects/<SLUG>.html` (confirm it redirects). Check dark + light themes and a
   mobile width.

6. **Ship it:** commit to `main` and push; then confirm live with `verify-deploy`.

## Notes

- Legal/brand invariants still apply: footer copyright, brand tokens
  (`--red-*` renders purple), image budget.
- Keep the page's `data-theme="dark"` default on `<html>` as the template has it.
- If several case studies start sharing a large block, lift it into `_partials/`
  rather than copy-pasting further (see AGENTS.md → Engineering Principles).
