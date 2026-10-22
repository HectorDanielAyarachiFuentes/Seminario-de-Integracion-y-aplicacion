import subprocess
import fitz

test_typ = """
#set page(paper: "a4", margin: 2.54cm)
#set par(justify: true, first-line-indent: 1.27cm)

#show heading.where(level: 1): it => block(spacing: 14pt)[
  #set align(center)
  #text(weight: "bold", size: 12pt)[#it.body]
] + par[]

#show heading.where(level: 2): it => block(spacing: 12pt)[
  #set align(left)
  #text(weight: "bold", size: 12pt)[#it.body]
] + par[]

#show heading.where(level: 3): it => block(spacing: 10pt)[
  #set align(left)
  #text(weight: "bold", style: "italic", size: 12pt)[#it.body]
] + par[]

== Delimitación del Objeto Problema
<delimitación-del-objeto-problema>
En este apartado se problematiza la evaluación...

=== Problematización y Construcción del Objeto de Estudio
<problematización-y-construcción-del-objeto-de-estudio>
Construir un problema científico exige desnaturalizar las rutinas cotidianas...
"""

with open("pruebas/test_par.typ", "w", encoding="utf-8") as f:
    f.write(test_typ)

subprocess.run(["quarto", "typst", "compile", "pruebas/test_par.typ", "pruebas/test_par.pdf"], capture_output=True)
doc = fitz.open("pruebas/test_par.pdf")
words = doc[0].get_text("words")
for w in words:
    if w[4] in ["En", "Construir"]:
        print(f"{w[4]} x0 = {w[0]:.2f}")
