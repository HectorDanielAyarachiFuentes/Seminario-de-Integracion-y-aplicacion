import subprocess, docx, pymupdf
from pathlib import Path

grid_md = """
+------------------------------------+---------------------------------------------------------------+
| Título:                            | Componentes identificados en el artículo científico           |
+====================================+===============================================================+
| **Título del artículo**            | **El rol de la Inteligencia Artificial en los procesos de     |
|                                    | reclutamiento y selección en la Gestión del Talento Humano**  |
+------------------------------------+---------------------------------------------------------------+
| **Referencia APA 7**               | Gonzabay Quirumbay, I. A., & Pacheco Barzallo, S. K. (2024).  |
|                                    | *Reincisol*, 3(6), 3880–3902.                                 |
|                                    | https://www.reincisol.com/ojs/index.php/reincisol/article/view/396 |
+------------------------------------+---------------------------------------------------------------+
| **Objetivo general**               | **Objetivo general:** Explorar el rol de la IA...             |
|                                    |                                                               |
| **Objetivos específicos**          | **Objetivos específicos:**                                    |
|                                    | 1. Sistematizar los roles de la IA.                           |
|                                    | 2. Evaluar la eficacia percibida.                             |
|                                    | 3. Analizar el impacto organizacional.                        |
+------------------------------------+---------------------------------------------------------------+
"""

Path("pruebas/grid_table.md").write_text(grid_md, encoding="utf-8")

# Test to typst
res_typ = subprocess.run(["quarto", "pandoc", "pruebas/grid_table.md", "-t", "typst"], capture_output=True, text=True)
print("TYPST OUTPUT:")
print(res_typ.stdout[:800])

# Test to docx
subprocess.run(["quarto", "pandoc", "pruebas/grid_table.md", "-o", "pruebas/grid_table.docx"], check=True)
doc = docx.Document("pruebas/grid_table.docx")
for r in doc.tables[0].rows:
    print(f"Row: {repr(r.cells[0].text[:30])} | {repr(r.cells[1].text[:60])}")
