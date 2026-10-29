# secbrain

Cursor plugin for the Obsidian second brain. It packages the six secbrain skills, the session rule that searches the vault first, and the `obsidian-secondbrain` MCP server.

The vault path and the Python interpreter stay out of this repo. Each person sets them after install.

## What is included

| Piece | Role |
| --- | --- |
| `skills/secbrain-init` | Set up or repair the vault, client config, and capture hooks |
| `skills/secbrain-log` | Append one raw line to today's log |
| `skills/secbrain-compact` | File this chat as a session note |
| `skills/secbrain-distill` | Turn the raw backlog into claim notes |
| `skills/secbrain-review` | Audit the vault and propose maintenance |
| `skills/secbrain-schedule` | Register or remove the daily distill job |
| `rules/secbrain.mdc` | Search the vault before the first action of a session |
| `mcp.json` | Starts the server through `scripts/launch_mcp.py` |

Invoke a skill with `/secbrain-log`, `/secbrain-compact`, and the other names. The rule loads on its own.

## Requirements

The MCP server is the `obsidian_secondbrain` package, not this plugin. Install it from the [obsidian-mcp checkout](https://github.com/alex106/Obcidian_MCP_Manager_Locals):

```bash
git clone https://github.com/alex106/Obcidian_MCP_Manager_Locals.git ~/Documents/obsidian-mcp
cd ~/Documents/obsidian-mcp
python -m venv .venv
.venv/bin/pip install -e .
```

On Windows the interpreter is `.venv\Scripts\python.exe`.

Capture hooks stay per project. Run `/secbrain-init` in a project so `install` copies `_common.py`, `capture_session.py`, `session_start.py`, `codex_turn_buffer.py`, `cursor_hooks.py`, and `mcp_server.py` into `<project>/.secbrain-scripts/` and points that project's client config at those copies. MCP args become the absolute path of `.secbrain-scripts/mcp_server.py`. The package stays installed in the venv; that file only launches it. Claude and Codex hook commands call the copies, with `--vault` on the command line. Cursor gets `.cursor/mcp.json` plus `.cursor/hooks.json` version 1 with five flat `{command, timeout}` entries, all calling `cursor_hooks.py --event <name> --vault <vault>`: `sessionStart` (stdout `additional_context`), `beforeSubmitPrompt` (must print `{"continue": true}` and buffer the prompt), `afterAgentResponse` (buffer the reply), `preCompact` and `sessionEnd` (file the buffer into one inbox note; do not parse `transcript_path`). Cursor also gets `.cursor/rules/secbrain.md` by default. VS Code and Copilot still have no hook config. They get the MCP launcher path. Automatic capture stays unavailable there; `--with-instructions` still applies.

The in-project vault directory and `.secbrain-scripts/` are personal. `install` writes a marked block into the project's `.gitignore`:

```
# secbrain:start
# Personal secbrain data. Do not commit.
.secbrain-scripts/
<vault dir relative to the project, only when the vault is inside the project and is not the project root>/
# secbrain:end
```

A vault given as an absolute path outside the project is not in the repo, so it gets no ignore line. `install` does not `git add` these folders. If they are already tracked, `install` reports a caveat and does not `git rm` them.

`install` also rewrites one vault note, `<notes folder>/Project profile.md` (default `30-Notes/Project profile.md`): languages by extension, git origin, current branch, convention files that exist, top-level layout, and a short README excerpt. It does not copy source or secrets. A second install overwrites that same note.

## Use it on this machine

Copy this folder to `~/.cursor/plugins/local/secbrain`. A symlink to a directory outside that folder is ignored.

Reload the window (**Developer: Reload Window**). The plugin starts `bash`, which runs `scripts/launch_mcp.py`. That script uses `~/Documents/obsidian-mcp/.venv` and, when the workspace has one, its `SecondBrain` directory. An empty **Configure** form used to leave the command as the literal `${OBSIDIAN_PYTHON}`, which Cursor cannot spawn.

Open **Customize** → **Configure** only to override those two paths:

- `OBSIDIAN_PYTHON` — the venv interpreter
- `OBSIDIAN_VAULT` — absolute path to the vault

If a project also has an `obsidian-secondbrain` entry in `.cursor/mcp.json`, disable that entry. Two configs with the same server name both try to start.

## Redistribute

1. Add a license file. The marketplace accepts open-source plugins.
2. Push this folder to a public Git repository. The manifest must stay at `.cursor-plugin/plugin.json`.
3. Submit the repository at [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

Teammates on a Teams or Enterprise plan can also import the repository as a team marketplace from **Dashboard → Plugins & MCPs**.
