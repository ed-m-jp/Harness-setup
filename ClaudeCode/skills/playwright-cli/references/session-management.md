# Browser Session Management

Run multiple isolated browser sessions concurrently with state persistence.

## Named Browser Sessions

Use the `-s` flag to isolate browser contexts. Each session has independent cookies, LocalStorage/SessionStorage, IndexedDB, cache, history, and open tabs.

```bash
# Two isolated sessions; commands are routed by session name
playwright-cli -s=auth open https://app.example.com/login
playwright-cli -s=public open https://example.com

playwright-cli -s=auth fill e1 "user@example.com"
playwright-cli -s=public snapshot
```

When `-s` is omitted, commands use the `default` session.

Set a default session name via environment variable:

```bash
export PLAYWRIGHT_CLI_SESSION="mysession"
playwright-cli open example.com  # Uses "mysession" automatically
```

## Session Lifecycle Commands

```bash
# List all sessions
playwright-cli list

# Stop a browser (default, or named with -s)
playwright-cli close
playwright-cli -s=mysession close

# Stop all sessions
playwright-cli close-all

# Forcefully kill all daemon processes (stale/zombie processes)
playwright-cli kill-all

# Delete a session's user data / profile directory
playwright-cli delete-data
playwright-cli -s=mysession delete-data
```

## Opening with Configuration

```bash
# Config file
playwright-cli open https://example.com --config=.playwright/my-cli.json

# Headed mode
playwright-cli open https://example.com --headed

# Select the browser engine
playwright-cli open https://example.com --browser=chrome    # chrome | firefox | webkit | msedge
```

### Persistent Profile

By default the browser profile is kept in memory only. Use `--persistent` to persist it to disk (auto-generated location), or `--profile` for a custom directory:

```bash
playwright-cli open https://example.com --persistent
playwright-cli open https://example.com --profile=/path/to/profile
```

## Attaching to a Running Browser

Use `attach` to connect to an already-running browser (e.g. to reuse a logged-in session) instead of launching a new one.

### Attach by channel name

Connect to a running Chrome or Edge instance by channel name. The browser must have remote debugging enabled — navigate to `chrome://inspect/#remote-debugging` and check "Allow remote debugging for this browser instance".

```bash
playwright-cli attach --cdp=chrome
playwright-cli attach --cdp=msedge
```

Supported channels: `chrome`, `chrome-beta`, `chrome-dev`, `chrome-canary`, `msedge`, `msedge-beta`, `msedge-dev`, `msedge-canary`.

When `--session` is not provided, the session is named after the channel (e.g. `--cdp=msedge` creates a session called `msedge`), so parallel attaches don't collide on `default`. Pass `--session=<name>` to override.

### Attach via CDP endpoint

Connect to a browser exposing a Chrome DevTools Protocol endpoint:

```bash
playwright-cli attach --cdp=http://localhost:9222
```

### Attach via browser extension

Connect to a browser with the Playwright extension installed:

```bash
playwright-cli attach --extension
```

### Detach

Tear down an attached session without affecting the external browser:

```bash
playwright-cli detach                # default attached session
playwright-cli -s=msedge detach      # specific attached session
```

`detach` only works on sessions created via `attach`. For sessions created via `open`, use `close`.
