---
name: pull-request-review
description: Manual-only skill. Use only when explicitly invoked by name or command, for example "use pull-request-review" or "/pull-request-review". Never implement, edit files, or produce diffs.
---

Review a pull request and all its comments, provide a detailed review of potential issues / bugs / improvements, in a non-verbose way.

This skill is read-only end to end. It reads and reports; it never fixes, pushes, replies, or resolves — on bot threads or human ones. Acting on the findings is separate work, done by a different agent session or by you.

## Non-negotiable rules

- Never implement, edit files, or produce diffs.
- Never post anything to GitHub. The output is a draft for the developer to read and post — see `.claude/rules/pr-review-reply-convention.md`.

# PR Review Workflow

1. Scan `docs/index.md` and read the topic page for each system the diff touches (e.g. a ZCS / event-listing change pulls in `docs/zcs/spotify-listing.md`). Lets you catch issues the rules files don't cover (killswitch wiring, profile trust gates, upstream pipeline assumptions).
2. Read the PR comments carefully; list each as a checklist item
3. Do NOT run tests
4. Output a concise summary (no AI preamble) to the CLI, suitable for the developer to post as a PR reply
5. For each issue you find, add a severity score next to it, and order your final message by severity score (out of 10) descending
6. Avoid NIT comments, or any feedback with score < 5.

## Only report what the PR introduces

Would this be equally broken on master? Then drop it. Don't report it, don't note it as pre-existing. Check master before claiming otherwise.

## One block per issue

Title + severity, then:

- **Problem:** what breaks, under 30 words.
- **Line:** `path/File.php:NN` + the offending code.
- **Fix:** the minimal edit, as code.

Code doesn't count toward the word limit. No alternatives, no caveats.
