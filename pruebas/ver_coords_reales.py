import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

# In layer1, all coordinates get +112.93 to X, +24.92 to Y
# In layer2, all coordinates have NO transform on layer2!

print("CABECERAS IN LAYER 2 (Global SVG coordinates):")
cabeceras = {
    'Gral Roca': (763.21 + 76.43, 266.36 + 135.00),
    'Choele Choel': (763.21 + 443.93, 266.36 + 203.93),
    'Río Colorado': (763.21 + 743.93, 266.36 + 145.36),
    'Gral Conesa': (763.21 + 662.50, 266.36 + 406.07),
    'Viedma': (763.21 + 920.36, 266.36 + 591.07),
    'San Antonio Oeste': (763.21 + 567.50, 266.36 + 553.21),
    'Valcheta': (763.21 + 345.36, 266.36 + 540.36),
    'Sierra Colorada': (763.21 + 51.07, 266.36 + 511.07),
    'Maquinchao': (763.21 - 127.50, 266.36 + 673.93),
    'Bariloche': (763.21 - 603.21, 266.36 + 665.36),
    'Pilcaniyeu': (763.21 - 496.07, 266.36 + 656.07),
    'Ñorquinco': (763.21 - 519.64, 266.36 + 830.36),
    'El Cuy': (763.21 - 59.64, 266.36 + 356.07),
}

for name, (gx, gy) in cabeceras.items():
    print(f"  {name:20}: ({gx:.1f}, {gy:.1f})")

