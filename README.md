# 🏛️ Seminario de Integración y Aplicación (SIA) — CURZAS (UNCo)
### Proyecto de Trabajo Final de Graduación (TFG) / Tesina

Repositorio académico e institucional para el desarrollo progresivo del **Trabajo Final de Graduación (TFG)** en el marco del **Seminario de Integración y Aplicación (SIA)** del **Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)** — **Universidad Nacional del Comahue (UNCo)**.

---

## 👤 Información Académica del Proyecto

* **Institución:** Universidad Nacional del Comahue (UNCo) — CURZAS
* **Departamento:** Departamento de Administración Pública
* **Carreras:**
  * Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos
  * Licenciatura en Administración Pública
* **Asignatura:** Seminario de Integración y Aplicación (SIA) — Ciclo Lectivo 2025 / 2026
* **Cátedra:**
  * **Profesora Responsable:** Dra. Deborah Noguera
  * **Ayudantes de Cátedra:** Esp. Federico Abeiro y Esp. María Cecilia Aguirre
* **Autor / Estudiante:** **Héctor Daniel Ayarachi Fuentes**
* **Línea de Investigación:** *Inteligencia Artificial y Gestión Humana en las Organizaciones*
* **Normativa Aplicable:** Resolución CD-CURZAS N° 266/23 (Estructura de Proyecto de TFG de hasta 25 páginas)
* **Estándar de Citación:** **Normas APA 7ma Edición** (American Psychological Association)
* **Metodología Técnica:** *Docs-as-Code* académico con soporte dual **Quarto (`.qmd`)** y **Typst (`.typ`)**

---

## 📂 Arquitectura General del Repositorio

El proyecto se encuentra modularizado en consonancia directa con las etapas pedagógicas de la cátedra:

```text
IA - Humano - TESINA/
├── .agents/                                 # Configuración, reglas y directrices de IA
│   └── rules/
│       ├── AGENTS.md                        # Reglas operativas y estándares del proyecto
│       ├── supreme_guidelines.md            # Directrices de estilo APA 7 y diseño CURZAS
│       └── notebooklm.md                    # Parámetros para uso de NotebookLM MCP
├── assets/                                  # Recursos gráficos e identidad visual
│   └── img/                                 # Logotipo oficial (CURZAS.png)
├── Entregas/                                # Carpeta unificada para PDFs y Word finales consolidados
├── IA-HERRAMIENTAS-QUANTO-TYPS/             # Ecosistema técnico y utilidades de automatización
│   ├── plantillas_pdf/                      # Motores y plantillas (1_typst, 2_playwright, etc.)
│   ├── herramientas/notebooklm/             # Scripts y documentación de NotebookLM
│   └── pruebas/                             # Entorno de pruebas y validaciones técnicas
└── Seminario de Integración y Aplicación/   # Módulos académicos y recursos oficiales
    ├── 1 - Introducción/                    # Fase 1: Introducción a la Investigación
    │   ├── Bibliografía - Introducción/
    │   ├── Bibliografía Metodológica General/
    │   ├── Líneas Temáticas de Investigación/
    │   ├── Presentación de Clase 1/
    │   └── Trabajo Práctico 1/
    ├── 2 - El problema/                     # Fase 2: Delimitación del Problema
    │   ├── Bibliografía - Formulación del Problema/
    │   ├── Bibliografía - Objetivos/
    │   ├── EJEMPLOS de Esquema 1° (LAP - RRHH)/
    │   ├── Material - Selección del tema/
    │   └── Trabajo Práctico n° 2/
    ├── 3 - Estado de la cuestión y marco teórico/ # Fase 3: Antecedentes y Marco Conceptual
    │   ├── Bibliografía - Estado del Arte/
    │   ├── Bibliografía - Marco Teórico/
    │   ├── Ejemplo Marco de Referencia (AP-RRHH)/
    │   ├── MOTORES de Búsqueda de Información/
    │   └── Trabajo Práctico n° 3/
    ├── 4 - Metodología/                     # Fase 4: Diseño Metodológico y Proyecto Integral
    │   ├── Bibliografia - Metodologia/
    │   └── Trabajo Práctico n° 4/
    └── Recursos TFG/                        # Normativa institucional, resoluciones y estilo
        ├── Modelo de Carátula SIA 2025.docx
        ├── Estructura de Proyecto de TFG.pdf
        └── Normas de estilo que deberán usar en el proyecto/
```

