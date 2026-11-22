with open('entregas/actividad_4/quarto/apa.csl', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'edition' in line.lower():
        print(line.strip())
