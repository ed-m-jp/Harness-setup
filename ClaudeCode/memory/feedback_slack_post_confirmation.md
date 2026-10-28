---
name: Always confirm before posting to Slack
description: Never send a Slack message before the user explicitly approves it — draft first, post only on the go-ahead
metadata:
  type: feedback
---

Never post to Slack (send_message, reply, broadcast, schedule) before the user has explicitly approved that exact message. Always present the draft and wait for a clear go-ahead.

**Why:** the user said "never post on slack again before asking me." Slack posts are outward-facing and irreversible (teammates get notified, content can be quoted/indexed), so they must not be sent on inferred intent.

**How to apply:**
- When a Slack post is the next step, write the draft in the reply and ask whether to post it — do not call the send tool yet.
- A prior approval of one message does not extend to the next one; re-confirm every time.
- "Good as is / lets go / send it" on a specific shown draft counts as approval for that draft only.
- Reading Slack (read_thread, read_channel, search) is fine without asking — this gate is for posting only.
- Same principle as commits/PRs: outward-facing actions are gated on explicit per-action confirmation.
