---
name: secbrain-distill
description: Distil the second-brain raw-capture backlog into atomic claim notes. Use when the user runs /secbrain-distill, or asks to distil the inbox, the backlog, or raw captures.
disable-model-invocation: true
---

# secbrain-distill

Turn raw captures into notes. One idea per note. Never edit a raw capture in place.

1. Call `distill_queue` (default limit 5). If the queue is empty, say so and stop.
2. Call `vault_health` and `list_notes` on the notes folder so you link into what already exists.
3. For each raw item, keep only ideas that will still matter later. For each idea, `find_notes` or `search_notes` first, then `create_concept_note`: title phrased as a claim, `links` set to existing note titles, `sources` set to the raw path.
4. Call `mark_distilled` on every source you handled, including items you skipped, with `produced` listing the notes you wrote (empty if you skipped it).
5. Report what you wrote and what you skipped, with paths.
