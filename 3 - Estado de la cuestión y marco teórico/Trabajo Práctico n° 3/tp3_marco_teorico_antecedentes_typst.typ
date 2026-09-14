// ==============================================================================
// TRABAJO PRÁCTICO N° 3 — SEMINARIO DE INTEGRACIÓN Y APLICACIÓN (SIA 2025/2026)
// CURZAS — Universidad Nacional del Comahue
// Autor: Héctor Daniel Ayarachi Fuentes
// Formato: Typst (Normas APA 7ma Edición & Modelo Oficial de Carátula SIA 2025)
// ==============================================================================

#set document(
  title: "Trabajo Práctico N° 3 — Marco Teórico y Antecedentes del TFG",
  author: "Héctor Daniel Ayarachi Fuentes"
)

#let primary = rgb("#0f2d59")       // Azul marino institucional CURZAS
#let accent = rgb("#c89632")        // Dorado elegante
#let text-main = rgb("#1f2937")     // Gris oscuro lectura
#let text-muted = rgb("#6b7280")    // Gris sutil
#let bg-card = rgb("#f8fafc")       // Fondo suave
#let border-subtle = rgb("#e2e8f0") // Bordes

#set text(
  font: ("Segoe UI", "Arial"),
  size: 10pt,
  fill: text-main,
  lang: "es"
)

#set par(
  justify: true,
  leading: 0.75em,
  first-line-indent: 0cm
)

// ==============================================================================
// 1. CARÁTULA OFICIAL SIA 2025
// ==============================================================================

#page(
  paper: "a4",
  margin: (top: 2.8cm, bottom: 2.5cm, left: 2.54cm, right: 2.54cm),
  header: none,
  footer: none
)[
  #align(center)[
    #image("../../assets/img/CURZAS.png", width: 105pt)
    #v(14pt)

    #text(size: 14pt, weight: "bold", fill: primary)[UNIVERSIDAD NACIONAL DEL COMAHUE]\
    #v(3pt)
    #text(size: 11pt, weight: "bold", fill: text-main)[COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)]\
    #v(2pt)
    #text(size: 10.5pt, style: "italic", fill: text-muted)[Departamento de Administración Pública]\
    #v(2pt)
    #text(size: 10.5pt, weight: "medium", fill: text-main)[Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos]\
    #text(size: 9pt, fill: text-muted)[(y Licenciatura en Administración Pública)]

    #v(24pt)
    #rect(fill: bg-card, stroke: 1pt + primary, inset: 14pt, radius: 4pt, width: 100%)[
      #text(size: 11pt, weight: "bold", fill: accent, tracking: 0.08em)[TRABAJO PRÁCTICO N° 3]\
      #v(6pt)
      #text(size: 13.5pt, weight: "bold", fill: primary)[Segunda Parte del Proyecto de TFG: Marco Teórico y Antecedentes]\
      #v(4pt)
      #text(size: 9.5pt, fill: text-muted)[Estructura Acumulativa (Res. CD-CURZAS N° 266/23)]
    ]

    #v(20pt)
  ]

  #align(left)[
    #block(inset: (left: 0.8cm, right: 0.8cm))[
      #grid(
        columns: (115pt, 1fr),
        row-gutter: 9pt,
        text(size: 9pt, weight: "bold", fill: text-muted)[MATERIA],
        text(size: 9.5pt, weight: "medium", fill: text-main)[Seminario de Integración y Aplicación (SIA)],

        text(size: 9pt, weight: "bold", fill: text-muted)[DOCENTE RESPONSABLE],
        text(size: 9.5pt, weight: "medium", fill: text-main)[Dra. Deborah Noguera],

        text(size: 9pt, weight: "bold", fill: text-muted)[AYUDANTES DE CÁTEDRA],
        text(size: 9.5pt, fill: text-main)[Esp. Federico Abeiro \ Esp. María Cecilia Aguirre],

        text(size: 9pt, weight: "bold", fill: text-muted)[ESTUDIANTE],
        text(size: 9.5pt, weight: "bold", fill: primary)[Héctor Daniel Ayarachi Fuentes],

        text(size: 9pt, weight: "bold", fill: text-muted)[DNI Y LEGAJO],
        text(size: 9.5pt, fill: text-main)[(Completar DNI y Legajo institucional)],

        text(size: 9pt, weight: "bold", fill: text-muted)[EMAIL],
        text(size: 9.5pt, fill: text-main)[(Completar correo institucional / personal)],

        text(size: 9pt, weight: "bold", fill: text-muted)[TÍTULO DEL TFG],
        text(size: 9.5pt, weight: "semibold", fill: text-main)[Inteligencia Artificial y Gestión Estratégica del Talento Humano: Oportunidades, Desafíos y Gobernanza en Organizaciones Contemporáneas],

        text(size: 9pt, weight: "bold", fill: text-muted)[DIRECTOR/A],
        text(size: 9.5pt, fill: text-muted)[(A designar en el cursado)],

        text(size: 9pt, weight: "bold", fill: text-muted)[CODIRECTOR/A],
        text(size: 9.5pt, fill: text-muted)[(A designar en el cursado)],

        text(size: 9pt, weight: "bold", fill: text-muted)[AÑO ACADÉMICO],
        text(size: 9.5pt, fill: text-main)[2025 / 2026]
      )
    ]
  ]

  #align(bottom + center)[
    #text(size: 8.5pt, fill: text-muted)[Viedma, Río Negro — República Argentina]
  ]
]

// ==============================================================================
// 2. CUERPO DEL DOCUMENTO
// ==============================================================================

