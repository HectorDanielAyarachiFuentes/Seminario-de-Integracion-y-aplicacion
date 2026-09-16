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
  * **Profesora Responsable de Cátedra:** Dra. Deborah Noguera
  * **Ayudantes de Cátedra:** Esp. Federico Abeiro y Esp. María Cecilia Aguirre
* **Autor / Estudiante:** **Tec. Sup. Héctor Daniel Ayarachi Fuentes** (Técnico Superior en Recursos Humanos — DNI N° 35.492.138 — Legajo N° 8252)
* **Línea de Investigación del TFG:** Inteligencia Artificial y Gestión Humana en las Organizaciones (*IA - Humano - TESINA*).
* **Marco Normativo:** Resolución CD-CURZAS N° 266/23 (Estructura formal del Proyecto de TFG) y resoluciones asociadas (Res. 26/23, 28/24).
* **Enfoque Técnico:** *Docs-as-Code* académico con soporte dual de composición y renderizado: **Typst (`.typ`)** y **Quarto (`.qmd`)**.

---

## 📂 2. Arquitectura del Repositorio y Mapeo de Fases

```text
IA - Humano - TESINA/
├── .agents/                                 # Configuración, reglas y skills del agente
│   ├── rules/
│   │   ├── AGENTS.md                        # Estándar operativo, académico y técnico (este archivo)
│   │   ├── notebooklm.md                    # Pautas para uso del servidor MCP NotebookLM
│   │   └── supreme_guidelines.md            # Pautas de estilo visual y composición APA 7
│   ├── skills/                              # Skills instaladas (ej. using-notebooklm-mcp)
│   └── mcp_config.json                      # Configuración de servidores MCP
├── assets/                                  # Recursos gráficos e imágenes del proyecto
│   └── img/                                 # Logotipos institucionales (CURZAS.png)
├── Entregas/                                # Repositorio central de versiones finales (.pdf / .docx)
├── IA-HERRAMIENTAS-QUANTO-TYPS/             # Banco de herramientas, plantillas y entornos
│   ├── plantillas_pdf/                      # Motores (1_typst, 2_playwright_html, etc.)
│   ├── herramientas/notebooklm/             # Utilidades para NotebookLM MCP
│   └── pruebas/                             # Entorno de pruebas y validaciones
└── Seminario de Integración y Aplicación/   # Módulos académicos y recursos oficiales
    ├── 1 - Introducción/                    # Módulo 1: Introducción a la Investigación
    │   ├── Bibliografía - Introducción/
    │   ├── Bibliografía Metodológica General/
    │   ├── Líneas Temáticas de Investigación/
    │   ├── Presentación de Clase 1/
    │   └── Trabajo Práctico 1/
    ├── 2 - El problema/                     # Módulo 2: Selección del Tema y Formulación
    │   ├── Bibliografía - Formulación del Problema/
    │   ├── Bibliografía - Objetivos/
    │   ├── EJEMPLOS de Esquema 1° (LAP - RRHH)/
    │   ├── Material - Selección del tema/
    │   └── Trabajo Práctico n° 2/
    ├── 3 - Estado de la cuestión y marco teórico/ # Módulo 3: Marco Teórico y Antecedentes
    │   ├── Bibliografía - Estado del Arte/
    │   ├── Bibliografía - Marco Teórico/
    │   ├── Ejemplo Marco de Referencia (AP-RRHH)/
    │   ├── MOTORES de Búsqueda de Información/
    │   └── Trabajo Práctico n° 3/
    ├── 4 - Metodología/                     # Módulo 4: Estrategia Metodológica Integral
    │   ├── Bibliografia - Metodologia/
    │   └── Trabajo Práctico n° 4/
    └── Recursos TFG/                        # Normativa, resoluciones y guías oficiales de cátedra
        ├── Modelo de Carátula SIA 2025.docx
        ├── Estructura de Proyecto de TFG.pdf
        └── Normas de estilo que deberán usar en el proyecto/
```

