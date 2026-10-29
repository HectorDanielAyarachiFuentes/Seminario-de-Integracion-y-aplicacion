import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()

print("--- ALL CIRCLES IN RioNegro.svg ---")
for c in root.findall('.//{http://www.w3.org/2000/svg}circle'):
    cx = float(c.get('cx', 0))
    cy = float(c.get('cy', 0))
    r = float(c.get('r', 0))
    cid = c.get('id', '')
    print(f"circle {cid:12}: cx={cx:.1f}, cy={cy:.1f}, r={r:.1f}")

print("\n--- ALL PATHS IN LAYER2 (CABECERAS) ---")
layer2 = root.find('.//*[@id="layer2"]')
for p in layer2.findall('.//{http://www.w3.org/2000/svg}path'):
    pid = p.get('id', '')
    trans = p.get('transform', '')
    d = p.get('d', '')
    # Check if there is sodipodi:cx or translation
    cx = p.get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}cx')
    cy = p.get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}cy')
    m = re.search(r'translate\(([^,\)]+),?([^\)]*)\)', trans)
    tx, ty = (float(m.group(1)), float(m.group(2))) if m else (0, 0)
    print(f"path {pid:10}: trans=({tx:.1f}, {ty:.1f}), cx={cx}, cy={cy}")

print("\n--- VIEDMA SPECIFIC ELEMENTS ---")
# Search for anything with 'viedma' or gold color '#c89632' or similar
for elem in root.iter():
    style = elem.get('style', '')
    eid = elem.get('id', '')
    if 'viedma' in eid.lower() or '#d4aa00' in style or '#c89632' in style or '#d4a' in style:
        print(f"elem {elem.tag} id={eid}: attribs={elem.attrib}")

