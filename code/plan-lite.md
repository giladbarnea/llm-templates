---
name: plan-lite
description: Lightweight plan prompt
---
Write a `plan.md`, but no implementation details — skipping them is the whole point, since the goal is to problem-solve in layers of increasing specificity.

**For implementation-layer aspects, stay low-specificity:**
No implementation details, no real code. Light pseudocode is fine; function signatures are fine. Full function coverage is discouraged (again, that defeats the point). Covering public functions is good; only mention the private ones they call, in pseudocode.

By pseudocode, I mean something like:
```
publicFunction(arg1: type1, arg2: type2) -> return_type:
  → calls privateHelper() to normalize input
  → calls anotherHelper() to persist result
  returns summary of the result
```
Shape and intent — not logic or loops.

**For higher-level aspects, go high-specificity:**
Discussing whole modules — what goes in, what comes out, their contracts and purpose — is encouraged. Discussing *relations between* modules, *temporal flow*, *state machines*, *dependency chains*, and *hierarchy* is highly encouraged.

Space (components), Time (flow), and the Ether in between (state, data and its mutation, purpose and role in the grand scheme) — that's where the value is.

Keep it cohesive and straightforward: no over-engineering, no scope creep. Intertwine sharp ASCII diagrams and concise descriptions. The plan is a good one if it is easy to understand and follow, and isn't too long — punchy and direct.
