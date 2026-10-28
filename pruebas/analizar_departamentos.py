import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

# The group capa_departamentos has transform="translate(112.92857, 24.923532)"
# Let's find each path inside poligonos_departamentos
group = root.find('.//*[@id=\"poligonos_departamentos\"]')
for p in group:
    d = p.get('d', '')
    coords = re.findall(r'([-\d\.]+),([-\d\.]+)', d)
    if coords:
        xs = [float(c[0]) + 112.93 for c in coords]
        ys = [float(c[1]) + 24.92 for c in coords]
        print(f"Path id={p.get('id')}: X=[{min(xs):.1f}, {max(xs):.1f}], Y=[{min(ys):.1f}, {max(ys):.1f}], Centroid=({sum(xs)/len(xs):.1f}, {sum(ys)/len(ys):.1f})")
