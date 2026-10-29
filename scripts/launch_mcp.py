#!/usr/bin/env python3
"""Start the second-brain MCP server.

Cursor runs this with bash, not with ${OBSIDIAN_PYTHON}. An empty Configure
form leaves that placeholder as the literal command, and the server dies
with ENOENT before Python starts. This file finds the venv interpreter and
replaces itself with `python -m obsidian_secondbrain`.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def configured(name: str) -> str | None:
    """A Configure value, ignoring an unsubstituted ${NAME} placeholder."""
    value = os.environ.get(name, "").strip()
    if not value or value.startswith("${"):
        return None
    return value


def python_exe() -> Path:
    chosen = configured("OBSIDIAN_PYTHON")
    if chosen:
        return Path(os.path.expanduser(chosen))
    home = Path.home()
    for candidate in (
        home / "Documents" / "obsidian-mcp" / ".venv" / "bin" / "python",
        home / "Documents" / "obsidian-mcp" / ".venv" / "Scripts" / "python.exe",
    ):
        if candidate.is_file():
            return candidate
    return Path(sys.executable)


def vault_dir() -> str | None:
    chosen = configured("OBSIDIAN_VAULT")
    if chosen:
        path = Path(os.path.expanduser(chosen))
        if path.is_dir():
            return str(path)
    cwd = Path.cwd()
    project_vault = cwd / "SecondBrain"
    if (project_vault / ".secondbrain" / "config.json").is_file() or (
        project_vault / ".obsidian"
    ).is_dir():
        return str(project_vault)
    return None


def main() -> None:
    py = python_exe()
    if not py.is_file():
        sys.stderr.write(
            "secbrain: no Python found. Install the package at "
            "~/Documents/obsidian-mcp or set OBSIDIAN_PYTHON in the plugin "
            f"Configure form. Looked at {py}\n"
        )
        sys.exit(1)

    env = os.environ.copy()
    vault = vault_dir()
    if vault:
        env["OBSIDIAN_VAULT"] = vault
    else:
        env.pop("OBSIDIAN_VAULT", None)

    os.execve(str(py), [str(py), "-m", "obsidian_secondbrain"], env)


if __name__ == "__main__":
    main()
