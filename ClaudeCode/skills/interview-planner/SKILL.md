---
name: interview-planner
description: require Claude Code Plan Mode, gather missing context, ask targeted questions via AskUserQuestion when needed, and produce a safe implementation plan.
disable-model-invocation: true
---

## Non-negotiable rules

- Require Claude Code Plan Mode. If Plan Mode is not active, tell the user to switch to Plan Mode first and stop.
- Stop after producing the plan unless the user asks to refine it.

## Workflow

1. Establish the task. If the user has not provided a concrete task or the task is vague, ask for the missing details.

2. Review available context. Infer likely impacted files, modules, entrypoints, constraints, and validation paths from conversation, memory, and repo context — do not ask for what can be inferred confidently.

3. Decide whether interview mode is needed. Use it unless the task is fully unambiguous from available context.

4. Run interview mode when needed.
   - Use the AskUserQuestion tool in compact batches.
   - Prefer three to five strong questions over many weak ones.
   - Ask only questions that most reduce ambiguity, risk, or rework.
   - If file references are not provided, ask for them only when they would materially improve plan quality or safety.
   - Do not ask for:
     - stack details already visible in the repo
     - conventions that can be inferred from nearby code
     - obvious restatements of the task
     - low-value preferences that do not change the plan

5. Produce the implementation plan.

## Plan calibration

- For small, localized tasks (~3 files or fewer, clear scope, obvious validation path), keep the plan compact.
- For broader, riskier, or cross-cutting tasks, expand proportionally.
- Increase planning depth when auth, payments, permissions, migrations, data deletion, schema changes, concurrency, shared infrastructure, or public APIs are involved.

## Refinement behavior

- If the user asks to refine the plan, add detail, reduce scope, compare options, or challenge assumptions, stay in planning mode and revise.
- If the user asks to implement during this skill, stay in planning mode and revise the plan instead.
