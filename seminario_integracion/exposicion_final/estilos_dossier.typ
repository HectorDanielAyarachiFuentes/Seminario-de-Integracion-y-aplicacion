// estilos_dossier.typ — Estilo editorial académico A4 para Dossier de Defensa Oral (CURZAS / UNCo)

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
  header: context {
    let p = counter(page).get().first()
    if p > 1 {
      grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 8.5pt, fill: rgb("#002B49"), weight: "bold")[UNIVERSIDAD NACIONAL DEL COMAHUE — CURZAS | SIA (2025/2026)],
        text(size: 8pt, fill: rgb("#718096"), style: "italic")[Dossier de Defensa Oral del TFG]
      )
      v(-4pt)
      line(length: 100%, stroke: 0.5pt + rgb("#CBD5E0"))
    }
  },
  footer: context {
    let p = counter(page).get().first()
    if p > 1 {
      line(length: 100%, stroke: 0.5pt + rgb("#CBD5E0"))
      v(2pt)
      grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 8pt, fill: rgb("#4A5568"))[Tesista: Daniel Ayarachi Fuentes | Cátedra: Dra. D. Noguera, Esp. F. Abeiro, Esp. M. C. Aguirre],
        text(size: 8.5pt, fill: rgb("#002B49"), weight: "bold")[Página #p]
      )
    }
  }
)

#set text(font: "Arial", size: 10.5pt, fill: rgb("#2D3748"))
#set par(justify: true, leading: 0.65em)

// Encabezados
#show heading.where(level: 1): it => {
  v(0.6cm)
  block(
    width: 100%,
    stroke: (bottom: 2pt + rgb("#002B49")),
    inset: (bottom: 6pt),
    [
      #text(size: 15pt, weight: "bold", fill: rgb("#002B49"))[#it.body]
    ]
  )
  v(0.3cm)
}

#show heading.where(level: 2): it => {
  v(0.4cm)
  text(size: 12.5pt, weight: "bold", fill: rgb("#007791"))[#it.body]
  v(0.2cm)
}

#show heading.where(level: 3): it => {
  v(0.25cm)
  text(size: 11pt, weight: "bold", fill: rgb("#1A202C"))[#it.body]
  v(0.15cm)
}

// Cajas de acotación escénica / Speech cues
#show quote: it => block(
  width: 100%,
  stroke: (left: 3pt + rgb("#002B49")),
  fill: rgb("#F7FAFC"),
  inset: (left: 12pt, right: 10pt, top: 8pt, bottom: 8pt),
  radius: (right: 4pt),
  [
    #set text(style: "italic", size: 10pt, fill: rgb("#1A202C"))
    #it.body
  ]
)

// Tablas elegantes
#set table(
  stroke: (x, y) => if y == 0 { (top: 1pt + rgb("#002B49"), bottom: 0.5pt + rgb("#002B49")) } else { (bottom: 0.3pt + rgb("#E2E8F0")) },
  inset: 5pt
)
#show table: set text(size: 9pt)
#show table.cell.where(y: 0): set text(weight: "bold", fill: rgb("#002B49"))
