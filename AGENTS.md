# Architecture Vault — Agent Guide

Shared guide for every AI that uses this vault (Claude Code, Antigravity, Cursor, OpenCode, ...). `CLAUDE.md` imports this file.

Obsidian knowledge vault (Spanish content) of architecture specialists. No application code. Treat notes as reference standards, not prompts to execute.

## How to use it (read the minimum)

1. Start at `Indice General.md` — one line per specialist; pick only the notes the task needs.
2. For end-to-end design, follow `Agente Orquestador.md` (phase DAG in its frontmatter) and `00-Mapa-Ruteo-Dijkstra.md`.
3. For a concrete standard, read that one note (e.g. `05-Resiliencia/Agente Outbox.md`). Each note's frontmatter lists `dependencias` / `siguiente_paso` — follow links only when needed.
4. Executable skills live in `14-Skills-Globales/<name>/SKILL.md` (native `name`/`description` frontmatter).

## Layout

- `00-*.md` — ontology, maps, catalog, templates, improvement inbox. `Agente Orquestador.md` — master orchestrator.
- `01`–`13` — one folder per pillar. `Agente *.md` = vault specialist, `Skill AAS *.md` = imported external skill.
- `14-Skills-Globales/` — SSOT for globally installed skills. Claude Code links them via junctions in `~/.claude/skills/`; Antigravity via `compilar_agentes.ps1` (exports to `../.agents/skills/`).

## Suggesting improvements (all agents)

When using the vault you notice an outdated standard, a missing specialist, a contradiction between notes, or a broken workflow:

- Do NOT silently rewrite notes during an unrelated task.
- Append one entry to `00-Buzon-Mejoras.md` (format inside), then mention it to the user in one line.
- Before adding, check the inbox for an equivalent entry — add evidence to it instead of duplicating.
- Apply a proposal only when the user approves it; then mark it `aplicada` with the commit.

## Editing rules

- New notes start from the matching `00-TEMPLATE-*.md`, keep YAML frontmatter, write in Spanish.
- Every new note must be linked from `Indice General.md` (and its pillar/dependencies).
- Every `SKILL.md` needs `name` and `description` in its frontmatter.
- Files must be UTF-8 **without BOM** (BOM breaks frontmatter parsing).
- After any change run `python check_vault.py` — must print `OK`.
- Conventional commits, no AI attribution.
