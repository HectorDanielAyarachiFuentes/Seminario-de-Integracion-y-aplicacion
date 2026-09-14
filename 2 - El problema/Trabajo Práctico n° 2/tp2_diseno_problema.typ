// Simple numbering for non-book documents
#let equation-numbering = "(1)"
#let callout-numbering = "1"
#let subfloat-numbering(n-super, subfloat-idx) = {
  numbering("1a", n-super, subfloat-idx)
}

// Theorem configuration for theorion
// Simple numbering for non-book documents (no heading inheritance)
#let theorem-inherited-levels = 0

// Theorem numbering format (can be overridden by extensions for appendix support)
// This function returns the numbering pattern to use
#let theorem-numbering(loc) = "1.1"

// Default theorem render function
#let theorem-render(prefix: none, title: "", full-title: auto, body) = {
  if full-title != "" and full-title != auto and full-title != none {
    strong[#full-title.]
    h(0.5em)
  }
  body
}
// Some definitions presupposed by pandoc's typst output.
#let content-to-string(content) = {
  if content.has("text") {
    content.text
  } else if content.has("children") {
    content.children.map(content-to-string).join("")
  } else if content.has("body") {
    content-to-string(content.body)
  } else if content == [ ] {
    " "
  }
}

#let horizontalrule = line(start: (25%,0%), end: (75%,0%))

#let endnote(num, contents) = [
  #stack(dir: ltr, spacing: 3pt, super[#num], contents)
]

#show terms.item: it => block(breakable: false)[
  #text(weight: "bold")[#it.term]
  #block(inset: (left: 1.5em, top: -0.4em))[#it.description]
]

// Some quarto-specific definitions.

#show raw.where(block: true): set block(
    fill: luma(230),
    width: 100%,
    inset: 8pt,
    radius: 2pt
  )

#let block_with_new_content(old_block, new_content) = {
  let fields = old_block.fields()
  let _ = fields.remove("body")
  if fields.at("below", default: none) != none {
    // TODO: this is a hack because below is a "synthesized element"
    // according to the experts in the typst discord...
    fields.below = fields.below.abs
  }
  block.with(..fields)(new_content)
}

#let empty(v) = {
  if type(v) == str {
    // two dollar signs here because we're technically inside
    // a Pandoc template :grimace:
    v.matches(regex("^\\s*$")).at(0, default: none) != none
  } else if type(v) == content {
    if v.at("text", default: none) != none {
      return empty(v.text)
    }
    for child in v.at("children", default: ()) {
      if not empty(child) {
        return false
      }
    }
    return true
  }

}

// Subfloats
// This is a technique that we adapted from https://github.com/tingerrr/subpar/
#let quartosubfloatcounter = counter("quartosubfloatcounter")

#let quarto_super(
  kind: str,
  caption: none,
  label: none,
  supplement: str,
  position: none,
  subcapnumbering: "(a)",
  body,
) = {
  context {
    let figcounter = counter(figure.where(kind: kind))
    let n-super = figcounter.get().first() + 1
    set figure.caption(position: position)
    [#figure(
      kind: kind,
      supplement: supplement,
      caption: caption,
      {
        show figure.where(kind: kind): set figure(numbering: _ => {
          let subfloat-idx = quartosubfloatcounter.get().first() + 1
          subfloat-numbering(n-super, subfloat-idx)
        })
        show figure.where(kind: kind): set figure.caption(position: position)

        show figure: it => {
          let num = numbering(subcapnumbering, n-super, quartosubfloatcounter.get().first() + 1)
          show figure.caption: it => block({
            num.slice(2) // I don't understand why the numbering contains output that it really shouldn't, but this fixes it shrug?
            [ ]
            it.body
          })

          quartosubfloatcounter.step()
          it
          counter(figure.where(kind: it.kind)).update(n => n - 1)
        }

        quartosubfloatcounter.update(0)
        body
      }
    )#label]
  }
}