---

## 📋 3. Estructura Progresiva de los Trabajos Prácticos (TPs)

Toda asistencia pedagógica y técnica debe responder a las pautas de cada módulo:

| Actividad | Ubicación | Contenido Requerido | Extensión Sugerida |
| :--- | :--- | :--- | :--- |
| **TP N° 1** | `Seminario de Integración y Aplicación/1 - Introducción/Trabajo Práctico 1/` | Selección y análisis crítico de **dos (2) artículos científicos** disciplinares. Cuadro comparativo con 11 variables metodológicas (Tema, Problema, Objetivos, Metodología, Muestra, Resultados, etc.) con carátula institucional. | 4 a 6 páginas |
| **TP N° 2** | `Seminario de Integración y Aplicación/2 - El problema/Trabajo Práctico n° 2/` | **Primera parte del Proyecto de TFG**: 1. Carátula oficial, 2. Tema de investigación (área disciplinar, contexto, período, personas/organización), 3. Delimitación del objeto problema (justificación y relevancia), 4. Definición de objetivos (General y Específicos). | ~5 páginas |
| **TP N° 3** | `Seminario de Integración y Aplicación/3 - Estado de la cuestión y marco teórico/Trabajo Práctico n° 3/` | **Segunda parte acumulativa**: Integra TP N° 2 + 5. Marco Teórico (posicionamiento teórico y conceptos centrales) + 6. Antecedentes (estado del arte). | Hasta 15 páginas (acumulado con TP2) |
| **TP N° 4** | `Seminario de Integración y Aplicación/4 - Metodología/Trabajo Práctico n° 4/` | **Proyecto de TFG Integral (Res. 266/23)**: Integra Primera parte (1-4) + Segunda parte (5-6) + Tercera parte: 7. Metodología/Técnicas, 8. Cronograma de actividades, 9. Viabilidad (recursos y autorizaciones), 10. Bibliografía completa APA 7. | 25 páginas (sin anexos) |

---

## 🛠️ 4. Ecosistema Tecnológico Unificado: Quarto (`.qmd`)

El proyecto adopta **Quarto (`.qmd`)** como motor único y central de autoría académica. A partir de un único código fuente en Quarto, el sistema genera automáticamente las dos versiones requeridas en la carpeta `Entregas/`:

### 1. Salidas Automatizadas desde Quarto:
* **Versión Word (`.docx`):** Para revisiones docentes, correcciones compartidas, sugerencias y control de cambios.
* **Versión PDF (`.pdf`):** Para presentación formal, visualización instantánea e impresión institucional con márgenes APA 7 (2,54 cm).

### 2. Pipeline de Compilación Automática
* **Compilar TP activo a Word y PDF:**
  ```powershell
  python compilar_todos.py
  ```
* **Compilar solo versión PDF:**
  ```powershell
  python compilar_todos.py --pdf
  ```
* **Compilar solo versión Word (.docx):**
  ```powershell
  python compilar_todos.py --word
  ```
* **Modo Vigilante (recompilación en vivo al guardar):**
  ```powershell
  python compilar_todos.py --watch
  ```

---

## 📐 5. Estándar de Formato y Normas APA 7ma Edición

Todos los documentos generados deben acatar rigurosamente las pautas de estilo de la cátedra y las **Normas APA 7ma Edición**:

1. **Configuración de Página y Márgenes:**
   * Tamaño: Papel Carta (*Letter*) o A4.
   * Márgenes: **2,54 cm (1 pulgada)** en los cuatro márgenes (superior, inferior, izquierdo y derecho).
2. **Tipografía y Legibilidad:**
   * Tipografías admitidas: *Segoe UI* (9.5pt a 10pt), *Times New Roman* (12pt) o *Arial* (11pt).
   * Interlineado: 1.5 a 2.0 (doble espacio según entrega), alineación a la izquierda (o justificado elegante según pauta del docente con sangría de primera línea de 1,27 cm).
