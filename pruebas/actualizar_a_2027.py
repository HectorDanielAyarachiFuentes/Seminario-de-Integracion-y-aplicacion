from pathlib import Path

qmd_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Entregas\Actividad 4\quarto\tp4_proyecto_tfg_integral.qmd")
dest_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Seminario de Integración y Aplicación\4 - Metodología\Trabajo Práctico n° 4\tp4_proyecto_tfg_integral.qmd")

text = qmd_path.read_text(encoding="utf-8")

# Cover pages
text = text.replace("Año 2026", "Año 2027")

# Titles and questions (2025–2026 -> 2026–2027)
text = text.replace("(2025–2026)", "(2026–2027)")
text = text.replace("período 2025–2026", "período 2026–2027")
text = text.replace("bienio 2025–2026", "período 2026–2027")

# Fases lines (2026 -> 2027)
text = text.replace("(Mes 1 / Mayo 2026)", "(Mes 1 / Mayo 2027)")
text = text.replace("(Mes 2 / Junio 2026)", "(Mes 2 / Junio 2027)")
text = text.replace("(Mes 3 / Julio 2026)", "(Mes 3 / Julio 2027)")
text = text.replace("(Mes 4 / Agosto 2026)", "(Mes 4 / Agosto 2027)")
text = text.replace("(Meses 5–6 / Septiembre–Octubre 2026)", "(Meses 5–6 / Septiembre–Octubre 2027)")
text = text.replace("(Mes 7 / Noviembre 2026)", "(Mes 7 / Noviembre 2027)")
text = text.replace("7 meses de ejecución:", "7 meses de ejecución durante el año 2027:")

# Table header (26 -> 27)
text = text.replace("| Mes 1 (May 26) | Mes 2 (Jun 26) | Mes 3 (Jul 26) | Mes 4 (Ago 26) | Mes 5 (Sep 26) | Mes 6 (Oct 26) | Mes 7 (Nov 26) |",
                    "| Mes 1 (May 27) | Mes 2 (Jun 27) | Mes 3 (Jul 27) | Mes 4 (Ago 27) | Mes 5 (Sep 27) | Mes 6 (Oct 27) | Mes 7 (Nov 27) |")

text = text.replace("seis fases de investigación:", "seis fases de investigación durante el año 2027:")
text = text.replace("La planificación mensual de 7 meses se adecua", "La planificación mensual de 7 meses durante 2027 se adecua")

# Delimitación temporal
text = text.replace("Bienio 2025–2026, período lectivo que enmarca", "Período lectivo 2026–2027, enmarcando el cursado y la ejecución del trabajo de campo en 2027")

# Anexo III
text = text.replace("de 2026", "de 2027")
text = text.replace("(SIA 2025/2026)", "(SIA 2026/2027)")

qmd_path.write_text(text, encoding="utf-8")
print(f"Updated {qmd_path}")

dest_path.write_text(text, encoding="utf-8")
print(f"Updated {dest_path}")
