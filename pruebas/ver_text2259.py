import re

with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    s = f.read()

m = re.search(r'<text id="text2259".*?</text>', s, re.DOTALL)
if m:
    print(m.group(0))

