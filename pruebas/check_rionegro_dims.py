import xml.etree.ElementTree as ET

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

print("viewBox:", root.attrib.get('viewBox'))
print("width:", root.attrib.get('width'))
print("height:", root.attrib.get('height'))

