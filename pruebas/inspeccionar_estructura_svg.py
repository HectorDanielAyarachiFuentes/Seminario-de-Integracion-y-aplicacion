# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('Entregas/Actividad 4/quarto/assets/red_territorial.svg')
root = tree.getroot()

print("Etiquetas en la raíz:")
for child in root:
    print(child.tag, child.attrib.get('id', ''))