3. **Pautas de Citación APA 7:**
   * **Citas narrativas:** Apellido del autor seguido del año entre paréntesis, ej.: *Según Oszlak (2020), la modernización...*
   * **Citas parentéticas:** Autor y año entre paréntesis al final de la idea, ej.: *(Chiavenato, 2019).*
   * **Citas textuales de menos de 40 palabras:** Insertadas dentro del párrafo entre comillas dobles, finalizando con autor, año y página: `"...texto citado..." (García, 2021, p. 45).`
   * **Citas textuales de más de 40 palabras:** En bloque independiente, sin comillas, con sangría izquierda completa de **1,27 cm (0,5 pulg)** y tamaño de fuente o espaciado diferenciado.
   * **Verbos de citación:** Emplear conectores académicos adecuados (*sostiene, argumenta, expone, señala, enfatiza, concluye*).
4. **Referencias Bibliográficas (Apartado Final):**
   * Orden estrictamente alfabético por apellido del primer autor.
   * Formato de **sangría francesa** (*hanging indent*) de 1,27 cm en todas las líneas posteriores a la primera.
   * Inclusión obligatoria de hipervínculos activos a DOI o URLs académicas estables.

---

## 🎓 6. Estándar de Portada Académica (Normas APA 7ma Edición - Student Title Page)

Basado en las pautas oficiales de **Normas APA 7ma Edición** para trabajos académicos de grado y adaptado a las especificaciones de CURZAS:

* **Estructura y Jerarquía en una Sola Página:**
  1. **Logotipo Institucional:** Emblema oficial de CURZAS (`assets/img/CURZAS.png`) centrado en la cabecera en alta definición (sin leyendas ni texto de "Figura").
  2. **Título del Trabajo:** En negrita con subtítulo explicativo de la línea temática del TFG.
  3. **Autor / Estudiante:**
     * `**Alumno:**`
     * `Técnico Superior en Gestión de Recursos Humanos Héctor Daniel Ayarachi Fuentes`
     * `Legajo N° 8252`
  4. **Afiliación Institucional:**
     * Departamento de Administración Pública
     * Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos *(o Lic. en Administración Pública)*
     * Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)
     * Universidad Nacional del Comahue
  5. **Asignatura y Equipo Docente:**
     * `SIA: Seminario de Integración y Aplicación`
     * `Dra. Deborah Noguera (Docente Responsable de Cátedra)`
     * `Esp. Federico Abeiro y Esp. María Cecilia Aguirre (Ayudantes de Cátedra)`
  6. **Año y Ubicación:**
     * `Año Académico 2026`
     * `Viedma, Río Negro — República Argentina`
* **Reglas de Formato y Paginación:**
  * Sin líneas horizontales decorativas (`---`), ni tablas ni rótulos de figuras en el logo.
  * Ocupa exactamente una página aislada antes del inicio del cuerpo principal (`{{< pagebreak >}}`).
  * **La carátula NO lleva número de página visible.**
  * **La hoja siguiente (inicio del desarrollo del TP) comienza su numeración visible desde el número 1.**

---

## 🧹 7. Higiene del Repositorio y Control de Calidad

1. **Prohibido ensuciar la raíz:** No almacenar borradores, scripts desechables o archivos de depuración en la raíz. Toda prueba va en `pruebas/` o `IA-HERRAMIENTAS-QUANTO-TYPS/pruebas/`.
2. **Entregables:** Toda versión final lista para presentación debe compilarse en `Entregas/` dentro de su carpeta respectiva (ej. `Entregas/Actividad 1/`).
3. **Consistencia de Rutas:** Emplear rutas relativas seguras referenciando `assets/img/CURZAS.png`.

---

## 🏷️ 8. Mensajes de Confirmación (Git Commits)

