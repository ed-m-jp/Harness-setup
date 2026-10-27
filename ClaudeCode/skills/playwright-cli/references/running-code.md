# Running Custom Playwright Code

Use `run-code` to execute arbitrary Playwright code for advanced scenarios not covered by CLI commands.

## Syntax

```bash
playwright-cli run-code "async page => {
  // Your Playwright code here
  // Access page.context() for browser context operations
}"
```

Load the function from a file instead of inline:

```bash
playwright-cli run-code --filename=./my-script.js
```

The code must be a single function expression; it is wrapped in `(...)` and evaluated. import/export/require syntax is not supported.

## Permissions

```bash
# Grant multiple permissions (optionally scoped to an origin)
playwright-cli run-code "async page => {
  await page.context().grantPermissions(['notifications', 'camera', 'microphone']);
  await page.context().grantPermissions(['clipboard-read'], { origin: 'https://example.com' });
}"

# Clear all permission overrides
playwright-cli run-code "async page => {
  await page.context().clearPermissions();
}"
```

### Geolocation

Geolocation requires the `geolocation` permission, then set coordinates:

```bash
playwright-cli run-code "async page => {
  await page.context().grantPermissions(['geolocation']);
  await page.context().setGeolocation({ latitude: 37.7749, longitude: -122.4194 });
}"
```

## Wait Strategies

```bash
# Wait for network idle
playwright-cli run-code "async page => {
  await page.waitForLoadState('networkidle');
}"

# Wait for an element to reach a state (with optional timeout)
playwright-cli run-code "async page => {
  await page.locator('.loading').waitFor({ state: 'hidden' });
  await page.locator('.result').waitFor({ timeout: 10000 });
}"

# Wait for a function to return true
playwright-cli run-code "async page => {
  await page.waitForFunction(() => window.appReady === true);
}"
```

## Frames and Iframes

```bash
# Work inside an iframe
playwright-cli run-code "async page => {
  const frame = page.locator('iframe#my-iframe').contentFrame();
  await frame.locator('button').click();
}"

# List all frame URLs
playwright-cli run-code "async page => {
  return page.frames().map(f => f.url());
}"
```

## File Downloads

```bash
playwright-cli run-code "async page => {
  const downloadPromise = page.waitForEvent('download');
  await page.getByRole('link', { name: 'Download' }).click();
  const download = await downloadPromise;
  await download.saveAs('./downloaded-file.pdf');
  return download.suggestedFilename();
}"
```

## Media Emulation

One-liner: `await page.emulateMedia({ colorScheme: 'dark' });` — also accepts `colorScheme: 'light'`, `reducedMotion: 'reduce'`, or `media: 'print'`.

## Clipboard

Requires the `clipboard-read` permission for reads: `navigator.clipboard.readText()` / `navigator.clipboard.writeText(text)` via `page.evaluate(...)`.

## JavaScript Execution

```bash
# Execute JS and return the result; second arg passes data into the browser
playwright-cli run-code "async page => {
  const multiplier = 5;
  return await page.evaluate(m => document.querySelectorAll('li').length * m, multiplier);
}"
```

Page info one-liners: `await page.title()`, `page.url()`, `await page.content()`, `page.viewportSize()`.

## Error Handling

```bash
playwright-cli run-code "async page => {
  try {
    await page.getByRole('button', { name: 'Submit' }).click({ timeout: 1000 });
    return 'clicked';
  } catch (e) {
    return 'element not found';
  }
}"
```

## Complex Workflows

```bash
# Login and save authenticated storage state for reuse
playwright-cli run-code "async page => {
  await page.goto('https://example.com/login');
  await page.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
  await page.getByRole('textbox', { name: 'Password' }).fill('secret');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForURL('**/dashboard');
  await page.context().storageState({ path: 'auth.json' });
  return 'Login successful';
}"
```
