# Big O Audit Reference

## Complexity Rubric

- Time complexity: describe the dominant growth term in the hot path.
- Memory complexity: describe peak extra space, including repeated copies or retained collections.
- If a change only improves constants, do not label it as a Big O fix.

## Validation Checklist

- Confirm the hot path is real and reachable.
- Confirm the collection size can grow enough to matter.
- Confirm the suggested fix reduces asymptotic growth or peak retained memory.
- Reject findings that are speculative, duplicate, or already bounded.

## Sub-agent Challenge Prompt

Ask a sub-agent to:

- find missed hotspots
- challenge each suspected issue
- point out false positives
- suggest tighter complexity estimates

Keep only findings that survive the challenge.

## Output Fields

For each finding, capture:

- priority
- location
- current complexity
- target complexity
- ease of fix
- evidence

