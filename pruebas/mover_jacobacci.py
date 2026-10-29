with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Jacobacci transform and Maquinchao transform
# Old Jacobacci: translate(360, 925) -> translate(395, 945)
text = text.replace(
    '<g id="nodo_jacobacci" transform="translate(360, 925)" filter="url(#shadow)">',
    '<g id="nodo_jacobacci" transform="translate(395, 945)" filter="url(#shadow)">'
)

# Old Maquinchao: translate(480, 920) -> translate(495, 915)
text = text.replace(
    '<g id="nodo_maquinchao" transform="translate(480, 920)" filter="url(#shadow)">',
    '<g id="nodo_maquinchao" transform="translate(495, 915)" filter="url(#shadow)">'
)

# 2. Update route path
# Old route: M 1315,830 L 1080,780 L 910,770 L 770,760 L 610,830 L 480,920 L 360,925
# New route: M 1315,830 L 1080,780 L 910,770 L 770,760 L 610,830 L 495,915 L 395,945
text = text.replace(
    '<path d="M 1315,830 L 1080,780 L 910,770 L 770,760 L 610,830 L 480,920 L 360,925" />',
    '<path d="M 1315,830 L 1080,780 L 910,770 L 770,760 L 610,830 L 495,915 L 395,945" />'
)

with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SVG ACTUALIZADO CON INGENIERO JACOBACCI DENTRO DE 25 DE MAYO!")
