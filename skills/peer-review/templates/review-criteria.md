---
name: review-criteria
description: Shared review criteria and response style included by both peer review modes
---

Review for major overlooks, critically incomplete understanding of the reality of the source code, significant missed opportunities to leverage elegant design and avoid implementation slop, obviously unnecessary over-engineering that could be collapsed to something simpler yet cleaner, etc. The threshold for what constitutes an issue is high — don't surface noise.

{ if the work includes tests }
Also review the tests for substantiality (test real, product spec-derived behavior) vs hollowness (don't really test anything and create false confidence) and general test design.
{ end if }

Respond succinctly, directly, with code snippets and without weasel words. If you are unsure of an observation, communicate that ("It looks to me like it might — please verify."). If you are certain, communicate as usual.
