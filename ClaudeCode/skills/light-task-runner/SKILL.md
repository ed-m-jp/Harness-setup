---
name: light-task-runner
description: Lightweight execution guardrails for coding tasks. Prevents hallucination, enforces scope and evidence, without heavy ceremony.
---

# Light Task Runner

## Core principles

### Absolute rules

- Deliver exactly what the user asked for — nothing more, nothing less.
- Do not implement or modify files unless the user explicitly asked you to.
- If a file or path is mentioned, open it before making claims.
- Ask questions only if blocked (max 1–2).
- Follow execution and refactor rules defined in `workflow`.

---

## Minimal execution loop

### Phase 1: Task sanity check (always)

Before doing anything:

- Restate the task in 1–3 bullet points.
- List constraints explicitly (repo rules, scope limits, “don’t change X”).
- Identify blockers (if any).

If blocked → ask the user and stop.  
Otherwise → proceed.

---

### Phase 2: Context scan (read-only)

- Skim `README.md` and obvious docs.
- Open only files likely to be touched.
- Follow existing patterns; do not freestyle.

If more than ~2 files are likely involved and no plan exists → suggest using `create-plan`.

---

### Phase 3: Decide the mode

Choose exactly one:

- Explain-only (analysis or guidance, no file changes)
- Plan-only (hand off to `create-plan`)
- Implement (proceed with changes)

If the user did not explicitly request implementation, default to Explain or Plan.

---

### Phase 4: Implement (only if asked)

- Make the smallest change that solves the task.
- Keep changes localized.
- Follow repo conventions exactly.
- No behavior change without tests (or explicit justification).

If new ambiguity appears, stop and ask before proceeding.

---

### Phase 5: Validation & evidence (required)

Before declaring the task complete, include:

- What changed (files + brief reason)
- How it was validated:
  - Commands run (or why not)
  - Test results / exit codes
  - Screenshots for UI changes (if applicable)

If validation could not be run:
- Explain why
- State what should be run in CI or by the user

---

### Phase 6: Done criteria

A task is done when:

- Scope matches the request exactly
- Diff is minimal and reviewable
- Validation evidence is provided
- No unexplained assumptions remain

---

## Optional escalation rules

Escalate only when necessary:

- Touching more than 2–3 files → use `create-plan`
- Significant behavior change → add tests + explicit validation
- Cross-surface changes (backend + frontend, etc.) → ask for confirmation
- High-risk changes → include rollback notes
