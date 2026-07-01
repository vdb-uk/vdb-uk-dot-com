#!/usr/bin/env bash

set -euo pipefail

log_file="/var/log/vdb-autodeploy.log"
repo_dir="/root/arbtechuk/vdb-uk-dot-com"

{
  echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] Starting auto-deploy"
  cd "$repo_dir"

  # Always fetch first so git can detect remote updates reliably.
  if ! git fetch --prune --quiet; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] git fetch failed"
    exit 1
  fi

  local_head=$(git rev-parse HEAD)
  remote_head=$(git rev-parse origin/main)

  if [ "$local_head" = "$remote_head" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] No updates available"
    exit 0
  fi

  if ! git pull --ff-only origin main; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] git pull --ff-only failed"
    exit 1
  fi

  if ! python3 build.py; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] build.py failed; keeping previous dist/"
    exit 1
  fi

  echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] Deploy build completed"
} | tee -a "$log_file"
