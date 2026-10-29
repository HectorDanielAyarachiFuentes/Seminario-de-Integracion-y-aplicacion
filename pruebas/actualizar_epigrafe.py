path = 'Entregas/Actividad 4/quarto/tp4_proyecto_tfg_integral.qmd'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

target = '![*Red Territorial de Nodos Universitarios del CURZAS-UNCo (Resolución CD-CURZA N° 196/2022).*](assets/red_territorial.svg){width=92%}'
replacement = '![*Red Territorial de Nodos Universitarios del CURZAS-UNCo (Resolución CD-CURZA N° 196/2022). Elaboración propia.*](assets/red_territorial.svg){width=92%}'

if target in text:
    text = text.replace(target, replacement)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("EPIGRAFE ACTUALIZADO CON 'ELABORACIÓN PROPIA'!")
else:
    print("NO SE ENCONTRÓ EL TEXTO TARGET")

