// ==============================================================================
// TRABAJO PRÁCTICO N° 4 — SEMINARIO DE INTEGRACIÓN Y APLICACIÓN (SIA 2025/2026)
// CURZAS — Universidad Nacional del Comahue
// PROYECTO DE TRABAJO FINAL DE GRADUACIÓN (TFG) INTEGRAL (RES. CD-CURZAS N° 266/23)
// Autor: Héctor Daniel Ayarachi Fuentes
// Formato: Typst (Normas APA 7ma Edición & Modelo Oficial de Carátula SIA 2025)
// ==============================================================================

#set document(
  title: "Proyecto de Trabajo Final de Graduación (TFG) — SIA CURZAS/UNCo",
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
// 1. CARÁTULA OFICIAL SIA 2025 (Res. CD-CURZAS N° 266/23)
// ==============================================================================

#page(
  paper: "a4",
  margin: (top: 2.8cm, bottom: 2.5cm, left: 2.54cm, right: 2.54cm),
  header: none,
  footer: none
)[
  #align(center)[
    #image("../../assets/img/CURZAS.png", width: 110pt)
    #v(14pt)

    #text(size: 14pt, weight: "bold", fill: primary)[UNIVERSIDAD NACIONAL DEL COMAHUE]\
    #v(3pt)
    #text(size: 11pt, weight: "bold", fill: text-main)[COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)]\
    #v(2pt)
    #text(size: 10.5pt, style: "italic", fill: text-muted)[Departamento de Administración Pública]\
    #v(2pt)
    #text(size: 10.5pt, weight: "medium", fill: text-main)[Ciclo Complementario de Licenciatura en Gestión de Recursos Humanos]\
    #text(size: 9pt, fill: text-muted)[(y Licenciatura en Administración Pública)]

    #v(22pt)
    #rect(fill: bg-card, stroke: 1.2pt + primary, inset: 15pt, radius: 4pt, width: 100%)[
      #text(size: 10.5pt, weight: "bold", fill: accent, tracking: 0.08em)[TRABAJO PRÁCTICO N° 4 — PROYECTO INTEGRAL DE TFG]\
      #v(6pt)
      #text(size: 13.5pt, weight: "bold", fill: primary)[Inteligencia Artificial y Gestión Estratégica del Talento Humano: Oportunidades, Desafíos y Gobernanza en Organizaciones Contemporáneas]\
      #v(5pt)
      #text(size: 9.5pt, fill: text-muted)[Proyecto de Trabajo Final de Graduación presentado bajo Resolución CD-CURZAS N° 266/23]
    ]

    #v(18pt)
  ]

  #align(left)[
    #block(inset: (left: 0.8cm, right: 0.8cm))[
      #grid(
        columns: (115pt, 1fr),
        row-gutter: 8.5pt,
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

        text(size: 9pt, weight: "bold", fill: text-muted)[DIRECTOR/A],
        text(size: 9.5pt, fill: text-muted)[(A designar)],

        text(size: 9pt, weight: "bold", fill: text-muted)[CODIRECTOR/A],
        text(size: 9.5pt, fill: text-muted)[(A designar)],

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
// 2. CUERPO DEL PROYECTO DE TFG (10 Puntos de la Res. CD-CURZAS N° 266/23)
// ==============================================================================

