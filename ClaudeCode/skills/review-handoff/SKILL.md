---
name: review-handoff
description: organize ai code review handoffs using a per-run review folder under /reviews/review-yyyy-mm-dd-hhmmss/ with review.md for findings and status.yaml for remediation tracking. use when chatgpt is asked to review a codebase, write review findings, hand findings from one agent to another, or maintain a clean claude-to-codex review workflow with separated ownership of findings and status.
---

# Review Handoff

Organize code review work into a per-run folder so findings and remediation stay separate and auditable.

## Overview

Use a dedicated review run directory for each review cycle:

- Claude or the reviewing agent writes findings to `review.md`
- Codex or the fixing agent updates `status.yaml`
- Do not let both agents freely rewrite the same prose sections

Review folders must live under `/reviews/` and use this exact folder naming pattern:

`review-YYYY-MM-DD-HHMMSS`

Example path:

`/reviews/review-2026-03-29-142355/`

Each review run directory must contain:

- `review.md`
- `status.yaml`

## Workflow

1. Create a new review run directory under `/reviews/`
2. Write findings into `review.md`
3. Track remediation state in `status.yaml`
4. Preserve `review.md` as the source review artifact
5. Update `status.yaml` instead of rewriting findings

## Ownership rules

- The reviewing agent owns `review.md`
- The remediation agent owns `status.yaml`
- Do not delete or silently rewrite original findings
- If a finding is unclear, interpret it conservatively and record assumptions in `status.yaml`

## Directory creation

When a new review session starts, generate a timestamped folder name in this format:

`review-YYYY-MM-DD-HHMMSS`

Use the helper script:

`python scripts/generate_review_dir.py`

That script creates:

- `reviews/review-YYYY-MM-DD-HHMMSS/review.md`
- `reviews/review-YYYY-MM-DD-HHMMSS/status.yaml`

## Writing `review.md`

Use the structure in `references/review-template.md`.

Rules:

- Assign stable IDs like `R-001`, `R-002`
- Include severity, category, files, confidence, problem, why it matters, and recommended fix
- Keep findings actionable
- Avoid style-only nitpicks unless they materially affect correctness, maintainability, security, or testability
- Do not mark items fixed in `review.md`

## Writing `status.yaml`

Use the structure in `references/status-template.yaml`.

Allowed statuses:

- `open`
- `in_progress`
- `fixed`
- `not_fixing`
- `duplicate`
- `needs_human`

Rules:

- Every item in `status.yaml` must reference a finding ID from `review.md`
- Record notes for every non-open status
- For fixed items, include changed files and tests added when relevant
- Prefer updating structured fields over adding freeform prose outside the schema

## Review quality bar

Prioritize:

- correctness bugs
- security issues
- reliability issues
- performance issues with practical impact
- missing tests around risky logic
- maintainability issues that are likely to cause defects

## References

- Review template: `references/review-template.md`
- Status template: `references/status-template.yaml`
- Examples: `references/examples.md`