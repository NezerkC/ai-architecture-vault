---
tipo: buzon-mejoras
tags:
  - gobernanza/mejora-continua
  - harness/universal
---

# BUZÓN DE MEJORAS DE LA BÓVEDA

Canal compartido entre todas las IAs que usan la bóveda (ver `AGENTS.md`). Cada agente agrega propuestas acá en lugar de reescribir notas sin aprobación. El usuario decide qué se aplica.

## Formato de entrada

```markdown
### YYYY-MM-DD — <título corto>
- **Agente:** <claude-code | antigravity | cursor | opencode | ...>
- **Nota(s):** [[Nombre de la nota]]
- **Tipo:** desactualizado | faltante | contradicción | workflow | skill
- **Evidencia:** <qué se observó y dónde>
- **Propuesta:** <cambio concreto>
- **Estado:** abierta | aprobada | aplicada (<commit>) | descartada (<motivo>)
```

## Abiertas

### 2026-10-06 — Matizar la prohibición de librerías de terceros en el dominio
- **Agente:** claude-code
- **Nota(s):** [[Agente Hexagonal]]
- **Tipo:** contradicción
- **Evidencia:** Al auditar Visión OS (`vision-cognitive-agent`, rama `refactor/clean-hexagonal-architecture`), `core/domain/*.py` importa solo `pydantic`. La nota prohíbe "librerías de terceros" en el dominio sin excepción, pero el proyecto exige por convención envelopes Pydantic v2 (`.agents/AGENTS.md`), práctica habitual en Python (equivalente a Zod en TS), y Pydantic no introduce I/O ni infraestructura.
- **Propuesta:** Distinguir entre librerías de infraestructura (frameworks web, ORMs, SDKs de IA, clientes de red: prohibidas) y librerías puras de modelado/validación sin I/O (Pydantic, Zod, attrs: permitidas si el proyecto lo adopta como convención). Agregar el criterio "¿la dependencia puede hacer I/O o atar el dominio a un proveedor?".
- **Estado:** abierta

### 2026-10-06 — Herramientas de IA que necesitan el host (automatización de escritorio)
- **Agente:** claude-code
- **Nota(s):** [[Agente Sandbox Aislamiento]]
- **Tipo:** faltante
- **Evidencia:** En Visión OS, `cognitivo/ejecutor_izquierdo.py` controla mouse/teclado y abre aplicaciones locales: por naturaleza no puede correr en un sandbox efímero sin red como exige la nota. La nota no cubre ese caso, y ahí aparecieron fallas concretas: aprobación HITL decorativa (el comando corría antes de aprobar), posibilidad de reemplazar la acción pendiente después de mostrar el ticket, XSS en el ticket que permitía auto-aprobarse, inyección de eventos desde el navegador vía cross-protocol POST al broker TCP local, y ausencia de timeout.
- **Propuesta:** Agregar una sección "Herramientas que requieren el host" con controles mínimos: (1) HITL real que bloquee la ejecución hasta la aprobación, ligada al payload exacto mostrado (sin reemplazo del request pendiente, una sola decisión, expiración); (2) contenido del ticket escapado; (3) timeout estricto con kill del árbol de procesos (`taskkill /T` / process group), no solo del shell; (4) canal de eventos local que rechace tráfico no autenticado o de otro protocolo; (5) registro de auditoría. Referencia: commits `837879a` y `aafba1c` de Visión OS.
- **Estado:** abierta

## Cerradas

_(vacío)_

Relacionado: [[Indice General]] · [[Agente Orquestador]]
