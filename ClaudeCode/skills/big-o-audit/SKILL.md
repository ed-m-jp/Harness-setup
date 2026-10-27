---
name: big-o-audit
description: Codebase audit for asymptotic speed and memory issues. Use when asked to review a repo for Big O hot spots, repeated scans, N+1 patterns, unnecessary allocation or copying, full-table scans, or to produce a prioritized complexity report validated by a sub-agent.
---

# Big O Audit

## Goal

Find real asymptotic problems, not micro-optimizations. Prefer simple fixes that reduce growth in time or memory without adding unnecessary abstractions, compatibility layers, or broad rewrites.

## Audit Workflow

1. Map hot paths before ranking issues:
   - user-facing request handlers
   - import and export pipelines
   - background jobs and queue consumers
   - pagination loops and batch processors
   - large in-memory transforms
   - database or API fan-out paths
2. Look for asymptotic smells:
   - repeated scans of the same collection
   - nested loops over independently growing datasets
   - `collect()`, `toList()`, `all()`, or equivalent materialization followed by repeated filtering, grouping, or sorting
   - n+1 reads, writes, API calls, database queries, filesystem reads, or parsing operations
   - repeated normalization, serialization, deserialization, regex work, or parsing of the same input
   - copying large arrays, objects, strings, buffers, or snapshots more than once
   - full-table scans where an index, predicate pushdown, streaming, or pre-aggregation should be used
   - unbounded caches, buffers, logs, retained snapshots, or result accumulation
3. For each suspected issue, record:
   - current Big O for time and memory
   - why the cost grows with input size
   - which code path makes the issue hot or meaningful
   - the smallest fix that improves the asymptotic behavior
4. Ignore constant-factor noise unless it is on a hot path and causes measurable memory pressure. Do not report style preferences as Big O findings.
5. Validate every finding against direct code evidence. Cite the file, function, and lines or code shape that prove the growth pattern.
6. Challenge the findings before finalizing:
   - Act as a skeptical secondary reviewer.
   - Look for missed issues, false positives, and better complexity estimates.
   - Remove findings that cannot be defended with direct evidence.
   - Keep findings that survive the challenge or whose risk is clearly explained.

## Complexity Rules

- Distinguish input dimensions when needed. Use names such as `n = rows`, `m = users`, `p = pages`, or `k = related records per item` instead of collapsing everything into `n`.
- Include memory complexity when allocation, materialization, caching, buffering, or copying is central to the issue.
- For database, API, filesystem, and parser fan-out, describe both algorithmic complexity and round-trip or I/O count, for example: `O(n)` queries from an n+1 pattern.
- Do not claim an asymptotic improvement when the proposed fix only changes constants. Mention constant-factor opportunities only in a brief note if the user asked for general performance feedback.
- Prefer small fixes: pre-index with a map/set, batch requests, push filtering into the database, stream instead of materialize, reuse parsed forms, avoid duplicate sorts, or bound caches.

## Report Format

Return only validated findings unless the user explicitly asks for notes or raw observations.

Use one row per issue with these columns:

| Priority | Location | Summary | Current Big O | Target Big O after fix | Ease of fix | Why it matters |
|----------|----------|---------|---------------|------------------------|-------------|----------------|

Priority values:

- `High`: unbounded or user-facing asymptotic growth, repeated full scans, n+1 on a common path, or major memory blowups.
- `Medium`: clear inefficiency on a meaningful path, but bounded, less frequent, or lower blast radius.
- `Low`: smaller hotspot, admin-only path, rare job, or lower-risk growth issue.

After the table, add `Evidence:` with one or two concise sentences per finding. Include the file/function/line range or exact code shape. If a fix only reduces constants, exclude it from the table.

If there are no valid findings, say so explicitly and list the main areas checked.

## Delivery

Push the final report into an Artifact — do not leave it in terminal output or a local md file only.

1. Load the `artifact-design` skill before writing the page.
2. Write the report as an HTML file (findings table + `Evidence:` notes), then publish it with the `Artifact` tool.
3. Give the user the artifact URL as the deliverable. Keep a local md copy only if the user asks for one.
4. On a re-run of the same audit, republish to the same artifact URL instead of creating a new one.
