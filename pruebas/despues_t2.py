with open('entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('**Tabla 2 (Continuación)**')
if idx != -1:
    print(text[idx+500:idx+1500])
