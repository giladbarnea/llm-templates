---
allowed-tools: Bash(*)
description: "Writes or updates handover context in .claude/conversations/YYYY-MM-DD_hh-mm-ss/handover.md, which will allow a fresh instance of the agent to pick up where the previous instance left off."
---

# A Good Handover File

A good handover file is a file that allows a fresh instance of the agent to pick up where the previous instance left off. It should communicate the purpose/intent, help avoid the mistakes/pitfalls we've encountered, and understand the changes we've made since starting the conversation, to preserve continuity. The content of the handover file should be concise because the fresh instance will read not only this file but all the past handover files of this project.

## If the user asked you to write a handover file covering the entire conversation, because they'll be starting a fresh session with you immediately after your response:
Think about what to include in the handover file, looking at the entire conversation, then write these instructions to ./.claude/conversations/YYYY-MM-DD_hh-mm-ss/handover.md (you may need to `mkdir -p` ./.claude/conversations/YYYY-MM-DD_hh-mm-ss directories first). Use `date '+%Y-%m-%d_%H-%M-%S'` to get the datetime.

## If you've been maintaining a handover file as you go:
Read the handover file and update it with any latest information worth including since the last update.