#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (top: 2.54cm, bottom: 2.54cm, left: 2.54cm, right: 2.54cm),
  header: [
    #grid(
      columns: (1fr, auto),
      text(size: 8.5pt, fill: text-muted)[UNCo — CURZAS | Proyecto de TFG (Res. CD N° 266/23)],
      text(size: 8.5pt, fill: primary, weight: "bold")[SIA 2025/2026]
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

= 2. Tema de Investigación
El proyecto aborda la intersección entre las tecnologías de Inteligencia Artificial (algoritmos predictivos y modelos generativos de lenguaje) y los procesos de gestión estratégica de personas en organizaciones del sector público y servicios de la provincia de Río Negro en el período 2023–2026.

= 3. Delimitación del Objeto Problema
¿De qué modo la incorporación de herramientas basadas en Inteligencia Artificial en los procesos de gestión del talento humano condiciona la percepción de equidad, el clima laboral y la toma de decisiones estratégicas en las organizaciones de la región durante el período 2023–2026?

*Justificación y Relevancia:* Aporta evidencia empírica regional y modelos de gobernanza aplicables que concilian productividad y salvaguarda de derechos individuales y colectivos.

= 4. Definición de Objetivos
- *Objetivo General:* Analizar el impacto de la incorporación de sistemas basados en IA en los subsistemas de gestión de recursos humanos, evaluando sus efectos sobre la percepción de justicia organizacional, la efectividad operativa y la configuración de esquemas de gobernanza ética.
- *Objetivos Específicos:*
  1. Caracterizar las herramientas algorítmicas de IA incorporadas o en fase piloto.
  2. Evaluar empíricamente las percepciones de transparencia y justicia organizacional.
  3. Identificar las barreras normativas, presupuestarias y sindicales existentes.
  4. Formular un esquema propositivo de gobernanza algorítmica centrado en el factor humano (_human-in-the-loop_).

= 5. Antecedentes (Estado del Arte)
Se sistematizan estudios internacionales (Tambe et al., 2019; Bankins, 2021) e iberoamericanos (Oszlak, 2020; Criado & Gil-Garcia, 2019; Fernández & Ramírez, 2023), constatándose la escasez de investigaciones empíricas aplicadas al sector público subnacional de la Patagonia.

= 6. Marco Teórico
La investigación se cimienta sobre:
1. *Teoría de la Justicia Organizacional (Colquitt, 2001):* Dimensiones distributiva, procesal e interaccional.
2. *Capacidades Estatales y Burocracia Inteligente (Evans, 1996; Oszlak, 2020).*
3. *Gobernanza Algorítmica y Mediación Humana (Bankins, 2021).*

= 7. Metodología / Materiales, Técnicas y Métodos

== 7.1. Enfoque y Diseño Metodológico
Se adopta un *enfoque mixto preponderantemente cualitativo* con integración de datos cuantitativos descriptivos (diseño secuencial explicativo).
- *Alcance:* Descriptivo-propositivo.
- *Diseño:* No experimental, transeccional contemporáneo.

== 7.2. Población, Muestra y Unidades de Análisis
- *Unidad de Análisis:* Las áreas de recursos humanos / personal y los colaboradores impactados por herramientas digitales.
- *Muestra Cualitativa:* Muestreo intencional no probabilístico de 12 directivos y técnicos de RRHH, más 4 representantes gremiales.
- *Muestra Cuantitativa:* Muestra representativa de 150 colaboradores para encuesta de clima y percepción tecnológica.

== 7.3. Técnicas e Instrumentos de Recolección de Datos
- Entrevistas semiestructuradas en profundidad.
- Encuesta estructurada con escala Likert validada.
- Análisis documental normativo (resoluciones, convenios colectivos, manuales de funciones).

= 8. Cronograma de Actividades

#table(
  columns: (2.5fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.5pt + border-subtle,
  inset: 6pt,
  
  [#text(fill: white, weight: "bold")[Actividad / Etapa]],
  [#text(fill: white, weight: "bold")[Bim 1]],
  [#text(fill: white, weight: "bold")[Bim 2]],
  [#text(fill: white, weight: "bold")[Bim 3]],
  [#text(fill: white, weight: "bold")[Bim 4]],
  [#text(fill: white, weight: "bold")[Bim 5]],
  [#text(fill: white, weight: "bold")[Bim 6]],

  [Ajuste final del diseño y aprobación de plan], [X], [], [], [], [], [],
  [Revisión bibliográfica ampliada y fichaje APA 7], [X], [X], [], [], [], [],
  [Construcción y validación de instrumentos], [], [X], [X], [], [], [],
  [Trabajo de campo: entrevistas y encuestas], [], [], [X], [X], [], [],
  [Procesamiento cualitativo y cuantitativo de datos], [], [], [], [X], [X], [],
  [Redacción del informe final de tesis], [], [], [], [], [X], [X],
  [Revisión con Director/a y defensa oral del TFG], [], [], [], [], [], [X]
)

= 9. Viabilidad del Proyecto
- *Recursos Humanos:* Estudiante tesista, acompañamiento de Director/a y Codirector/a, y colaboración de informantes clave de las organizaciones analizadas.
- *Recursos Técnicos y Materiales:* Equipamiento informático personal, software de análisis cualitativo y suite de composición tipográfica (*Typst* y *Quarto*).
- *Viabilidad Institucional:* Acceso garantizado a fuentes normativas públicas bajo principio de transparencia activa (Ley 27.275 y normativa rionegrina).

= 10. Bibliografía (Normas APA 7ma Edición)

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
