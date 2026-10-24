from pathlib import Path

qmd_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Entregas\Actividad 4\quarto\tp4_proyecto_tfg_integral.qmd")
dest_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Seminario de Integración y Aplicación\4 - Metodología\Trabajo Práctico n° 4\tp4_proyecto_tfg_integral.qmd")

text = qmd_path.read_text(encoding="utf-8")

# Cover pages back to Año 2026
text = text.replace("Año 2027", "Año 2026")

# Titles, questions and objectives back to 2025–2026
text = text.replace("(2026–2027)", "(2025–2026)")
text = text.replace("período 2026–2027", "período 2025–2026")
text = text.replace("Período lectivo 2026–2027, enmarcando el cursado y la ejecución del trabajo de campo en 2027 la formulación",
                    "Bienio 2025–2026, período lectivo que enmarca la formulación")
text = text.replace("Período lectivo 2026–2027, enmarcando el cursado y la ejecución del trabajo de campo en 2027",
                    "Bienio 2025–2026, período lectivo que enmarca la formulación del TFG")
text = text.replace("delimitado temporalmente al período 2026–2027", "delimitado temporalmente al bienio 2025–2026")

# Anexo III dates back to 2026 and SIA 2025/2026
text = text.replace("Viedma, Río Negro, ______ de ________________ de 2027", "Viedma, Río Negro, ______ de ________________ de 2026")
text = text.replace("(SIA 2026/2027)", "(SIA 2025/2026)")

# Fases text precision: explicitly note that the 7-month plan is projected for 2027
text = text.replace("un lapso intensivo y viable de 7 meses de ejecución durante el año 2027:",
                    "un lapso intensivo y viable de 7 meses de ejecución proyectados para el año 2027:")
text = text.replace("seis fases de investigación durante el año 2027:",
                    "seis fases de investigación para su desarrollo durante el año 2027:")
text = text.replace("La planificación mensual de 7 meses durante 2027 se adecua",
                    "La planificación mensual de 7 meses proyectada para el año 2027 se adecua")

qmd_path.write_text(text, encoding="utf-8")
print(f"Updated {qmd_path}")

dest_path.write_text(text, encoding="utf-8")
print(f"Updated {dest_path}")
