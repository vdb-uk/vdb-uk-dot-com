# Stage 5 — Partnerships Page (`partnerships.html`)

**Edits covered:** 15, 16, 17, 18, 19, 20, 22, 23, 24.
**File:** `partnerships.html` (1989 lines; `<body>` 1436–1988). Do after Stages 1–2.

This is the biggest **structural** rework: the page is reordered into a new 5-part cadence,
two sections are removed, two new sections are added, and several are rewritten. Do the
content edits first, then the reorder, so you're moving finished blocks.

> **Map correction:** the brief's "flow diagram" (edit 19) and "how the partnership works"
> (edit 22) are the **same section** — `pt-roles` (`1561–1613`), whose right-hand art is the
> vertical responsibility-map diagram. There is no separate standalone flow section.
>
> **Token note:** this page has an extra `:root` at `1236–1266` with `--hls-purple*`. Now
> that the brand primary is purple (Stage 1), reconcile the HLS accent so two purples don't
> clash — pick a distinct HLS shade or fold it into the palette.

---

## Current section order (what you're changing)

| # | Lines | Section | Heading |
|---|-------|---------|---------|
| Hero | 1501–1544 | `page-hero--partner` | "Programme leadership with software delivery built in" + 2-into-1 SVG diagram |
| Chips | 1549–1556 | `pt-assure` | Human-led · AI-assisted · Audit-ready · Clear escalation |
| Roles | 1561–1613 | `pt-roles` | "One delivery model, two clear roles" + vertical box diagram |
| Flow | 1618–1657 | `pt-flow` | "Lead, build, operate" (3 cards) |
| Principle | 1662–1683 | `pt-principle` | "People stay accountable" (eyebrow "Human-led, AI-assisted") |
| Where | 1688–1731 | `pt-where` | "Contracts this suits" (6-item checklist) |
| CTA | 1736–1759 | `pt-cta` | "A programme that needs both?" |

---

## Target cadence (edit 22) · ✅ confirmed

Reorder the whole page to:

1. **General hero** — edit 16 (rewrite, remove HLS-specific framing + diagram)
2. **Partnership with HLS** — edit 18 (NEW section; hosts the HLS detail + hero diagram)
3. **Validate, design, build** — edit 20 (recast the `pt-flow` cards)
4. **Methodology** — edit 22 (NEW; folds in `pt-roles` "one delivery model" + the relabelled
   vertical diagram from edit 19)
5. **Partnership with Braingraph** — edit 23 (NEW; ⏳ blocked on details)

…then the CTA. **Removed:** chips (`pt-assure`, edit 17) and "Contracts this suits"
(`pt-where`, edit 24). **Decision needed:** the `pt-principle` "People stay accountable"
section isn't named in the brief — its message (human accountability) overlaps the HLS
section. Recommend folding its blockquote into the HLS or Methodology section, then removing
`pt-principle`. Flag for Hannah.

---

## 5.1 — Hero: general redraft (edit 16) · 🟡 draft

**Location:** `1501–1544`. Current h1 "Programme leadership with software delivery built in";
subtitle (1515–18) is HLS-specific and contains an em dash; the 2-into-1 SVG diagram
(`pt-hero__art`, 1521–1542).

**New (dash-free, "VDB"):**
- **Heading:** "We build the right team for your needs"
- **Intro:** "VDB leads complex operational and research programmes. Through reliable
  partnerships we bring in the right specialists for each piece of work, so every programme
  gets the team it actually needs. Scroll on to meet the partners we work with and see what
  each one brings."

**Move the hero SVG diagram down** into the new "Partnership with HLS" section (5.3) — it's
HLS-specific and shouldn't sit in a now-general hero. _(This hero diagram is likely the same
"VDB/HLS delivery diagram" as edit 15 "replace with a photo" — confirm whether edit 15 meant
this page or the homepage; tracked in Stage 7.)_

---

## 5.2 — Remove the assurance chips (edit 17) · ✅ confirmed

**Location:** `pt-assure` `1549–1556` (Human-led · AI-assisted · Audit-ready · Clear
escalation). Delete the section. Reference: `17-partnerships-chips.png`.

---

## 5.3 — Add "Partnership with HLS" section (edit 18) · 🟡 draft

**NEW section** (cadence item 2). Hosts the HLS detail now that the hero is general.

**Draft (dash-free, "VDB"):**
- **Heading:** "Partnership with HLS" (full: "Partnership with Higher Level Software")
- **Body:** "Where a programme needs serious software and agentic systems behind it, we
  deliver with Higher Level Software as our technical delivery partner. VDB leads the
  programme and stays accountable to the client. HLS builds the software, hosting,
  integrations and agentic systems it runs on. Together we operate it under one cadence, with
  a named human accountable on each side."
- Hosts the **hero SVG diagram** moved from 5.1, and the **Validate/design/build cards**
  (5.4). Keep the existing HLS link → `https://higherlevelsoftware.com/partnerships.html`.

**Open (Hannah):** make this a **repeatable block** template, since the hero now promises
"more about each partnership" (HLS + Braingraph + future)? Recommend yes — build as a
reusable partnership-section pattern so 5.6 (Braingraph) is a clone.

---

