from pathlib import Path

qmd_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Entregas\Actividad 4\quarto\tp4_proyecto_tfg_integral.qmd")
dest_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Seminario de Integración y Aplicación\4 - Metodología\Trabajo Práctico n° 4\tp4_proyecto_tfg_integral.qmd")

text = qmd_path.read_text(encoding="utf-8")

# Ensure cover has Año 2026
if "Año 2026" not in text:
    text = text.replace("Año 2027", "Año 2026")

# Titles of the thesis project -> (2027)
text = text.replace("CURZAS-UNCo (2025–2026)", "CURZAS-UNCo (2027)")
text = text.replace("CURZAS-UNCo (2026–2027)", "CURZAS-UNCo (2027)")

# Questions and objectives
text = text.replace("durante el período 2025–2026?", "durante el año 2027?")
text = text.replace("durante el período 2026–2027?", "durante el año 2027?")

# Delimitación temporal
old_delim = "* **Delimitación Temporal:** Bienio 2025–2026, período lectivo que enmarca la formulación del TFG bajo la vigencia del nuevo Estatuto UNCo (Ord. CS N° 0988/2025)."
new_delim = "* **Delimitación Temporal:** Ciclo lectivo 2027 (mayo a noviembre de 2027), período en el que se llevará a cabo el trabajo de campo empírico, la recolección y análisis de datos y la redacción final del TFG, bajo la plena vigencia del nuevo Estatuto UNCo (Ord. CS N° 0988/2025)."
text = text.replace(old_delim, new_delim)

# Diseño metodológico
text = text.replace("delimitado temporalmente al bienio 2025–2026.", "delimitado temporalmente al ciclo lectivo 2027.")
text = text.replace("delimitado temporalmente al período 2025–2026.", "delimitado temporalmente al ciclo lectivo 2027.")

# Note in Anexo III
text = text.replace("Viedma, Río Negro, ______ de ________________ de 2025", "Viedma, Río Negro, ______ de ________________ de 202__")
text = text.replace("Viedma, Río Negro, ______ de ________________ de 2026", "Viedma, Río Negro, ______ de ________________ de 202__")
text = text.replace("Viedma, Río Negro, ______ de ________________ de 2027", "Viedma, Río Negro, ______ de ________________ de 202__")

qmd_path.write_text(text, encoding="utf-8")
print(f"Updated {qmd_path}")

dest_path.write_text(text, encoding="utf-8")
print(f"Updated {dest_path}")
