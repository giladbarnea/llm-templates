---
name: self-peer-review
description: Instructions for dispatching a subagent to review your own completed work — commit first, then send this prompt
---

First, commit your work to have a commit reference. Then dispatch a large, high-thinking subagent with the following prompt, filling in the placeholders:

---

The user has given me this task:
<original-user-task>
{original_task}
</original-user-task>

I have attempted to complete it. It's committed to {commit_sha}.

Conduct thorough documentation and source code research. Alternate between `git show` and `gsd`/`git diff` to see the before and after of my work. Follow call/dependency graphs completely to roots and leaves.

{ if the original task references skills }
Load the referenced skills yourself for complete understanding: {skill_names}
{ end if }

@templates/review-criteria.md
