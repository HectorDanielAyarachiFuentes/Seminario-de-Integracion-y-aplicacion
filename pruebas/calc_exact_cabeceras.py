import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

layer2 = root.find('.//*[@id="layer2"]')
paths = layer2.findall('.//{http://www.w3.org/2000/svg}path')

# Names corresponding to the 13 paths in order:
names = [
    "General Roca",
    "Choele Choel",
    "Río Colorado",
    "General Conesa",
    "Viedma",
    "San Antonio Oeste",
    "Valcheta",
    "Sierra Colorada",
    "Maquinchao",
    "Bariloche",
    "Pilcaniyeu",
    "Ñorquinco",
    "El Cuy"
]

for i, p in enumerate(paths):
    trans = p.attrib.get('transform', '')
    m = re.search(r'translate\(([^,\)]+),?([^\)]*)\)', trans)
    if m:
        tx = float(m.group(1))
        ty = float(m.group(2))
        gx = 763.21 + tx + 112.93
        gy = 266.36 + ty + 24.92
        print(f"{names[i]:25}: Global ({gx:.1f}, {gy:.1f}) | path={p.attrib.get('id')}")

