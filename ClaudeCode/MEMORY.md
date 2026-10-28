# Memory Index (Global)

- [Collaboration Workflow](memory/feedback_workflow.md) — Plan-first, no guessing, DRY/SOLID/YAGNI, read ticket → investigate → propose → validate → implement; subagent cap 2–3
- [Git handling is user's responsibility](memory/feedback_git_handling.md) — never propose branch ops/stash/cherry-pick; user manages git, I edit files in current branch
- [No redundant guards on validated values](memory/feedback_no_redundant_guards.md) — once a value has passed validation, drop the `?? null` / `if (!x)` defensive checks
- [Thin controllers](memory/feedback_thin_controllers.md) — controllers only validate inputs, call services, return response; never put domain logic or queries in a controller method
- [Always confirm before posting to Slack](memory/feedback_slack_post_confirmation.md) — draft Slack messages and wait for explicit per-message approval; reading Slack is fine
- [rm -rf is blocked](memory/feedback_rm_rf_blocked.md) — never run or suggest `rm -rf`; leave temp artifacts for the user or use .gitignore
- [Google-logged-in playwright-cli profile](memory/reference_google_profile_playwright.md) — personal WSL Chrome profile at ~/.pw-profiles/google-chrome (edward.maire@zaiko.io); reuse via --profile/attach; NOT in any skill
