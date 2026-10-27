---
name: heavy-task-orchestrator
description: >-
  Strict, audit-grade workflow for large, high-risk, or regulated engineering
  tasks. Opt-in only — must be explicitly requested by the user (e.g. "use the
  heavy orchestrator"). Never activate automatically.
metadata:
  short-description: Heavy audit-grade workflow
---

# Heavy Work Orchestrator (Opt-In)

## Purpose

Strict, audit-grade workflow for **large, high-risk, or regulated** engineering tasks.
It is **not active by default** and must be explicitly requested.

## Activation rules

This workflow applies **only** when:

- The user explicitly requests it (e.g. "use the heavy orchestrator")
- The user confirms after a suggestion for strict/audit-grade execution

If not explicitly activated, ignore this document entirely.

## Relationship to other rules

When active, this workflow **temporarily overrides**:
- `light-task-runner`
- escalation heuristics
- default minimal execution flow

It **does not override**:
- Tier 1 safety and scope rules
- "Do not implement unless explicitly asked"
- `workflow` rules (code quality, PR discipline, patterns)
- `personas`

After completion, control returns to the default workflow.

## Core principles

- Correctness > speed
- Evidence > confidence
- Explicit decisions > implicit assumptions
- No skipped steps
- No speculative work

## Workflow phases

### Phase 0 — Instruction audit

- Identify all instruction sources (system instructions, repo AGENTS.md, task-specific docs).
- Record conflicts and resolutions in `verification.md`.
- Ask the user if conflicts cannot be resolved safely.

### Phase 1 — Requirements

- Extract requirements exactly as stated.
- List constraints and non-goals.
- Identify blocking unknowns — stop and ask if correctness is blocked.
- Deliverable: `requirements.md` — see `references/artifact-templates.md` for format.

### Phase 2 — Plan (with task tracker)

- Create a clear, ordered execution plan as a checklist.
- Deliverable: `plan.md` — see `references/artifact-templates.md` for format and rules.

### Phase 3 — Design

- Document 2-3 viable approaches.
- Analyze tradeoffs (risk, complexity, maintenance).
- Select one approach with justification.
- Deliverable: `design.md` — see `references/artifact-templates.md` for format.

### Phase 4 — Implementation

- Re-read all artifacts before coding.
- Implement incrementally, following the plan in order.
- Keep changes targeted.
- Stop and ask if new ambiguity appears.
- After completing a checklist item and verifying it, update its checkbox in `plan.md`.

### Phase 5 — Verification (mandatory)

- Define success **before** declaring completion.
- Include: tests run (exact commands + results), observable behavior, exit codes.
- Deliverable: `verification.md` — see `references/artifact-templates.md` for format.

## Completion checklist

See `references/completion-checklist.md` for the full checklist to run before declaring done.

## Exit condition

After completion:
- Delete the `.orchestrator/` directory and all its contents.
- Do not continue using this workflow. Return to the default light execution model.