// callout rendering
// this is a figure show rule because callouts are crossreferenceable
#show figure: it => {
  if type(it.kind) != str {
    return it
  }
  let kind_match = it.kind.matches(regex("^quarto-callout-(.*)")).at(0, default: none)
  if kind_match == none {
    return it
  }
  let kind = kind_match.captures.at(0, default: "other")
  kind = upper(kind.first()) + kind.slice(1)
  // now we pull apart the callout and reassemble it with the crossref name and counter

  // when we cleanup pandoc's emitted code to avoid spaces this will have to change
  let old_callout = it.body.children.at(1).body.children.at(1)
  let old_title_block = old_callout.body.children.at(0)
  let children = old_title_block.body.body.children
  let old_title = if children.len() == 1 {
    children.at(0)  // no icon: title at index 0
  } else {
    children.at(1)  // with icon: title at index 1
  }

  // TODO use custom separator if available
  // Use the figure's counter display which handles chapter-based numbering
  // (when numbering is a function that includes the heading counter)
  let callout_num = it.counter.display(it.numbering)
  let new_title = if empty(old_title) {
    [#kind #callout_num]
  } else {
    [#kind #callout_num: #old_title]
  }

  let new_title_block = block_with_new_content(
    old_title_block,
    block_with_new_content(
      old_title_block.body,
      if children.len() == 1 {
        new_title  // no icon: just the title
      } else {
        children.at(0) + new_title  // with icon: preserve icon block + new title
      }))

  align(left, block_with_new_content(old_callout,
    block(below: 0pt, new_title_block) +
    old_callout.body.children.at(1)))
}

// 2023-10-09: #fa-icon("fa-info") is not working, so we'll eval "#fa-info()" instead
#let callout(body: [], title: "Callout", background_color: rgb("#dddddd"), icon: none, icon_color: black, body_background_color: white) = {
  block(
    breakable: false, 
    fill: background_color, 
    stroke: (paint: icon_color, thickness: 0.5pt, cap: "round"), 
    width: 100%, 
    radius: 2pt,
    block(
      inset: 1pt,
      width: 100%, 
      below: 0pt, 
      block(
        fill: background_color,
        width: 100%,
        inset: 8pt)[#if icon != none [#text(icon_color, weight: 900)[#icon] ]#title]) +
      if(body != []){
        block(
          inset: 1pt, 
          width: 100%, 
          block(fill: body_background_color, width: 100%, inset: 8pt, body))
      }
    )
}




#let article(
  title: none,
  subtitle: none,
  authors: none,
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  lang: "en",
  region: "US",
  font: none,
  fontsize: 11pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: none,
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  mathfont: none,
  codefont: none,
  linestretch: 1,
  sectionnumbering: none,
  linkcolor: none,
  citecolor: none,
  filecolor: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  doc,
) = {
  // Set document metadata for PDF accessibility
  set document(title: title, keywords: keywords)
  set document(
    author: authors.map(author => content-to-string(author.name)).join(", ", last: " & "),
  ) if authors != none and authors != ()
  set par(
    justify: true,
    leading: linestretch * 0.65em
  )
  set text(lang: lang,
           region: region,
           size: fontsize)
  set text(font: font) if font != none
  show math.equation: set text(font: mathfont) if mathfont != none
  show raw: set text(font: codefont) if codefont != none

  set heading(numbering: sectionnumbering)

  show link: set text(fill: rgb(content-to-string(linkcolor))) if linkcolor != none
  show ref: set text(fill: rgb(content-to-string(citecolor))) if citecolor != none
  show link: this => {
    if filecolor != none and type(this.dest) == label {
      text(this, fill: rgb(content-to-string(filecolor)))
    } else {
      text(this)
    }
   }

  let has-title-block = title != none or (authors != none and authors != ()) or date != none or abstract != none
  if has-title-block {
    place(
      top,
      float: true,
      scope: "parent",
      clearance: 4mm,
      block(below: 1em, width: 100%)[

        #if title != none {
          align(center, block(inset: 2em)[
            #set par(leading: heading-line-height) if heading-line-height != none
            #set text(font: heading-family) if heading-family != none
            #set text(weight: heading-weight)
            #set text(style: heading-style) if heading-style != "normal"
            #set text(fill: heading-color) if heading-color != black

            #text(size: title-size)[#title #if thanks != none {
              footnote(thanks, numbering: "*")
              counter(footnote).update(n => n - 1)
            }]
            #(if subtitle != none {
              parbreak()
              text(size: subtitle-size)[#subtitle]
            })
          ])
        }

        #if authors != none and authors != () {
          let count = authors.len()
          let ncols = calc.min(count, 3)
          grid(
            columns: (1fr,) * ncols,
            row-gutter: 1.5em,
            ..authors.map(author =>
                align(center)[
                  #author.name \
                  #author.affiliation \
                  #author.email
                ]
            )
          )
        }

        #if date != none {
          align(center)[#block(inset: 1em)[
            #date
          ]]
        }

        #if abstract != none {
          block(inset: 2em)[
          #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
          ]
        }
      ]
    )
  }

  if toc {
    let title = if toc_title == none {
      auto
    } else {
      toc_title
    }
    block(above: 0em, below: 2em)[
    #outline(
      title: toc_title,
      depth: toc_depth,
      indent: toc_indent
    );
    ]
  }

  doc
}

#set table(
  inset: 6pt,
  stroke: none
)
#let brand-color = (:)
#let brand-color-background = (:)
#let brand-logo = (:)

#set page(
  paper: "us-letter",
  margin: (bottom: 2.5cm,left: 2.5cm,right: 2.5cm,top: 2.5cm,),
  numbering: "1",
  columns: 1,
)

