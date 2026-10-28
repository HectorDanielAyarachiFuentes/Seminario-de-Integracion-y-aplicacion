import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

group = root.find('.//*[@id="poligonos_departamentos"]')
p2204 = group.find('.//*[@id="path2204"]')
d = p2204.get('d')
coords = re.findall(r'([-\d\.]+),([-\d\.]+)', d)
for c in coords:
    x = float(c[0]) + 112.93
    y = float(c[1]) + 24.92
    print(f"({x:.1f}, {y:.1f})")
