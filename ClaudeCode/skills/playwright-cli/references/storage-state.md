# Storage Management

Manage cookies, localStorage, sessionStorage, and complete browser storage state.

## Storage State (auth reuse)

Save and restore complete browser state (cookies + storage). This is the headline use: log in once, save the state, and reuse it to skip login in later sessions.

```bash
# Save: auto-generated filename (storage-state-{timestamp}.json) or a specific path
playwright-cli state-save
playwright-cli state-save auth.json

# Load a saved state, then open a page to apply it
playwright-cli state-load auth.json
playwright-cli open https://app.example.com/dashboard   # already logged in
```

The saved JSON has two top-level keys: `cookies` (array of cookie objects — `name`, `value`, `domain`, `path`, `expires`, `httpOnly`, `secure`, `sameSite`) and `origins` (per-origin `localStorage` as `{ name, value }` pairs).

### Authentication state reuse

```bash
# Step 1: log in and save the authenticated state
playwright-cli open https://app.example.com/login
playwright-cli snapshot
playwright-cli fill e1 "user@example.com"
playwright-cli fill e2 "password123"
playwright-cli click e3
playwright-cli state-save auth.json

# Step 2: later, restore and skip login
playwright-cli state-load auth.json
playwright-cli open https://app.example.com/dashboard
```

## Cookies

```bash
# List (optionally filter by domain or path)
playwright-cli cookie-list
playwright-cli cookie-list --domain=example.com
playwright-cli cookie-list --path=/api

# Get / set / delete / clear
playwright-cli cookie-get session_id
playwright-cli cookie-set session abc123
playwright-cli cookie-set session abc123 --domain=example.com --path=/ --httpOnly --secure --sameSite=Lax
playwright-cli cookie-set remember_me token123 --expires=1893456000   # Unix timestamp
playwright-cli cookie-delete session_id
playwright-cli cookie-clear
```

### Advanced: multiple cookies / custom options

For adding several cookies at once, use `run-code`:

```bash
playwright-cli run-code "async page => {
  await page.context().addCookies([
    { name: 'session_id', value: 'sess_abc123', domain: 'example.com', path: '/', httpOnly: true },
    { name: 'preferences', value: JSON.stringify({ theme: 'dark' }), domain: 'example.com', path: '/' }
  ]);
}"
```

## Local Storage

```bash
playwright-cli localstorage-list
playwright-cli localstorage-get token
playwright-cli localstorage-set theme dark
playwright-cli localstorage-set user_settings '{"theme":"dark","language":"en"}'   # JSON value
playwright-cli localstorage-delete token
playwright-cli localstorage-clear
```

### Advanced: multiple operations

```bash
playwright-cli run-code "async page => {
  await page.evaluate(() => {
    localStorage.setItem('token', 'jwt_abc123');
    localStorage.setItem('user_id', '12345');
    localStorage.setItem('expires_at', Date.now() + 3600000);
  });
}"
```

## Session Storage

```bash
playwright-cli sessionstorage-list
playwright-cli sessionstorage-get form_data
playwright-cli sessionstorage-set step 3
playwright-cli sessionstorage-delete step
playwright-cli sessionstorage-clear
```

## Security Notes

- Never commit storage state files containing auth tokens; add them to `.gitignore` and delete after automation completes.
- Use environment variables for sensitive data. Sessions default to in-memory mode, which is safer for sensitive operations.
