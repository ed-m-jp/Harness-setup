---
name: playwright-cli
description: Automate browser interactions, test web pages and work with Playwright tests.
allowed-tools: Bash(playwright-cli:*) Bash(npx:*) Bash(npm:*)
---

<!-- Local fork of the @playwright/cli bundled skill (playwright-core .../cli-client/skill).
     Trimmed + extended for QA use (qa-planner) and token efficiency. Network-inspection,
     multi-browser, and debug-stepping commands added; redundant Quick-start and
     Windows-escaping sections dropped. Shared with the team, so Installation is kept.
     Re-sync manually against the bundle after a `@playwright/cli` upgrade. -->

# Browser Automation with playwright-cli

`playwright-cli` drives a **persistent** browser session: each invocation acts on the running
browser and returns the page state. After every command you get a snapshot whose elements carry
refs (`e3`, `e15`) — pass those refs to the next command. Use `-s=<name>` to run isolated sessions
in parallel (e.g. one per browser engine).

## Installation

If the global `playwright-cli` command isn't available, check for a local copy first:

```bash
npx --no-install playwright-cli --version
```

If that works, prefix every command with `npx` (`npx playwright-cli ...`). Otherwise install it
globally:

```bash
npm install -g @playwright/cli@latest
```

Then install the browser engines you need (see **Browsers & sessions** below) — e.g.
`playwright-cli install-browser firefox`.

## Commands

### Core

```bash
playwright-cli open                       # open the browser
playwright-cli open https://example.com/  # open and navigate
playwright-cli goto https://playwright.dev
playwright-cli type "search query"
playwright-cli click e3
playwright-cli dblclick e7
playwright-cli fill e5 "user@example.com" --submit   # --submit presses Enter after filling
playwright-cli drag e2 e8
playwright-cli drop e4 --path=./image.png            # or --data="text/plain=hello world"
playwright-cli hover e4
playwright-cli select e9 "option-value"
playwright-cli upload ./document.pdf
playwright-cli check e12
playwright-cli uncheck e12
playwright-cli snapshot
playwright-cli eval "document.title"
playwright-cli eval "el => el.getAttribute('data-testid')" e5   # read attrs not in the snapshot
playwright-cli dialog-accept                         # or dialog-accept "text" / dialog-dismiss
playwright-cli resize 1920 1080
playwright-cli close
```

### Navigation / Keyboard / Mouse

```bash
playwright-cli go-back        # go-forward, reload
playwright-cli press Enter    # ArrowDown, etc.
playwright-cli keydown Shift  # keyup Shift
playwright-cli mousemove 150 300
playwright-cli mousedown      # mousedown right / mouseup / mouseup right
playwright-cli mousewheel 0 100
```

### Save as

```bash
playwright-cli screenshot                 # screenshot e5  /  --filename=page.png
playwright-cli pdf --filename=page.pdf
```

### Tabs

```bash
playwright-cli tab-list
playwright-cli tab-new https://example.com/page
playwright-cli tab-close 2
playwright-cli tab-select 0
```

### Storage

```bash
playwright-cli state-save auth.json       # save cookies + storage (omit name -> timestamped)
playwright-cli state-load auth.json       # restore, to skip login

playwright-cli cookie-list                # --domain=example.com
playwright-cli cookie-get session_id      # cookie-set <name> <value> [--domain= --httpOnly --secure] / cookie-delete / cookie-clear
playwright-cli localstorage-list          # localstorage-get/set/delete/clear <key> [value]
playwright-cli sessionstorage-list        # sessionstorage-get/set/delete/clear <key> [value]
```

### Network

```bash
# Inspect (run after the page loads or after an action). Requests are numbered from 1.
playwright-cli requests              # numbered list of all requests since page load (--static to include static assets)
playwright-cli request 5             # full details of request #5: headers, body, response
playwright-cli request-headers 5     # request headers only
playwright-cli request-body 5        # request body only
playwright-cli response-headers 5    # response headers only
playwright-cli response-body 5       # response body (text inlined; binary saved to a file)

# Mock / control
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "https://api.example.com/**" --body='{"mock": true}'
playwright-cli route-list
playwright-cli unroute "**/*.jpg"    # unroute (no arg) removes all routes
playwright-cli network-state-set offline   # or: online
```

### DevTools

