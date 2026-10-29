import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()
group = root.find('.//*[@id="poligonos_departamentos"]')

# Let's inspect path2256 (El Cuy) and path2249 (the green polygon)
for p in group:
    pid = p.get('id')
    fill = p.get('style', '')
    coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p.get('d'))
    xs = [float(c[0]) + 112.93 for c in coords]
    ys = [float(c[1]) + 24.92 for c in coords]
    print(f"{pid}: fill={fill[:30]}, X=[{min(xs):.1f}, {max(xs):.1f}], Y=[{min(ys):.1f}, {max(ys):.1f}], Center=({sum(xs)/len(xs):.1f}, {sum(ys)/len(ys):.1f})")

