// estilos_diapositivas.typ — Configuración visual de diapositivas 16:9 en Typst (CURZAS / UNCo)

#set page(
  paper: "presentation-16-9",
  margin: (top: 0.9cm, bottom: 0.8cm, left: 1.4cm, right: 1.4cm),
  fill: rgb("#FFFFFF"),
  header: context {
    let p = counter(page).get().first()
    if p > 1 {
      grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 8.5pt, fill: rgb("#002B49"), weight: "bold")[CURZAS — Universidad Nacional del Comahue | Seminario de Integración y Aplicación],
        text(size: 8pt, fill: rgb("#718096"), style: "italic")[TFG: Evaluación del Desempeño Docente 360°]
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
        text(size: 8.5pt, fill: rgb("#002B49"), weight: "bold")[Diapositiva #p de 5]
      )
    }
  }
)

#set text(font: "Arial", size: 10.5pt, fill: rgb("#2D3748"))
#set par(justify: false, leading: 0.55em)

// Salto de página automático en cada Diapositiva (Heading 1)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(0.1cm)
  block(
    width: 100%,
    stroke: (bottom: 2pt + rgb("#002B49")),
    inset: (bottom: 4pt),
    [
      #text(size: 15pt, weight: "bold", fill: rgb("#002B49"))[#it.body]
    ]
  )
  v(0.2cm)
}

#show heading.where(level: 2): it => {
  v(0.1cm)
  text(size: 11pt, weight: "bold", fill: rgb("#007791"))[#it.body]
  v(0.1cm)
}

#show heading.where(level: 3): it => {
  text(size: 10pt, weight: "bold", fill: rgb("#1A202C"))[#it.body]
}
