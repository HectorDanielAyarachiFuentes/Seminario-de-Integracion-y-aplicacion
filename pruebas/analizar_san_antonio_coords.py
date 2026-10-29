import xml.etree.ElementTree as ET
import re

tree = ET.parse('Presentacion/assets/RioNegro.svg')
root = tree.getroot()
p = None
for elem in root.findall('.//{http://www.w3.org/2000/svg}path'):
    if elem.get('id') == 'path2204':
        p = elem
        break

coords = re.findall(r'([-\d\.]+),([-\d\.]+)', p.attrib['d'])
pts = [(float(c[0]) + 112.93, float(c[1]) + 24.92) for c in coords]
xs = [pt[0] for pt in pts]
ys = [pt[1] for pt in pts]
print(f'San Antonio Dept (path2204): x in [{min(xs):.1f}, {max(xs):.1f}], y in [{min(ys):.1f}, {max(ys):.1f}]')

# Look at points in San Antonio along the south (y around 1050-1120)
south_pts = [pt for pt in pts if pt[1] > 1000]
print(f'South boundary points (y > 1000):')
for pt in south_pts:
    print(f'  ({pt[0]:.1f}, {pt[1]:.1f})')

# Look at points around SAO (y around 800-880)
sao_pts = [pt for pt in pts if 750 < pt[1] < 900 and pt[0] > 1150]
print(f'Coastline near SAO:')
for pt in sao_pts:
    print(f'  ({pt[0]:.1f}, {pt[1]:.1f})')
