#!/usr/bin/env python3

from __future__ import annotations

from datetime import datetime
from pathlib import Path


REVIEW_TEMPLATE = """# Review Findings

## R-001
Status: open
Severity: high
Category: bug
Files: path/to/file.py
Confidence: high

Problem:
...

Why it matters:
...

Recommended fix:
...

---
"""

STATUS_TEMPLATE = """review:
  id: review-{stamp}
  source_file: reviews/review-{stamp}/review.md
items:
  - id: R-001
    status: open
    owner: remediation-agent
    notes: ""
    files_changed: []
    tests_added: []
"""


def main() -> None:
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    review_dir = Path("reviews") / f"review-{stamp}"
    review_dir.mkdir(parents=True, exist_ok=False)

    review_file = review_dir / "review.md"
    status_file = review_dir / "status.yaml"

    review_file.write_text(REVIEW_TEMPLATE, encoding="utf-8")
    status_file.write_text(STATUS_TEMPLATE.format(stamp=stamp), encoding="utf-8")

    print(str(review_dir))
    print(str(review_file))
    print(str(status_file))


if __name__ == "__main__":
    main()