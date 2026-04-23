---
name: smart-compact
description: Instructions for tree-shaking a user-provided AI session transcript
---
This Skill’s purpose is to compact an AI session transcript by removing redundant-information messages and keeping the contentful ones intact.

### 1. Skip Trial-and-Error Bouts (All Tools)
**Drop the struggle; keep the resolution.**
-   Identify sequences of thrashing—whether it's fighting syntax errors, correcting failed attempts, or guessing paths. Discard the entire iterative loop of failures and keep only the final, successful tool invocation that resolves the bout.
-   Drop external technical difficulties like user interrupts, connection retries, etc.

### 2. Skip "murmur"
- **Drop "murmur"**: Isolated messages like "Good, that worked.", "File has been created/updated successfully", or "Now I’ll do this or that: ..."
- **Drop tool messages merely confirming success**: "Action X was successful" or "Tool completed with no output." Also drop Todo updates/writes. These messages don’t hold real content, reading more like the assistant murmuring under its breath.
- Note that these can show up in user messages as well as assistant messages.

### 3. The "Final Observation" Rule (`Read`, `Bash` Exploration)
**Keep only the tool call that successfully acquires the target information.**
-  **Reads:** Keep only the last `Read` of a file before it is acted upon. Drop redundant reads of unchanged files.
- **Scratchpads**: Drop reads, writes and edits of transient/debug/temporary files created by the agent during the session with the purpose of helping itself arrive at some desired state.
-  **Bash:** Group commands by semantic purpose. Keep only the one that effectively returns the answer, dropping empty returns or redundant variations.

### 4. The "Settled State" Rule (“CRUD”-ing files)
**Compress piecemeal mutations into their final intended state.** Treat sequences of writing, editing, reading, etc. of the same file (regardless of via `Bash` or dedicated tools like `Read`, `Write`, `Edit`) identically as file state mutations. We are only interested in the final state of the file, not the mutations. Keep only the final call that settles the file's state.

### 5. The "Definitive Validation" Rule (`Bash` Execution)
**Keep the proof, drop the debugging loop.** For commands that validate system state (e.g., running `pytest` or a build script), keep only the final successful execution that proves the task is complete.

### 6. Practical Implementation (Using `ccc`)
**Construct the compressed history using inclusive slice notation.** Build a script of sequential `ccc` commands, specifying *only the indices you want to keep*.
-  **Keep a single message:** `ccc <session_id> 5 --tools '!Glob' --no-metadata`
-  **Keep a range of messages:** `ccc <session_id> 10:15 --tools '!Glob' --no-metadata` (Note: `start:end` is inclusive of the start index, but **exclusive** of the end index. To keep 10 through 14, use `10:15`).
-  **Combine them:** Chain multiple commands together, outputting metadata only on the very first invocation.
-  **Test your script:** Do not run it blind, because the output will be massive. Instead, filter for just the included message indexes: `/tmp/your-script.sh | grep -E 'i="'`. This outputs the list of all opening tags in the compacted session, along with their index, for you to validate the compaction. 
