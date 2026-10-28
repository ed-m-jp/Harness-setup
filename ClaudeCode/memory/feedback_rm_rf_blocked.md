---
name: feedback-rm-rf-blocked
description: rm -rf is a blocked command in this environment — never run or suggest running it
metadata:
  type: feedback
---

`rm -rf` is a blocked command in this environment. The user explicitly stated I am not allowed to run it.

**Why:** It is a hard harness/permission guardrail on this machine, not a per-task preference. Attempting it just gets denied and wastes a turn.

**How to apply:** Never invoke `rm -rf` via Bash, and don't propose it as a cleanup step. For removing stray/temp artifacts (e.g. the `.playwright-cli/` snapshot dir a tool writes into the repo), either leave it for the user to delete themselves or prefer a non-destructive fix like adding the path to `.gitignore`.
