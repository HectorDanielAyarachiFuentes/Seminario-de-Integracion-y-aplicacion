from pathlib import Path

qmd_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Entregas\Actividad 4\quarto\tp4_proyecto_tfg_integral.qmd")
dest_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Seminario de Integración y Aplicación\4 - Metodología\Trabajo Práctico n° 4\tp4_proyecto_tfg_integral.qmd")

lines = qmd_path.read_text(encoding="utf-8").splitlines()

new_fases_lines = [
    "Las actividades de investigación se estructuran en seis fases secuenciales coordinadas a lo largo de un lapso intensivo y viable de 7 meses de ejecución:",
    "",
    "* **Fase 1: Preparación, diseño y avales (Mes 1 / Mayo 2026):** Aprobación del proyecto en el SIA; solicitud formal de aval académico ante la Dirección del Departamento y el Decanato del CURZAS; contacto informativo con ADUNC y Centro de Estudiantes; calibración de instrumentos y prueba piloto con 2 docentes y 5 estudiantes. *Entregable:* Aval institucional e instrumentos validados.",
    "* **Fase 2: Relevamiento normativo y entrevistas (Mes 2 / Junio 2026):** Sistematización documental de estatutos, ordenanzas y CCT; concreción de las 8 entrevistas semiestructuradas a docentes, autoridades y dirigentes gremiales; transcripción y codificación temática preliminar. *Entregable:* Fichas normativas y transcripciones codificadas.",
    "* **Fase 3: Aplicación del sondeo exploratorio (Mes 3 / Julio 2026):** Parametrización y lanzamiento del cuestionario digital a docentes y estudiantes de Viedma y Nodos Territoriales; seguimiento de participación; cierre y depuración de la base de datos. *Entregable:* Base de datos anonimizada y depurada.",
    "* **Fase 4: Procesamiento analítico y triangulación (Mes 4 / Agosto 2026):** Procesamiento descriptivo del sondeo y análisis de contenido temático de las entrevistas; contrastación cruzada de fuentes normativas, testimoniales y cuantitativas. *Entregable:* Informe diagnóstico integrado de factibilidad.",
    "* **Fase 5: Formulación de lineamientos y redacción (Meses 5–6 / Septiembre–Octubre 2026):** Elaboración de lineamientos orientativos para el Departamento; reunión de consulta y devolución con docentes; redacción integral del borrador de TFG. *Entregable:* Borrador completo de Tesina.",
    "* **Fase 6: Revisión final, tramitación y defensa oral (Mes 7 / Noviembre 2026):** Supervisión y visto bueno final de la Dirección de TFG; presentación formal ante mesa de entradas del CURZAS; designación de jurados y defensa oral del TFG. *Entregable:* Trabajo Final de Graduación aprobado."
]

new_crono_lines = [
    "El proyecto se planifica en un lapso de 7 meses continuos distribuidos en etapas mensuales articuladas con las seis fases de investigación:",
    "",
    "| Etapa / Actividad Metodológica | Mes 1 (May 26) | Mes 2 (Jun 26) | Mes 3 (Jul 26) | Mes 4 (Ago 26) | Mes 5 (Sep 26) | Mes 6 (Oct 26) | Mes 7 (Nov 26) |",
    "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    "| 1. Aprobación del Proyecto de TFG (SIA) | **X** | | | | | | |",
    "| 2. Gestión de avales y diseño de instrumentos (Fase 1) | **X** | | | | | | |",
    "| 3. Prueba piloto de instrumentos (Fase 1) | **X** | | | | | | |",
    "| 4. Trabajo de campo: normativa y entrevistas (Fase 2) | | **X** | | | | | |",
    "| 5. Trabajo de campo: sondeo en Viedma y Nodos (Fase 3) | | | **X** | | | | |",
    "| 6. Procesamiento de datos y triangulación (Fase 4) | | | | **X** | | | |",
    "| 7. Redacción de Tesina y lineamientos (Fase 5) | | | | | **X** | **X** | |",
    "| 8. Revisión final, tramitación y defensa de TFG (Fase 6) | | | | | | | **X** |",
    "",
    "*Nota.* Elaboración propia. La planificación mensual de 7 meses se adecua a la escala operativa de un investigador individual y a los plazos académicos reglamentados por el CURZAS-UNCo."
]

# Find indices for Fases
fases_start = None
fases_end = None
for i, line in enumerate(lines):
    if "Las actividades de investigación se estructuran en seis fases" in line:
        fases_start = i
    if fases_start is not None and "* **Fase 6:" in line:
        fases_end = i + 1
        break

print(f"Fases: {fases_start} to {fases_end}")

# Find indices for Cronograma
crono_start = None
crono_end = None
for i, line in enumerate(lines):
    if "El proyecto se planifica en un lapso de 18 meses" in line:
        crono_start = i
    if crono_start is not None and "*Nota.* Elaboración propia. La planificación contempla" in line:
        crono_end = i + 1
        break

print(f"Crono: {crono_start} to {crono_end}")

if fases_start is not None and crono_start is not None:
    # Replace crono first (it's later in file)
    lines[crono_start:crono_end] = new_crono_lines
    # Then replace fases
    lines[fases_start:fases_end] = new_fases_lines

    # Also update Anexo III date
    for i, line in enumerate(lines):
        if "Viedma, Río Negro, ______ de ________________ de 2025" in line:
            lines[i] = "Viedma, Río Negro, ______ de ________________ de 2026"

    new_text = "\n".join(lines) + "\n"
    qmd_path.write_text(new_text, encoding="utf-8")
    print(f"Successfully updated {qmd_path}")
    dest_path.write_text(new_text, encoding="utf-8")
    print(f"Successfully updated {dest_path}")
else:
    print("Could not locate blocks")
