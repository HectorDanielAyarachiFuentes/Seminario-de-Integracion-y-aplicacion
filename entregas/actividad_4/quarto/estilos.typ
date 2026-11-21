// estilos.typ — Configuración visual para PDF/Typst (Normas APA 7ma Edición / SIA CURZAS)
// Fuente única de estilo para mantener el documento Quarto limpio y desacoplado.

// ─── Párrafos con sangría reglamentaria APA 7 (1.27 cm) e interlineado ──
#set par(justify: true, leading: 0.75em, first-line-indent: 1.27cm)

// ─── Índice de Contenidos (TOC): Nivel 1 en negrita ─────────────────────
#show outline.entry.where(level: 1): set text(weight: "bold")

// ─── Encabezados APA 7ma Edición ─────────────────────────────────────────
// Nivel 1: Centrado, Negrita
#show heading.where(level: 1): it => block(spacing: 14pt)[
  #set align(center)
  #text(weight: "bold", size: 12pt)[#it.body]
] + par[]

// Nivel 2: Alineado a la izquierda, Negrita
#show heading.where(level: 2): it => block(spacing: 12pt)[
  #set align(left)
  #text(weight: "bold", size: 12pt)[#it.body]
] + par[]

// Nivel 3: Alineado a la izquierda, Negrita y Cursiva
#show heading.where(level: 3): it => block(spacing: 10pt)[
  #set align(left)
  #text(weight: "bold", style: "italic", size: 12pt)[#it.body]
] + par[]

// Nivel 4: Alineado a la izquierda, Negrita (11pt)
#show heading.where(level: 4): it => block(spacing: 8pt)[
  #set align(left)
  #text(weight: "bold", size: 11pt)[#it.body]
] + par[]

// ─── Citas en bloque APA 7 (sangría izquierda 1.27 cm, sin comillas) ─────
#show quote: it => block(inset: (left: 1.27cm), spacing: 10pt)[
  #set par(justify: true, first-line-indent: 0pt, leading: 0.75em)
  #it.body
]

// ─── Tablas estilo APA 7 (triple línea horizontal, sin bordes verticales) ─
#show table: it => {
  set text(size: 8pt)
  block(width: 100%, breakable: true)[
    #line(length: 100%, stroke: 1pt + black)
    #v(-7.5pt)
    #it
    #v(-7.5pt)
    #line(length: 100%, stroke: 1pt + black)
  ]
}
#set table(
  stroke: (x, y) => none,
  inset: (x: 2.5pt, y: 1.8pt)
)
#show table.cell: set par(first-line-indent: 0pt, leading: 0.45em, justify: false)
#show table.cell.where(y: 0): set text(weight: "bold")

// ─── Figuras y Epígrafes APA 7 ──────────────────────────────────────────
#show figure: it => block(spacing: 10pt)[#it]
#show figure.caption: it => {
  set text(size: 9.5pt)
  set par(first-line-indent: 0pt, leading: 0.5em)
  it
}

// ─── Bibliografía APA 7 ────────────────────────────────────────────────
#set bibliography(title: [Referencias Bibliográficas], style: "apa")

// ─── Sangría Francesa (Hanging Indent 1.27 cm) para Pandoc Citeproc ─────
#show <refs>: it => block[
  #set par(first-line-indent: -1.27cm, hanging-indent: 1.27cm)
  #it
]
