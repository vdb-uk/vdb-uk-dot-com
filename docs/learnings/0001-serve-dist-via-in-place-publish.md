# 0001 — Serve `dist/` via in-place publish (never rename the dir)

- **Date:** 2026-07-01
- **Area:** deploy / build / infra

## Problem

nginx serves the built site from `dist/` via a Docker bind mount
(`/root/arbtechuk/vdb-uk-dot-com/dist:/usr/share/nginx/html:ro`). `build.py`
originally published by building into `dist.tmp` and then renaming it over
`dist/` (`shutil.rmtree(dist)` + `dist.tmp` → `dist`).

That looks atomic and safe, but it silently breaks the running site. Verified on
the VPS with a throwaway container: after the rename, reads inside the container
returned `cat: can't open '.../index.html': No such file or directory`.

## What we learned

A Docker bind mount is pinned to the **inode** of the source directory at
container start. Renaming `dist/` swaps its inode, so the running container stays
bound to the old (now-unlinked) directory and never sees the new build — the very
first cron rebuild after cutover would take the live site down until someone
recreated the container.

**In-place file updates are visible; directory renames are not.** Replacing the
files *inside* the stable `dist/` directory (keeping its inode) is seen by nginx
immediately, because nginx opens each file fresh per request.

## How to apply

`build.py`'s `publish()` keeps `dist/`'s inode stable: it replaces each file
atomically with `os.replace` and prunes stale entries, so a concurrent request
never sees a missing file. **Never reintroduce a `dist/` directory rename**, and
never point the bind mount at a path that gets swapped. If you refactor `build.py`,
preserve `publish()` (there's a comment in the code explaining why).

Same rule applies to any future atomic-swap deploy idea: swap file contents, not
the mounted directory — or recreate the container after the swap.
