with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re

l1 = re.search(r'(<g[^>]*id="layer1"[^>]*>.*?</g>\s*</g>)', text, re.DOTALL)
l2 = re.search(r'(<g[^>]*id="layer2"[^>]*>.*?</g>\s*</g>)', text, re.DOTALL)

print("Found l1:", bool(l1))
print("Found l2:", bool(l2))

if l1:
    with open('pruebas/layer1_raw.xml', 'w', encoding='utf-8') as f_out:
        f_out.write(l1.group(1))
if l2:
    with open('pruebas/layer2_raw.xml', 'w', encoding='utf-8') as f_out:
        f_out.write(l2.group(1))

