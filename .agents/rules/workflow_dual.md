# 🧭 Modelo de Inteligencia Dual: GitNexus + NotebookLM

Este documento define la arquitectura simbiótica de trabajo entre los dos motores de inteligencia del proyecto, sus roles específicos y el flujo operativo de 5 fases.

---

## 🏛️ 1. Arquitectura de Colaboración Simbiótica

```text
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITECTURA DE INTELIGENCIA DUAL                            │
├───────────────────────────────────────┬─────────────────────────────────────────┤
│    🧠 NOTEBOOKLM (Cerebro Académico)  │     🕸️ GITNEXUS (Cerebro Técnico)       │
├───────────────────────────────────────┼─────────────────────────────────────────┤
│ • Rigor conceptual y epistemológico   │ • Integridad de código y arquitectura   │
│ • Bibliografía de cátedra (SIA 1-4)   │ • Pipeline Docs-as-Code (compilar_todos)│
│ • Resoluciones UNCo (Res. 266/23)     │ • Grafo de dependencias y llamadas      │
│ • Consignas de TPs y devoluciones     │ • Análisis de impacto (blast radius)    │
│ • Generación de resúmenes y audios    │ • Detección de cambios y regresiones    │
│ ➔ GOBIERNA EL CONTENIDO Y EL FONDO    │ ➔ GOBIERNA LA FORMA Y LA INFRAESTRUCTURA│
└───────────────────────────────────────┴─────────────────────────────────────────┘
                                       │
                                       ▼
                  📄 DOCUMENTOS QUARTO (.qmd) + TYPST (.typ)
                                       │
                                       ▼
              📦 ENTREGABLES INSTITUCIONALES (.pdf + .docx APA 7)
```

---

## 👥 2. Matriz de Responsabilidades

| Dimensión | 🧠 NotebookLM (`notebooklm-mcp`) | 🕸️ GitNexus (`gitnexus`) |
| :--- | :--- | :--- |
| **Rol Primario** | Asistente de Investigación y Rigor Académico | Asistente de Código y Control de Arquitectura |
| **Fuentes de Verdad** | PDFs de autores (Sampieri, Sautu, Yuni & Urbano, Sabino, Chiavenato, Oszlak), normativa CURZAS, devoluciones docentes. | Código fuente (`compilar_todos.py`, scripts, filtros Pandoc, plantillas Typst, configs). |
| **Operación Típica** | Consultar marco conceptual, verificar coherencia de objetivos, sintetizar aportes teóricos. | Analizar impacto previo (`impact`), inspeccionar flujos (`processes`), validar cambios antes de commit (`detect-changes`). |
| **Salida Producida** | Fundamentación teórica, citas bibliográficas APA 7 exactas, guías de estudio. | Grafo de dependencias AST (90+ nodos, flujos de compilación), reportes de riesgo, refactorización segura. |

---

## 🔄 3. Flujo Operativo Integrado (Workflow de 5 Fases)

Para el desarrollo y ajuste de cualquier Trabajo Práctico o sección de la Tesina:

1. **Fase 1 — Indagación Teórica y Metodológica (NotebookLM):**
   * Consultar las fuentes académicas del módulo para formular problema, objetivos y marco conceptual según la cátedra SIA y Res. CD-CURZAS N° 266/23.
   * Extraer citas textuales exactas y referencias según APA 7ma Edición.
2. **Fase 2 — Composición Docs-as-Code (Quarto / BibTeX):**
   * Redactar los contenidos en los archivos `.qmd` del módulo correspondiente y en `Entregas/`.
   * Registrar las fuentes en el archivo `referencias.bib` con metadatos completos (autor, año, título, editorial/revista, DOI/URL).
3. **Fase 3 — Control de Arquitectura y Análisis de Impacto (GitNexus):**
   * Antes de modificar el pipeline `compilar_todos.py` o scripts auxiliares:
     ```powershell
     node .gitnexus/run.cjs impact "<nombre_de_la_funcion>" --direction upstream --repo .
     ```
   * Validar que el cambio no afecte la compilación de entregas anteriores ya aprobadas.
4. **Fase 4 — Compilación Automatizada y Detección de Cambios (Python + GitNexus):**
   * Ejecutar la compilación del documento:
     ```powershell
     python compilar_todos.py
     ```
   * Verificar la estabilidad estructural mediante análisis de grafo:
     ```powershell
     node .gitnexus/run.cjs detect-changes --scope all --repo .
     ```
5. **Fase 5 — Retroalimentación Docente y Mejora Continua (NotebookLM):**
   * Las devoluciones del equipo docente (Dra. Deborah Noguera, Esp. Federico Abeiro, Esp. María Cecilia Aguirre) se ingresan a NotebookLM para orientar las correcciones conceptuales, cerrando el ciclo de mejora continua.

---

## 🛡️ 4. Guardarraíles de Coexistencia Obligatorios

* **Prohibición de invención en ambos planos:**
  * En lo académico: Jamás inventar citas, autores ni datos empíricos; validar siempre con NotebookLM.
  * En lo técnico: Jamás alterar funciones ni pipelines a ciegas; validar siempre el impacto con GitNexus.
* **Higiene del repositorio:** Pruebas y scripts experimentales deben guardarse en `pruebas/`, manteniendo limpia la raíz del proyecto.
