---
name: workflow
description: Execution workflow, definition of done, and operational notes.
---

# Workflow

## Goal

Keep changes small, reviewable, aligned with existing patterns and do not introduce new abstractions unless required while maintaining a clear PR narrative.

## Canonical execution rules

This file is the single source of truth for:
- change size and scope expectations
- refactor boundaries
- testing requirements
- PR discipline
- cleanup expectations

Other skills may reference these rules but must not restate or override them.

## Branch & PR discipline
- One branch per task.
- Open a draft PR early and keep it draft until checks are green.
- Keep commits small and atomic.
- Ask for a ticket number if one is required; use a fallback like "no-ticket" if none exists.

## Absolute rules
- Principles to follow: DRY, SOLID, YAGNI, KISS, no over engineering, no useless abstraction.
- Do not commit secrets or local config files (.env, tokens, private keys, auth.json, etc.).
- Fail fast on missing required config (no silent defaults).
- No speculative abstractions; keep changes minimal and aligned to existing patterns.
- Don't edit existing migrations; add new ones for schema changes.
- Avoid drive-by dependency upgrades; keep lockfile changes scoped and justified.
- No behavior changes without tests (or explicit justification).
- Avoid cross-surface refactors (backend + frontend + infra) unless required.
- After fixing the root problem, remove leftover scaffolding/temporary edits.

## Task loop
1. Locate existing patterns (similar controllers/components/tests). Copy the pattern; don't freestyle.
2. Make the smallest change that solves the task. No drive-by refactors.
3. Use the appropriate persona for the task (Architect/Planner for plans, Coder for implementation, Tester for tests, Reviewers for reviews).
4. Run the most relevant local checks (see project scripts).
5. Update PR description with:
   - What changed + why
   - Test plan with exact commands run
   - Screenshots for UI changes
   - Notes on migrations/config/feature flags
6. Keep PR scoped. If you have to touch adjacent/legacy surfaces do it surgically.
7. After you fix the root problem, remove any leftover edits that are no longer necessary.

## Definition of done
- Diff is minimal and follows existing patterns.
- Tests/checks run are listed with exact commands and CI is green.
- Env/config/migration changes are documented.
- Screenshots exist for UI changes.

## Operational notes
- Rollback mindset: keep changes easy to revert (small diffs, feature flags when risky).
- For UI changes: include before/after screenshots and any manual verification steps.
- For migrations: note deploy order/requirements and document any backfills with rollback steps.
