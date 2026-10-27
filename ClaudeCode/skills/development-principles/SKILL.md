---
name: development-principles
description: General development principles and abstraction policy.
metadata:
  short-description: These principles guide reasoning and decision-making. Concrete execution rules are defined in `workflow`.
---

# Development Principles

## Goal

Build only what the task needs, validate at boundaries, and keep changes minimal and reviewable.

## Principles
- Small diffs win: easiest to review, easiest to rollback.
- Validate inputs at boundaries: requests, jobs, commands, API entry points.
- Catch errors at boundaries: controllers/job handlers/CLI entry points. Don't swallow exceptions deep inside helpers.
- No implicit defaults for required config: missing config should break loudly, not limp along.
- YAGNI: build only what the task needs right now.

## Abstraction policy (no speculation)
- Add abstractions only to remove real duplication or enable required variation.
- Remove indirection that no longer pays rent.
