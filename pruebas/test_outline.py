import subprocess
from pathlib import Path
import pymupdf

test_typ = """
#set page(paper: "a4", margin: 2.54cm)
#set text(font: "Segoe UI", size: 10pt)

// Caratula
#align(center)[
  #v(2cm)
  #text(size: 16pt, weight: "bold")[TRABAJO PRACTICO N 1]
]
#pagebreak()

// Indice
#outline(title: [Indice de Contenidos], indent: 1.5em)
#pagebreak()

// Cuerpo
= Introduccion y Objetivos
Texto de introduccion...
= Matriz Metodologica
Texto de matriz...
"""

Path("pruebas").mkdir(exist_ok=True)
Path("pruebas/test.typ").write_text(test_typ, encoding="utf-8")
subprocess.run(["quarto", "typst", "compile", "pruebas/test.typ", "pruebas/test.pdf"], check=True)

doc = pymupdf.open("pruebas/test.pdf")
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    print(f"--- Page {i} ---")
    print(page.get_text())
