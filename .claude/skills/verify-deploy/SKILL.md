---
name: verify-deploy
description: Confirm a push to main actually went live on the VPS via the auto-deploy cron — checks VPS HEAD, the deploy log, live HTTP, and container health
user_invocable: true
arguments:
  - name: sha
    description: "Short commit SHA you expect live (default: current origin/main HEAD)"
    required: false
---

# Verify a deploy went live

The VPS cron pulls `origin/main` and rebuilds every minute (see AGENTS.md →
Deploy Workflow). Use this after pushing to confirm the change is actually serving
— don't assume the push is enough (see `docs/learnings/0002`).

## Steps

1. **Know the target SHA** and connect via the Tailscale IP (no rate limiting):
   ```bash
   cd <repo root>
   git rev-parse --short origin/main            # the SHA you expect live
   VPS=100.64.222.60                            # Tailscale; from secrets.env otherwise
   ```

2. **Wait for the cron and check the VPS caught up** (it runs every minute, so
   allow up to ~70s). Poll remotely:
   ```bash
   ssh root@$VPS 'cd /root/arbtechuk/vdb-uk-dot-com && git rev-parse --short HEAD'
   ssh root@$VPS 'tail -3 /var/log/vdb-autodeploy.log; cat /run/vdb-autodeploy.last'
   ```
   Expect HEAD == your target SHA and a `Deploy complete -> <sha>` log line.

3. **Confirm nginx serves it.** nginx runs behind `nginx-proxy`; fetch through the
   proxy network with the real Host header (the `nginx:alpine` image has no
   curl/wget inside, so use a throwaway curl container):
   ```bash
   ssh root@$VPS "docker run --rm --network proxy curlimages/curl:latest \
     -s -o /dev/null -w '%{http_code}\n' -H 'Host: vdb-uk.com' http://vdb-web/"
   ```
   Expect `200`. To confirm specific content, drop `-o /dev/null -w` and grep the
   body (e.g. for the `<title>` or a string you changed).

4. **Check container health / mount** (should mount `dist/`, and normal rebuilds
   must NOT recreate the container — see `docs/learnings/0001`):
   ```bash
   ssh root@$VPS "docker inspect vdb-web \
     --format 'up={{.State.Running}} started={{.State.StartedAt}} mount={{range .Mounts}}{{.Source}}{{end}}'"
   ```
   Expect `Running=true` and mount `/root/arbtechuk/vdb-uk-dot-com/dist`.

5. **End-user check (through Cloudflare):**
   ```bash
   curl -s -o /dev/null -w 'HTTP %{http_code}\n' https://vdb-uk.com/
   ```
   If it lags, Cloudflare/browser cache is usually the cause — hard-refresh.

## Notes

- SSH warns about post-quantum key exchange — harmless; filter it if it clutters
  output: `... 2>&1 | grep -vi 'post-quantum\|store now\|upgraded\|openssh.com'`.
- A directory listing like `/images/` returning `403` is expected (autoindex off);
  individual files serve `200`.
- If HEAD is stuck behind `origin/main`, check the deploy log for a build failure
  (it keeps the previous `dist/` on failure) and that `/usr/local/bin/vdb-autodeploy.sh`
  matches the repo copy.
