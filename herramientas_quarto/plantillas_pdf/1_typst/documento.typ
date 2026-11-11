#set page(paper: "a4", margin: (x: 2cm, y: 2.5cm), numbering: "1 / 1")
#set text(font: "Segoe UI", size: 10.5pt, fill: rgb("202020"))

#align(center)[
  #text(size: 18pt, weight: "bold", fill: rgb("192d5f"))[Universidad Nacional del Comahue] \
  #text(size: 12pt, fill: rgb("c89632"))[CURZAS - Planeamiento y Control de las Organizaciones]
]

#v(0.8em)
#line(length: 100%, stroke: 1.2pt + rgb("192d5f"))
#v(1em)

= Avance 1: Contexto, Modelo de Gestión y Gobernanza (Plantilla Typst)
El *CURZAS* es una unidad académica dependiente de la UNCo con sede en Viedma, regida bajo los principios de autonomía y autarquía universitaria.

#v(0.5em)
#rect(
  width: 100%,
  fill: rgb("f5f8fa"),
  stroke: (left: 3.5pt + rgb("192d5f")),
  inset: 10pt,
  radius: 2pt
)[
  *Misión Institucional:* Generación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte.
]

#v(1em)
== Matriz de Rendición de Cuentas (Accountability)

#table(
  columns: (1.2fr, 2.5fr, 1.8fr),
  fill: (col, row) => if row == 0 { rgb("192d5f") } else if calc.even(row) { rgb("f5f8fa") } else { white },
  stroke: 0.5pt + rgb("d0e0f0"),
  inset: 7pt,
  [#text(fill: white, weight: "bold")[Tipo de Accountability]], 
  [#text(fill: white, weight: "bold")[Mecanismos Vigentes]], 
  [#text(fill: white, weight: "bold")[Evidencia Normativa]],
  
  [*Horizontal* \ (Intra-estatales)], 
  [- Auditoría Interna UNCo \ - AGN y SIGEN \ - Control Consejo Directivo], 
  [- Informes de auditoría \ - Ley 24.156 \ - Memoria Anual],
  
  [*Vertical* \ (Representativo)], 
  [- Elecciones periódicas directas \ - Cogobierno cuatro claustros], 
  [- Estatuto General UNCo \ - Calendario electoral],
  
  [*Social* \ (Ciudadanía)], 
  [- Publicación de presupuestos y nóminas web \ - Solicitudes AIP], 
  [- Portal Transparencia Activa \ - Ley 27.275]
)