#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (top: 2.54cm, bottom: 2.54cm, left: 2.54cm, right: 2.54cm),
  header: [
    #grid(
      columns: (1fr, auto),
      text(size: 8.5pt, fill: text-muted)[UNCo — CURZAS | Seminario de Integración y Aplicación (SIA)],
      text(size: 8.5pt, fill: primary, weight: "bold")[TP N° 3]
    )
    #v(3pt)
    #line(length: 100%, stroke: 0.4pt + border-subtle)
  ],
  footer: [
    #line(length: 100%, stroke: 0.4pt + border-subtle)
    #v(4pt)
    #grid(
      columns: (1fr, auto, 1fr),
      align: (left, center, right),
      text(size: 8.5pt, fill: text-muted)[Héctor Daniel Ayarachi Fuentes],
      image("../../assets/img/CURZAS.png", height: 12pt),
      text(size: 8.5pt, fill: text-main)[
        #context [Página #counter(page).display("1") de #counter(page).final().at(0)]
      ]
    )
  ]
)

#show heading.where(level: 1): it => [
  #v(14pt)
  #text(weight: "bold", size: 12pt, fill: primary)[#it.body]
  #v(6pt)
]

#show heading.where(level: 2): it => [
  #v(10pt)
  #text(weight: "bold", size: 10.5pt, fill: primary)[#it.body]
  #v(4pt)
]

= 1. Tema de Investigación y Contexto
El presente proyecto analiza la incorporación de herramientas de Inteligencia Artificial (IA) en la gestión de personas en organizaciones del sector público y servicios de la comarca Viedma - Carmen de Patagones y la provincia de Río Negro en el período 2023–2026.

= 2. Delimitación del Objeto Problema
¿De qué modo la incorporación de sistemas basados en Inteligencia Artificial en los procesos de gestión del talento humano condiciona la percepción de equidad, el clima laboral y la toma de decisiones estratégicas en las organizaciones de la región durante el período 2023–2026?

= 3. Objetivos del TFG
- *Objetivo General:* Analizar el impacto de la incorporación de sistemas basados en IA en los subsistemas de gestión de recursos humanos, evaluando sus efectos sobre la percepción de justicia organizacional, la efectividad operativa y la configuración de esquemas de gobernanza ética.
- *Objetivos Específicos:*
  1. Relevar y caracterizar las tecnologías de IA aplicadas a la gestión de personal.
  2. Evaluar las percepciones de equidad y transparencia algorítmica de los colaboradores.
  3. Identificar condicionantes normativos, institucionales y gremiales.
  4. Diseñar pautas de gobernanza institucional con supervisión humana (_human-in-the-loop_).

= 4. Marco Teórico

== 4.1. Teoría de la Justicia Organizacional y Percepción del Trabajo
La literatura contemporánea señala que la aceptación de sistemas automatizados en el entorno de trabajo está directamente mediada por la percepción de justicia (Colquitt, 2001). Según este enfoque, se distinguen tres dimensiones críticas:
- *Justicia Distributiva:* Percepción de equidad en las recompensas o promociones mediadas por algoritmos.
- *Justicia Procesal:* Transparencia, auditabilidad y consistencia en los criterios de evaluación.
- *Justicia Interaccional:* Calidad del trato y fundamentación humana que acompaña la comunicación de la decisión.

== 4.2. Capacidades Estatales y Burocracia Inteligente
En la administración pública, la incorporación tecnológica debe examinarse a la luz de las capacidades estatales (Evans, 1996; Oszlak, 2020). Una burocracia 4.0 exige fortalecer competencias analíticas y éticas en los equipos estatales.

== 4.3. Gobernanza Algorítmica y Enfoque _Human-in-the-Loop_
Frente al riesgo de opacidad algorítmica, se postula el paradigma _human-in-the-loop_ (Bankins, 2021), garantizando la supervisión humana en decisiones laborales de impacto.

= 5. Antecedentes y Estado del Arte
- *Tambe, Cappelli y Yakubovich (2019):* Analizaron los desafíos de calidad de datos y variabilidad conductual en la implementación de IA en recursos humanos.
- *Bankins (2021):* Revisión sistemática sobre implicancias éticas y sesgos algorítmicos en el ciclo laboral.
- *Oszlak (2020) y Fernández & Ramírez (2023):* Diagnósticos sobre capacidades estatales y modernización digital en Iberoamérica y Argentina.

= 6. Referencias Bibliográficas (Normas APA 7ma Edición)

#set par(first-line-indent: -1.27cm, leading: 0.85em)
#block(inset: (left: 1.27cm))[
Bankins, S. (2021). The ethical implications of AI adoption in employee lifecycle processes: A systematic review. *Journal of Business Ethics*, 178(3), 735–752. https://doi.org/10.1007/s10551-021-04896-x

Colquitt, J. A. (2001). On the dimensionality of organizational justice: A construct validation of a measure. *Journal of Applied Psychology*, 86(3), 386–400. https://doi.org/10.1037/0021-9010.86.3.386

Criado, J. I., & Gil-Garcia, J. R. (2019). Creating public value through smart technologies and data analytics in government. *Information Polity*, 24(3), 245–250. https://doi.org/10.3233/IP-190180

Evans, P. (1996). El Estado como problema y como solución. *Desarrollo Económico*, 35(140), 529–562.

Fernández, M. J., & Ramírez, S. (2023). Inteligencia artificial y empleo público: Dilemas éticos y capacidades estatales. *Revista del CLAD Reforma y Democracia*, (85), 45–78. https://doi.org/10.32749/clad.ryd.85.02

Oszlak, O. (2020). *El Estado en la era del exponente tecnológico: Hacia una burocracia 4.0*. Instituto Nacional de la Administración Pública (INAP).

Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial intelligence in human resource management: Challenges and a path forward. *California Management Review*, 61(4), 15–42. https://doi.org/10.1177/0008125619867910
]
