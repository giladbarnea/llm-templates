---
name: run-interactive
description: This skill should be used when running interactive CLI programs that require user input (installation wizards, configuration scripts, prompts asking for y/n, passwords, names, etc.). Enables completing multi-step interactive processes that would otherwise block waiting for stdin.
---

# Run Interactive

Run interactive CLI processes that prompt for user input.

## When to Use

- Installation wizards (e.g., `npm init`, `cargo init`, `pip install` with prompts)
- Configuration scripts that ask questions
- Any CLI that blocks waiting for stdin input
- Multi-step interactive processes

## Interface

**Files created by the driver:**

| File | Purpose |
|------|---------|
| `/tmp/interactive_<id>.log` | Read this — contains process output and signals |
| `/tmp/interactive_<id>.in` | Write here — send input to the process |

**Log format:**

```
[START] <command>    — Process started
[PID] <n>            — Process ID
[OUT] <line>         — Output from the process
[AWAIT]              — Process is waiting for input (respond now)
[SENT] <text>        — Input was sent to the process
[EXIT:<code>]        — Process exited with code
```

## Workflow

### 1. Start the driver in background

```bash
python3 ~/.claude/skills/run-interactive/scripts/driver.py <session_id> <command> [args...] &
```

Use a unique session ID (e.g., `npm_init_1`, `install_abc`).

### 2. Read the log to see output

```bash
cat /tmp/interactive_<session_id>.log
```

### 3. When `[AWAIT]` appears, send a response

Write the response to the input file (no trailing newline needed):

```bash
echo -n "my response" > /tmp/interactive_<session_id>.in
```

Or use the Write tool to create `/tmp/interactive_<session_id>.in` with the response.

### 4. Repeat steps 2-3 until `[EXIT:<code>]` appears

## Example Session

Running `npm init`:

```bash
# Start
python3 ~/.claude/skills/run-interactive/scripts/driver.py npm1 npm init &

# Check output
cat /tmp/interactive_npm1.log
# [START] npm init
# [PID] 12345
# [OUT] package name: (myproject)
# [AWAIT]

# Send response
echo -n "my-package" > /tmp/interactive_npm1.in

# Check again
cat /tmp/interactive_npm1.log
# ...
# [SENT] my-package
# [OUT] version: (1.0.0)
# [AWAIT]

# Continue until [EXIT:0]
```

## Special Keys

TTYs use byte sequences, not key events. Send these via the input file:

| Key | Sequence | Bash |
|-----|----------|------|
| Enter | `\n` | `printf '\n'` |
| Tab | `\t` | `printf '\t'` |
| Up | `\x1b[A` | `printf '\x1b[A'` |
| Down | `\x1b[B` | `printf '\x1b[B'` |
| Right | `\x1b[C` | `printf '\x1b[C'` |
| Left | `\x1b[D` | `printf '\x1b[D'` |
| Ctrl+C | `\x03` | `printf '\x03'` |
| Ctrl+D | `\x04` | `printf '\x04'` |
| Backspace | `\x7f` | `printf '\x7f'` |
| Escape | `\x1b` | `printf '\x1b'` |

**Combine sequences for menu navigation:**

```bash
# Down, Down, Enter (select third option)
printf '\x1b[B\x1b[B\n' > /tmp/interactive_<id>.in
```

## Notes

- The driver uses PTY, so the process behaves as if in a real terminal
- `[AWAIT]` detection is heuristic on macOS (output stopped + process sleeping)
- Empty responses are valid (just press enter): `printf '\n' > /tmp/interactive_<id>.in`
- For passwords, the response won't echo in `[OUT]` (normal TTY behavior)
