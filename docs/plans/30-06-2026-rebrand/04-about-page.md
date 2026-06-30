# Stage 4 — About Page (`about.html`)

**Edits covered:** 10, 11, 12, 13, 14, 26b.
**File:** `about.html`. Do after Stages 1–2; independent of Stages 3, 5, 6.

> **Why these are here, not on the homepage:** the brief presents 10/11/12 as homepage
> items, but verification shows they live on `about.html`. The award-badge "Recognised at
> the highest level" block, the large Hannah portrait, the team carousel, and the
> Company Details card are all on this page. (See README routing correction.)

Line numbers drift as edits land — re-grep before each. EN **and** CY for every change.

---

## 4.1 — Remove the large portrait photo (edit 10) · ✅ confirmed

**Location:** `<img src="/images/hannah-blouse.jpg" …>` at `1759` (896×1195, alt "Hannah Van
Den Bergh — Founder and Director of VDB"). It sits between the award section and Hannah's
bio (`<h2>Hannah Van Den Bergh</h2>` at 1766). Hannah: "I hate it."

**Action:** remove the big portrait image (and its wrapper, if the layout is a two-column
image+bio that would otherwise leave an empty column — collapse to single column).

**⚠️ Note:** the alt text contains an em dash ("Founder and Director of VDB") — moot once
removed, but if any nearby Hannah imagery stays, apply the Stage 2 dash rule.

**Open → Stage 7:** does anything replace the slot? Options: leave empty (bio goes full
width), or a new straight-on photo of Hannah in the team-photo style. This is **not** the
same as edit 13 (that's a different *team member*).

---

## 4.2 — Remove "Working across the UK" + Company Details (edit 11) · ✅ confirmed · ❓ card decision

**Location:** `<section class="uk-presence reveal">` starting **2132** — eyebrow "Where we
work" (2136), h2 "Working across the UK" (2140), and the `.company-card` aside (~2148–2172):
Legal name **VandenberghUK Ltd** (2158), Director **Hannah Van Den Bergh**, Companies House
**#12296613**, Location.

**Action:** remove the whole `.uk-presence` section.

**❓ Company Details decision (Stage 7):** Companies House details are often kept for
legitimacy. **Keep-and-move to footer, or delete entirely?**
- **Key fact that de-risks deletion:** the footer **already** carries
  `© 2026 VandenberghUK Ltd (company no. 12296613)` on every page. So the legal entity +
  company number survive even if the card is deleted. Only the **Director** and **Location**
  rows would be lost.
- **Recommendation:** delete the card (legitimacy already covered by the footer copyright).
  If Hannah wants Director/Location retained, add a slim line to the footer rather than
  rebuilding the card. Confirm.
- Also remove the footer "Working across the UK" contact line (`2267`) if that phrasing is
  being retired, or keep as a location note — confirm with the card decision.

Reference: `docs/input/website-review/11-working-across-uk-REMOVED.png`.

---

## 4.3 — Track record redesign: "Recognised at the highest level" (edit 12) · ✅ Option B

**Problem (Hannah):** as-is it reads as though *VDB* won these awards. In reality VDB
**championed and supported the businesses** that were recognised, from early stage to
scale-up. Redesign for clarity.

**Location:** the "Track record" block — eyebrow `1685`, h2 "Recognised at the highest
level" `1688–89`, and four `award-card`s: **Earthshot Prize** (1700–01), **Terra Carta Labs**
(1713), **Dyson Award** (1725–26), **Forbes 30 Under 30** (1738).

**Selected: Option B. Final spec (dash-free):**
- **Eyebrow:** TRACK RECORD _(keep)_
- **Headline:** "We back businesses recognised at the highest level"
- **Subhead:** "We have championed and supported businesses from early stage through to
  scale-up. The ventures we have backed have gone on to be Earthshot Prize shortlisted,
  Terra Carta Labs winners, Dyson Award winners and Forbes 30 Under 30 listees."
- **Journey strip** (new small element): **Early stage → Growth → Scale-up** _(render as
  three steps; "→" here is a UI connector, not prose — implement as styled chevrons/SVG, not
  a literal em dash in copy)._
- **Relabel each badge** with the supported venture's achievement (exact sub-labels to
  confirm at build):
  - Earthshot Prize · supported venture shortlisted
  - Terra Carta Labs · supported venture won
  - Dyson Award · supported venture won
  - Forbes 30 Under 30 · supported founder listed
- **Partners line** (this is edit **26b**, below): "We have partnered with Imperial College
  London, the University of Cambridge, Defra, Innovate UK, the Forestry Commission, Plus X
  Innovation and the Welsh Government."

**Align Hannah's bio:** the bio paragraph at `1772` (and EN equivalent) says she "built
partnerships that have won recognition from Earthshot, Terra Carta, Dyson, and Forbes" —
consistent with the reframe (partnerships won recognition, not VDB). Light-touch check that
the wording doesn't imply VDB itself won the awards. Update CY to match.

Reference: `docs/input/website-review/12-track-record.png`.

---

## 4.4 — Partner names line (edit 26b) · ✅ confirmed

Part of 4.3's partners line. Versus the old set: **NHS → Plus X Innovation**,
**Cranswick → Welsh Government**; keep Imperial, Cambridge, Defra, Innovate UK, Forestry
Commission. _(The homepage "Trusted by" strip is the separate edit 26a — Stage 3.6.)_
Same Cranswick-in-BlakBear flag applies (Stage 7).

---

## 4.5 — Team photos (edits 13 + 14) · ⏳ blocked on assets

**Location:** the team carousel section (h2 `1810`), cards e.g. `team-adam.jpg` (1826),
`team-rob.jpg` (1841), plus the others (Steph, Naz, etc.) seen in the carousel markup.
Candidate replacement headshots already sit in `docs/input/images/` (rob, adam, kester,
steph, plus the originals).

**Edit 13 — one straight-on swap:** replace a specific team member's *angled* photo with a
straight-on shot matching the others. ⏳ Need: which member + the photo file. Then drop into
that card's `<img>` (keep dimensions/`loading`/`data-alt-*`).

**Edit 14 — dynamic style for all:** move all team headshots toward candid/environmental
"in the work" shots (the Kester Leek shot is the reference direction). ⏳ Need: supplied
photos per member in that style. This is an asset-gathering task, then a straightforward
`<img>` swap per card.

**Implementation is trivial once photos arrive** — optimise to <200KB JPG per `CLAUDE.md`,
descriptive filenames (`team-<name>.jpg`), update `images/`. Tracked in Stage 7.

---

## Verification (Stage 4)
- Screenshot the About page top-to-bottom EN + CY, light + dark, against
  `docs/input/website-review/10,11,12,13,14-*.png`.
- Confirm the large portrait and `.uk-presence` section are gone and the layout reflows
  cleanly (no empty grid columns).
- Confirm the award block now reads as "businesses we backed", with the journey strip and
  relabelled badges.
- `grep -n 'uk-presence\|hannah-blouse\|Recognised at the highest' about.html` →
  expect only the intended survivors.
