# 🤖 Reglas de Comportamiento del Agente (Agent Rules)

Este archivo define la estructura, estándares y pautas operativas obligatorias para cualquier IA o asistente que trabaje en este repositorio de **Trabajo Final de Graduación (TFG) / Tesina**.

---

## 🏛️ 1. Contexto Académico e Institucional

* **Institución:** Universidad Nacional del Comahue (UNCo) — Centro Universitario Regional Zona Atlántica y Sur (CURZAS).
* **Departamento:** Departamento de Administración Pública.
* **Carreras:**
  * Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos.
  * Licenciatura en Administración Pública.
* **Materia:** **Seminario de Integración y Aplicación (SIA)** (Año Académico 2025 / 2026).
* **Equipo Docente:**
  * **Profesora Responsable:** Dra. Deborah Noguera
  * **Ayudantes de Cátedra:** Esp. Federico Abeiro y Esp. María Cecilia Aguirre
* **Autor / Estudiante:** **Tec. Sup. Héctor Daniel Ayarachi Fuentes** (Legajo N° 8252 — DNI N° 35.492.138).
* **Línea de Investigación:** Inteligencia Artificial y Gestión Humana en las Organizaciones (*IA - Humano - TESINA*).
* **Marco Normativo:** Resolución CD-CURZAS N° 266/23 (Estructura formal del TFG) y Res. 26/23, 28/24.
* **Enfoque Técnico:** *Docs-as-Code* académico con **Quarto (`.qmd`)** como autoría central y renderizado dual (Word y PDF).

---

## 📂 2. Arquitectura del Repositorio y Mapeo de Fases

```text
IA - Humano - TESINA/
├── .agents/                                 # Reglas, skills y configuración del agente
│   └── rules/                               # AGENTS.md, gitnexus.md, notebooklm.md, supreme_guidelines.md, git_commits.md
├── assets/img/CURZAS.png                    # Logotipo oficial CURZAS para carátulas
├── Entregas/                                # Entregas finales (.qmd, .docx, .pdf por actividad)
├── compilar_todos.py                        # Pipeline automatizado de compilación dual
├── Seminario de Integración y Aplicación/   # Módulos académicos 1 a 4 y recursos oficiales
└── pruebas/                                 # Entorno aislado para pruebas técnicas y scripts temporales
```

---

## 📋 3. Estructura Progresiva de los Trabajos Prácticos (TPs)

| Actividad | Ubicación de Trabajo | Contenido Requerido | Extensión |
| :--- | :--- | :--- | :--- |
| **TP N° 1** | `Seminario de Integración y Aplicación/1 - Introducción/` | Análisis crítico de 2 artículos científicos disciplinares. Cuadro comparativo con 11 variables metodológicas y carátula institucional. | 4 a 6 págs. |
| **TP N° 2** | `Seminario de Integración y Aplicación/2 - El problema/` | **Parte 1 del TFG:** Carátula oficial, delimitación del tema (área, contexto, período, personas/organización), objeto problema, justificación y objetivos (general y específicos). | ~5 págs. |
| **TP N° 3** | `Seminario de Integración y Aplicación/3 - Estado de la cuestión.../` | **Parte 2 acumulativa:** Integra TP2 + Marco Teórico (posicionamiento teórico y conceptos centrales) + Antecedentes (estado del arte). | Hasta 15 págs. |
| **TP N° 4** | `Seminario de Integración y Aplicación/4 - Metodología/` | **Proyecto Integral (Res. 266/23):** Integra Partes 1 y 2 + Estrategia Metodológica + Cronograma + Viabilidad + Bibliografía completa APA 7. | ~25 págs. |

---

## 🛠️ 4. Ecosistema Tecnológico: Quarto y Pipeline de Compilación

El proyecto utiliza **Quarto (`.qmd`)** como fuente única de verdad. Desde cada `.qmd`, `compilar_todos.py` post-procesa y genera automáticamente ambas salidas en `Entregas/`:
1. **Versión Word (`.docx`):** Para revisiones de cátedra, sugerencias y control de cambios.
2. **Versión PDF (`.pdf`):** Para presentación formal e impresión institucional APA 7.

### Comandos de Compilación:
* **Compilar entrega activa a Word y PDF:** `python compilar_todos.py`
* **Compilar únicamente PDF:** `python compilar_todos.py --pdf`
* **Compilar únicamente Word:** `python compilar_todos.py --word`
* **Modo Vigilante (compilación en vivo al guardar):** `python compilar_todos.py --watch`

---

## 📐 5. Estándar de Formato, Carátula y Normas APA 7ma Edición

Todos los documentos deben cumplir estrictamente el estándar (ampliado en [.agents/rules/supreme_guidelines.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/supreme_guidelines.md)):

