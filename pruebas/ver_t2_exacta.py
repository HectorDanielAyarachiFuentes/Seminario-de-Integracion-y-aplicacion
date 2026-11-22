with open('entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\*\*Tabla 2\*\*.*?(?=\n###|\n## 4\.5|\Z)', text, re.DOTALL)
if m:
    print("MATCH FOUND:")
    print(m.group(0)[:500])
    print("...")
    print(m.group(0)[-300:])
else:
    print("NO MATCH")
