---
allowed-tools: Bash(*)
description: "Writes or updates handover context in .agents/sessions/YYYY-MM-DD_hh-mm-ss/handover.md, which will allow a fresh instance of the agent to pick up where the previous instance left off."
---

# A Good Handover File

A good handover file lets a new agent instance pick up where the previous one left off. It should clearly state purpose and intent, highlight the mistakes and pitfalls we’ve encountered, record the changes made since the conversation began to preserve continuity, and reference the relevant files/modules — both source code and documentation. Keep it absolutely succinct and concise—the new instance will read this file as well as all prior handovers for the project. A handover is useless if it’s anywhere near as long as the conversation itself.

Review the full conversation. Decide what to omit because it isn’t useful for getting a fresh agent up to speed, and what to keep but condense because it’s too detailed. 
