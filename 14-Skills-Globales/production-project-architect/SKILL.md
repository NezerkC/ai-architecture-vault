---
name: production-project-architect
description: Orquestador maestro de arquitectura e ingeniería de software para crear proyectos de producción end-to-end (Dominio DDD, Capas Hexagonales, Base de Datos ACID, Testing TDD/Fitness y CI/CD).
---

# SKILL: PRODUCTION PROJECT ARCHITECT

Esta skill coordina el pipeline de 5 fases para crear y estructurar un proyecto de software profesional:

## Fase 1: Dominio Puro & Gobernanza (DDD + ADR)
- Modela Entidades, Value Objects, Agregados e Invariantes sin dependencias de frameworks en `src/domain/`.
- Registra la decisión técnica inicial en `docs/adr/0001-architecture-decisions.md`.

## Fase 2: Capas & Contratos (Clean / Hexagonal + Zod / Pydantic)
- Define Puertos de entrada (Casos de Uso) y salida (Interfaces de Repositorio/Servicios) en `src/application/ports/`.
- Implementa esquemas de validación estricta en runtime en `src/application/schemas/`.

## Fase 3: Persistencia & Resiliencia (PostgreSQL + Migraciones + Outbox)
- Modela tablas relacionales con constraints e índices en `migrations/`.
- Configura patrón Outbox transaccional y Unit of Work en `src/infrastructure/persistence/`.

## Fase 4: Calidad & Testing (TDD + Fitness Functions)
- Escribe tests unitarios de dominio y casos de uso con ciclo Red-Green-Refactor.
- Configura tests de arquitectura para impedir importaciones cruzadas prohibidas.

## Fase 5: DevOps, Docker & CI/CD
- Crea `Dockerfile` multi-stage corriendo bajo usuario no-root (`USER app`).
- Configura `.github/workflows/ci.yml` con linter, typecheck, tests y escaneo de vulnerabilidades.
