---
name: secbrain-log
description: Append one raw entry to today's second-brain daily log. Use when the user runs /secbrain-log, or asks to log, capture, or remember a fact in the vault without distilling it.
disable-model-invocation: true
---

# secbrain-log

Append the user's text to today's log. Do not rewrite the log, and do not turn the entry into a concept note.

1. The text to log is whatever the user wrote after the command. If they wrote nothing, ask for the one line to keep and stop.
2. Call `log_entry` with that text and `source` `manual`.
3. Reply with the note path the tool returned. One line is enough.
