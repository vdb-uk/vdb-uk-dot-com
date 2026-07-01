#!/usr/bin/env bash
# Auto-deploy vdb-uk.com: if the VPS is behind origin/main, pull and rebuild.
# nginx serves the built dist/ (see docker-compose.yml), so a deploy is:
#   git pull --ff-only  +  python3 build.py  (which republishes dist/ in place).
# The cron entry redirects stdout/stderr to /var/log/vdb-autodeploy.log, so this
# script just prints; it stays silent on no-op runs to keep the log clean.
set -euo pipefail

repo_dir="/root/arbtechuk/vdb-uk-dot-com"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $*"; }

cd "$repo_dir"

# Heartbeat: prove the job ran this minute, even if the fetch later fails.
date -u +%FT%TZ > /run/vdb-autodeploy.last

if ! git fetch --prune --quiet; then
  log "[ERROR] git fetch failed"
  exit 1
fi

local_head=$(git rev-parse HEAD)
remote_head=$(git rev-parse origin/main)

if [ "$local_head" = "$remote_head" ]; then
  exit 0  # up to date — stay silent
fi

log "[INFO] Deploying ${local_head:0:7} -> ${remote_head:0:7}"

if ! git pull --ff-only origin main; then
  log "[ERROR] git pull --ff-only failed"
  exit 1
fi

if ! python3 build.py; then
  log "[ERROR] build.py failed; keeping previously served dist/"
  exit 1
fi

log "[INFO] Deploy complete -> $(git rev-parse --short HEAD)"
