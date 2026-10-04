---
name: harness-configurator
description: Configura, valida y ajusta los sandboxes de los motores de agentes integrados (Claude Code, OpenCode, Antigravity, Hermes/DeepSeek) en harnesses/.
---

# SKILL: HARNESS CONFIGURATOR

Permite configurar y auditar los sandboxes de los distintos motores de ejecución en `harnesses/`:
1. Identifica el harness destino (`harnesses/claude/`, `harnesses/opencode/`, `harnesses/antigravity/`, `harnesses/hermes_deepseek/`).
2. Valida la sintaxis de los archivos JSON/YAML.
3. Configura herramientas MCP y modelos locales sin ensuciar la raíz del proyecto.
4. Audita permisos y variables de entorno seguras.
