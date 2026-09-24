---
tipo: dashboard
tags:
  - obsidian/dashboard
  - arquitectura/hub
  - harness/universal
---

# ARCHITECTURE AGENT NETWORK (UNIVERSAL HARNESS & OBSIDIAN VAULT)

Sistema integral de arquitectura de software, infraestructura cloud-native y metodologías de ingeniería para desarrollo guiado por agentes. Compatible con **Antigravity**, **OpenCode**, **Claude Code**, **Cursor** y **Obsidian**.

---

## 🧭 Orquestador Principal
- [[Agente Orquestador]] — *Lead Software Architect (Pipeline DAG, gobernanza y síntesis de `architecture.md`)*

---

## 🗂️ Catálogo Completo de Agentes Especialistas (13 Módulos)

### 01. Metodologías de Diseño y Desarrollo (XDD)
- [[Agente RDD]] — *README-Driven Development (Visión e interfaz pública)*
- [[Agente BDD]] — *Behavior-Driven Development (Escenarios en Gherkin)*
- [[Agente SDD]] — *Spec-Driven Development (Fases de cambio, tareas atómicas y orquestación)*
- [[Agente DDD]] — *Domain-Driven Design (Bounded Contexts, Entidades y Agregados)*
- [[Agente CDD]] — *Contract-Driven Development (Fronteras e interfaces formales)*
- [[Agente TDD]] — *Test-Driven Development (Pruebas unitarias deterministas)*
- [[Agente EDD]] — *Eval-Driven Development (Evaluación estadística de IA y Golden Datasets)*

### 02. Patrones Arquitectónicos
- [[Agente Monolito Modular]] — *Módulos cohesivos con API pública e internal aislada*
- [[Agente Hexagonal]] — *Puertos y Adaptadores (Desacoplamiento total del núcleo)*
- [[Agente Clean Architecture]] — *Capas concéntricas con regla de dependencia estricta*
- [[Agente EDA]] — *Event-Driven Architecture (CloudEvents y Dead Letter Queues)*
- [[Agente CQRS]] — *Segregación estricta de Commands y Queries*

### 03. Contratos, Especificaciones y Validación
- [[Agente JSON Schema]] — *Validación formal y Structured Outputs para LLMs*
- [[Agente Runtime Validation]] — *Tipado estricto en tiempo de ejecución (Pydantic / Zod)*
- [[Agente OpenAPI]] — *Estándares de APIs REST y AsyncAPI 3.0*
- [[Agente Tool Schemas]] — *Definición estricta de Function Calling para agentes*

### 04. Gobernanza y Decisiones
- [[Agente ADR]] — *Architecture Decision Records (Registro inmutable de trade-offs)*
- [[Agente RFC]] — *Request for Comments (Propuestas técnicas colaborativas)*
- [[Agente Fitness Functions]] — *Verificación automatizada de arquitectura en CI/CD*
- [[Skill AAS Code Review]] — *Revisión estricta de PRs, invariantes de Clean Architecture y gates de merge*

### 05. Patrones de Resiliencia y Consistencia
- [[Agente Idempotencia]] — *Llaves de idempotencia y prevención de doble procesamiento*
- [[Agente Outbox]] — *Transactional Outbox Pattern (Garantía contra Dual-Write)*
- [[Agente Circuit Breaker]] — *Protección contra fallas en cascada y fail-fast*
- [[Agente Retry Backoff]] — *Reintentos exponenciales con Full Jitter*

### 06. Observabilidad y Auditoría
- [[Agente OpenTelemetry]] — *Tracing distribuido de extremo a extremo (TraceID)*
- [[Agente Structured Logging]] — *Logs tipados en JSON y sanitización de PII*
- [[Agente SLI SLO]] — *Métricas de confiabilidad y presupuestos de error*

### 07. Seguridad y Fronteras (Guardrails)
- [[Agente Zero Trust]] — *Principio de menor privilegio y tokens efímeros*
- [[Agente Sanitizacion Fronteras]] — *Defensa contra Prompt Injection y sanitización de I/O*
- [[Agente Sandbox Aislamiento]] — *Ejecución segura de código dinámico en microVMs*
- [[Skill AAS Security Engineer]] — *Auditoría de vulnerabilidades OWASP, SAST/SCA y hardening*

### 08. Especialistas en Lenguajes
- [[Agente TypeScript]] — *Tipado estricto, Result Types y tsconfig de producción*
- [[Agente Python]] — *Python 3.12+, Mypy estricto, AsyncIO y empaquetado con uv*
- [[Agente Kotlin]] — *Kotlin 2.0+, Coroutines, Flow, Jetpack Compose y KMP en IntelliJ IDEA*
- [[Agente Go]] — *Interfaces idiomáticas, concurrencia segura y context propagation*
- [[Agente Rust]] — *Memory safety, Tokio async y Traits para puertos*

### 09. Especialistas en Frameworks y Runtimes
- [[Agente React]] — *Arquitectura de componentes, Custom Hooks desacoplados y estado inmutable*
- [[Agente NextJS]] — *Server Components, Server Actions seguras y patrón BFF*
- [[Agente NestJS Fastify]] — *Inyección de dependencias modular sobre motor Fastify*
- [[Agente FastAPI]] — *Driving Adapters REST asíncronos y DI nativo*

### 10. Persistencia y Almacenamiento
- [[Agente PostgreSQL]] — *Modelado relacional, índices concurrentes y Zero-Downtime*
- [[Agente Vector DB]] — *Indexación HNSW, búsqueda híbrida y pre-filtering en Qdrant*
- [[Agente Redis Cache]] — *Cache-Aside con Jitter, distributed locking y rate limiting*

### 11. DevOps, Infraestructura y Plataforma
- [[Agente Docker OCI]] — *Imágenes multi-stage, distroless y usuario non-root*
- [[Agente Kubernetes]] — *Manifests con probes, resource limits y NetworkPolicies*
- [[Agente CI CD Pipeline]] — *Pipelines deterministas en GitHub Actions / GitLab CI*
- [[Agente Terraform IaC]] — *Infrastructure as Code modular con remote state locking*
- [[Agente GitOps]] — *Despliegues declarativos con ArgoCD / Flux y auto-healing*
- [[Skill AAS DevOps Cloud]] — *Automatización de infraestructura cloud y pipelines de despliegue*

### 12. Metodologías Ágiles e Ingeniería de Entrega
- [[Agente Scrum]] — *Sprints con Definition of Done e incremento vertical (INVEST)*
- [[Agente XP]] — *Extreme Programming, refactoring continuo y diseño simple (YAGNI)*
- [[Agente Trunk Based Development]] — *Branches efímeras (< 24h) y Feature Flags*
- [[Agente Kanban WIP]] — *Límites estrictos de trabajo en progreso y flujo continuo*
- [[Agente Continuous Delivery DORA]] — *Las 4 métricas DORA y releases continuos*
- [[Agente Shape Up]] — *Ciclos de 6 semanas, fixed time/variable scope y apuestas (Bets)*

### 13. Presentación & Frontend (Pilar AAS)
- [[Skill AAS UI UX Pro Max]] — *Sistemas de diseño, wireframes y tokens visuales*
- [[Skill AAS Frontend Design]] — *Implementación de componentes, Tailwind y Server Components*

---

## 📊 Vista en Grafo (Graph View)
Presioná `Ctrl + G` en Obsidian para navegar el mapa interactivo de agentes y sus dependencias.

