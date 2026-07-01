#!/usr/bin/env bash
# Ensure the `dev-browser` CLI is installed, installing it if missing.
#
# dev-browser (https://github.com/sawyerhood/dev-browser, MIT) gives an agent a
# real headless browser it can drive with small JavaScript scripts — used by the
# visual-verify skill to screenshot pages before committing.
#
# It is a GLOBAL agent tool, not a site dependency: it never touches the site's
# build and the site itself stays npm-free (see AGENTS.md → "No frameworks").
#
# Idempotent — safe to run every time; it only does work when something is missing.
set -euo pipefail

if command -v dev-browser >/dev/null 2>&1; then
  echo "dev-browser present: $(command -v dev-browser)"
else
  if ! command -v npm >/dev/null 2>&1; then
    echo "ERROR: dev-browser needs Node.js/npm, which isn't installed on this machine." >&2
    echo "Install Node (https://nodejs.org/ — on macOS: 'brew install node'), then re-run." >&2
    exit 1
  fi
  echo "Installing dev-browser globally (npm install -g dev-browser)…"
  npm install -g dev-browser
fi

# Install/verify the bundled Playwright Chromium. Fast no-op once present.
echo "Ensuring Playwright Chromium (dev-browser install)…"
dev-browser install

echo "dev-browser ready."
