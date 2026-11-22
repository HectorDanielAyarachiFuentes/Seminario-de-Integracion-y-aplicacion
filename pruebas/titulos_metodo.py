with open('entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('### Población, Muestra y Unidades de Análisis')
idx_end = text.find('### Técnicas e Instrumentos de Recolección de Datos')
print(text[idx:idx_end])
