
#set page(paper: "a4", margin: 2.54cm)
#set par(justify: true, first-line-indent: 1.27cm)

#show heading.where(level: 3): it => block(spacing: 10pt)[
  #set align(left)
  #text(weight: "bold", style: "italic", size: 12pt)[#it.body]
] + text(size: 0pt)[#box()]

=== Problematización y Construcción

Construir un problema científico exige desnaturalizar las rutinas cotidianas.
