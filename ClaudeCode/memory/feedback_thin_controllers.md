---
name: Thin controllers — business logic in services
description: Controllers must only validate inputs, call a service/helper, and return the response (DTOs can do mapping). Business logic in controllers is a correction.
metadata:
  type: feedback
---

Controllers must stay thin. Their job is: validate inputs (Form Request / DTO), delegate to a service or helper, and return the response. They must not contain business logic, query building, or domain rules. DTOs may carry some mapping logic but never business logic. New helper methods that compute domain facts (legacy detection, eligibility checks, ID gathering, etc.) belong on a service, not as `private function` on the controller.

**Why:** Edward called this out after I added `private function getLegacyQuestionnaireIdsForEvent(Event $event): array` directly inside `Zcs/EventController::questionnaires()` for ZAI-13718. The Zaiko project's `backend-convention.md` already states "Controllers must be thin — delegate business logic to services" — but this is also Edward's personal correction, so treat it as load-bearing.

**How to apply:** Whenever I'm about to write a `private function` in a controller that does anything beyond formatting/wiring (anything involving a query, a domain check, a business decision), stop and put it on the relevant service instead. The service for an area usually already exists — extend the existing one rather than creating a new service-of-one. The controller method should read like: pull validated input → call `$this->fooService->doThing(...)` → return the response.
