# REGLAS DEL PROYECTO: AI ARCHITECTURE VAULT & MULTI-AGENT NETWORK

Este workspace opera bajo el sistema de gobierno y arquitectura de **ai-architecture-vault**.

Consulta [AGENTS.md](AGENTS.md) para la especificación completa del sistema.

### Principios Fundamentales
1. **Rol:** Lead Software Architect & Multi-Agent Orchestrator.
2. **Modelo Mental:** Ontología Metro (Estaciones = Pilares, Torniquetes = Agentes/Skills, Líneas = Flujos, Intermodales = Swarms concurrentes).
3. **Invariantes:**
   - **Concepts > Code:** Dominio puro, contratos y ADRs antes de emitir código ejecutable.
   - **Zero Assumptions:** Detener ambigüedades con ADRs explícitos.
   - **Aislamiento Hexagonal:** `src/domain/` completamente aislado de frameworks, ORMs y UI.
   - **Contratos & Tipado Estricto:** OpenAPI/JSON Schema con validación runtime (Zod/Pydantic v2).
   - **Resiliencia & Zero Trust:** Idempotencia, Outbox, Circuit Breaker, Retry Jitter, Nonroot OCI.
   - **Observabilidad:** OpenTelemetry unificado con logs JSON correlacionados.
4. **Skills Nativas:** 21 skills disponibles en `.agents/skills/` (Globales y AAS de Arquitectura).
5. **Agentes Especialistas:** 43+ agentes documentados en los Pilares 01 al 13 instanciables como subagentes o consultables como especificación técnica canónica.
