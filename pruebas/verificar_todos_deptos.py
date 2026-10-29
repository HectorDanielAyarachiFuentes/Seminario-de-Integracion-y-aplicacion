import xml.etree.ElementTree as ET
import re

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()
group = root.find('.//*[@id="poligonos_departamentos"]')

polys = {}
for p in group:
    pid = p.get('id')
    coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p.get('d'))
    pts = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]
    polys[pid] = pts

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

deptos = [
    ("Gral. Roca", "path2278", (730, 270)),
    ("Avellaneda", "path2290", (965, 530)),
    ("Pichi Mahuida", "path2300", (1360, 520)),
    ("El Cuy", "path2256", (600, 520)),
    ("9 de Julio", "path2220", (840, 670)),
    ("Conesa", "path2191", (1450, 710)),
    ("Valcheta", "path2216", (1060, 660)),
    ("San Antonio", "path2204", (1190, 940)),
    ("Adolfo Alsina", "path2205", (1500, 760)),
    ("25 de Mayo", "path2249", (560, 1030)),
    ("Pilcaniyeu", "path2289", (250, 800)),
    ("Bariloche", "path2275", (70, 1030)),
    ("Ñorquinco", "path2263", (220, 1070)),
]

for name, pid, (x, y) in deptos:
    inside = point_in_poly(x, y, polys[pid])
    print(f"{name:15} in {pid:10} at ({x}, {y}): {inside}")
