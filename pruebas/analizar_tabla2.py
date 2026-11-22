import re

with open('entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\*\*Tabla 2\*\*.*?(?=\*\*Tabla 3|\n## 4\.5|\Z)', text, re.DOTALL)
if m:
    print(m.group(0))
