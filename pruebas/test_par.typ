
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
