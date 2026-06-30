# VDB Rebrand & Content Overhaul — Master Plan

**Created:** 2026-06-30 · **Owner:** Hannah Van Den Bergh · **Source brief:** `docs/input/website-review/website-edits.md` (27 edits) + annotated screenshots in the same folder.

This is the implementation plan for the full set of changes Hannah requested in the
2026-06-30 website review. It is split into **staged documents**: foundation work that
touches every page comes first, then page-by-page content work, then the items blocked
on assets/decisions.

> The source brief is a *change request*. These documents are the *build plan*: every
> edit is mapped to a stage, grounded in the actual code, with target copy inlined so
> each doc is self-contained.

---

## What this is, in one paragraph

Hannah's review is **not a tweak list — it's a rebrand plus a content rework.** The
"Welsh Slate" red/serif identity documented in `CLAUDE.md` is being replaced with the
new **VDB brand** (purple primary, orange/teal accents, Outfit + DM Sans), the company
is renamed from "VDB UK / VandenberghUK" to plain **"VDB"** in all marketing copy, the
contact domain moves to `@vdb-uk.com`, dashes are stripped site-wide, and the homepage
and Partnerships page get significant structural and copy changes.

---

## Staging strategy & sequencing

Stages are ordered by dependency. **Stage 1 must land before everything else** because
the palette/font/logo tokens are duplicated into every HTML file — doing content work
first would mean re-touching every page twice.

```
 Stage 1  Brand foundation ............. palette, fonts, logo, CLAUDE.md   ← do first, unblocks all
    │                                    (touches all ~24 pages)
    ▼
 Stage 2  Global copy rules ............ dashes, "VDB" naming, @vdb-uk.com ← site-wide sweep
    │                                    (touches ~34 pages)
    ▼
 Stage 3  Homepage ..................... index.html        ┐
 Stage 4  About page ................... about.html        │ independent of
 Stage 5  Partnerships page ............ partnerships.html │ each other; can
 Stage 6  Capabilities pages & routes .. new capability set ┘ run in parallel
    │                                                         after Stages 1–2
    ▼
 Stage 7  Assets & open questions ...... photos, Braingraph, email, images ← blocked on Hannah
```

Stages 3–6 are independent of each other and can be done in any order (or in parallel)
once Stages 1 and 2 are in. Stage 7 tracks everything that cannot be completed until
Hannah supplies an asset or a decision.

> **Routing correction (verified against the code):** The brief implies edits 10, 11
> and 12 (large portrait, "Working across the UK" / Company Details, and the
> "Recognised at the highest level" award badges) are on the homepage. They are **not** —
> they live on **`about.html`**, along with the team carousel that edits 13/14 target.
> The homepage carries the partner strip (edit 26a) but no award-badge or company-details
> block. The staging below reflects the real layout, not the brief's page labels.

---

## Document index

