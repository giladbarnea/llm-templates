---
name: peer-review (user-as-mediator)
description: Prompt template for when the user is mediating — directing you as reviewer at another agent's completed work
---

Send the following prompt to the reviewer, substituting `{research_targets}` (what to read) and `{task}` (what to actually do with it):

---

$catchup {research_targets}. Read all the files there fully. Then read all the source code files referenced, climb up and down the call graph to exhaust to roots and leaves in order to get the full picture.

Finally, {task}.

@templates/review-criteria.md
