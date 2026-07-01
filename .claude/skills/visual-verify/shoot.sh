#!/usr/bin/env bash
# Screenshot one or more pages in dark + light theme at desktop + mobile widths
# using dev-browser (headless Chromium). Part of the visual-verify skill.
#
# Usage:  shoot.sh <base_url> [<path> ...]
#   shoot.sh http://localhost:8000 / /about.html /contact.html
#   shoot.sh https://vdb-uk.com/ /about.html      # (also works against live prod)
#
# With no paths it captures the home page ("/"). Prints each saved PNG as a
# "SAVED: <path>" line (files land in ~/.dev-browser/tmp/) for the agent to read.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BASE="${1:-}"
if [ -z "$BASE" ]; then
  echo "usage: shoot.sh <base_url> [<path> ...]" >&2
  exit 2
fi
shift
[ "$#" -eq 0 ] && set -- /   # default to home page

command -v dev-browser >/dev/null 2>&1 || {
  echo "dev-browser not found — run ensure-dev-browser.sh first." >&2
  exit 1
}

# JSON-encode inputs so they drop safely into the generated JS.
BASE_JSON="$(python3 -c 'import json,sys; print(json.dumps(sys.argv[1]))' "$BASE")"
PATHS_JSON="$(python3 -c 'import json,sys; print(json.dumps(sys.argv[1:]))' "$@")"

{
  printf 'const BASE = %s;\n' "$BASE_JSON"
  printf 'const PATHS = %s;\n' "$PATHS_JSON"
  cat "$SCRIPT_DIR/shoot.js"
} | dev-browser --headless --timeout 120