| Stage | Document | Covers (edit #s) | Touches |
|-------|----------|------------------|---------|
| 1 | [`01-brand-foundation.md`](01-brand-foundation.md) | 01, 02, 21 | All pages (tokens, fonts, logo) |
| 2 | [`02-global-copy-rules.md`](02-global-copy-rules.md) | 08, 19 (naming), 25 | ~34 pages (text sweep) |
| 3 | [`03-homepage.md`](03-homepage.md) | 03, 04, 05, 06, 07, 09, 26a, 27 | `index.html` |
| 4 | [`04-about-page.md`](04-about-page.md) | 10, 11, 12, 13, 14, 26b | `about.html` |
| 5 | [`05-partnerships-page.md`](05-partnerships-page.md) | 15, 16, 17, 18, 19, 20, 22, 23, 24 | `partnerships.html` |
| 6 | [`06-capabilities-and-routes.md`](06-capabilities-and-routes.md) | 05 (routes), 09 (links) | `capabilities/*.html`, all footers |
| 7 | [`07-assets-and-open-questions.md`](07-assets-and-open-questions.md) | 10, 11, 13, 14, 15, 23, 25, 26, 27, 01 (CTA) | Tracking / handoff |

---

## Traceability matrix — every edit is accounted for

Status legend: ✅ confirmed & buildable · 🟡 drafted, needs Hannah's sign-off · ⏳ blocked on asset/decision

| # | Area | Change | Stage | Status |
|---|------|--------|-------|--------|
| 01 | Header | Logo → `vdb-wordmark.svg`; red → purple | 1 | ✅ **BUILT** (logo = cleaned inline VDB monogram, brand-kit SVG still a TODO; CTAs orange) |
| 02 | Site-wide | Fonts → Outfit + DM Sans | 1 | ✅ **BUILT** |
| 03 | Hero stats | 8+→25, 350+→3 programmes, 5+→10; drop "+" | 3 | ✅ |
| 04 | "What we do" | New intro hook | 3 | ✅ |
| 05 | Capability cards | Replace all 6 | 3 + 6 | 🟡 |
| 06 | "Our approach" | Develop→Design, move bullets | 3 | 🟡 |
| 07 | Secretariat featured block | Remove | 3 | ✅ |
| 08 | Whole site | Remove dashes | 2 | 🟡 (rule set; audit) |
| 09 | Footer capabilities | Match new 6 | 3 + 6 | 🟡 |
| 10 | Large portrait (**about.html**) | Remove | 4 | ✅ (replacement → Stage 7) |
| 11 | "Working across UK" / Company Details (**about.html**) | Remove section | 4 | ✅ (Company Details Q → Stage 7) |
| 12 | Track record / award badges (**about.html**) | Redesign (Option B) | 4 | ✅ |
| 13 | Team photo (**about.html** carousel) | Straight-on swap | 4 + 7 | ⏳ photo |
| 14 | Team photos (**about.html** carousel) | Dynamic style | 4 + 7 | ⏳ photos |
| 15 | VDB/HLS diagram | Replace with photo | 5 + 7 | ⏳ photo/decision |
| 16 | Partnerships hero | General redraft | 5 | 🟡 |
| 17 | Partnerships chips | Remove | 5 | ✅ |
| 18 | Partnerships | Add "Partnership with HLS" | 5 | 🟡 |
| 19 | Flow diagram | Relabel + VDB naming | 5 | ✅ |
| 20 | "How it fits" | → Validate, design, build | 5 | 🟡 |
| 21 | Brand assets | Ingest brand kit | 1 | ✅ **BUILT** (palette/fonts from brief; logo SVGs still ⏳ Stage 7) |
| 22 | Partnerships IA | New 5-part cadence | 5 | ✅ |
| 23 | Partnerships | Add "Partnership with Braingraph" | 5 + 7 | ⏳ details |
| 24 | Partnerships | Remove "Contracts this suits" | 5 | ✅ |
| 25 | Site-wide | Domain/email → `@vdb-uk.com` | 2 | 🟡 (exact address → Stage 7) |
| 26 | Partner strip (a: index "Trusted by"; b: about partners line) | NHS→Plus X, Cranswick→Welsh Govt | 3 + 4 | ✅ |
| 27 | Case studies | New NPK green-tankering card | 3 | ✅ (image + which card → Stage 7) |

---

## The 5 site-wide changes (read before any stage)

These are cross-cutting and define the rest of the work:

1. **Palette: red → purple.** Primary `#c8283f` → **`#5E1A8E`**. New accents: **orange
   `#E89A3C`** (CTAs/hero), **teal `#1C9C8E`** (secondary). New neutrals (ink/slate/
   mist/line/surface). Full spec in Stage 1.
2. **Type: serif → sans.** Crimson Pro → **Outfit (headings)**; Outfit body → **DM Sans
   (body)**. Stage 1.
3. **Brand name → "VDB".** Drop "VDB UK" and "VandenberghUK" from marketing copy.
   **Exception: legal entity references stay "VandenberghUK Ltd"** (footer copyright,
   privacy data-controller). Stage 2.
4. **Domain/email → `@vdb-uk.com`.** Currently `hannah@vandenberghuk.com`. Exact address
   TBC by Hannah. Stage 2 + Stage 6.
5. **No dashes.** Remove all em (—) and en (–) dashes, rewrite as full sentences.
   **247 occurrences across 34 files.** Stage 2.

---

## Blocked on Hannah (Stage 7 detail)

Nothing below can be *completed* until these land. Track in
[`07-assets-and-open-questions.md`](07-assets-and-open-questions.md).

- **Brand kit files** — the plan references `work/vdb-brand/` (logo SVGs, tokens, fonts);
  **this folder is not in the repo.** Needed to apply Stage 1 exactly. Hex/font specs
  from the brief let us proceed on best-effort if the files are delayed.
- **CTA button colour** — orange vs purple (edit 01).
- **Company Details card** — keep-and-move-to-footer, or delete (edit 11).
- **Exact contact address** — `hello@` / `contact@` / `hannah@vdb-uk.com` (edit 25).
- **Team photos** — one straight-on swap (13) + dynamic set for all (14).
- **VDB/HLS diagram → photo** — which photo, home vs partnerships (15).
- **Braingraph details** — what they do / proof points (23).
- **New NPK case study** — which of 4 cards it replaces + the image (27).
- **Case-study Cranswick mention** — leave or change in BlakBear study (26).
- **Sign-off on drafted copy** — edits 05, 06, 09, 16, 18, 20, 22 are drafts.

---

## Key risks & decisions

- **No build step.** Tokens/CSS are duplicated into every HTML file (red hex appears 72×
  across 24 files). A rebrand is therefore a *repeated* edit, not a one-line change. Stage
  1 defines a consistent find/replace recipe and a verification grep to prove completeness.
- **`projects/` legacy pages.** `projects/*.html` are legacy redirects to `case-studies/`.
  Decide whether they get the rebrand too (recommended: yes for tokens, since they may be
  hit directly) — see Stage 5.
- **Welsh (cy) content.** Every copy change must update **both** `data-en` and `data-cy`.
  Machine translation is acceptable initially per `CLAUDE.md`; flag government-facing
  Welsh for professional review.
- **Legal text trap.** The "VDB UK"→"VDB" sweep (246 occurrences) must whitelist legal
  entity strings. Also fix the latent bug at `accessibility.html:1504` ("VDB UK Ltd" →
  "VandenberghUK Ltd").
- **`CLAUDE.md` goes stale.** Its "Design System" section describes the old red/serif
  identity. Stage 1 updates it so the repo stays self-documenting.

---

## Working method (applies to every stage)

1. **Branch.** Do the rebrand on a feature branch, not `main` directly — it is a large,
   reviewable change. Suggest `rebrand-2026-06`.
2. **Token-first.** Land Stage 1 and verify with grep before any content work.
3. **Bilingual.** Update `data-en` and `data-cy` together, every time.
4. **Screenshot-verify.** Use the browser/Playwright tools to capture before/after of each
   changed section and compare against the brief's annotated screenshots
   (`docs/input/website-review/NN-*.png`).
5. **Deploy per `CLAUDE.md`.** `git push`, then `ssh … git pull --ff-only` on the VPS.
   No build step; pulled files serve instantly.

## Definition of done

- All ✅ edits implemented and screenshot-verified EN + CY.
- Grep proves zero `#c8283f`, zero `Crimson Pro`, zero `@vandenberghuk.com` (outside the
  whitelisted legal/LinkedIn strings), and zero stray em/en dashes in body copy.
- `CLAUDE.md` design-system section updated to the new brand.
- All 🟡 drafts signed off by Hannah; all ⏳ items either delivered or explicitly parked
  in Stage 6 with the blocker named.
