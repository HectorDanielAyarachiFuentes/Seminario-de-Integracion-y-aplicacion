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
#counter(page).update(1)
#outline(title: [Indice de Contenidos], indent: 1.5em)
#pagebreak()

// Cuerpo
= Introduccion y Objetivos
Texto de introduccion...
"""

Path("pruebas/test_counter.typ").write_text(test_typ, encoding="utf-8")
subprocess.run(["quarto", "typst", "compile", "pruebas/test_counter.typ", "pruebas/test_counter.pdf"], check=True)

doc = pymupdf.open("pruebas/test_counter.pdf")
print("Total pages:", len(doc))
for i, page in enumerate(doc):
    print(f"--- Page {i} ---")
    print("Content:\n", page.get_text())
    print("Blocks at bottom:", [b[4].strip() for b in page.get_text("blocks") if b[1] > page.rect.height * 0.85])
