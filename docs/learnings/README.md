# Learnings

Compounding knowledge for this repo. When we solve something non-obvious, we
write it down here so the next change — by any agent or person — starts ahead
instead of rediscovering it.

## How to use this

- **Before non-trivial work,** skim the index below for a relevant lesson.
- **After solving something non-obvious,** add an entry (see template) and a
  one-line pointer to the index. One lesson per file.
- If a lesson implies a rule, also encode it where it's enforced (a code comment
  at the point of risk, or a line in `AGENTS.md`) so it can't quietly regress.

## Index

- [0001 — Serve `dist/` via in-place publish (never rename the dir)](0001-serve-dist-via-in-place-publish.md) — why `build.py` must not swap the `dist/` inode.
- [0002 — The VPS's installed scripts can drift from the repo copy](0002-vps-installed-scripts-can-drift.md) — re-install `vdb-autodeploy.sh` after editing it.
- [0003 — Truthful full-page screenshots need theme seeding + force-reveal](0003-truthful-screenshots.md) — why `visual-verify` sets the theme and un-hides `.reveal` sections before shooting.

## Template

```markdown
# NNNN — Short title

- **Date:** YYYY-MM-DD
- **Area:** deploy / build / css / content / infra / …

## Problem
What went wrong or was surprising — concrete symptoms.

## What we learned
The root cause and the durable insight.

## How to apply
The rule to follow next time. Link the code/commit that encodes it.
```
