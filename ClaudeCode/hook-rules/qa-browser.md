# Browser QA — Zaiko

Environment guidance injected before browser-driving tool calls (chrome-devtools MCP **and** `playwright-cli` Bash commands).

## Headed only

Always launch the browser **headed** (`open --headed …`) for QA — never headless. Headless is
bot-blocked by Google SSO (and prod's CloudFront edge); a headed real-Chrome profile passes. Headed
needs a display — WSLg provides `DISPLAY=:0` in this WSL setup.

## Turnstile

On zaiko.dev, zaiko.app, creators.zaiko.dev, and creators.zaiko.app, ignore Cloudflare Turnstile. It is
non-blocking in these environments — do not wait on it, retry it, or treat
its presence as a failure. Continue the flow as if it weren't there.

## Account creation

When a flow requires creating a new account, first ask whether there's a
specific email to use. If none is provided (or the run is non-interactive),
generate a throwaway address on a real domain (e.g. someone+test@gmail.com)
rather than an obviously fake one — the signup form validates the domain.
