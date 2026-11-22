with open('entregas/actividad_4/TP4_Ayarachi_Fuentes_COMPLETO.qmd', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('### Población y Muestra')
if idx != -1:
    print(text[idx:idx+2500])
