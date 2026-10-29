import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()
group = root.find('.//*[@id="poligonos_departamentos"]')

p2256 = [p for p in group if p.get('id') == 'path2256'][0]
coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p2256.get('d'))
pts2256 = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]

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

print("Check point (550, 720) in path2256 (El Cuy):", point_in_poly(550, 720, pts2256))

p2249 = [p for p in group if p.get('id') == 'path2249'][0]
coords249 = re.findall(r'([-\d\.]+),([-\d\.]+)', p2249.get('d'))
pts2249 = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords249]

print("Check point (550, 720) in path2249 (Green):", point_in_poly(550, 720, pts2249))

# Find the best center in path2249 (green) for 25 de Mayo:
for x in range(400, 700, 20):
    for y in range(850, 1100, 20):
        if point_in_poly(x, y, pts2249):
            # check distance to nodes (Jacobacci 395, 945), (Maquinchao 495, 915), (Los Menucos 610, 830)
            d_j = ((x-395)**2 + (y-945)**2)**0.5
            d_m = ((x-495)**2 + (y-915)**2)**0.5
            d_lm = ((x-610)**2 + (y-830)**2)**0.5
            min_d = min(d_j, d_m, d_lm)
            if min_d > 100:
                print(f"Good spot inside 25 de Mayo: ({x}, {y}), min distance to nodes: {min_d:.1f}")
