import re

svg_path = "entregas/actividad_4/quarto/assets/red_territorial.svg"
with open(svg_path, "r", encoding="utf-8") as f:
    svg = f.read()

svg = svg.replace('style="stroke="#0284c7;', 'style="stroke:#0284c7;')

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)
print("Corregido el error de comillas en SVG!")