* **Idioma Obligatorio:** Todos los mensajes de commit generados o propuestos deben redactarse exclusivamente en **español**.
* **Formato:** *Conventional Commits*:
  * `feat:` para nuevas secciones del TFG, actividades o plantillas.
  * `fix:` para correcciones de estilo, citas APA 7 o errores de maquetación.
  * `docs:` para actualizaciones de bibliografía, marcos teóricos o consignas.
  * `refactor:` para reestructuración de código Quarto o Typst.
  * `chore:` para tareas de mantenimiento, limpieza o actualización de reglas.

---

## 🧠 9. Lecciones Aprendidas y Soluciones Técnicas (Memoria Operativa)

Para garantizar consistencia en todos los Trabajos Prácticos y en el Trabajo Final de Graduación:

1. **Centrado del Logotipo Institucional en Quarto puro:**
   * La sintaxis estándar para que Quarto no agregue rótulos no deseados (como *"Figura 1"*) es colocar la imagen en bloque centrado limpio:
     ```markdown
     ::: {align="center"}
     ![](../../assets/img/CURZAS.png){width=135px}
     :::
     ```
   * En Word (`.docx`), Pandoc no aplica por defecto la propiedad `center` al objeto de dibujo del logo. El compilador automatizado (`compilar_todos.py`) asegura la alineación centrada del párrafo que contiene la imagen en Word.
   * En PDF, el compilador garantiza que el logo quede centrado en las coordenadas exactas de la página.

2. **Numeración de Páginas (Regla Académica Estricta):**
   * **En la Carátula (Página 1):** La portada jamás debe mostrar número de página visible.
   * **En el Contenido (Página 2 en adelante):** El conteo visible de páginas debe iniciar en **`1`** al comenzar la Introducción.
   * **En Word (`.docx`):** Requiere activar `different_first_page_header_footer = True`, insertar el campo de numeración dinámica `{PAGE}` centrado en el pie de página, y establecer el inicio de sección en `w:start="0"`.
   * **En PDF (`.pdf`):** La página 1 queda limpia sin número en pie y las páginas siguientes se reenumeran correlativamente desde `1`.

3. **Estructura de Entregas:**
   * Cada actividad se organiza en una subcarpeta limpia dentro de `Entregas/` (ej. `Entregas/Actividad 1/`) conteniendo:
     * El código fuente Quarto (`.qmd`).
     * El archivo Word editable para revisión (`.docx`).
     * El archivo PDF listo para presentación (`.pdf`).

4. **Tablas Estilo APA 7ma Edición:**
   * Prohibición absoluta de líneas verticales y cuadrícula enrejada.
   * Únicamente tres líneas horizontales principales: borde superior de la tabla (1pt), borde divisor del encabezado (0.5pt a 0.75pt) y borde inferior de la tabla (1pt).
   * En Typst se implementa en `include-before-body` con stroke selectivo y encabezado en negrita.
   * En Word (`.docx`), el compilador configura `w:tblBorders` con `w:insideH="none"`, `w:insideV="none"`, y aplica `w:tcBorders` inferior a la fila 0.

5. **Referencias Bibliográficas con Sangría Francesa (*Hanging Indent*):**
   * Sangría obligatoria de 1,27 cm (0.5 pulg / 36 pt / 1.5em) en todas las líneas siguientes a la primera.
   * En Typst: ````{=typst} #set par(hanging-indent: 1.5em, justify: false) ```` precediendo a `# Referencias Bibliográficas {.unnumbered}`.
   * En Word: `compilar_todos.py` aplica automáticamente `left_indent = Inches(0.5)` y `first_line_indent = Inches(-0.5)`.

6. **Índice de Contenidos Dinámico y Sin Duplicación de Títulos:**
   * No anteponer números manuales en encabezados Markdown (ej. escribir `# Introducción...` en vez de `# 1. Introducción...`) para evitar la duplicación generada por `number-sections: true`.
   * El Índice de Contenidos se ubica en su propia hoja (Página 2) inmediatamente posterior a la carátula y previa a la Introducción, sincronizando dinámicamente los números exactos de página.


