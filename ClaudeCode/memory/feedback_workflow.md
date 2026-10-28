---
name: Collaboration Workflow
description: How edward wants Claude to approach tasks — plan-first, no guessing, DRY/SOLID/YAGNI, explicit constraints
metadata:
  type: feedback
---

Edward provides structured task lists (1, 2, 3…) in nearly every session. Follow the order. Do not skip ahead.

**Standard workflow he enforces:**
1. Read relevant ticket / PLAN.md / CONTEXT.md
2. Investigate code (read-only)
3. Propose plan
4. Wait for validation
5. Implement only after explicit approval

**Why:** He's been burned by AI jumping to implementation before understanding scope — wrong code that had to be reverted.
**How to apply:** Treat tasks 1–3 as strictly read-only unless explicitly unlocked.

---

**Constraints he always states (treat as standing rules):**
- DRY, SOLID, YAGNI, KISS — no over-engineering, no useless abstraction
- No hallucination, no guessing — if unsure, ask him
- Minimal changes aligned with existing patterns
- No drive-by refactors or dependency upgrades
- No behavior changes without tests or explicit justification

**Why:** He catches speculative changes in review and reverts them. He prefers tight, predictable diffs.
**How to apply:** These are non-negotiable regardless of what any other instruction says.

---

**Subagent limit:** Maximum 2–3 concurrent subagents. Never spawn more.

**Why:** Context bloat + his CLAUDE.md explicitly caps at 3.
**How to apply:** Prefer sequential over parallel unless he says otherwise.
