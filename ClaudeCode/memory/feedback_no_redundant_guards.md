---
name: no-redundant-guards-for-validated-values
description: "After a value has passed validation (Laravel rules, Spatie LaravelData, etc.), don't add defensive ?? null / ?? false / null-checks against it"
metadata:
  type: feedback
---

Once a value has cleared upstream validation, treat its presence and shape as guaranteed and write code that reflects that. Adding `?? null`, `?? false`, `if (!$x)` guards, optional chaining, or "just in case" null checks against an already-validated input is bloat that obscures the actual logic.

**Why:** The user explicitly called this out while reviewing `DuplicateEventRequestDTO::withValidator()` — once `rules()` declared `'startDatetime' => ['required', new ZcsDateTimeRule(...)]` and we passed the `$validator->failed()` short-circuit, writing `$input['startDatetime'] ?? null` is dead defensive code that lies about the actual contract. Same for any field marked `'required'` or with a non-nullable cast, and same for boolean fields like `isEndLate` that are `required` + `boolean`.

**How to apply:**
- Inside a Laravel validator's `after()` callback (past the `if ($validator->failed()) return;` guard), required-rule fields are guaranteed present — use `$input['field']` directly, not `$input['field'] ?? default`.
- Same for typed DTO properties after Spatie LaravelData has hydrated them: a `public string $name` is a string; don't `(string) $this->name`. A non-Optional CarbonImmutable is a CarbonImmutable; don't `?->` it.
- Don't write `if (!$start || !$end) return;` immediately after parsing two `required` datetime inputs.
- The exception is *genuinely* `Optional`/`nullable` fields, OR external boundaries (`$request->input(...)`, JSON payloads from outside, `mixed` returns). Those need explicit handling. The point is: only guard where the type system genuinely doesn't know.
