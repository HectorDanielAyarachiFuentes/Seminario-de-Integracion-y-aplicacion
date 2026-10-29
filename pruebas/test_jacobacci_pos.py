import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()
p2249 = None
for p in root.findall('.//{http://www.w3.org/2000/svg}path'):
    if p.get('id') == 'path2249':
        p2249 = p
        break

coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p2249.get('d'))
poly = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]

def point_in_poly(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# Test candidate positions for Jacobacci, Maquinchao, Los Menucos
print("Jacobacci (395, 945):", point_in_poly(395, 945, poly))
print("Jacobacci (410, 945):", point_in_poly(410, 945, poly))
print("Jacobacci (430, 950):", point_in_poly(430, 950, poly))
print("Maquinchao (548, 974):", point_in_poly(548, 974, poly))
print("Maquinchao (635, 940):", point_in_poly(635, 940, poly))
print("Los Menucos (750, 880):", point_in_poly(750, 880, poly))
print("Los Menucos (838, 884):", point_in_poly(838, 884, poly))
