import xml.etree.ElementTree as ET

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

print("Buscando capas y grupos en RioNegro.svg:")
for child in root:
    print(child.tag, child.attrib.get('id'))
    if child.attrib.get('id') in ['layer1', 'layer2']:
        for sub in child:
            print("  sub:", sub.tag, sub.attrib.get('id'), sub.attrib.get('d', '')[:40])

