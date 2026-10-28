---
name: reference-google-profile-playwright
description: Personal WSL playwright-cli Chrome profile pre-logged-into Google (edward.maire@zaiko.io) — paths + reuse commands
metadata:
  type: reference
---

A persistent, Google-logged-in Chrome profile exists for driving `playwright-cli`, set up 2026-06-25. **Personal only** — the user explicitly does NOT want this in the project skill or the global `playwright-cli` skill. Everything runs **inside WSL with Linux browsers** (no Windows browser).

**Profile:** `~/.pw-profiles/google-chrome` — system `/usr/bin/google-chrome`, signed in as `edward.maire@zaiko.io`. Holds live Google session tokens → treat as a credential, keep outside any repo, never commit.

**How it was bootstrapped (one-time):** launched the *real* (non-automation) Chrome so Google's bot detection didn't block the login, then quit to flush cookies:
`/usr/bin/google-chrome --user-data-dir=$HOME/.pw-profiles/google-chrome --no-first-run --no-default-browser-check https://accounts.google.com/` → log in → fully quit (Ctrl+Q).

**How to reuse (verified working — automation-launched `--profile` still landed on myaccount.google.com logged in, not a sign-in wall):**
```bash
playwright-cli -s=chrome open --browser=chrome --profile=$HOME/.pw-profiles/google-chrome <url>
```

**Most robust Chrome path (no automation launch → Google never re-challenges):** start real Chrome with a debug port on the profile, then attach:
```bash
/usr/bin/google-chrome --user-data-dir=$HOME/.pw-profiles/google-chrome --remote-debugging-port=9222 ... &
playwright-cli -s=chrome attach --cdp=http://localhost:9222   # detach (not close) when done
```

**Caveats:** (1) Chrome won't open a `--user-data-dir` another Chrome holds (`SingletonLock`) — quit the real Chrome before `playwright-cli` opens the same dir. (2) A `--profile` launch is automation-flagged, so Google can occasionally force a re-verify; re-bootstrap or use attach. (3) Firefox is NOT set up — would need a headed bootstrap via Playwright's bundled Firefox (no system FF in WSL) and reuse via `--profile`; Firefox has no CDP `attach`.

Related: [[project_playwright_cli_fork]] (the QA skill itself), and `rm -rf` is blocked here.
