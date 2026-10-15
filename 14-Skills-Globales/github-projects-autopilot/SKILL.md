---
name: github-projects-autopilot
description: Automatiza el seguimiento de tareas en GitHub Projects e Issues a partir de requerimientos o guías académicas/técnicas. Crea workflows de GitHub Actions que inspeccionan el código en cada git push, cierran tareas completadas automáticamente, promueven la siguiente tarea con instrucciones de la IA y proveen un asistente local (progreso.ps1). Úsala cuando el usuario quiera automatizar GitHub Projects, sincronizar tareas con el código o pida "avancemos" en un proyecto con seguimiento automático.
---

# GitHub Projects Autopilot & AI Task Coach

Esta skill elimina la gestión manual de tableros de tareas (GitHub Projects / Issues), conectando directamente el **código fuente real** con el estado del tablero mediante **GitHub Actions** y un **asistente local de terminal**.

---

## 1. ¿Cómo funciona la Automatización? (Doble Motor)

El sistema opera de **dos formas simultáneas y complementarias**:

### Motor A · Automático en cada `git push` (24/7 en GitHub Actions)
* **No requiere abrir el chat ni intervención manual.**
* Vive en `.github/workflows/auto-progress-tracker.yml` con el disparador `on: push: branches: [ main ]`.
* Cada vez que cualquier integrante del equipo sube código (`git push`), GitHub Actions:
  1. Escanea el árbol de código fuente buscando las evidencias técnicas de cada tarea (clases, funciones, componentes UI, anotaciones de base de datos, tests).
  2. **Si detecta que una tarea ya se cumplió en el código:** Le asigna la etiqueta `estado: finalizado`, publica un comentario de verificación en el Issue y **cierra el Issue automáticamente** (`state: closed`, `state_reason: completed`), lo que mueve la tarjeta a la columna **`Done`** en GitHub Projects.
  3. **Promueve la siguiente tarea pendiente:** Identifica la primera tarea aún no cumplida, le asigna `estado: en-curso` y publica un comentario con la **Guía Paso a Paso de la IA** indicando a los compañeros qué archivos editar a continuación.

### Motor B · Modo Copiloto en el Chat (Cuando el usuario dice *"Avancemos"*)
* Cuando el usuario escribe `"avancemos"`, `"qué toca hacer"` o `"siguiente tarea"`:
  1. El agente ejecuta `powershell -ExecutionPolicy Bypass -File .\progreso.ps1` (o inspecciona las reglas definidas) para identificar la tarea actualmente en `EN CURSO`.
  2. Explica en 3 líneas claras qué se va a construir.
  3. Implementa el código correspondiente respetando la arquitectura del proyecto y verifica que compile/pase los tests.
  4. Realiza el `git commit -m "feat: ... (closes #N)"` y `git push origin main`, disparando el Motor A en GitHub para actualizar el tablero para todo el equipo.

---

## 2. Protocolo Paso a Paso para Inicializar un Proyecto Nuevo

Cuando el usuario pida configurar el Autopilot de GitHub Projects en cualquier repositorio:

### Paso 1: Extraer el Backlog desde el Caso / Guías
* Analiza los requerimientos funcionales (`RF`), reglas de negocio (`RN`) o guías de laboratorio del proyecto.
* Divide el trabajo en **8 a 12 tareas secuenciales y verificables en código** (desde la arquitectura base hasta la persistencia y pruebas).

### Paso 2: Generar `.github/workflows/seed-project-backlog.yml`
* Crea un workflow con `actions/github-script@v7` y permisos `issues: write` que:
  1. Cree las etiquetas estándar:
     * `estado: finalizado` (`#0E8A16`)
     * `estado: en-curso` (`#FBCA04`)
     * `estado: por-hacer` (`#1D76DB`)
     * `prioridad: alta` (`#D93F0B`)
     * `prioridad: media` (`#0075CA`)
  2. Verifique los Issues existentes (`state: 'all'`) por título para ser **100% idempotente** (nunca duplicar Issues).
  3. Cree los Issues con su checklist de criterios de aceptación.

### Paso 3: Generar `.github/workflows/auto-progress-tracker.yml`
* Crea el workflow que se ejecuta en cada `push` a `main`.
* Define para cada tarea una regla booleana determinista (`isDone`) basada en la existencia de archivos, clases, firmas de métodos o componentes en el código fuente, diferenciando entre código de dominio y código de interfaz (`uiCode`).
* Incluye para cada tarea un bloque `coachTip` con instrucciones claras para el equipo.

### Paso 4: Generar `progreso.ps1` en la raíz del proyecto
* Crea un script PowerShell compatible con Windows PowerShell 5.1 y PowerShell 7 (usando caracteres ASCII limpios en consola) que evalúe las mismas reglas localmente y muestre:
  * Porcentaje de avance global (`X% (N/Total Tareas)`).
  * Lista de tareas con estado `[LISTO]`, `[EN CURSO]` y `[PENDIENTE]`.
  * Bloque destacado `QUE TOCA HACER AHORA` con la instrucción exacta de la tarea activa.
