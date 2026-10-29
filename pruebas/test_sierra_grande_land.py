import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()
p = None
for elem in root.findall('.//{http://www.w3.org/2000/svg}path'):
    if elem.get('id') == 'path2204':
        p = elem
        break

coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p.attrib['d'])
pts = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]

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

# Test candidate positions for Sierra Grande
for x in [1240, 1250, 1260, 1270, 1280, 1290, 1300]:
    for y in [1060, 1070, 1080]:
        print(f"Sierra Grande ({x}, {y}): {point_in_poly(x, y, pts)}")

# Test candidate positions for SAO
for x in [1310, 1320, 1330, 1340, 1350, 1360]:
    for y in [820, 830, 840, 850]:
        print(f"SAO ({x}, {y}): {point_in_poly(x, y, pts)}")
