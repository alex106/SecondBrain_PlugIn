---
name: secbrain-schedule
description: Register or remove the daily Windows Task Scheduler job that distils the second-brain vault. Use when the user runs /secbrain-schedule, or asks to schedule, time, or cancel the daily distill.
disable-model-invocation: true
---

# secbrain-schedule

This job is Windows Task Scheduler. It runs Claude Code, not this Cursor chat. Do not hand-edit the task.

Find the package the same way `/secbrain-init` does, and set `PY` to its venv Python. Every command is:

```
"$PY" -m obsidian_secondbrain.cli schedule-distill --project "<project root>"
```

- To register, the user must give a time as `HH:MM` (24-hour). Pass `--time` with that value. If they gave no time, ask for one and stop.
- To remove, pass `--remove` and no `--time`.
- Read the JSON. On success, report `task_name`, `time`, and the `next_step` query. On failure, report `error` and stop.
- `claude` must be on PATH. If the JSON says it is missing, say so. Do not invent another runner.
