---
name: secbrain-review
description: Audit the second-brain vault and propose the next maintenance moves. Use when the user runs /secbrain-review, or asks to review, check, or audit the vault.
disable-model-invocation: true
---

# secbrain-review

Look, then propose. Do not create, move, or archive notes in this pass unless the user already asked for a specific change.

1. Call `vault_health`.
2. For each unresolved `[[link]]`, say whether it should become a note or be rewritten.
3. For each orphan, call `related_notes` and say where it belongs.
4. If five or more related notes have no map, propose `build_map`. Mention `resurface_notes` only when the backlog is already clear.
5. List the proposed changes with reasons. Wait for the user before writing.
