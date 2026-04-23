---
name: peer-review
description: Prompt a subagent to review your work. Only use the skill when the user says so
---
First, commit your work to git to have a commit reference at hand.
Then dispatch a large, high-thinking subagent to review your work. 
Like the academic peer review method, to guarantee objectivity, you must hand the subagent only my original task verbatim, and a request for review, and nothing more. Not interpretations, no decision rationals, no "specifically, look at ...". These all constitute biasing the subagent. 

Use this template exactly:

<prompt-template>

The user has given me this task:
<original-task>
{{ ... }}
</original-task>

I have attempted to complete it.
Perform a thorough source code research and thinking, then use gsd and git show to see the before and after my work. Load the initial skills the user has instructed me to load for complete requirements understanding: {{skill names}}
Review my work for major overlooks, incomplete understanding of the requirements, significant missed opportunities to leverage elegant design and avoid implementation slop, etc.
Respond succinctly, directly, with code snippets and without weasle words. If you are unsure of an observation, communicate that ("It looks to me like it might - please verify."). If you are certain, communicate as usual.

</prompt-template>

If you have been explicitly instructed by me to write tests, use "...and avoid implementation slop, bad test design, etc."

That's it.
