---
name: testing
description: Testing and build guidance for changes.
---

# Testing

## Goal

Run the most relevant checks for the change and document exactly what was run.
You are always allowed to access the network to run backend tests.

## Workflow
1. Check project scripts (composer.json, package.json, etc.).
2. Run the most relevant checks for the change.
3. If you can't run something, say why and rely on CI.

## Output format
Provide:
- Exact commands run
- Any skipped commands and why

## Constraints
- Prefer scripts from project config.
- Limit backend tests to the test file you changed when possible.
- For frontend-only changes, run lint + unit tests where applicable.