#show: doc => article(
  lang: "es",
  font: ("Arial",),
  fontsize: 12pt,
  toc_title: [Tabla de contenidos],
  toc_depth: 3,
  doc,
)
#set par(justify: true, leading: 0.75em)
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
#set table(
  stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.5pt + black) } else if y == 5 { (bottom: 1pt + black) } else { none },
  inset: 5pt
)
#show table: set text(size: 9.5pt)
#show table.cell: set par(first-line-indent: 0pt, leading: 0.5em)
#show table.cell.where(y: 0): set text(weight: "bold")
#show figure: it => block(spacing: 10pt)[#it]
#show figure.caption: set text(size: 9.5pt, style: "italic")
#show figure.caption: set par(first-line-indent: 0pt)

#align(center)[
  #image("../../assets/img/CURZAS.png", width: 110pt)

  #v(1.2em)

  #text(weight: "bold")[Universidad Nacional del Comahue] \
  #text(weight: "bold")[Complejo Universitario Regional Zona Atlántica y Sur] \
  #text(weight: "bold")[Departamento de Administración Pública]

  #v(3.5em)

  #text(weight: "bold")[Licenciatura en Gestión de Recursos Humanos]
]

#v(3.5em)

#block(inset: (left: 0cm))[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.8em)
  Materia: Seminario de Integración y Aplicación \
  Profesores: Dra. Deborah Noguera \
  #h(5.8em) Esp. Federico Abeiro \
  #h(5.8em) Esp. María Cecilia Aguirre \
  \
  Estudiante: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes \
  DNI y LEGAJO: DNI N° 35.492.138 — Legajo N° 8252 \
  Email: hectordanielayarachifuentes\@gmail.com \
  \
  Director/a: (A designar antes de finalizar el cursado del SIA) \
  Codirector/a: (A designar antes de finalizar el cursado del SIA)
]

#v(4em)

#align(center)[
  Viedma, Río Negro - Año 2026
]
#pagebreak()
#set page(numbering: none)
#outline(title: [Índice de Contenidos], indent: auto)
#pagebreak()
#counter(page).update(1)
#set page(numbering: "1")
#set par(first-line-indent: 1.27cm)

#align(center)[
  #set par(first-line-indent: 0pt)
  #text(weight: "bold", size: 12pt)[Evaluación del Desempeño Docente y Factibilidad de Implementación de un Modelo de Retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo (2025–2026)] \
  #v(0.4em)
  #text(style: "italic", size: 11pt)[Trabajo Práctico N° 2: Primera Parte de la Estructura del Proyecto de Investigación de TFG]
]
#v(1em)
= Tema de Investigación
<tema-de-investigación>
== Identificación del Tema y Encuadre en el Modelo de Francisco Longo
<identificación-del-tema-y-encuadre-en-el-modelo-de-francisco-longo>
Este proyecto de investigación se ubica en el cruce disciplinar entre la #strong[Administración Pública] y la #strong[Gestión de Recursos Humanos]. Su abordaje responde a los desafíos actuales de modernización institucional y desarrollo de capacidades estatales en el sector público (Oszlak, 2020). Conforme a las pautas del Seminario de Integración y Aplicación (SIA) y a los criterios del Reglamento de Trabajo Final de Graduación (Universidad Nacional del Comahue - CURZAS, 2023), el tema se delimita mediante el criterio de "pirámide invertida" (Sautu, 2005), transitando desde el macrosistema de gestión pública hasta el análisis empírico de un problema situado en el ámbito universitario regional.

A nivel teórico, la investigación adopta como marco analítico el #strong[Modelo de Gestión del Empleo Público y Recursos Humanos] de #strong[Francisco Longo (2006)]. Este modelo concibe la administración de personas como un sistema articulado con la estrategia institucional y compuesto por subsistemas interdependientes:

#block[
#figure([
#box(image("assets/Sistemas-longo.svg", width: 70.0%))
], caption: figure.caption(
position: bottom, 
[
#emph[Subsistemas de la Gestión de Recursos Humanos en el Sector Público (Longo, 2006).]
]), 
kind: "quarto-float-fig", 
supplement: "Figura", 
)


]
Dentro de este esquema, el trabajo hace foco en el #strong[Subsistema de Gestión del Rendimiento (Evaluación del Desempeño)], articulado con tres subsistemas clave: #strong[Gestión del Desarrollo] (capacitación y carrera docente), #strong[Organización del Trabajo] (perfiles y funciones académicas) y #strong[Gestión de las Relaciones Humanas] (clima laboral y cultura participativa).