1. **Márgenes y Tipografía:** 2,54 cm (1 pulgada) en los 4 bordes. Fuente: *Segoe UI*, *Times New Roman* o *Arial* (10-11 pt), interlineado 1.5 a 2.0. Sangría de primera línea: 1,27 cm.
2. **Tablas APA 7:** Sin líneas verticales ni cuadrícula enrejada. Solo 3 líneas horizontales: borde superior (1pt), divisor de encabezado (0.5-0.75pt) y borde inferior (1pt).
3. **Referencias Bibliográficas:** Orden alfabético, sangría francesa (*hanging indent*) de 1,27 cm y enlaces DOI/URL activos.
4. **Reglas de Oro de Portada y Paginación:**
   * La carátula ocupa **exactamente 1 página** con el logotipo de CURZAS (`assets/img/CURZAS.png`) centrado (sin rótulo de figura).
   * **La portada jamás muestra número de página visible.**
   * **El cuerpo del trabajo (página siguiente) inicia visiblemente en el número 1.**
   * El Índice de Contenidos se ubica en su propia hoja tras la portada y antes de la introducción.
   * No anteponer números manuales a encabezados (usar `# Título` en vez de `# 1. Título`) para evitar duplicación con `number-sections: true`.

---

## 🧠 6. Lecciones Técnicas Aprendidas (Memoria Operativa)

1. **Logo Centrado en Quarto:** Usar bloque limpio `::: {align="center"}` con `![](assets/img/CURZAS.png){width=135px}` para evitar rótulos de figura automáticos de Pandoc.
2. **Paginación Word vs PDF:** En Word, `compilar_todos.py` activa `different_first_page_header_footer = True`, campo `{PAGE}` y `w:start="0"`. En PDF, la primera página queda desprovista de pie de página y las siguientes se enumeran desde 1.
3. **Tablas OpenXML en Word:** `compilar_todos.py` limpia bordes internos (`w:insideH="none"`, `w:insideV="none"`) e inyecta la línea inferior al encabezado automáticamente.

---

## 🧭 7. Ecosistema de Inteligencia Dual: GitNexus + NotebookLM

El proyecto opera bajo un modelo de colaboración simbiótica:

```text
┌───────────────────────────────────────┬─────────────────────────────────────────┐
│    🧠 NOTEBOOKLM (Cerebro Académico)  │     🕸️ GITNEXUS (Cerebro Técnico)       │
├───────────────────────────────────────┼─────────────────────────────────────────┤
│ • Rigor conceptual y epistemológico   │ • Integridad de código y arquitectura   │
│ • Bibliografía de cátedra (SIA 1-4)   │ • Pipeline Docs-as-Code (compilar_todos)│
│ • Resoluciones UNCo (Res. 266/23)     │ • Grafo de dependencias y llamadas      │
│ • Consignas de TPs y devoluciones     │ • Análisis de impacto (blast radius)    │
│ ➔ GOBIERNA EL CONTENIDO Y EL FONDO    │ ➔ GOBIERNA LA FORMA Y LA INFRAESTRUCTURA│
└───────────────────────────────────────┴─────────────────────────────────────────┘
```

### Protocolo Operativo y Guardarraíles:
* **Antes de editar código (`compilar_todos.py` o scripts):** Ejecutar análisis de impacto con `node .gitnexus/run.cjs impact "<simbolo>" --direction upstream --repo .`. Nunca editar a ciegas ni omitir riesgos HIGH/CRITICAL.
* **Antes de hacer commit:** Validar con `node .gitnexus/run.cjs detect-changes --scope all --repo .`.
* **Consultas Académicas:** Validar siempre marcos conceptuales y citas con NotebookLM. Prohibido inventar citas o fuentes.

---

## 🧹 8. Higiene del Repositorio y Commits

1. **Higiene de Raíz:** No dejar borradores en la raíz. Toda prueba va en `pruebas/`.
2. **Entregables:** Cada actividad debe compilarse en `Entregas/Actividad X/` con sus 3 archivos (`.qmd`, `.docx`, `.pdf`).
3. **Commits en Español:** Seguir *Conventional Commits* en español (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`). Ver [.agents/rules/git_commits.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/git_commits.md).

---

## 📚 9. Mapeo de Reglas Específicas del Proyecto

Para consultar las reglas especializadas cargadas en el entorno:
* **Código y Arquitectura:** [.agents/rules/gitnexus.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/gitnexus.md)
* **Investigación y MCP:** [.agents/rules/notebooklm.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/notebooklm.md)
* **Estilo Visual y APA 7:** [.agents/rules/supreme_guidelines.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/supreme_guidelines.md)
* **Convención de Commits:** [.agents/rules/git_commits.md](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/.agents/rules/git_commits.md)
