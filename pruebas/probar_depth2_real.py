import shutil
import subprocess
import fitz
import os

# Backup _01
shutil.copy('entregas/actividad_4/quarto/secciones/_01_caratula_e_indice.qmd', 'pruebas/_01_backup.qmd')

with open('entregas/actividad_4/quarto/secciones/_01_caratula_e_indice.qmd', 'r', encoding='utf-8') as f:
    t = f.read()

# Reemplazar con depth 2 y 11pt
t_test = t.replace(
    '#show outline.entry: set text(size: 8.5pt)\n#show outline.entry: set block(spacing: 0.45em)\n#show outline.entry.where(level: 1): set text(weight: "bold")\n#outline(title: [Índice de Contenidos], indent: 1.2em, depth: 3)',
    '#show outline.entry: set text(size: 11pt)\n#show outline.entry: set block(spacing: 0.75em)\n#show outline.entry.where(level: 1): set text(weight: "bold")\n#outline(title: [Índice de Contenidos], indent: 1.5em, depth: 2)'
)

with open('entregas/actividad_4/quarto/secciones/_01_caratula_e_indice.qmd', 'w', encoding='utf-8') as f:
    f.write(t_test)

print("Compilando con Quarto...")
subprocess.run("quarto render entregas/actividad_4/quarto/tp4_proyecto_tfg_integral.qmd --to typst", shell=True, capture_output=True)

# Restaurar backup
shutil.copy('pruebas/_01_backup.qmd', 'entregas/actividad_4/quarto/secciones/_01_caratula_e_indice.qmd')

test_pdf = 'entregas/actividad_4/quarto/tp4_proyecto_tfg_integral.pdf'
if os.path.exists(test_pdf):
    doc = fitz.open(test_pdf)
    print(f"Total páginas en test PDF: {doc.page_count}")
    # Renderizar página 2
    page2 = doc.load_page(1)
    pix = page2.get_pixmap(dpi=150)
    pix.save('pruebas/indice_depth2_11pt.png')
    print("Guardado pruebas/indice_depth2_11pt.png!")
