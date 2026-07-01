# 0002 — The VPS's installed scripts can drift from the repo copy

- **Date:** 2026-07-01
- **Area:** deploy / infra

## Problem

The repo's `vdb-autodeploy.sh` is a *review copy*. The script the cron actually
runs lives at `/usr/local/bin/vdb-autodeploy.sh` on the VPS. When we adopted the
`src/` → `build.py` → `dist/` pipeline, the docs described a build-aware deploy —
but the **installed** script still only did `git pull` and never ran `build.py`.
A plain merge would have pulled the new tree and never built `dist/`, so the new
content would silently not go live (the old root-mounted files kept serving).

## What we learned

Files that live outside the repo on the VPS — the deploy script, the cron entry,
the `docker-compose.yml` mount of the *running* container — are not updated by
`git pull`. They can drift from what the repo claims. `docker-compose.yml` changes
(e.g. changing the nginx mount from repo-root to `dist/`) also require a one-time
`docker compose up -d` to recreate the container; the cron won't do it.

## How to apply

- Treat `git pull` as updating **files only**. Runtime config (installed scripts,
  cron, container mounts) needs an explicit step.
- After editing `vdb-autodeploy.sh`, re-install it:
  `install -m755 vdb-autodeploy.sh /usr/local/bin/vdb-autodeploy.sh`.
- After changing `docker-compose.yml`, recreate: `docker compose up -d` (build
  `dist/` first if the mount points at it, so the target exists).
- When asked to "make sure it deploys," actually verify end-to-end: VPS HEAD moved,
  build ran (log), live HTTP serves the change, container not unexpectedly broken.
  The `verify-deploy` skill captures this.
