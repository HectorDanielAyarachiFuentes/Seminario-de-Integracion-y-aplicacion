import xml.etree.ElementTree as ET

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

layer1 = root.find('.//*[@id="layer1"]')
layer2 = root.find('.//*[@id="layer2"]')

print("=== LAYER 1 (Textos) ===")
for elem in layer1.iter():
    if elem.tag.endswith('text'):
        tid = elem.attrib.get('id', '')
        x = elem.attrib.get('x', '')
        y = elem.attrib.get('y', '')
        style = elem.attrib.get('style', '')
        txt = ''.join(elem.itertext()).strip()
        print(f"ID={tid}, pos=({x},{y}), style={style[:40]} -> {txt}")

print("\n=== LAYER 2 (Puntos Cabeceras) ===")
for elem in layer2.iter():
    if elem.tag.endswith('path'):
        pid = elem.attrib.get('id', '')
        transform = elem.attrib.get('transform', '')
        d = elem.attrib.get('d', '')
        print(f"PID={pid}, transform={transform}, d={d[:30]}")

