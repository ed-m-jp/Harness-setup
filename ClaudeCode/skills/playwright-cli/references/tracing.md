# Tracing

Capture detailed execution traces for debugging and analysis. Traces include DOM snapshots, screenshots, network activity, console logs, and timing.

## Basic Usage

```bash
# Start trace recording
playwright-cli tracing-start

# Perform actions
playwright-cli open https://example.com
playwright-cli click e1
playwright-cli fill e2 "test"

# Stop trace recording
playwright-cli tracing-stop
```

## What a Trace Captures

Tracing writes a `.playwright-cli/traces/` directory containing the action log (`trace-{timestamp}.trace`), the network log (`trace-{timestamp}.network`), and a `resources/` directory of cached assets (images, fonts, stylesheets, scripts) for replay.

Captured per step:

- **Actions** — clicks, fills, hovers, keyboard input, navigations.
- **DOM** — full snapshot before and after each action.
- **Screenshots** — visual state at each step.
- **Network** — all requests/responses with headers, bodies, sizes, and timing (DNS, connect, TLS, TTFB, download), including failures.
- **Console** — all `console.log`/`warn`/`error` messages.
- **Timing** — precise timing for each operation.

Compared to video/screenshots, a trace is the only one offering step-by-step replay with DOM and network inspection (video is best for demos, screenshots for quick capture).

## Use Cases

- **Debugging failed actions** — inspect the DOM state at the moment a click/fill failed.
- **Analyzing performance** — view the network waterfall to find slow resources.
- **Capturing evidence** — record a complete user flow for documentation.

```bash
playwright-cli tracing-start
playwright-cli open https://app.example.com
playwright-cli click e5      # this fails — trace shows DOM state at the attempt
playwright-cli tracing-stop
```

## Notes

- Start tracing before the problem — trace the entire flow, not just the failing step.
- Tracing adds overhead, and large traces consume significant disk space. Clean up old traces, e.g. `find .playwright-cli/traces -mtime +7 -delete`.
- Some dynamic content may not replay perfectly.
