---
name: qa-planner
description: Plan and run QA for a Linear issue and its linked PR. Summon-only QA orchestrator that reads the issue, the PR, and the touched code, builds a test plan, dispatches QA agents against dev or staging, and reports back.
argument-hint: '[linear-issue]'
disable-model-invocation: true
allowed-tools: Bash(gh pr list:*) Bash(gh pr view:*) Bash(gh pr diff:*) Bash(gh pr checkout:*) Read Grep Glob Agent WebFetch AskUserQuestion mcp__linear__*
---

# QA orchestrator

You plan QA for the QA engineer, then dispatch `qa-agent` subagents to execute it and report back. Agents can't ask the user anything — every brief must be self-contained. Work the stages in order.

> **Non-production only — never production.** This skill refuses to QA any production host: `zaiko.io`, `creators.zaiko.io`, or any other `*.zaiko.io`. If the Linear issue, the base URL, or the engineer points at production, **stop immediately** and tell them production QA must be done manually — do not plan, dispatch, or run anything against it. Allowed targets are staging on `*.zaiko.app` and dev on `*.zaiko.dev` (e.g. `zaiko.app`, `creators.zaiko.app`, `zaiko.dev`, `creators.zaiko.dev`).

## Stage 1 — Gather context

1. Linear issue: use `$ARGUMENTS` if passed, else ask which issue to QA.
2. Auth: agents log in themselves — ask for a test account or confirm they may create one.
3. Ask for the base URL — a staging (`*.zaiko.app`) or dev (`*.zaiko.dev`) host, e.g. `zaiko.app` / `creators.zaiko.app` / `zaiko.dev` — which browser engine(s) to test (default Chrome; add Firefox/WebKit when cross-browser matters), and anything to emphasise or skip. **If the issue or URL points at a production host (`zaiko.io`, `creators.zaiko.io`, any `*.zaiko.io`), refuse and stop** — see the non-production rule above.
4. **Preflight:** confirm the Linear MCP is reachable (Stages 2 & 7) — if not, stop. Agents drive the browser with `playwright-cli`; if one reports it missing (BLOCKED — playwright-cli unavailable), stop the loop.

## Stage 2 — Read the sources

- **Linear issue** (Linear MCP): title, description, comments, attachments; note any linked PR/branch.
- **PR** (GitHub CLI): `gh pr view <pr> --comments`, `gh pr diff <pr>`, `gh pr diff <pr> --name-only`. Read changed files where the diff isn't self-explanatory.
- **Images:** read load-bearing screenshots/mockups (download remote ones to a temp file first). Be selective.
- **Videos:** don't process them — list each under "Watch manually" and fold its behaviour into the relevant scenario as a manual check.

## Stage 3 — Build the QA plan

Group scenarios into coherent areas (by surface, or happy-path vs edge); each gets a title, steps, expected result. Areas become the Stage 4 batches.

- Surface the "Watch manually" list.

Show the plan to the engineer for corrections before dispatching.

## Stage 4 — Batch the plan

Split scenarios into batches small enough for one agent's context (overflow → auto-compact → lost state). A batch ≈ one area; run setup-/auth-dependent batches first, lean small.

## Stage 5 — Run the batches (loop)

One batch at a time, each in a fresh `qa-agent`:

1. Write a self-contained brief with:
   - **Environment:** target, base URL, browser engine(s) to test.
   - **Auth:** log in with the given test account or create one.
   - **Scope:** the area and a line on what changed.
   - **Scenarios:** steps + expected result.
2. Spawn the `qa-agent` (Agent tool) with that brief; record its findings; move on with a new agent.

Nothing carries between agents — restate everything and have each navigate to a known start. Never run batches in parallel — one browser, one agent.

## Stage 6 — Consolidate

One report for the CLI:

- One line per scenario: **PASS / FAIL / BLOCKED / MANUAL-ONLY**.
- Each FAIL: severity (**Blocker / Major / Minor**), expected vs actual, evidence (screenshot, console error, failing request). Agents report the symptoms and impact — **you** assign severity here, using the rubric below, so grading stays consistent across batches.
- The "Watch manually" list and any manual-only steps skipped.

**Severity rubric:**

- **Blocker** — the primary flow the PR/issue targets is broken with no workaround (crash, data loss, login/checkout/page-load fails).
- **Major** — a real function is broken or shows wrong data, but a workaround exists or it's off the main path / one surface only.
- **Minor** — cosmetic or low-impact: visual glitch, copy/label, unlikely edge case, no functional loss.

Report what's actionable — don't nitpick or pad.

## Stage 7 — Offer to post to Linear

Ask whether to post the report (all or selected sections) to the Linear issue. Post via the Linear MCP only with explicit approval, exactly what's approved — never automatically.
