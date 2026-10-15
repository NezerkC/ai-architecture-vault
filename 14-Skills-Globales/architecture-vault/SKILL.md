---
name: architecture-vault
description: Consulta la bóveda de arquitectura compartida (estándares canónicos de patrones, metodologías XDD, contratos, resiliencia, observabilidad, seguridad, lenguajes, frameworks, persistencia, DevOps y agilidad) y aplica la nota correcta a la tarea. Úsala en cualquier proyecto cuando haya que diseñar o revisar arquitectura, elegir o implementar un patrón (Hexagonal, Clean, CQRS, EDA, Outbox, Circuit Breaker, idempotencia...), definir contratos/validación, testing (TDD/BDD), CI/CD, Docker/K8s, o cuando el usuario mencione "la bóveda", "la vault" o un "Agente X" de la bóveda. También para proponer mejoras a la bóveda.
---

# Architecture Vault (on-demand lookup)

Vault root: `C:\Users\lolpl\.gemini\antigravity\scratch\architecture-vault`
Shared by several AIs. The vault is the source of truth — never copy its content into memory or other files; read it when needed.

## Protocol

1. **Route** with the pillar table below. If the exact note name is unclear, read `Indice General.md` (one line per note) — never scan the whole vault.
2. **Read only the 1–3 notes** the task needs. Follow `dependencias` / `siguiente_paso` in a note's frontmatter only if the task actually crosses into that area.
3. For end-to-end system design, read `Agente Orquestador.md` (phase DAG) and `00-Mapa-Ruteo-Dijkstra.md`, then load specialists phase by phase.
4. **Apply** the standard to the user's project and **cite** the note used (e.g. "según `05-Resiliencia/Agente Outbox.md`"). If the project's own conventions contradict the vault, the project wins — say so.
5. **Improve**: if a note is outdated, contradictory or missing, append an entry to `00-Buzon-Mejoras.md` (format inside), tell the user in one line, and do not edit other notes without approval. Vault editing rules: `AGENTS.md`.

## Pillar routing

| Need | Folder |
|---|---|
| TDD, BDD, DDD, CDD, RDD, EDD, SDD, context distilling | `01-Metodologias/` |
| Hexagonal, Clean, Modular Monolith, EDA, CQRS | `02-Patrones/` |
| JSON Schema, OpenAPI/AsyncAPI, Zod/Pydantic, tool schemas | `03-Contratos-Validacion/` |
| ADR, RFC, fitness functions, code review | `04-Gobernanza/` |
| Circuit breaker, retry/backoff, idempotency, outbox | `05-Resiliencia/` |
| OpenTelemetry, SLI/SLO, structured logging | `06-Observabilidad/` |
| Zero Trust, input/prompt sanitization, sandboxing, OWASP | `07-Seguridad/` (start at `Hub-Seguridad.md`) |
| TypeScript, Python, Kotlin, Go, Rust | `08-Lenguajes/` |
| React, Next.js, NestJS+Fastify, FastAPI | `09-Frameworks/` |
| PostgreSQL, Redis, vector DBs | `10-Persistencia/` |
| Docker, Kubernetes, CI/CD, Terraform, GitOps, RPA Windows | `11-DevOps-Infra/` |
| Scrum, XP, Kanban, Shape Up, trunk-based, DORA | `12-Metodologias-Agiles/` |
| UI/UX, design systems, frontend components | `13-Presentacion-Frontend/` |
| Multi-agent workflows (which agents, in what order) | `00-Catalogo-Skills-Multiagente.md` |

Note names follow `Agente <Tema>.md` (vault specialist) or `Skill AAS <Tema>.md` (imported skill).
