import xml.etree.ElementTree as ET

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

header = root.find('.//*[@id="clean_header"]')
if header is not None:
    print("=== clean_header ===")
    for elem in header.iter():
        print(elem.tag, elem.attrib, ''.join(elem.itertext()).strip())

ocean = root.find('.//*[@id="ocean_labels"]')
if ocean is not None:
    print("=== ocean_labels ===")
    for elem in ocean.iter():
        print(elem.tag, elem.attrib, ''.join(elem.itertext()).strip())

