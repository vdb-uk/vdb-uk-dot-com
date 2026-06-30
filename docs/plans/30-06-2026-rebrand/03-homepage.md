# Stage 3 — Homepage (`index.html`)

**Edits covered:** 03, 04, 05, 06, 07, 09 (footer → spec'd in Stage 6), 26a, 27.
**File:** `index.html` (2624 lines; `<body>` 1803–2623). Do after Stages 1–2.

Line numbers are from the current file and will drift as edits land — re-grep before each.
Every copy change updates **both `data-en` and `data-cy`**. All copy below is **dash-free**
(Stage 2 rule already applied to these drafts).

---

## 3.1 — Hero stat cards (edit 03) · ✅ confirmed

**Location:** `.hero__stats` `1902–1931`. Four cards; change three, drop all "+".

| Card | Figure (line) | Label (lines) | New figure | New label |
|------|---------------|---------------|------------|-----------|
| 1 | £255m (1904) | "Unlocked for UK R&D projects since 2020" (1905–08) | **£255m** _(unchanged)_ | unchanged |
| 2 | 8+ (1911) | "Major funded projects delivered" (1912–15) | **25** | "Successful projects delivered" |
| 3 | 350+ (1918) | "Healthcare locations using our innovations" (1919–22) | **3** | "Multi-year programmes" |
| 4 | 5+ (1925) | "Years building innovation partnerships" (1926–29) | **10** | "Years building innovation partnerships" |

Notes: card 3 was **factually wrong** per Hannah (350+ healthcare) — replace the whole stat.
Remove the trailing `+` on cards 2/3/4. £255m unchanged. Update CY labels too. Card colour
classes (`--gold`/`--red`/`--white`) get reskinned in Stage 1; confirm figures read well in
the new palette.

---

## 3.2 — "What we do" intro hook (edit 04) · ✅ confirmed

**Location:** `.capabilities__subtitle` `1969–1972` (eyebrow 1961–64 "What we do" and h2
1965–68 "Capabilities built for complex delivery" stay).

**New hook (Draft A, dash-free):**
> "We have an appetite for the ambitious. We combine expertise in project delivery,
> engineering, science and finance to deliver the most complex, multi-stakeholder
> programmes."

Replace EN; write the CY equivalent.

---

## 3.3 — Replace all six capability cards (edit 05) · 🟡 draft

**Location:** `.capabilities__grid` `1975–2077`. Six `cap-card`s today:
1. Secretariat & Programme Management → `/capabilities/secretariat.html` (h3 1980, link 1988)
2. Research & Innovation → `/capabilities/research.html` (1997 / 2005)
3. Funding & Grant Strategy → `/capabilities/funding.html` (2014 / 2022)
4. Science & Engineering → `/capabilities/science.html` (2031 / 2039)
5. ESG & Sustainability → `/capabilities/esg.html` (2048 / 2056)
6. Translation & Language Services → `/capabilities/translation.html` (2065 / 2073)

**New set (replace all six, in order). Drops Secretariat + Translation.** Body copy is the
brief's drafted 2-sentence-per-card text (dash-free):

1. **Research and innovation** — "We run primary and secondary research that validates new
   ideas before they scale, combining human-centred design, user workshops and peer-reviewed
   evidence. From early discovery to investment-ready insight, we connect rigorous research
   to real-world impact for government, universities and enterprise."
2. **Product and system development** _(highlight app development)_ — "We design and build
   the products and digital systems that turn ideas into deployable solutions, with
   particular strength in app development, from web and mobile applications to secure client
   portals, dashboards and integrated data pipelines. Working with our technical delivery
   partner Higher Level Software, we ship dependable, auditable software and connected
   hardware, from the GripAble/SqueezAble rehabilitation platform to BlakBear's digital
   freshness sensors."
3. **Fundraising and scale-up** — "We have unlocked over £255m for UK R&D since 2020,
   building the strategy, assembling the consortium and positioning each bid to win across
   Innovate UK, UKRI, Defra and charitable funders. Beyond the grant we help ventures scale,
   structuring post-award delivery and investment readiness, as when we helped Plus X
   Innovation's accelerator support 69 companies that went on to raise £180m."
4. **Science and engineering** — "We take science from lab to market, building demonstrators,
   running field trials and developing scalable solutions across deep tech, from
   bio-fertiliser production to medical sensor technology. Our scientists and engineers turn
   promising research into robust, manufacturable products, as with NPK Recovery's process
   for converting waste into crop nutrients."
5. **Sustainability** — "We help organisations turn sustainability ambition into measurable
   outcomes through climate research, ESG risk frameworks and circular-economy innovation.
   Our work spans Earthshot Prize shortlistees and Terra Carta Labs winners, from recovering
   nutrients out of waste streams to digital sensors that cut food waste across production
   facilities."
6. **Partnership building** — "Complex programmes succeed on the right partners, so we
   assemble and lead multi-stakeholder consortia spanning universities, public bodies,
   enterprises and spin-outs, from Imperial College to the Arts Council of Wales. We bring
   the operational leadership and, with our technical partner Higher Level Software, the
   dependable delivery that keep every stakeholder aligned and accountable."

**Build notes:**
- Each card links to a capability subpage. Routes change with the new set — **see Stage 6**
  (research-and-innovation, product-and-system-development, fundraising-and-scale-up,
  science-and-engineering, sustainability, partnership-building). Wire links to match Stage
  6's chosen filenames.
- New/renamed cards need **icons** (Product & system development, Partnership building,
  Fundraising & scale-up) — pick from the existing icon set; flagged for build.
- Provide CY for all six.
- **Confirmed:** dropping Secretariat + Translation cards is intended.

---

## 3.4 — "Our approach": Validate · Design · Build (edit 06) · 🟡 draft

**Location:** `.approach__pillars` `2096–2186`; section h2 `2090–2093` "Validate. Develop.
Build." → **"Validate. Design. Build."**

Three columns today — Validate (V, 2098–2124), Develop (D, 2128–2154), Build (B, 2158–2184).

**Changes:**
1. Rename middle column **Develop → Design** (h3 2129–2132). Big initial stays "D".
2. Section heading → **"Validate. Design. Build."**
3. Move bullet **"Market development"** out of the middle column into **Validate**.
4. Move bullet **"Business development"** out of the middle column into **Build**.
5. New intro copy for the Design column.

**Resulting bullets:**
- **Validate:** Primary & secondary research · Human-centred design · Stakeholder workshops
  · Peer-reviewed evidence · **Market development** _(moved in)_
- **Design** _(was Develop)_: Funding strategy & bid writing · Consortium building
- **Build:** Product & prototype development · Field trials & validation · Spin-out creation
  · Scaling partnerships · **Business development** _(moved in)_

**Design column intro (draft, dash-free):**
> "With the concept proven, we design how it gets delivered, shaping the solution, the
> funding strategy and the consortium needed to make it real. This is where a validated idea
> becomes a fundable, buildable plan, with the right partners and resources behind it."

**Open (Hannah):** Design column has only 2 bullets vs 5 each side — add 1–2 (e.g. "Product
& system design", "Solution architecture", "Service & UX design")? And consider rewording
"Market development" → "Market research / validation" in the Validate column. Update CY.

---

## 3.5 — Remove the Secretariat featured block (edit 07) · ✅ confirmed

**Location:** "Featured capability — Government Secretariat & Programme Delivery" section
`2325–2368` (`id="about"`, image + checklist + CTA to `/capabilities/secretariat.html`).

**Action:** delete the whole `<section>`. Rationale: Secretariat is dropped from the
capability set (3.3) so the standalone feature goes too.

**Watch-outs:**
- The section has `id="about"` — check nothing links to `#about` on this page (the nav
  "About" points to `/about.html`, so likely safe, but grep `href="#about"`).
- Removing it changes page rhythm between "Selected case studies" and the CTA banner —
  screenshot-check spacing.
- Reference screenshot: `docs/input/website-review/07-secretariat-programme-delivery-ARCHIVED.png`.

---

## 3.6 — Partner strip swap (edit 26a) · ✅ confirmed

**Location:** `.partners` strip `1938–1954` (label "Trusted by" 1940–43; logo spans
1944–52). Current: **Defra, Innovate UK, Imperial College, Cambridge, NHS, Forestry
Commission, Cranswick**.

**Changes:**
- **NHS → Plus X Innovation**
- **Cranswick → Welsh Government**

Keep the other five. _(The matching "partners line" prose on `about.html` is edit 26b —
Stage 4.)_

**⚠️ Flag carried to Stage 7:** the BlakBear case study still names Cranswick ("17 Cranswick
production sites"). Hannah only asked to change the strip — leave the case study or change it
too? Logos here are plain text spans, so it's a text swap.

---

## 3.7 — New NPK "green-tankering" case study card (edit 27) · ✅ copy final (image + slot pending)

**Location:** `.projects__grid` `2235–2319`. Four cards today: NPK Recovery (2236), GripAble
(2257), Arts Council of Wales (2278), BlakBear/Cranswick (2299).

**New card copy (final, dash-free):**
> **Eyebrow:** NPK RECOVERY
> **Heading:** "A mobile app that makes event waste greener"
> **Body:** "VDB and Higher Level Software built the NPK Recovery app for event organisers,
> turning green tankering, the sustainable disposal of event waste, into a few taps.
> Organisers compare NPK against competitors on cost and environmental impact, then book a
> collection slot in the app. It puts a transparent, lower-impact option in the hands of the
> people planning the event."
> **Metric line:** "Tonnes diverted from wastewater treatment"

**Open → Stage 7:**
1. **Which card does it replace?** Recommendation: **BlakBear/Cranswick** (2299) — Cranswick
   is being de-emphasised (edit 26). Alternative: replace the existing NPK bio-fertiliser
   card to avoid two NPK eyebrows. Hannah decides.
2. **Image** — Hannah is sending one; save to `images/` (descriptive name, <200KB per
   `CLAUDE.md`), wire into the chosen card's `<img>` + `data-alt-en/cy`.

Showcases the HLS partnership (Stage 5) and the "Product and system development / app
development" capability (3.3) — keep wording consistent across all three.

---

## 3.8 — Footer capabilities list (edit 09) · 🟡 spec in Stage 6

**Location:** footer CAPABILITIES column `2410–2423`. Current six links (Secretariat,
Research, Funding, Science, ESG, Translation) → new six. The footer is **duplicated on every
page**, so this is specified once in **Stage 6** (capabilities & routes) and applied to all
footers. New list, in homepage order:
1. Research and innovation · 2. Product and system development · 3. Fundraising and scale-up
· 4. Science and engineering · 5. Sustainability · 6. Partnership building.

---

## Verification (Stage 3)
- Screenshot hero (stats), capabilities grid, approach section, case studies, CTA — EN + CY,
  light + dark — against `docs/input/website-review/02,03,04,05,06,08,27-*.png`.
- Confirm Secretariat featured block gone and page flows cleanly.
- Confirm capability-card links resolve to the Stage 6 routes (no 404s).
- `grep -n 'Develop\|350+\|8+\|Secretariat' index.html` → expect only intended survivors.
