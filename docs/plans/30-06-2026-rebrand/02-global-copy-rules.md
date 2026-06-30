# Stage 2 — Global Copy Rules

**Edits covered:** 08 (remove dashes), 19 naming + the global "VDB" rule, 25 (domain/email).
**Touches:** ~34 HTML files. Run after Stage 1, before/alongside Stages 3–6.

Three site-wide text sweeps. All three are mechanical but **require human judgement on
exceptions** — do not blind-`sed` them. Every change must update **both `data-en` and
`data-cy`** (and any `data-title-*`, `data-content-*`, `data-alt-*`, `data-aria-label-*`).

---

## 2.1 — "VDB UK" / "VandenberghUK" → "VDB" (global brand rule)

### Footprint
- **246** occurrences of the string `VDB UK`
- **28** occurrences of `VandenberghUK`

### Rule
Marketing/UI copy uses **"VDB"** only. Drop "UK" and "Vandenbergh".

### ⚠️ Exceptions that MUST stay (do not change)
A recent commit (`f3a8528`, "correct legal entity to VandenberghUK Ltd") deliberately set
the legal name. The legal entity is **unchanged at Companies House**; this rule is about
on-site branding only. **Keep these as-is:**

| Where | String to KEEP | Files |
|-------|----------------|-------|
| Footer copyright (every page) | `© 2026 VandenberghUK Ltd (company no. 12296613)` | all (e.g. `index.html:2449`, `contact.html:1473`) |
| Privacy data-controller | `VandenberghUK Ltd (trading as VDB UK)` | `privacy.html:1477` (EN), `:1534` (CY) |
| Privacy meta description | `VDB UK (VandenberghUK Ltd)` | `privacy.html:7` |
| LinkedIn URL | `linkedin.com/company/vandenberghuk` | `contact.html:1357,1468`, `partnerships.html:1813` — this is the real LinkedIn handle; only change if the LinkedIn page is renamed |

### 🐞 Bug to fix while here
`accessibility.html:1504` reads `VDB UK Ltd (registered address available via Companies
House)` — the legal entity is **"VandenberghUK Ltd"**, not "VDB UK Ltd". Correct it to
`VandenberghUK Ltd`.

### Known prose hotspots (from page maps)
- `partnerships.html`: hero subtitle (1516), `pt-roles` copy (1573), flow card tag (1632),
  CTA "Talk to VDB UK" (1750), header logo aria (1443). The page is inconsistent today
  ("VDB UK" in prose, "VDB" in diagrams/footer) — Stage 5 makes it uniformly "VDB".
- `index.html`: hero desc (1884–1887), footer brand blurb (2398–2409), schema/meta.
- All pages: nav logo aria-label, `<title>`/meta brand strings.

### Method
1. `grep -rn 'VDB UK' --include='*.html' .` and triage every hit against the exception
   table before replacing.
2. Replace in EN **and** CY spans (Welsh keeps "VDB" too — it's a brand name).
3. Update `<title>`, meta `data-title-*`/`data-content-*`, and aria-labels.
4. Re-grep; the only `VandenberghUK` / `VDB UK` survivors should be the whitelisted legal
   strings.

---

## 2.2 — Remove all dashes, write full sentences (edit 08)

### Footprint
**247 em/en dash occurrences across 34 files.** This is the largest copy task.

### Rule
Remove every em dash (—) and en dash (–) from **body copy**. Rewrite as either two full
sentences or join with a comma / "and". Example from the brief (CTA, `index.html` /
edit 08 screenshot):
- Before: `…or need a delivery partner — we'd love to hear from you.`
- After: `…or need a delivery partner. We'd love to hear from you.`

### Cautions
- **Don't strip dashes inside code/CSS** — the grep will hit CSS comments, `font-feature`
  ranges, SVG, etc. Only rewrite **visible prose** (text nodes inside `data-en`/`data-cy`,
  headings, paragraphs, list items, alt text).
- **Number ranges / date ranges** (e.g. "2020–2024", "9–5") read fine with an en dash but
  the rule says remove dashes — convert to "2020 to 2024". Confirm tone with Hannah for
  ranges; default to "to".
- Welsh copy has its own dashes — rewrite those too, keeping grammatical sense (machine
  translation acceptable per `CLAUDE.md`; flag government-facing pages for review).
- Hyphens in compound words (e.g. "human-centred", "multi-year", "scale-up") are **hyphens,
  not en/em dashes** — leave them. The grep below targets only — and –.

### Method (page-by-page audit)
```bash
# list files + line numbers of every em/en dash
grep -rnE '—|–' --include='*.html' .
# count remaining after each page is done (target: only intentional ranges, if any)
grep -rcE '—|–' --include='*.html' . | grep -v ':0'
```
Work the list top to bottom; for each hit decide split-sentence vs comma vs "and". Many
will be in case-study summaries and capability copy. Re-run the count to drive it to zero
(or to a documented, Hannah-approved set of numeric ranges).

> Drafts in this plan (Stages 3–5) are already written **dash-free**, so applying them
> resolves those instances; this sweep covers the *existing* live copy not otherwise being
> rewritten.

---

## 2.3 — Domain / email → `@vdb-uk.com` (edit 25)

### Current state
- The only contact email on the site is **`hannah@vandenberghuk.com`** (e.g.
  `contact.html:1344,1466`, `index.html:2384` CTA `mailto:`, `partnerships.html:1811`,
  and the footer contact column on most pages).
- No `vdb-uk.com` reference exists anywhere yet.

### Rule
Display **`@vdb-uk.com`** everywhere a contact address shows: `mailto:` links, footer
contact column, contact-page email, the homepage CTA button. Hannah is actioning the
mailbox/domain move separately; the site copy just needs to reflect the new address.

### ⏳ Blocked on exact address (Stage 7)
Need the precise mailbox: `hello@vdb-uk.com` / `contact@vdb-uk.com` / `hannah@vdb-uk.com`.
**Recommendation:** `hannah@vdb-uk.com` (1:1 swap, lowest risk, matches current personal
address). Until confirmed, do not push the email change live — the old mailbox should keep
working until the new one is verified.

### Method (once address confirmed)
```bash
grep -rn 'vandenberghuk.com' --include='*.html' .   # find every mailto + display string
```
1. Replace `mailto:hannah@vandenberghuk.com` and its visible text on every page.
2. Update footer contact column + contact page (both the `<a>` href and the displayed text).
3. Leave the **LinkedIn** `linkedin.com/company/vandenberghuk` URL unless the LinkedIn page
   itself is renamed (it's a real handle, not an email domain).
4. Re-grep: `grep -rn '@vandenberghuk' --include='*.html' .` → expect 0 email hits.

---

## Definition of done (Stage 2)
- `grep 'VDB UK'` / `'VandenberghUK'` returns only the whitelisted legal/LinkedIn strings.
- `accessibility.html:1504` legal-entity bug fixed.
- Dash count driven to zero in prose (or a documented numeric-range exception set).
- `@vandenberghuk.com` email replaced site-wide with the confirmed `@vdb-uk.com` address
  (gated on Stage 7 address confirmation + mailbox cutover).
- EN and CY both updated for every change.