---

## 📋 Mapa de Trabajos Prácticos (SIA 2025/2026)

| Módulo / TP | Carpeta | Consigna Central | Salidas / Entregables |
| :--- | :--- | :--- | :--- |
| **TP N° 1** | `Seminario de Integración y Aplicación/1 - Introducción/Trabajo Práctico 1/` | Análisis crítico de dos (2) artículos científicos disciplinares y completado de matriz comparativa (Tipo de estudio, Problema, Objetivos, Metodología, Muestra, Resultados) con carátula oficial. | `tp1_analisis_articulos.typ` / `.qmd` |
| **TP N° 2** | `Seminario de Integración y Aplicación/2 - El problema/Trabajo Práctico n° 2/` | **Primera parte del TFG**: Carátula oficial, delimitación del Tema, formulación y justificación del Problema de investigación, y Objetivos (General y Específicos). Extensión: ~5 páginas. | `tp2_diseno_problema.typ` / `.qmd` |
| **TP N° 3** | `Seminario de Integración y Aplicación/3 - Estado de la cuestión y marco teórico/Trabajo Práctico n° 3/` | **Segunda parte acumulativa**: Integra TP N° 2 + Marco Teórico (posicionamiento y conceptos clave) + Antecedentes (Estado del arte). Extensión: hasta 15 páginas. | `tp3_marco_teorico_antecedentes.typ` / `.qmd` |
| **TP N° 4** | `Seminario de Integración y Aplicación/4 - Metodología/Trabajo Práctico n° 4/` | **Proyecto de TFG Integral (Res. 266/23)**: Proyecto completo de hasta 25 páginas incorporando Metodología, Cronograma, Viabilidad y Referencias APA 7. | `tp4_proyecto_tfg_integral.typ` / `.qmd` |

---

## 🚀 Flujo de Compilación Unificado: Quarto (`.qmd`) a Word y PDF

El proyecto utiliza **Quarto (`.qmd`)** como único código fuente, generando de forma automática y simultánea las versiones en **Word (`.docx`)** y **PDF (`.pdf`)** en la carpeta `Entregas/`:

```powershell
# 1. Compilar el TP activo a PDF y Word (.docx) simultáneamente
python compilar_todos.py

# 2. Compilar SOLO versión PDF
python compilar_todos.py --pdf

# 3. Compilar SOLO versión Word (.docx)
python compilar_todos.py --word

# 4. Modo Vigilante (recompila automáticamente en segundo plano al guardar)
python compilar_todos.py --watch
```

### Compilación Manual con Quarto CLI:

```powershell
# Generar Word (.docx)
quarto render "Seminario de Integración y Aplicación/1 - Introducción/Trabajo Práctico 1/tp1_analisis_articulos.qmd" --to docx

# Generar PDF (.pdf)
quarto render "Seminario de Integración y Aplicación/1 - Introducción/Trabajo Práctico 1/tp1_analisis_articulos.qmd" --to typst
```

---

## 🎓 Pautas de Estilo y Normas APA 7ma Edición

* **Márgenes:** 2,54 cm en todos los márgenes.
* **Carátula Institucional:** Respetando la estructura de `Seminario de Integración y Aplicación/Recursos TFG/Modelo de Carátula SIA 2025.docx` con el logotipo oficial de CURZAS (`assets/img/CURZAS.png`).
* **Citas en el texto:**
  * Menos de 40 palabras: Entrecomillado dentro del flujo del texto.
  * Más de 40 palabras: Bloque sangrado independiente a 1,27 cm (0,5 pulg), sin comillas.
* **Bibliografía:** Con sangría francesa (*hanging indent*) de 1,27 cm, ordenada alfabéticamente y con enlaces directos a DOI/URL.
