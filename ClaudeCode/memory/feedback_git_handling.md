---
name: Git handling is the user's responsibility
description: Don't propose branch creation, checkout, stash, cherry-pick, or any git state changes — user manages git themselves
metadata:
  type: feedback
---

Never propose git branch operations (create branch, checkout, stash, cherry-pick, rebase, etc.). When the user asks for a code change, just edit the files in the current working tree.

**Why:** the user said "who asked you to create the branch? I will do all the git myself and don't want this, when I ask something do it in the current branch." They were annoyed by repeated AskUserQuestion offers about branch handling.

**How to apply:**
- Don't ask "which branch should I work on" or offer git options in AskUserQuestion.
- Don't suggest `git stash`, `git checkout -b`, `git cherry-pick`, or branch-switching workflows.
- If a file's content depends on a different branch, just edit the current state of the file — trust the user has the right branch checked out.
- If you genuinely can't proceed (e.g. file doesn't exist), say so plainly and let the user resolve it; don't propose git remedies.
- Commits/PRs are still gated on explicit user request, but everything between them is the user's domain.
