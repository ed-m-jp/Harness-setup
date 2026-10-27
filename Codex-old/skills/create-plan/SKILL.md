---
name: create-plan
description: >-
  Create a concise, actionable plan for a coding task. Use when a user explicitly
  asks for a plan, says "plan this", "how should we approach", or requests a
  strategy for implementing a feature, bug fix, refactor, or migration. Also
  trigger when the user says "create a plan" or invokes /create-plan.
metadata:
  short-description: Create a plan
---

# Create Plan

## Goal

Turn a user prompt into a **single, actionable plan** delivered in the final assistant message.

## Planning Rules

- Operate in read-only mode unless the repo explicitly requires writing a plan file (e.g. PLAN.md).
- This skill is triggered by `light-task-runner` when more than 1 non-test file will change. Do not apply a different threshold.
- Ensure "Run linter" and "Run tests" are always the final two items in any plan.

## Workflow

1. **Scan context quickly**
   - Read `README.md` and any obvious docs (`docs/`, `CONTRIBUTING.md`, `ARCHITECTURE.md`).
   - Skim relevant files (the ones most likely touched).
   - Identify constraints (language, frameworks, CI/test commands, deployment shape).

2. **Ask follow-ups only if blocking**
   - Ask **at most 1-2 questions**.
   - Only ask if you cannot responsibly plan without the answer; prefer multiple-choice.
   - If unsure but not blocked, make a reasonable assumption and proceed.

3. **Create the plan**
   - Follow the template in `references/plan-template.md` exactly.
   - Use the guidance in `references/checklist-guidance.md` for writing good action items.
   - Scale action items to the task size (3-5 for small changes, 6-10 for larger work), ordered: discovery -> changes -> tests -> rollout.
   - Include at least one item for **tests/validation** and one for **edge cases/risk** when applicable.

4. **After approval (if repo requires a plan file)**
   - Write the validated plan to `PLAN.md` (or equivalent).
   - Update checkboxes as work progresses.
   - Remove `PLAN.md` once work is done, unless the repo says to keep it.

5. **Do not preface the plan with meta explanations; output only the plan.**
