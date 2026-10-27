# Checklist Item Guidance

## Good checklist items

- Point to likely files/modules: `src/...`, `app/...`, `services/...`
- Name concrete validation: "Run `npm test`", "Add unit tests for X"
- Include safe rollout when relevant: feature flag, migration plan, rollback note
- Are verb-first: "Add...", "Refactor...", "Verify...", "Ship..."
- Are atomic: one action per item, can be checked off independently
- Follow a logical order: discovery -> changes -> tests -> rollout

## Bad checklist items

- Vague steps: "handle backend", "do auth", "update things"
- Too many micro-steps: one item per line change
- Code snippets: keep the plan implementation-agnostic
- Compound items: "Add X and also refactor Y" (split into two)

## Ordering pattern

1. Discovery / investigation steps
2. Core implementation changes
3. Supporting changes (types, configs, migrations)
4. Tests and validation
5. Linting and code quality
6. Rollout / deployment considerations

The final two items should always be:
- "Run linter"
- "Run tests"
