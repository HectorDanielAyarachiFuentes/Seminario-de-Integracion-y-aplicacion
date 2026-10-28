import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

group = root.find('.//*[@id="poligonos_departamentos"]')
for p in group:
    d = p.get('d', '')
    coords = re.findall(r'([-\d\.]+),([-\d\.]+)', d)
    if coords:
        xs = [float(c[0]) + 112.93 for c in coords]
        ys = [float(c[1]) + 24.92 for c in coords]
        pid = p.get('id')
        print(f"{pid}: X=[{min(xs):.0f}, {max(xs):.0f}], Y=[{min(ys):.0f}, {max(ys):.0f}], Center=({(min(xs)+max(xs))/2:.0f}, {(min(ys)+max(ys))/2:.0f})")