El propósito central es indagar si la evaluación docente puede superar la lógica tradicional de control formal o punitivo (Chiavenato, 2020) para orientarse hacia un enfoque formativo de aprendizaje continuo. Para ello, se analiza la factibilidad de un modelo de #strong[retroalimentación 360 grados], que articula diversas miradas sobre la labor docente: autoevaluación, valoración de pares disciplinares, apreciación de los estudiantes y seguimiento de directores departamentales (Dalmau et al., 2017; Lepsinger & Lucia, 2009).

== Descripción Contextual Socioeconómica, Histórica e Institucional
<descripción-contextual-socioeconómica-histórica-e-institucional>
El estudio se sitúa en el #strong[Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)], unidad académica descentralizada de la #strong[Universidad Nacional del Comahue (UNCo)] en la ciudad de Viedma, capital de Río Negro. A nivel histórico y regulatorio, la Ley N° 24.521 de Educación Superior (Ministerio de Educación, 1995) fijó el mandato de que las universidades nacionales incorporen mecanismos periódicos de autoevaluación y aseguramiento de la calidad en sus tareas de docencia, investigación y extensión.

En este marco, el #strong[Departamento de Administración Pública] cumple una función estratégica en el desarrollo comarcal y provincial. Tiene a su cargo las carreras de Licenciatura en Administración Pública, Licenciatura en Gestión de Recursos Humanos y ciclos de complementación curricular para agentes públicos. Su comunidad estudiantil está conformada tanto por jóvenes de la comarca Viedma-Carmen de Patagones como por trabajadores insertos en organismos públicos de diversa índole.

A esta realidad se suma la consolidación de la #strong[Red de Nodos Universitarios] en localidades de la Línea Sur y la Costa Atlántica rionegrina (tales como Sierra Grande, Valcheta, Los Menucos y Ramos Mexía, entre otras localidades). Esta expansión territorial impone modalidades pedagógicas híbridas que combinan entornos virtuales y encuentros presenciales, lo que demanda de los equipos docentes competencias específicas de tutoría y acompañamiento digital.

En el plano normativo, la actividad docente en el CURZAS se encuentra reglada por el Estatuto de la UNCo (Ordenanza N° 470/2009 y sus modificatorias), el Reglamento de Carrera Docente (Ordenanza N° 0920/2019 y sus normas complementarias) y el Convenio Colectivo de Trabajo Docente homologado por Decreto N° 1246/2015 (Poder Ejecutivo Nacional, 2015). Estos instrumentos fijan mecanismos periódicos de evaluación con fines de permanencia y promoción, que incluyen informes de labor académica, dictámenes de pares y encuestas estudiantiles de fin de cuatrimestre.

A partir de este marco, el proyecto plantea como #strong[supuesto de partida e hipótesis exploratoria] que, en la dinámica cotidiana, dichos dispositivos podrían estar funcionando prioritariamente con un sentido administrativo y sumativo, enfocado en el cumplimiento reglamentario. No obstante, lejos de asumir una conclusión anticipada, #strong[será necesario indagar empíricamente si] estas herramientas operan de manera aislada o si generan instancias efectivas de retroalimentación pedagógica. Examinar si los resultados evaluativos se vinculan efectivamente con planes de capacitación y mejora docente constituye el objetivo central del relevamiento de campo para el período #strong[2025--2026].

= Delimitación del Objeto Problema
<delimitación-del-objeto-problema>
== Problematización y Construcción del Objeto de Estudio
<problematización-y-construcción-del-objeto-de-estudio>
Construir un problema científico exige desnaturalizar las rutinas cotidianas de la organización para reflexionar sobre sus supuestos teórico-metodológicos (Wainerman & Sautu, 2011). En la educación pública, la evaluación docente suele debatirse entre dos lógicas: el control formal-estatutario y el acompañamiento formativo enfocado en el desarrollo continuo (Longo, 2006).

En este sentido, la investigación no parte de suponer una falta de mecanismos de evaluación ---ya que existen normas y procedimientos vigentes---, sino de indagar la #strong[posible desconexión entre los circuitos de evaluación del rendimiento y las oportunidades reales de desarrollo pedagógico]. Si bien se aplican periódicamente encuestas a estudiantes, #strong[se plantea como hipótesis a contrastar si estos instrumentos son percibidos en la práctica como un trámite formal], con escasa incidencia en la autoevaluación docente, el diálogo entre pares o la planificación del departamento.

Para responder a este interrogante, la literatura especializada destaca el modelo de #strong[evaluación multiactoral o 360 grados] (Dalmau et al., 2017; Lepsinger & Lucia, 2009) como una herramienta idónea para articular distintas fuentes de retroalimentación: la reflexión del propio docente, el juicio de colegas de cátedra, la valoración de los estudiantes y el seguimiento institucional.

Conviene advertir que #strong[la evaluación 360° no garantiza resultados formativos de forma automática]. Las investigaciones comparadas señalan que su viabilidad depende de condiciones precisas: anonimato y confidencialidad de los datos, instrumentos pedagógicamente válidos, sensibilización previa de los claustros y un clima institucional de confianza que aleje cualquier percepción de control punitivo.