## 5.4 — "Lead, build, operate" → "Validate, design, build" (edit 20) · 🟡 draft

**Location:** `pt-flow` `1618–1657`. Keep the eyebrow+heading+body 3-card cadence; recast to
match the homepage "Our approach" (Stage 3.4).

| Eyebrow | Heading | Body |
|---------|---------|------|
| VDB | **Validate** | "VDB leads the programme. We validate the need and shape the approach through project management, stakeholder engagement, funding and governance, and stay accountable to the client." |
| VDB and HLS | **Design** | "Together we design the delivery model: the right team, the architecture and the cadence, agreed before build begins." |
| Higher Level Software | **Build** | "HLS builds the software, hosting, integrations and agentic systems the programme runs on, then we operate it with reporting, support and oversight, and a named human accountable on each side." |

The old "Operate" card's content (reporting/oversight/named human) folds into **Build** to
keep three cards. Open: keep a separate 4th "Operate" idea? (Brief default: fold into Build.)
This section sits inside the HLS block (5.3) per the cadence.

---

## 5.5 — Methodology section + flow diagram relabel (edits 22 + 19) · ✅ confirmed

**NEW "Methodology" section** (cadence item 4) that folds in the existing `pt-roles`
"One delivery model, two clear roles" content + its vertical diagram.

**Methodology copy (draft, dash-free):**
> **Eyebrow:** OUR METHODOLOGY
> **Heading:** "One delivery model, two clear roles"
> "VDB leads the client relationship and the operational programme: project management,
> stakeholder engagement, funding and governance. Higher Level Software sits behind it as
> technical delivery partner, owning the software, hosting, integrations, reporting tooling
> and agentic systems. The result is one delivery model for programmes that need both
> operational leadership and serious software, with human oversight, acceptance criteria and
> audit trails across both. We run every programme through the same path: validate, design,
> build."
> **Link:** "About Higher Level Software →" pointing to the HLS section (5.3).

**Relabel the vertical box diagram (edit 19), `pt-respmap` `1586–1611`:**

| Box | Current | New |
|-----|---------|-----|
| 1 | "Client outcome" | **"Client needs"** |
| 2 | "VDB · programme lead" / "research · science · governance" | "VDB · programme lead" / **"project management · stakeholder engagement · governance"** |
| 3 | "HLS · technical delivery" / "software · hosting · agents" | _unchanged_ |
| 4 | "Human oversight + reporting" / "acceptance · audit trail · escalation" | _unchanged_ |

Plus the global "VDB UK" → "VDB" rule throughout the page (header logo aria 1443, hero,
flow-card tag 1632, CTA "Talk to VDB UK" 1750). **Open:** keep "· programme lead" as box 2's
title or replace with the three descriptors directly? (Default: keep "programme lead".)

---

## 5.6 — Add "Partnership with Braingraph" (edit 23) · ⏳ blocked

**NEW section** (cadence item 5), mirroring the HLS block (5.3). ⏳ Need from Hannah: what
Braingraph does, what they bring to VDB programmes, proof points. Build as a clone of the
HLS section template once details arrive. Tracked in Stage 7. _(Do not pull from un-linked
drives without go-ahead.)_

---

## 5.7 — Remove "Contracts this suits" (edit 24) · ✅ confirmed

**Location:** `pt-where` `1688–1731` (6-item checklist). Delete. Rationale: "we decide who
it suits." Reference: `24-contracts-this-suits-REMOVED.png`.

---

## 5.8 — VDB/HLS diagram → photo (edit 15) · ⏳ blocked

The brief wants the "one delivery model" diagram swapped for a photo. **Which diagram and
which page is ambiguous** — there are two: the hero 2-into-1 SVG (1521–1542) and the vertical
`pt-respmap` (1586–1611). The vertical one carries real meaning and is now the Methodology
diagram (5.5), so it should **stay**. The hero SVG is the more likely "replace with a photo"
candidate. ⏳ Need: which photo + confirm home vs partnerships. If a diagram is replaced, its
"two firms, one delivery model" message must move into nearby copy. Tracked in Stage 7.

---

## Recommended execution order within this stage
1. Rewrite copy in place: hero (5.1), flow cards → Validate/Design/Build (5.4), relabel
   diagram (5.5), apply VDB naming.
2. Build the new HLS section (5.3) and Methodology section (5.5).
3. Delete chips (5.2) and "Contracts this suits" (5.7); decide on `pt-principle`.
4. Reorder into the cadence (hero → HLS → V/D/B → Methodology → [Braingraph] → CTA).
5. Leave a placeholder/commented stub for Braingraph (5.6) and the diagram→photo (5.8).

## Verification (Stage 5)
- Screenshot the reordered page EN + CY, light + dark, against
  `docs/input/website-review/16,17,19,20,22,24-*.png`.
- Confirm chips + "Contracts this suits" are gone, HLS + Methodology sections exist, diagram
  relabelled, and the page reads top-to-bottom in the new cadence.
- `grep -n 'pt-assure\|pt-where\|Client outcome\|Lead, build, operate\|VDB UK' partnerships.html`
  → expect only intended survivors (and zero "VDB UK").
- Confirm the partnership-specific `data-cy` is at least placeholder-equal to `data-en`
  for any new sections (Welsh translation flagged for later review).
