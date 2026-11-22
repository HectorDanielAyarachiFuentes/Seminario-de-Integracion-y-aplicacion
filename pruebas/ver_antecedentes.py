with open('entregas/actividad_4/quarto/secciones/_03_marco_teorico_y_antecedentes.qmd', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'garciadefanelli' in l.lower() or 'marquina' in l.lower():
        start = max(0, i-5)
        end = min(len(lines), i+15)
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
        break
