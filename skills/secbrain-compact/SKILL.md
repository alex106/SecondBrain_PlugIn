---
name: secbrain-compact
description: Compact the current chat into one durable second-brain session note. Use when the user runs /secbrain-compact, or asks to file, compact, or save this session in the vault.
disable-model-invocation: true
---

# secbrain-compact

File this chat. You write the summary. The tool only stores it.

1. From this conversation, write a durable summary: what was being done and why, decisions and their reasons, what is still open, which files changed. A reader six months from now should not need the transcript. Leave out pleasantries and the blow-by-blow.
2. Call `capture_session` with that summary, the decisions, the open questions, and the artifacts touched.
3. If one idea is bigger than this session, also call `find_notes` or `search_notes`, then `create_concept_note` for that idea, and pass the new path to `mark_distilled` on the session note.
4. Reply with the session-note path and, if you wrote one, the concept-note path.
