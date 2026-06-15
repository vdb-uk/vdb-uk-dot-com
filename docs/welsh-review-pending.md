# Welsh review pending — before the language toggle is re-enabled

The Welsh language toggle is hidden site-wide (`lang-config.js` → `WELSH_ENABLED = false`,
commit `3872420`). The site currently displays **English only**.

New content added by the **supplier-assurance / partnerships** work ships in English now.
For structural integrity the bilingual `data-cy` / `data-content-cy` spans are present, but
they are currently **populated with the English text as a placeholder** (clearly not Welsh).

**Before the toggle is turned back on, a Welsh reviewer must translate every item below.**
Until then these placeholders are never displayed.

## Reviewer

- **Who:** _open question — to be named._
- **When the toggle comes back:** _open question._

## Items needing reviewed Welsh

### `partnerships.html` (net-new page)
- `<title>` `data-title-cy` and `<meta description>` `data-content-cy`
- Hero: h1, subtitle
- Assurance strip: "Human-led", "AI-assisted", "Audit-ready", "Clear escalation"
- "One delivery model, two clear roles": kicker, heading, both paragraphs, the
  "About Higher Level Software" link
- "Lead, build, operate": kicker, heading, the three step verbs (Lead / Build / Operate),
  the "Together" tag and all three descriptions
- "People stay accountable": kicker, heading, lede, and the oversight-principle blockquote
- "Contracts this suits": kicker, heading, intro, and the six checklist items
- CTA: heading, body, "Talk to VDB UK" and "Higher Level Software, our technical partner"

### `index.html` (homepage partnership band)
- Label "Technical delivery partner"
- Band sentence (contains the bold "Higher Level Software")
- "How the partnership works" link

### `about.html` (Adam Chesney bio refresh — both team cards)
- Role: "Software, AI and Cloud Systems"
- Bio: "Founder of Higher Level Software. Builds human-supervised agentic systems, hosted
  software platforms, operational tooling, reporting workflows, and support infrastructure
  for complex programmes."

### Header nav + footer "Partnerships" link (all pages) — **already correct Welsh**
- `data-cy="Partneriaethau"` is genuine Welsh already used elsewhere on the site
  (e.g. "Partneriaethau ar gyfer graddio"). No review needed for this string.
