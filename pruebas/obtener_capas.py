with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# find layer1
l1_start = text.find('<g\n     inkscape:label="Capa 1"')
if l1_start == -1:
    l1_start = text.find('id="layer1"')
    l1_start = text.rfind('<g', 0, l1_start)

# find layer2
l2_start = text.find('id="layer2"')
l2_start = text.rfind('<g', 0, l2_start)

print("l1_start:", l1_start)
print("l2_start:", l2_start)

