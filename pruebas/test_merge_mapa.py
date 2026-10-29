# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

# Read RioNegro.svg
with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    rio = f.read()

# Let's inspect the exact lines of layer1 and layer2 in RioNegro.svg
tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

# The red dots in layer2:
# In RioNegro.svg:
# <g id="layer2" transform="translate(112.92857,24.923532)">
#   <g id="g2564">
#     <path ... />
# ...

print("Root tags:", [c.attrib.get('id') for c in root])

