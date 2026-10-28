# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

for elem in root.iter():
    if elem.tag.endswith('text'):
        full_text = ' '.join(''.join(elem.itertext()).split())
        tid = elem.attrib.get('id', '')
        x = elem.attrib.get('x', '')
        y = elem.attrib.get('y', '')
        print(f"[{tid}] ({x}, {y}): {full_text}")