En una universidad pública cogobernada, es indispensable #strong[diferenciar la evaluación orientada a la mejora pedagógica de aquella vinculada a decisiones laborales sumativas] (como la permanencia o promoción regladas por la Ordenanza N° 0920/2019 y modificatorias, y el CCT Docente, Decreto N° 1246/2015). Trasladar herramientas de gestión sin cuidar esta frontera o sin el acuerdo de los claustros podría despertar comprensibles prevenciones. Por eso, la viabilidad de cualquier propuesta descansa en la #strong[gobernanza universitaria]: un espacio colegiado donde las políticas de gestión de personas se construyen sobre #emph[variables de control compartido] (Matus, 1993; Longo, 2006).

== Desglose de las Cuatro (4) Delimitaciones Metodológicas
<desglose-de-las-cuatro-4-delimitaciones-metodológicas>
Siguiendo las pautas de la cátedra, la delimitación del problema comprende cuatro dimensiones constitutivas:

+ #strong[Delimitación Temática:] Mecanismos de estructuración de la evaluación del desempeño docente y análisis de factibilidad para implementar un modelo de retroalimentación multiactoral (360°), articulando autoevaluación, valoración de pares, opinión de estudiantes y seguimiento departamental.
+ #strong[Delimitación Semántica y Teórica:] Precisión de conceptos estructurantes: #emph[Evaluación del Desempeño Docente] (apreciación formativa del quehacer pedagógico en el subsistema de rendimiento); #emph[Modelo 360° / Retroalimentación Multiactoral] (dispositivo de consulta y triangulación de juicios valorativos); #emph[Gobernanza Universitaria] (cogobierno, diálogo paritario y control compartido de variables institucionales; Matus, 1993); y #emph[Gestión del Desarrollo] (aprendizaje continuo y formación pedagógica articulada; Longo, 2006).
+ #strong[Delimitación Temporal:] Período de investigación #strong[2025--2026], organizado en dos etapas:
  - #strong[Fase preliminar y documental (2025):] Formulación del problema, revisión bibliográfica sistemática sobre evaluación 360°, análisis normativo institucional (Estatuto UNCo, Ordenanzas CS N° 470/2009 y N° 0920/2019 con sus modificatorias, y CCT Docente Decreto N° 1246/2015) y diseño metodológico.
  - #strong[Fase empírica y propositiva (2026):] Trabajo de campo mediante entrevistas a autoridades y docentes, encuestas a estudiantes, análisis multidimensional de factibilidad e informe final de Tesina para el Seminario de Integración y Aplicación (SIA).
+ #strong[Delimitación Geográfica e Institucional:] Departamento de Administración Pública, Complejo Universitario Regional Zona Atlántica y Sur (CURZAS), Universidad Nacional del Comahue, ciudad de Viedma, Río Negro.

== Operacionalización de las Dimensiones de Factibilidad
<operacionalización-de-las-dimensiones-de-factibilidad>
=== Definición Conceptual y Operativa de Factibilidad
<definición-conceptual-y-operativa-de-factibilidad>
En el marco de la gestión pública universitaria, la #strong[factibilidad] en esta investigación no se concibe como una viabilidad técnica abstracta ni como una imposición gerencial vertical. Se define operativamente como la #strong[convergencia de condiciones normativas, organizacionales, técnicas y de legitimidad institucional que permitan implementar un modelo de retroalimentación 360° con sentido formativo y sin vulnerar derechos laborales adquiridos].

En términos prácticos, determinar si el modelo es factible en el Departamento de Administración Pública del CURZAS implica responder a cuatro interrogantes centrales: 1. #strong[Compatibilidad jurídica:] ¿Puede aplicarse con fines formativos sin colisionar con la estabilidad laboral regulada por el Estatuto UNCo, la Carrera Docente (Ord. N° 0920/2019 y modificatorias) y el CCT Docente (Decreto N° 1246/2015)? 2. #strong[Capacidad técnica y de gestión:] ¿Existen plataformas informáticas (SIU-Guaraní, campus virtual) y circuitos administrativos capaces de resguardar el anonimato y procesar devoluciones oportunas? 3. #strong[Aceptación y confianza de los claustros:] ¿Existe disposición en docentes, estudiantes y autoridades para participar en una evaluación multiactoral, disipando temores a controles punitivos? 4. #strong[Legitimidad en el cogobierno:] ¿Cuenta la propuesta con viabilidad política para ser tratada y consensuada en los órganos colegiados sobre variables de control compartido (Matus, 1993; Longo, 2006)?

=== Dimensiones de Observación y Fuentes Empíricas
<dimensiones-de-observación-y-fuentes-empíricas>
Para contrastar estos aspectos en el trabajo de campo, la investigación desagrega la factibilidad en cinco dimensiones observables:

