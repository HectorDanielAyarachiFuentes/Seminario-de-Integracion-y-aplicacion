with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace 25 de Mayo and El Cuy coordinates
text = text.replace('<text x="550" y="720">25 de Mayo</text>', '<text x="560" y="1030">25 de Mayo</text>')
text = text.replace('<text x="590" y="530">El Cuy</text>', '<text x="600" y="520">El Cuy</text>')

with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SVG ACTUALIZADO CON 25 DE MAYO ADENTRO DEL POLÍGONO VERDE!")

