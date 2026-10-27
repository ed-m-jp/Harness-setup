# Artifact Templates

Create and maintain these files **only while the heavy orchestrator is active** in a `.orchestrator/` directory at the repo root. Do not create them outside of this workflow. Delete the `.orchestrator/` directory when the workflow exits.

## requirements.md

```markdown
# Requirements

## User requirements
- <Requirement 1>
- <Requirement 2>

## Constraints
- <Constraint 1>
- <Constraint 2>

## Non-goals
- <What is explicitly out of scope>

## Blocking unknowns
- <Unknown 1> — resolution: <asked user / assumed X>
```

## plan.md

```markdown
# Execution Plan

[ ] <Step 1 — meaningful unit of work>
[ ] <Step 2>
[ ] <Step 3>
[ ] <Step 4>
```

Rules:
- Each checkbox = one meaningful unit of work (not micro-steps).
- Check an item only when fully complete.
- Do not auto-check remaining items.
- Leave incomplete items unchecked if work is paused.
- Do not modify the plan structure unless requirements change.

## design.md

```markdown
# Design

## Approach A — <name>
- Description: ...
- Pros: ...
- Cons: ...

## Approach B — <name>
- Description: ...
- Pros: ...
- Cons: ...

## Selected approach
<Approach X> — <justification>

## Tradeoffs accepted
- <Tradeoff 1>
```

## verification.md

```markdown
# Verification

## Instruction conflicts
- <Conflict 1> — resolution: <how resolved>

## Tests run
| Command | Result | Exit code |
|---------|--------|-----------|
| `<cmd>` | <pass/fail> | <code> |

## Observable behavior
- <What was verified manually>

## Evidence
- <Screenshots, logs, or output snippets>
```
