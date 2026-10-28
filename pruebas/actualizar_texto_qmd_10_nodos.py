path = 'Entregas/Actividad 4/quarto/tp4_proyecto_tfg_integral.qmd'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Exact replacement for the 10 nodes list
old_list = "Los Menucos, Sierra Colorada, Valcheta, Ramos Mexía, San Antonio Oeste, General Conesa, Lamarque, Maquinchao, Comallo y Sierra Grande"
new_list = "Valcheta, Ramos Mexía, Sierra Colorada, Los Menucos, Maquinchao, Ingeniero Jacobacci, San Antonio Oeste / Las Grutas, Sierra Grande, General Conesa y Río Colorado"

count = text.count(old_list)
print(f"Occurrences found: {count}")

if count > 0:
    text = text.replace(old_list, new_list)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("TEXTO DEL QMD ACTUALIZADO EXITOSAMENTE!")
else:
    print("NO SE ENCONTRÓ LA LISTA ANTIGUA EXACTA")

