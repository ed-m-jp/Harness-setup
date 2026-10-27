---
name: light-task-runner
description: >-
  Default execution framework for all tasks. Enforces quality, correctness,
  and evidence without blocking the agent from acting. Assumes a sandboxed
  workspace environment.
---

# Light Task Runner

## Core principles

- If a file or path is mentioned, open it before making claims.
- Ask questions only if blocked (max 1-2).
- Do not cut corners to avoid adjacent changes that are necessary for correctness (e.g., fixing a broken import caused by your rename).
- Follow execution and refactor rules defined in `workflow`. Do not restate them here.

---

## Mode gate

If the task is purely advisory or explanatory (no file changes needed), respond directly.
The execution loop below applies only to tasks that involve changes.

---

## Execution loop

### Phase 1: Context scan (read-only)

- Skim `README.md` and obvious docs.
- Open only files likely to be touched.
- Identify constraints (repo rules, scope limits, existing patterns).

If blocked by missing information -> ask the user and stop.
Otherwise -> proceed.

---

### Phase 2: Scope check

Evaluate how many **non-test** files will be changed:

- **1 file** (excluding tests) -> proceed directly to Phase 3.
- **More than 1 file** (excluding tests) -> use `create-plan` before implementing. Do not skip this step. Wait for user approval of the plan before proceeding to Phase 3.

Test files do not count toward this threshold. A task touching 1 source file + 3 test files proceeds directly.

---

### Phase 3: Implement

- Make targeted changes that solve the task.
- If new ambiguity appears mid-implementation, stop and ask before proceeding.
- Do not move to Phase 4 until tests covering the changes exist, or the absence of tests is justified in Phase 4.

---

### Phase 4: Validation & done

Before declaring the task complete:

- What changed (files + brief reason)
- How it was validated:
  - Commands run (or why not)
  - Test results / exit codes
  - Screenshots for UI changes (if applicable)
- If validation could not be run, explain why and state what should be run in CI or by the user

The task is done when the request is fulfilled, evidence is provided, and no unexplained assumptions remain.

---

## Escalation rules

- Cross-surface changes (backend + frontend, etc.) -> ask for confirmation before starting
- High-risk changes (migrations, auth, security) -> include rollback notes
- Heavy / audit-grade work -> suggest `heavy-task-orchestrator` (user must opt in)
