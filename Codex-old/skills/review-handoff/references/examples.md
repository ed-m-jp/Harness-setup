# Example usage

## Reviewer prompt

Review this project for correctness, security, reliability, performance, and missing tests.

Create a new review run directory under `/reviews/` using the required timestamped naming pattern. Write findings to `review.md` using stable IDs like `R-001`. Do not fix code. Do not mark items fixed in `review.md`.

## Remediation prompt

Read the latest `reviews/review-YYYY-MM-DD-HHMMSS/review.md` and address findings one by one.

Update `status.yaml` only. Do not rewrite or delete original findings. For each item, set one of:

- `open`
- `in_progress`
- `fixed`
- `not_fixing`
- `duplicate`
- `needs_human`

For fixed items, record changed files and tests added.