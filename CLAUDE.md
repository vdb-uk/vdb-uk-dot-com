# CLAUDE.md — VDB UK Website

## What This Is

Static website for VDB UK (VandenberghUK Ltd) at https://vdb-uk.com/. Innovation consultancy founded by Hannah Van Den Bergh, based at Future Space, UWE Bristol.

## Architecture

- **Hosting:** VPS at 217.154.35.232, nginx container via `nginx-proxy` + `acme-companion`
- **SSL:** Let's Encrypt (auto-renewing)
- **DNS:** Cloudflare zone `vdb-uk.com` — A record to VPS, CNAME www to apex
- **Repo:** `arbtechuk/vdb-uk-dot-com` (public)
- **VPS path:** `/root/arbtechuk/vdb-uk-dot-com/`
- **Container path:** `/home/node/.openclaw/arbtechuk/vdb-uk-dot-com/`

Edits to files on the VPS are served instantly — the nginx container mounts the directory as a read-only volume. No build step.

## Deploy Workflow

After making changes locally:

```bash
git add -A && git commit -m "..."
git push
# Then pull on VPS to make it live:
source secrets.env
ssh root@$VPS_IP "cd /root/arbtechuk/vdb-uk-dot-com && git pull --ff-only"
```

The `secrets.env` file (gitignored) contains `VPS_IP` for SSH access.

## Site Structure

```
/
├── index.html                          # Homepage
├── about.html                          # About VDB
├── contact.html                        # Contact page
├── capabilities/
│   ├── secretariat.html                # Secretariat & Programme Management
│   ├── research.html                   # Research & Innovation
│   ├── funding.html                    # Funding & Grant Strategy
│   ├── science.html                    # Science & Engineering
│   ├── esg.html                        # ESG & Sustainability
│   └── translation.html               # Translation & Welsh Language
├── case-studies/
│   ├── index.html                      # Case Studies catalogue (all 10)
│   ├── devolved-funding-architecture.html  # Wales/ACW funding
│   ├── npk-recovery.html              # NPK Recovery circular economy
│   ├── gripable.html                   # GripAble/SqueezAble MedTech
│   ├── plus-x-innovation.html         # Plus X hardware accelerator
│   ├── blakbear.html                   # BlakBear food-waste sensors
│   ├── lga-funding-analysis.html      # LGA funding analysis
│   ├── wales-nutrient-recovery.html   # Wales nutrient recovery
│   ├── wales-bilingual-organisations.html  # Bilingual governance
│   ├── devolved-political-campaigns.html   # Political campaigns
│   └── cambridge-sustainability-research.html  # Cambridge research
├── projects/                           # Legacy redirects only — all point to /case-studies/
├── images/                             # All site images
├── docs/plans/                         # Build plans and content specs
├── docker-compose.yml                  # VPS container config
└── CNAME                               # Custom domain for GitHub Pages (legacy)
```

## Design System

- **Palette:** VDB brand — primary purple `#5E1A8E`, orange CTAs `#E89A3C`, teal secondary `#1C9C8E`, on the dark slate hero / stone-cream light backgrounds. NOTE: the rebrand (2026-06, see `docs/plans/30-06-2026-rebrand/`) remapped the token *values* in place — the `--red-*` custom properties now hold purple values, `--orange-500`/`--teal-500` are the accent tokens, and `--gold-*` is retained as a warm accent. So `var(--red-500)` renders purple. Don't be misled by the legacy token names.
- **Fonts:** Outfit (headings, 600) + DM Sans (body, 16px/1.65) — loaded from Google Fonts. (Was Crimson Pro serif before the 2026-06 rebrand.)
- **i18n:** All content bilingual EN/CY. Toggle in header. Auto-detect browser language. Content uses `data-en` / `data-cy` attributes on `<span>` elements, controlled by `data-lang` on `<html>`.

## Conventions

- **Single-file pages:** Each page is a self-contained HTML file. Shared styles are duplicated (no build tool). When the site grows, extract to a shared CSS file.
- **Images:** Optimised JPGs under 200KB each in `images/`. Use descriptive filenames like `hero-secretariat.jpg`, `project-npk-field.jpg`.
- **Welsh translations:** Machine translation is acceptable for initial deployment but government-facing pages (especially Secretariat) need professional review before sharing with Welsh public sector contacts.
- **No frameworks:** Plain HTML/CSS/JS. No build step. No npm. Keep it simple — Hannah's AI agent needs to be able to edit these files directly.

## VPS Access

SSH access uses the IP from `secrets.env`. Prefer Tailscale IP (100.64.222.60) — no rate limiting. Public IP (217.154.35.232) has aggressive rate limiting.

## Plans & Specs

Full page-by-page build plan with content outlines and image generation prompts: `docs/plans/vdb-website-pages.md`
