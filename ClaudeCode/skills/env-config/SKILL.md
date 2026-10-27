---
name: env-config
description: Environment and config rules when adding or changing env vars or config access.
---

# Env and Config

## Goal

Apply consistent rules when adding or changing environment variables or configuration access.

## Workflow
1. Identify any new or changed env/config values.
2. Validate required config early; fail loudly if missing.
3. Update .env.example with safe placeholders when adding env vars.
4. Use env() only in config files; use config() everywhere else.
5. Document new requirements in README or inline where appropriate.

## Output format
Provide:
- Changes made to env/config usage
- Any required documentation updates

## Constraints
- No silent defaults for required config.
- Do not commit secrets or local config files.
