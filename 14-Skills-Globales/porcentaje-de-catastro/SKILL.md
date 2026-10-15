---
name: porcentaje-de-catastro
description: >-
  Genera una radiografía ejecutiva y porcentual del estado de un proyecto o migración ("Porcentaje de Catastro"), detallando: (1) lo que había (base/requerimientos), (2) cómo va (porcentaje global, tabla por capas técnicas y tabla módulo por módulo con semáforos), y (3) hacia dónde tiene que ir el progreso (qué falta hacer, responsables y siguiente paso). Úsala siempre que el usuario pida "porcentaje de catastro", "catastro de avance", "catastro del proyecto" o pregunte cuánto se ha portado/avanzado en porcentaje.
---

# Porcentaje de Catastro — Radiografía de Progreso de Proyecto

Cuando el usuario solicite un **"porcentaje de catastro"** (o catastro de avance), realiza una inspección real del repositorio y entrega un informe estructurado con las siguientes secciones obligatorias:

## 1. Fase de Inspección Previa
Antes de calcular porcentajes, verifica en el proyecto:
- Configuración base, compilación (`build`), linter y pipelines CI/CD.
- Datos maestros, modelos, assets e integraciones.
- Lógica de negocio (utilidades, hooks, contextos, servicios).
- Suite de pruebas unitarias/integración y su estado actual.
- Vistas, pantallas o endpoints completados frente al total requerido.

## 2. Estructura Obligatoria del Informe

### A. Resumen Global y Lo Que Había (Base)
- Indica el **porcentaje de avance global estimado (`~XX%`)**.
- Resume brevemente cuál es el universo total del proyecto (ej. cuántas páginas, módulos o requerimientos componen el 100% original).

### B. Tabla 1: Avance por Capas Técnicas (Cómo va)
Presenta una tabla con semáforo (`✅ 100%`, `🟢 70-99%`, `🟡 30-69%`, `🔴 0-29%`):

| Capa del Proyecto | % Avance | Estado Actual (Lo que ya existe) |
| :--- | :---: | :--- |
| **1. Configuración, Build y CI/CD** | **XX%** | Detalle real de herramientas y pipelines listos |
| **2. Datos, Modelos y Recursos** | **XX%** | Estado de bases de datos, mocks, imágenes o catálogos |
| **3. Lógica de Negocio y Estado** | **XX%** | Estado de hooks, contextos, validaciones y servicios |
| **4. Suite de Pruebas (Testing)** | **XX%** | Cantidad de tests pasando y cobertura |
| **5. Diseño y Sistema Visual** | **XX%** | Estado de estilos, temas y componentes base |
| **6. Vistas / Páginas / Endpoints** | **XX%** | Cantidad de pantallas o rutas listas vs pendientes |

### C. Tabla 2: Desglose Detallado y Hacia Dónde Va el Progreso
Presenta una tabla ítem por ítem (o página por página) que conecte **lo que ya está hecho** con **lo que falta hacer** y **quién o en qué orden debe abordarse**:

| Módulo / Página Original | Avance | ¿Qué ya está hecho? | ¿Qué falta hacer? (Meta) | Responsable / Prioridad |
| :--- | :---: | :--- | :--- | :--- |
| Nombre del ítem | **XX%** | Piezas ya construidas | Trabajo pendiente exacto | Integrante o prioridad |

### D. Conclusión Ejecutiva y Siguiente Paso
- Cierra con un diagnóstico claro de en qué punto se encuentra el equipo y propone la **acción inmediata más efectiva** para hacer avanzar el porcentaje.
