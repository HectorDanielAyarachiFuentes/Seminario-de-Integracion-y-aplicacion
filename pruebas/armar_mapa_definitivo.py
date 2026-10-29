import xml.etree.ElementTree as ET
import re

# Read RioNegro.svg
with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    rio_text = f.read()

# Extract layer1 and layer2 from RioNegro.svg
tree_rio = ET.parse('Presentacion/assets/RioNegro.svg')
root_rio = tree_rio.getroot()

# In RioNegro.svg, layer1 has the department paths and the texts!
# Let's extract the department paths and texts
l1 = root_rio.find('.//*[@id="layer1"]')
l2 = root_rio.find('.//*[@id="layer2"]')

# Let's write a generator that builds red_territorial.svg perfectly
script = """# -*- coding: utf-8 -*-
with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    rio = f.read()

# Replace department text colors to black (#000000)
rio_black = rio.replace('fill:#0f2d59', 'fill:#000000')

print('RioNegro ready')
"""
print("Extractor ready")

