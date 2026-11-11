// estilos.typ — Configuración visual para PDF/Typst (APA 7 / SIA CURZAS)
// Extraído del YAML include-before-body para mantener el QMD limpio.

// ─── Párrafos ───────────────────────────────────────────────────────────
#set par(justify: true, leading: 0.75em)

// ─── Encabezados ────────────────────────────────────────────────────────
#show heading.where(level: 1): it => block(spacing: 14pt)[
  #set align(center)
  #text(weight: "bold", size: 12pt)[#it.body]
]
#show heading.where(level: 2): it => block(spacing: 12pt)[
  #set align(left)
  #text(weight: "bold", size: 12pt)[#it.body]
]
#show heading.where(level: 3): it => block(spacing: 10pt)[
  #set align(left)
  #text(weight: "bold", style: "italic", size: 12pt)[#it.body]
]

// ─── Tablas estilo APA 7 (solo bordes horizontales) ─────────────────────
#set table(
  stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.5pt + black) } else if y == 5 { (bottom: 1pt + black) } else { none },
  inset: 5pt
)
#show table: set text(size: 9.5pt)
#show table.cell: set par(first-line-indent: 0pt, leading: 0.5em)
#show table.cell.where(y: 0): set text(weight: "bold")

// ─── Figuras ────────────────────────────────────────────────────────────
#show figure: it => block(spacing: 10pt)[#it]
#show figure.caption: set text(size: 9.5pt, style: "italic")
#show figure.caption: set par(first-line-indent: 0pt)
