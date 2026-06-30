# Stage 7 — Assets & Open Questions (handoff tracker)

This stage holds everything that **cannot be completed until Hannah supplies an asset or
makes a decision.** It is the single checklist to clear before the rebrand is "done". Each
item names the blocker, the recommended default (so work can proceed provisionally), and
where the implementation lives.

Legend: ⏳ waiting · ✅ resolved (move the date + answer inline when it lands)

---

## A. Assets to supply

| ⏳ | Item | Needed for | Where it lands | Recommended default if delayed |
|----|------|-----------|----------------|--------------------------------|
| ⏳ | **Brand kit** `work/vdb-brand/` (logo SVGs, tokens, fonts, style guide) | Stage 1 (exact logo + tokens) | `work/vdb-brand/` (gitignored) | Build palette/fonts from the brief's hexes; use a temporary text "VDB" wordmark until SVGs arrive |
| ⏳ | **`vdb-wordmark.svg` / `vdb-reversed.svg` / `vdb-favicon.svg`** | Stage 1.3 logo swap | header + footer (all pages), favicon | Inline text wordmark stand-in; flag as provisional |
| ⏳ | **Team straight-on photo** (edit 13) | Stage 4.5 | one team carousel card | leave current photo; do not guess which member |
| ⏳ | **Dynamic team photos, all members** (edit 14) | Stage 4.5 | team carousel cards | keep current headshots; candid direction noted |
| ⏳ | **NPK app case-study image** (edit 27) | Stage 3.7 | chosen project card `<img>` | ship card with a placeholder, swap on arrival |
| ⏳ | **Replacement for the removed Hannah portrait slot** (edit 10) | Stage 4.1 | About page | leave slot empty (bio full-width) |

## B. Content/details to supply

| ⏳ | Item | Needed for | Notes |
|----|------|-----------|-------|
| ⏳ | **Braingraph details** (edit 23) | Stage 5.6 | What they do, what they bring, proof points. Build as a clone of the HLS section once supplied. Do not pull from un-linked drives without go-ahead. |
| ⏳ | **NPK metric figure** (edit 27) | Stage 3.7 | "Tonnes diverted from wastewater treatment" — a number would strengthen it ("X tonnes diverted") |
| ⏳ | **Award badge sub-labels** (edit 12) | Stage 4.3 | Confirm exact wording, e.g. "Earthshot Prize · supported venture shortlisted" |

## C. Decisions to make

| ⏳ | Decision | Affects | Recommendation |
|----|----------|---------|----------------|
| ⏳ | **CTA button colour: orange `#E89A3C` vs purple** (edit 01) | Stage 1.1 | Orange CTAs, purple primary, teal secondary (the brief's own recommendation) |
| ⏳ | **Stat-figure colour** now that "gold" is retired (Stage 1) | Stage 1.1 / 3.1 | Orange for figures (single warm accent) |
| ⏳ | **Company Details card: keep-and-move to footer vs delete** (edit 11) | Stage 4.2 | Delete — footer copyright already carries "VandenberghUK Ltd (no. 12296613)"; add a slim footer line only if Director/Location must stay |
| ⏳ | **Exact contact address** `hello@` / `contact@` / `hannah@vdb-uk.com` (edit 25) | Stage 2.3 | `hannah@vdb-uk.com` (1:1 swap); don't push live until the new mailbox is verified |
| ⏳ | **Edit 15: which diagram, which page** (home vs partnerships; hero SVG vs vertical map) | Stage 5.8 | Replace the partnerships **hero** SVG only; keep the vertical Methodology diagram |
| ⏳ | **Which case-study card the NPK app replaces** (edit 27) | Stage 3.7 | BlakBear/Cranswick (Cranswick de-emphasised) |
| ⏳ | **Cranswick in the BlakBear case study** — leave or change (edit 26) | Stage 3.6 / 4.4 | Hannah's call; she only asked to change the partner strip |
| ⏳ | **`pt-principle` "People stay accountable"** — fold in or remove (Stage 5) | Stage 5 | Fold its blockquote into the HLS or Methodology section, then remove |
| ⏳ | **Capability slugs: keep legacy vs descriptive + redirects** | Stage 6.1 | Keep legacy slugs, relabel only |
| ⏳ | **Retire Secretariat/Translation pages: redirect (A) vs orphan (B)** | Stage 6.3 | Redirect to `/#capabilities`; still rebrand them while served |
| ⏳ | **`projects/*.html` legacy redirects: rebrand them too?** | Stage 1.4 | Yes — apply tokens in case hit directly |
| ⏳ | **`--hls-purple` vs new brand purple** | Stage 1.1 / 5 | Pick a distinct HLS shade or fold into palette |

## D. Copy sign-offs (🟡 drafts awaiting Hannah)

These are written and buildable but want Hannah's yes before going live:
- Edit 04 hook re-confirm (dash-free version) · Edit 05 six-card copy · Edit 06 Design column
  intro + bullet question · Edit 09 footer list · Edit 16 hero · Edit 18 HLS section ·
  Edit 20 Validate/Design/Build cards · Edit 22 Methodology.

---

## How to use this tracker
1. As each asset/decision lands, replace ⏳ with ✅, add the answer + date inline, and update
   the matching stage doc + the README traceability matrix.
2. Anything still ⏳ at deploy time ships with its documented **default** (and a visible note
   in the PR/commit) so the rebrand isn't held hostage to one missing photo.
3. The Welsh (cy) translations across all new/changed copy are a standing follow-up — machine
   translation is acceptable for launch per `CLAUDE.md`, but government-facing pages need
   professional review before sharing with Welsh public-sector contacts.