```bash
playwright-cli console                 # console messages (e.g. console warning to filter)
playwright-cli run-code "async page => await page.context().grantPermissions(['geolocation'])"
playwright-cli run-code --filename=script.js
playwright-cli tracing-start           # tracing-stop
playwright-cli video-start video.webm  # video-stop
playwright-cli video-chapter "Chapter Title" --description="Details" --duration=2000
playwright-cli video-show-actions --duration=600 --position=top-right   # video-hide-actions
playwright-cli generate-locator e5 --raw       # produce a Playwright locator for an element
playwright-cli highlight e5 --style="outline: 3px dashed red"   # highlight --hide to clear

# launch the dashboard for UI review / design feedback — user annotates the page, you receive
# the annotated screenshot, snapshot, and notes
playwright-cli show --annotate

# stepping a paused `npx playwright test --debug=cli` session (see references/playwright-tests.md)
playwright-cli pause-at <location>     # resume / step-over
```

## Raw output

The global `--raw` option strips page status, generated code, and snapshot sections, returning only
the result value — use it to pipe output into other tools. `--json` wraps every reply as JSON.

```bash
playwright-cli --raw eval "JSON.stringify(performance.timing)" | jq '.loadEventEnd - .navigationStart'
TOKEN=$(playwright-cli --raw cookie-get session_id)
playwright-cli list --json
```

## Browsers & sessions

Chrome is the default engine. Firefox / WebKit (Safari) / Edge matter too — use them when installed,
and install them on demand.

```bash
# choose the engine
playwright-cli open --browser=chrome     # firefox | webkit | msedge
playwright-cli install-browser firefox   # install an engine that isn't present yet

# run the same scenario across engines with named, isolated sessions (run sequentially)
playwright-cli -s=chrome  open --browser=chrome  https://app.example.com
playwright-cli -s=firefox open --browser=firefox https://app.example.com
playwright-cli -s=webkit  open --browser=webkit  https://app.example.com

# profiles & attach
playwright-cli open --persistent              # or --profile=/path/to/profile (default is in-memory)
playwright-cli attach --cdp=chrome            # attach to a running Chrome/Edge (reuse a logged-in session)
playwright-cli attach --cdp=http://localhost:9222
playwright-cli -s=msedge detach               # leave the external browser running

# lifecycle
playwright-cli list                # list sessions and their state
playwright-cli close               # close default  (-s=name close for a named session)
playwright-cli close-all           # close every session
playwright-cli kill-all            # force-kill stale/zombie processes
playwright-cli delete-data         # delete a persistent session's user data
```

Each session has independent cookies, storage, cache, history, and tabs. **Never run sessions in
parallel against one flow** — for QA, one agent drives one browser at a time; use separate `-s=`
sessions only for cross-browser runs done in sequence.

## Snapshots

After each command `playwright-cli` saves a snapshot file and prints its path. Take one on demand,
optionally scoped or shallow:

```bash
playwright-cli snapshot                       # whole page, timestamped file
playwright-cli snapshot --filename=after.yaml  # name it when it's part of the result
playwright-cli snapshot "#main"               # scope to a selector
playwright-cli snapshot --depth=4             # limit depth for efficiency
playwright-cli snapshot e34                   # partial snapshot rooted at a ref
playwright-cli snapshot --boxes               # include [box=x,y,w,h] per element
```

## Targeting elements

Prefer refs from the snapshot. CSS selectors and Playwright locators also work:

```bash
playwright-cli click e15
playwright-cli click "#main > button.submit"
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli click "getByTestId('submit-button')"
```

## Example: QA a flow + capture evidence

```bash
playwright-cli -s=fx open --browser=firefox https://app.example.com/login
playwright-cli -s=fx snapshot
playwright-cli -s=fx fill e1 "user@example.com"
playwright-cli -s=fx fill e2 "secret" --submit
playwright-cli -s=fx snapshot                  # verify authenticated state
playwright-cli -s=fx console warning           # app-side errors?
playwright-cli -s=fx requests                  # locate a failing request by number
playwright-cli -s=fx response-body 7           # inspect its response
playwright-cli -s=fx screenshot --filename=evidence.png
playwright-cli -s=fx close
```

## Specific tasks

- **Running and Debugging Playwright tests** [references/playwright-tests.md](references/playwright-tests.md)
- **Request mocking** [references/request-mocking.md](references/request-mocking.md)
- **Running Playwright code** (waits, permissions, downloads, iframes) [references/running-code.md](references/running-code.md)
- **Browser session management** (multi-browser, attach, cleanup) [references/session-management.md](references/session-management.md)
- **Spec-driven testing (plan / generate / heal)** [references/spec-driven-testing.md](references/spec-driven-testing.md)
- **Storage state (cookies, localStorage, auth reuse)** [references/storage-state.md](references/storage-state.md)
- **Test generation** [references/test-generation.md](references/test-generation.md)
- **Tracing** [references/tracing.md](references/tracing.md)
- **Video recording** [references/video-recording.md](references/video-recording.md)
- **Inspecting element attributes** [references/element-attributes.md](references/element-attributes.md)
