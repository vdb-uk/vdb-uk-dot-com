---
name: preview
description: Build the site with build.py and serve dist/ locally so you can view and screenshot changes before pushing
user_invocable: true
arguments:
  - name: port
    description: "Port to serve on (default: 8000)"
    required: false
---

# Preview the site locally

Build the source into `dist/` and serve it locally so changes can be viewed and
screenshotted before pushing (pushing to `main` auto-deploys to production, so
always preview first).

## Steps

1. **Build** from `src/` + shared assets into `dist/`:
   ```bash
   python3 build.py
   ```
   Expect `build.py completed in ...s (exit=0)`. A non-zero exit means a build
   error (usually a missing `@include` partial) — fix it before serving.

2. **Serve `dist/`** on the chosen port (default 8000), in the background:
   ```bash
   python3 -m http.server <PORT> --directory dist
   ```

3. **Open / screenshot** `http://localhost:<PORT>/` to review. For visual work,
   use the browser tools to load the page and capture both dark and light themes
   (there's a theme toggle in the header) and a mobile width. Check the specific
   page you changed, not just the homepage.

4. **Iterate:** edit files in `src/` / `_partials/` / `styles.css` / `site.js`,
   re-run `python3 build.py`, and refresh. Never edit `dist/` directly — it is
   regenerated on every build.

5. **Stop the server** when done (kill the background `http.server`).

## Notes

- `dist/` is gitignored and rebuilt on the VPS; it is only a local artifact here.
- If a page 404s, check the file exists under `src/` and that its `@include`
  paths resolve (`build.py` fails loudly on a missing include).
- When the preview looks right, ship it: commit to `main`, push, then confirm
  live with the `verify-deploy` skill.
