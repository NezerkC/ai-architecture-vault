---
name: architecture-audit
description: Auditoría exhaustiva de arquitectura de software. Explica el paso a paso, qué hacer, cómo hacerlo, la distribución de capas y genera un informe de remediación priorizado.
parameters:
  target_path:
    type: string
    description: "Ruta del proyecto o directorio a auditar (por defecto la raíz del workspace)"
    required: false
  audit_lens:
    type: string
    description: "Lente de auditoría: 'full' (completa), 'layers' (capas), 'security' (seguridad), 'resilience' (resiliencia), 'ddd' (dominio)"
    required: false
---

# SKILL: ARCHITECTURE AUDIT & DIAGNOSTIC INSPECTOR

Esta skill ejecuta una auditoría profunda sobre cualquier proyecto de software para evaluar su madurez arquitectónica, detectar anti-patrones y generar un plan de acción correctivo paso a paso.

---

## 1. Las 6 Lentes de Inspección (Paso a Paso)

### Lente 1: Distribución y Límites de Capas (Screaming / Clean Architecture)
* **Qué buscar:** ¿La estructura de carpetas grita la intención del negocio (`domain/`, `application/`, `infrastructure/`, `presentation/`)?
* **Regla Inviolable:** Las capas internas **no deben conocer** a las externas.
  * ❌ `domain/` no puede importar nada de `infrastructure/`, `fastapi`, `express`, ORMs o clientes HTTP.
  * ❌ `application/` define interfaces (puertos), no implementaciones concretas.

### Lente 2: Pureza del Dominio e Invariantes (DDD)
* **Qué buscar:** ¿Las entidades son modelos anémicos (meras estructuras de datos con getters/setters) o protegen sus reglas de negocio?
* **Regla Inviolable:** Toda mutación de estado debe validarse mediante métodos semánticos explícitos (ej. `order.pay()` en vez de `order.status = 'PAID'`).

### Lente 3: Contratos & Validación de Entrada/Salida
* **Qué buscar:** ¿Los datos que ingresan desde HTTP o CLI se validan estrictamente en la frontera?
* **Herramientas:** Pydantic v2 en Python, Zod en TypeScript, `kotlinx.serialization` en Kotlin.

### Lente 4: Persistencia y Resiliencia
* **Qué buscar:** 
  * ¿Las transacciones son atómicas (ACID) mediante Unit of Work?
  * Si se emiten eventos, ¿se usa el patrón Transactional Outbox para no perder mensajes?
  * ¿Las operaciones de escritura soportan claves de idempotencia?
  * ¿Las llamadas a servicios externos tienen Circuit Breaker y Retry con Backoff?

### Lente 5: Seguridad y Gestión de Secretos (Zero Trust)
* **Qué buscar:** Escaneo de API keys, tokens de Telegram o credenciales en texto plano.
* **Aislamiento:** ¿Los contenedores Docker corren como usuario no-root? ¿Los sandboxes de harnesses están aislados?

### Lente 6: Gobernanza y Calidad (Fitness Functions)
* **Qué buscar:** ¿Existen tests de arquitectura automatizados que fallen en el CI si alguien viola una capa?

---

## 2. Flujo de Ejecución del Agente Auditor

1. **Inspección de Archivos:** Escanear la raíz y subdirectorios del proyecto.
2. **Evaluación de Importaciones:** Revisar declaraciones `import` en archivos de dominio.
3. **Cálculo del Health Score (0 a 100%):**
   * Separación de Capas: 25 pts.
   * Pureza de Dominio DDD: 20 pts.
   * Contratos & Validación: 15 pts.
   * Resiliencia & Datos: 15 pts.
   * Seguridad & Secretos: 15 pts.
   * Calidad & Tests: 10 pts.
4. **Generación del Entregable:** Crear `docs/audit/AUDIT_REPORT.md`.

---

## 3. Formato del Informe Entregable (`docs/audit/AUDIT_REPORT.md`)

```markdown
# INFORME DE AUDITORÍA ARQUITECTÓNICA
Fecha: YYYY-MM-DD | Score de Salud: XX/100

## 1. Resumen Ejecutivo
[Diagnóstico general de la base de código]

## 2. Matriz de Deuda Técnica
| Severidad | Problema Encontrado | Archivo Afectado | Agente Asignado |
| :--- | :--- | :--- | :--- |
| CRÍTICA | Import de ORM en Dominio | src/domain/user.py | Agente DDD |
| ALTA | Falta clave de Idempotencia | src/application/pay.py | Agente Idempotencia |

## 3. Plan de Remediación Paso a Paso
1. **Paso 1:** [Acción concreta con código antes/después]
2. **Paso 2:** [Instrucciones de refactorización]
```