#table(
  columns: (33.33%, 33.33%, 33.33%),
  align: (left,left,left,),
  table.header([Dimensión de Factibilidad], [Criterios y Aspectos a Observar], [Indicadores y Fuentes Empíricas],),
  table.hline(),
  [#strong[Normativa y Estatutaria]], [Compatibilidad con el Estatuto UNCo (Ord. 470/2009 y modif.), la Carrera Docente (Ord. N° 0920/2019 y modificatorias) y el CCT Docente (Decreto N° 1246/2015)], [Análisis documental normativo; ausencia de colisión con la estabilidad y derechos adquiridos],
  [#strong[Técnica e Instrumental]], [Disponibilidad de plataformas digitales, recursos informáticos y diseño pedagógico de instrumentos], [Relevamiento de entornos virtuales (SIU-Guaraní, campus virtual); validez y confidencialidad técnica],
  [#strong[Organizacional y Procedimental]], [Roles departamentales, comisiones curriculares, circuitos de devolución y tiempos de gestión], [Procedimientos administrativos instituidos; capacidad de canalizar la retroalimentación formativa],
  [#strong[Cultural y Actitudinal]], [Nivel de confianza institucional, cultura participativa y disposición de los claustros ante la coevaluación], [Cuestionarios y entrevistas; percepción de utilidad pedagógica y eventuales prevenciones frente al control sumativo],
  [#strong[Gobernanza y Política Institucional]], [Participación y legitimación en el cogobierno (Consejo Directivo y Departamental) y mesas paritarias], [Acuerdos colegiados; consulta a representaciones gremiales sobre variables de control compartido],
)
=== Criterios Cualitativos para la Interpretación de Resultados
<criterios-cualitativos-para-la-interpretación-de-resultados>
Para valorar las conclusiones del relevamiento empírico sin recurrir a mediciones forzadas, la investigación establece tres categorías cualitativas de interpretación:

- #strong[Factibilidad Alta (Favorable):] Se verifica cuando existe compatibilidad normativa plena, soporte tecnológico adecuado, disposición favorable de los tres claustros (docentes, alumnos y directores) y viabilidad de tratamiento colegiado en el cogobierno.
- #strong[Factibilidad Condicionada (Media / Viable con adecuaciones):] Se constata cuando no existen impedimentos jurídicos ni rechazo de fondo, pero la aplicación requiere pasos previos de gestión institucional: acuerdos paritarios específicos sobre confidencialidad, adecuación de plataformas digitales, instancias de sensibilización docente o implementación gradual mediante pruebas piloto.
- #strong[Factibilidad Baja (Desfavorable / Inviable):] Se determina ante la presencia de barreras estructurales no superables en el corto plazo, tales como colisión con el régimen estatutario de carrera docente, desconfianza generalizada en los claustros o carencia absoluta de soporte técnico y administrativo.

== Pregunta General de Investigación
<pregunta-general-de-investigación>
A partir de las precisiones metodológicas señaladas, se formula el interrogante central de la investigación:

#quote(block: true)[
#strong[¿De qué manera se estructuran los mecanismos de evaluación del desempeño docente y qué factibilidad presenta la implementación de un modelo de retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo (2025--2026)?]
]

= Justificación y Relevancia de la Investigación
<justificación-y-relevancia-de-la-investigación>
La pertinencia del proyecto se sustenta en tres planos complementarios, acatando el esquema formal establecido por la normativa de graduación institucional (Universidad Nacional del Comahue - CURZAS, 2023):

== Plano Cognitivo y Disciplinar
<plano-cognitivo-y-disciplinar>
En el plano teórico, el trabajo busca aportar al campo de la Administración Pública y la Gestión de Recursos Humanos en el sector estatal, dialogando con los enfoques sobre modernización y capacidades institucionales (Oszlak, 2020). La implementación de modelos de retroalimentación 360° en universidades públicas argentinas ---con estructuras de cogobierno, autonomía y regímenes paritarios específicos--- representa un área de vacancia que amerita ser investigada de forma situada.

Asimismo, la investigación operacionaliza el Subsistema de Gestión del Rendimiento de Longo (2006) en una universidad patagónica. Se examina en qué condiciones la evaluación docente puede orientarse al aprendizaje continuo, generando evidencia empírica sobre la articulación entre gobernanza colegiada y dispositivos de retroalimentación en organizaciones públicas complejas.

== Plano Social e Institucional
<plano-social-e-institucional>
A nivel social e institucional, el trabajo ofrece un valor concreto al CURZAS y a la UNCo al producir un diagnóstico riguroso sobre la viabilidad de renovar las prácticas evaluativas. En caso de constatarse su factibilidad, la retroalimentación multiactoral podría fortalecer la cultura de mejora continua y transparencia en la educación superior pública.

Asimismo, la investigación considera las expectativas y percepciones de los distintos claustros: - #strong[Cuerpo docente:] Permite conocer si la autoevaluación y el intercambio reflexivo entre pares son valorados como un apoyo formativo para la Carrera Docente (Ord. N° 0920/2019 y modificatorias; CCT Docente, Decreto N° 1246/2015), o si generan reparos frente a sobrecargas de tareas o al uso de la información. - #strong[Claustro estudiantil:] Indaga la disposición de los estudiantes para que su opinión trascienda la encuesta administrativa de cierre lectivo y se convierta en un insumo constructivo para mejorar la enseñanza. - #strong[Autoridades departamentales:] Posibilita diagnosticar las capacidades técnicas y de gestión necesarias para procesar juicios evaluativos múltiples e integrarlos a la planificación académica y a los planes de capacitación.

== Plano Personal y Profesional
<plano-personal-y-profesional>
En el orden formativo, el proyecto articula la Licenciatura en Gestión de Recursos Humanos con la formación previa como Técnico Superior en Recursos Humanos y los marcos de la Administración Pública. Permite consolidar habilidades de diagnóstico organizacional e investigación aplicada en el ámbito universitario regional, reafirmando el compromiso ético con el fortalecimiento de la universidad pública en la Patagonia.

= Definición de Objetivos del TFG
<definición-de-objetivos-del-tfg>
En estricta correspondencia lógica y simétrica con la pregunta general de investigación, los objetivos se formulan mediante verbos en infinitivo que denotan acción empíricamente contrastable:

== Objetivo General
<objetivo-general>
- #strong[Analizar] los mecanismos de estructuración de la evaluación del desempeño docente y determinar las condiciones de factibilidad organizacional, técnica, normativa y de gobernanza para la eventual implementación de un modelo de retroalimentación multiactoral (360°) en el Departamento de Administración Pública del CURZAS-UNCo (2025--2026).

== Objetivos Específicos
<objetivos-específicos>
+ #strong[Relevar y caracterizar] los instrumentos normativos, procedimientos y prácticas vigentes aplicadas a la evaluación del desempeño docente en el Departamento de Administración Pública del CURZAS-UNCo, distinguiendo las prescripciones estatutarias de su implementación efectiva.
+ #strong[Explorar las percepciones, disposiciones y expectativas] de los distintos claustros involucrados (docentes, estudiantes y directores de departamento) respecto a la retroalimentación multiactoral (360°) y las condiciones de confianza institucional requeridas.
+ #strong[Identificar los condicionantes técnico-organizacionales, normativos y de gobernanza] (acuerdos paritarios, Carrera Docente según Ord. N° 0920/2019 y sus modificatorias, confidencialidad y cogobierno) que inciden en la factibilidad del modelo.
+ #strong[Proponer lineamientos orientativos] para una eventual implementación de un modelo de retroalimentación multiactoral (360°), en función de las condiciones y límites de factibilidad identificados en la investigación empírica.

== Matriz de Consistencia Metodológica y Articulación con Longo (2006)
<matriz-de-consistencia-metodológica-y-articulación-con-longo-2006>
Para dotar de consistencia analítica a la investigación, cada subsistema del modelo de Longo (2006) aporta una clave interpretativa específica al problema planteado: \* #strong[Gestión del Rendimiento:] actúa como eje estructurante para examinar los mecanismos evaluativos vigentes y explorar su potencial transformación hacia una lógica formativa e integral. \* #strong[Organización del Trabajo:] permite contrastar los perfiles, funciones docentes y exigencias pedagógicas (presenciales e híbridas en los nodos territoriales) con los criterios reales de evaluación. \* #strong[Gestión del Desarrollo:] analiza la articulación efectiva entre los resultados evaluativos y los planes de capacitación continua, perfeccionamiento didáctico y carrera docente. \* #strong[Gestión de las Relaciones Humanas y Sociales:] indaga el clima laboral, la confianza interclaustros y los acuerdos paritarios indispensables para legitimar la coevaluación y disipar temores al control punitivo.

En consecuencia, el modelo de Longo no se utiliza únicamente como encuadre teórico, sino como criterio de lectura para analizar la articulación entre evaluación del desempeño, desarrollo de capacidades docentes, organización del trabajo y relaciones institucionales, permitiendo identificar condiciones que favorecen o limitan la factibilidad de una retroalimentación 360°.

#table(
  columns: (25%, 25%, 25%, 25%),
  align: (left,left,left,left,),
  table.header([Nivel de Objetivo], [Dimensión y Acción Metodológica], [Subsistema de RR.HH. (Longo, 2006)], [Fuente, Actor e Instrumento Previsto],),
  table.hline(),
  [#strong[General]], [#strong[Factibilidad integral:] Análisis multidimensional de mecanismos actuales y viabilidad de retroalimentación 360°], [#strong[Gestión del rendimiento] (#emph[Evaluación del desempeño y retroalimentación formativa])], [Claustros y autoridades del Departamento de Administración Pública (CURZAS-UNCo)],
  [#strong[Específico 1]], [#strong[Dimensión normativa-institucional:] Relevamiento y análisis documental de ordenanzas, reglamentos y prácticas vigentes], [#strong[Gestión del rendimiento en articulación con Organización del trabajo] (#emph[Evaluación vigente y perfiles/funciones docentes según Estatuto y Ord. N° 0920/2019 y modificatorias])], [Estatuto UNCo (Ord. 470/2009 y modif.), Ord. N° 0920/2019 (y modif.) y CCT Docente (Decreto N° 1246/2015) (Matriz de análisis documental)],
  [#strong[Específico 2]], [#strong[Dimensión intersubjetiva-cultural:] Exploración de percepciones, disposiciones y expectativas ante la evaluación 360°], [#strong[Gestión de las relaciones humanas y sociales] (#emph[Cultura participativa, clima laboral y diálogo interclaustro])], [Docentes, estudiantes y directores de departamento (Guías de entrevista y cuestionarios diagnósticos)],
  [#strong[Específico 3]], [#strong[Dimensión técnico-viabilidad:] Identificación de condicionantes paritarios, procedimentales, gremiales y de confidencialidad], [#strong[Gestión de las relaciones humanas (paritarias) en articulación con Gestión del empleo] (#emph[Condiciones de trabajo, estabilidad y Carrera Docente - Dec.~N° 1246/2015 y Ord. N° 0920/2019 y modif.])], [Representantes docentes y autoridades académicas (Matriz de análisis de viabilidad institucional)],
  [#strong[Específico 4]], [#strong[Dimensión propositiva-orientativa:] Proposición de lineamientos orientativos para una eventual aplicación formativa], [#strong[Gestión del desarrollo] (#emph[Capacitación, aprendizaje continuo y mejora pedagógica])], [Síntesis analítica del proyecto adaptada al contexto institucional del CURZAS (Esquema metodológico orientativo)],
)
#pagebreak()
#show heading.where(level: 1): set align(center)
#set par(first-line-indent: 0pt, hanging-indent: 1.27cm, justify: false)
#heading(level: 1, numbering: none)[Referencias]
<referencias-1>
Chiavenato, I. (2020). #emph[Gestión del talento humano: El nuevo papel de los recursos humanos en las organizaciones] (5.ª ed.). McGraw-Hill Interamericana.

Dalmau, I., Llinares, C., & Montañana, A. (2017). La evaluación docente del profesorado universitario mediante el modelo 360°: Hacia un sistema formativo e integral. #emph[Revista de Docencia Universitaria], 15(2), 245--266. https:/\/doi.org/10.4995/redu.2017.6053

Lepsinger, R., & Lucia, A. D. (2009). #emph[The art and science of 360 degree feedback] (2.ª ed.). Pfeiffer.

Longo, F. (2006). #emph[Mérito y flexibilidad: La gestión de las personas en las organizaciones del sector público]. Paidós.

Matus, C. (1993). #emph[Política, planificación y gobierno]. Fundación ALTIDIR.

Ministerio de Educación. (1995, 10 de agosto). #emph[Ley N° 24.521 de Educación Superior]. Boletín Oficial de la República Argentina.

Oszlak, O. (2020). #emph[El Estado en la era del exponente tecnológico: Hacia una burocracia 4.0]. Instituto Nacional de la Administración Pública.

Poder Ejecutivo Nacional. (2015, 2 de julio). #emph[Decreto N° 1246/2015. Convenio Colectivo de Trabajo para los Docentes de las Instituciones Universitarias Nacionales]. Boletín Oficial de la República Argentina.

Sautu, R. (2005). #emph[Todo es teoría: Objetivos y métodos de investigación]. Lumiere.

Universidad Nacional del Comahue. (2009). #emph[Ordenanza N° 470/2009: Estatuto de la Universidad Nacional del Comahue] (y sus normas modificatorias). Consejo Superior.

Universidad Nacional del Comahue. (2019). #emph[Ordenanza N° 0920/2019: Reglamento de Carrera Docente] (y sus normas modificatorias y complementarias). Consejo Superior.

Universidad Nacional del Comahue - CURZAS. (2023). #emph[Resolución CD-CURZAS N° 266/2023: Reglamento de Trabajo Final de Graduación (TFG) para las carreras del Departamento de Administración Pública] (y resoluciones complementarias). Consejo Directivo.

Wainerman, C., & Sautu, R. (Comps.). (2011). #emph[La trastienda de la investigación] (4.ª ed.). Manantial.
