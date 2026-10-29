import xml.etree.ElementTree as ET

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

layer2 = root.find('.//*[@id="layer2"]')
print("Layer2 hijos:", len(layer2))
for elem in layer2.iter():
    if elem.tag.endswith('path'):
        print(elem.attrib.get('id'), elem.attrib.get('d', '')[:40], elem.attrib.get('transform', ''))

layer1 = root.find('.//*[@id="layer1"]')
print("Layer1 text hijos:")
for elem in layer1.iter():
    if elem.tag.endswith('text'):
        text = ' '.join(''.join(elem.itertext()).split())
        print(elem.attrib.get('id'), elem.attrib.get('x'), elem.attrib.get('y'), text)

