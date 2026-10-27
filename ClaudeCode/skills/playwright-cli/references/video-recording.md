# Video Recording

Capture browser automation sessions as video for debugging, documentation, or verification. Produces WebM (VP8/VP9 codec).

## Basic Recording

```bash
# Open browser first
playwright-cli open

# Start recording (use a descriptive path)
playwright-cli video-start recordings/login-flow.webm

# Add a chapter marker for section transitions
playwright-cli video-chapter "Getting Started" --description="Opening the homepage" --duration=2000

# Navigate and perform actions
playwright-cli goto https://example.com
playwright-cli snapshot
playwright-cli click e1

playwright-cli video-chapter "Filling Form" --description="Entering test data" --duration=2000
playwright-cli fill e2 "test input"

# Stop and save
playwright-cli video-stop
```

Video is a visual recording (good for demos/documentation); for DOM/network/console inspection use [tracing](tracing.md) instead.

## Rich overlays via run-code

For a polished "hero" video, drive the whole scenario through `playwright-cli run-code --filename your-script.js` instead of the CLI. This lets you add paced typing (`pressSequentially` with `delay`), pauses, chapter cards, and annotations. Workflow: run the scenario via CLI first to note all locators/actions, then write the script (using `page.screencast.*`) and run it.

Overlays are `pointer-events: none`, so sticky overlays stay visible while you click/fill without interfering.

```js
async (page) => {
  await page.screencast.start({ path: 'video.webm', size: { width: 1280, height: 800 } });
  await page.goto('https://demo.playwright.dev/todomvc');

  // Full-screen chapter card (blurs page, blocks until duration expires, auto-removes)
  await page.screencast.showChapter('Adding Todo Items', { description: 'Add items to the list.', duration: 2000 });
  await page.getByRole('textbox', { name: 'What needs to be done?' }).pressSequentially('Walk the dog', { delay: 60 });
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');

  // Sticky custom HTML overlay; dispose when done
  const annotation = await page.screencast.showOverlay(
    `<div style="position:absolute;top:8px;right:8px;padding:6px 12px;background:rgba(0,0,0,0.7);border-radius:8px;color:white;">✓ Item added</div>`
  );
  await page.waitForTimeout(1500);
  await annotation.dispose();

  // You can also highlight a locator's bounding box via showOverlay(html, { duration }).
  await page.screencast.stop();
};
```

### Overlay API

- `page.screencast.showChapter(title, { description?, duration?, styleSheet? })` — full-screen chapter card with blurred backdrop, for section transitions.
- `page.screencast.showOverlay(html, { duration? })` — custom HTML overlay for callouts, labels, highlights. Returns a disposable when no `duration` is given.
- `disposable.dispose()` — remove a sticky overlay.
- `page.screencast.hideOverlays()` / `showOverlays()` — temporarily hide/show all overlays.

## Notes

- Recording adds slight overhead; large recordings consume significant disk space.
