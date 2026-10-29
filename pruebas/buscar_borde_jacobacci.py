import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

group = root.find('.//*[@id="poligonos_departamentos"]')
p2249 = None
for p in group:
    if p.get('id') == 'path2249':
        p2249 = p
        break

coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p2249.get('d'))
points = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]

print("Puntos del contorno de 25 de Mayo:")
for x, y in sorted(points, key=lambda pt: pt[1]):
    if 850 <= y <= 1000 and x < 500:
        print(f"({x:.1f}, {y:.1f})")
