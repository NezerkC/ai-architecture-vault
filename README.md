# Architecture Agent Network & Obsidian Vault

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Obsidian Vault](https://img.shields.io/badge/Obsidian-Vault-7C3AED.svg?logo=obsidian&logoColor=white)](https://obsidian.md)
[![Multi-Agent Network](https://img.shields.io/badge/Agents-Network%20Ontology-blue.svg)](https://github.com/NezerkC/ai-architecture-vault)
[![Clean Architecture](https://img.shields.io/badge/Architecture-Clean%20%2F%20Hexagonal-107C41.svg)](https://github.com/NezerkC/ai-architecture-vault)

Sistema integral de arquitectura de software, infraestructura cloud-native y metodologías de ingeniería para desarrollo guiado por agentes de IA y navegación de conocimiento en Obsidian.

Compatible con **Antigravity**, **Claude Code**, **Cursor**, **OpenCode** y **Obsidian**.

---

## 🏛️ Modelo Mental: La Ontología Metro

Para que tanto ingenieros humanos como agentes de IA compartan el mismo modelo conceptual, la bóveda organiza su conocimiento bajo una analogía de **Red de Transporte (Metro)**:

| Concepto Metro | Concepto Arquitectónico / Vault | Definición |
| :--- | :--- | :--- |
| **Entrada (Torniquete)** | **Agente Especialista** | Interfaz o skill especializada que recibe una tarea técnica concreta (ej. Agente TDD, Agente PostgreSQL). |
| **Estación** | **Pilar Arquitectónico** | Dominio o *Bounded Context* que agrupa agentes y estándares afines (ej. `07-Seguridad`, `10-Persistencia`). |
| **Línea de Metro** | **Flujo Transversal (Feature / Epic)** | Ruta que conecta múltiples pilares para resolver un requerimiento complejo (ej. Flujo de Autenticación cruza Frontend, Seguridad y Persistencia). |
| **Combinación** | **Hub Simple** | Cruce entre pilares con transferencia de contexto ligera entre agentes específicos. |
| **Estación Intermodal** | **Hub Masivo (Scatter-Gather)** | Punto de alta complejidad donde se despiertan múltiples agentes en paralelo para sincronizar el estado global. |

El **`[[Agente Orquestador]]`** utiliza algoritmos de ruteo (Dijkstra) para trazar la ruta crítica óptima entre pilares ante cualquier requerimiento de software.

---

## 📂 Estructura de la Bóveda

```text
architecture-vault/
├── 00-Catalogo-Skills-Multiagente.md   # Registro maestro de agentes
├── 00-Mapa-Red-Metro-Lineas.md        # Líneas y flujos transversales
├── 00-Mapa-Ruteo-Dijkstra.md          # Matriz de pesos y costos de ruteo
├── 00-Ontologia-Metro.md              # Glosario y modelo conceptual
├── 00-TEMPLATE-*.md                   # Plantillas oficiales para nuevas notas
├── 01-Metodologias/                   # XDD (TDD, BDD, DDD, CDD, RDD, EDD, SDD)
├── 02-Patrones/                       # Hexagonal, Clean, Modular, EDA, CQRS
├── 03-Contratos-Validacion/           # JSON Schema, OpenAPI, Pydantic, Zod
├── 04-Gobernanza/                     # ADRs, RFCs, Fitness Functions
├── 05-Resiliencia/                    # Circuit Breaker, Outbox, Retry Jitter
├── 06-Observabilidad/                 # OpenTelemetry, SLI/SLO, Logging JSON
├── 07-Seguridad/                      # Zero Trust, Sanitización, Sandboxing
├── 08-Lenguajes/                      # TypeScript, Python, Kotlin, Go, Rust
├── 09-Frameworks/                     # FastAPI, NextJS, NestJS Fastify
├── 10-Persistencia/                   # PostgreSQL, Vector DB, Redis Cache
├── 11-DevOps-Infra/                   # Docker OCI, Kubernetes, CI/CD, Terraform
├── 12-Metodologias-Agiles/            # Scrum, XP, Trunk-Based, Kanban, Shape Up
├── 13-Presentacion-Frontend/          # Design Systems, UI/UX, Componentes
├── Agente Orquestador.md              # Orquestador maestro del pipeline
├── Indice General.md                  # Dashboard principal de navegación
└── landing-agents.html                # Visualizador interactivo de agentes
```

---

## 🚀 Modo de Uso

### 1. Como Bóveda en Obsidian (Navegación Humana)
1. **Abrir la Bóveda**: Iniciar Obsidian y seleccionar *Open folder as vault*, eligiendo este directorio.
2. **Dashboard de Inicio**: Abrir `Indice General.md` para visualizar el catálogo completo de pilares y agentes.
3. **Navegación Gráfica**:
   - Presionar `Ctrl + G` (o `Cmd + G` en macOS) para explorar la vista en grafo con las conexiones bidireccionales (WikiLinks).
   - Abrir `landing-agents.html` en el navegador para una experiencia visual interactiva de la red.
4. **Trazado de Arquitectura**: Consultar `00-Mapa-Ruteo-Dijkstra.md` para seguir el pipeline paso a paso al diseñar un nuevo sistema o funcionalidad.

### 2. Con Agentes de IA y Harnesses (Antigravity, Cursor, Claude Code)
- **Base de Conocimiento**: Apuntar el contexto del agente a esta carpeta para que utilice los estándares formales de arquitectura al proponer o escribir código.
- **Invocación de Especialistas**: Cuando se requiera implementar un estándar concreto, consultar la nota del agente correspondiente (ejemplo: leer `05-Resiliencia/Agente Circuit Breaker.md` para replicar el patrón de resiliencia exacto).
- **Orquestación**: Utilizar `Agente Orquestador.md` como prompt de sistema o rol director cuando un agente deba liderar el diseño de una solución de punta a punta.
- **Pipeline GitOps (Habilidades Nativas)**: Ejecutar `.\compilar_agentes.ps1` (Docs-as-Code). Este script escanea la bóveda, lee los YAML Frontmatters y compila/exporta los archivos Markdown estáticos a la carpeta oculta `.agents/skills/SKILL.md`, volviendo las Skills ejecutables de manera nativa para Antigravity.

---

## 🤝 Cómo Aportar al Repositorio

Agradecemos contribuciones que fortalezcan los patrones de arquitectura, incorporen nuevos agentes especialistas o refinen la gobernanza técnica del sistema.

### Reglas de Contribución

1. **Uso Obligatorio de Plantillas**:
   - Para un nuevo agente: utilizar `00-TEMPLATE-Skill-Especialista.md`.
   - Para un nuevo pilar de dominio: utilizar `00-TEMPLATE-Pilar-Dominio.md`.
   - Para un hub o intersección: utilizar `00-TEMPLATE-Hub-Relacional.md`.
2. **Frontmatter YAML**: Toda nota debe incluir metadatos estandarizados al inicio (`tipo`, `tags`, `dominio`).
3. **Enlaces Bidireccionales**: Cada nuevo agente debe conectarse con su pilar, sus dependencias y estar indexado en `Indice General.md` y `00-Catalogo-Skills-Multiagente.md`.
4. **Calidad de Contenido (Conceptos > Código)**: Los documentos no son snippets triviales; deben detallar el problema técnico, la solución canónica, los trade-offs y los criterios de validación.

### Flujo de Trabajo con Git

1. **Fork** del repositorio en GitHub:
   ```bash
   https://github.com/NezerkC/ai-architecture-vault
   ```
2. **Clonar** tu fork localmente:
   ```bash
   git clone https://github.com/NezerkC/ai-architecture-vault.git
   cd ai-architecture-vault
   ```
3. **Crear una rama** para tu cambio:
   ```bash
   git checkout -b feat/nuevo-agente-kafka
   ```
4. **Hacer commit** siguiendo [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat(patrones): add Kafka streaming specialist agent"
   ```
5. **Enviar los cambios y abrir un Pull Request**:
   ```bash
   git push origin feat/nuevo-agente-kafka
   ```
6. En el Pull Request, describir:
   - Qué problema resuelve el nuevo agente o mejora.
   - Qué pilares y notas se conectan con este aporte.
