with open('entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('**5. Gobernanza Multinivel**')
print("Index:", idx)
if idx != -1:
    print(text[idx:idx+800])
