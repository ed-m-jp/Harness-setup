---
name: coding-conventions
description: Coding conventions for PHP and JS/TS projects.
---

# Coding Conventions

## Goal

Follow the repo's lint/format rules and keep code style consistent with existing patterns.
Conventions apply only when they do not conflict with `workflow` rules.

## PHP
- Follow repo tooling (phpcs/Pint or equivalent). Don't win against the formatter.
- PSR-12 style, 4-space indentation.
- Prefer strict types and explicit return types in new/modified code where consistent with surrounding code.
- Arrays: follow the configured linter/formatter. If unspecified, default to modern `[]`.
- Use statements should be sorted alphabetically

## JS / TS / Vue
- Follow ESLint + Prettier configs (typical: 2-space indentation, single quotes, semicolons).
- Avoid `any` unless unavoidable; prefer proper types at boundaries (API payloads, page props).
- Vue component naming: multi-word names except for allowed overrides (e.g. `Pages/**`).
