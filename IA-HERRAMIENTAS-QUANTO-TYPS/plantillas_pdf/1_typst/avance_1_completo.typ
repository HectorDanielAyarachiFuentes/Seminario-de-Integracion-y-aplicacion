// ==========================================
// CONFIGURACIÓN GENERAL Y TIPOGRAFÍA
// ==========================================
#set document(title: "Avance 1: Contexto, Modelo de Gestión y Gobernanza - CURZAS", author: "Héctor Daniel Ayarachi Fuentes")
#set text(font: "Segoe UI", size: 10pt, fill: rgb("#24292f"), lang: "es")
#set par(justify: true, leading: 0.7em)

// Paleta de Colores Moderna y Minimalista
#let primary = rgb("#0f2d59")       // Azul marino profundo
#let accent = rgb("#c89632")        // Dorado elegante
#let text-main = rgb("#1f2937")     // Gris carbón para lectura descansada
#let text-muted = rgb("#6b7280")    // Gris suave para subtítulos
#let bg-card = rgb("#f8fafc")       // Fondo neutro premium
#let border-subtle = rgb("#e2e8f0") // Bordes sutiles

// Componente: Caja Destacada Minimalista
#let callout(title, body) = [
  #v(8pt)
  #block(
    width: 100%,
    fill: bg-card,
    stroke: (left: 3pt + primary, rest: 0.5pt + border-subtle),
    inset: (x: 14pt, y: 12pt),
    radius: (right: 4pt),
    [
      #text(weight: "bold", fill: primary, size: 8.5pt, tracking: 0.08em)[#upper(title)] \
      #v(4pt)
      #text(size: 9.5pt, fill: text-main)[#body]
    ]
  )
  #v(8pt)
]

// Estilos de Títulos
#show heading.where(level: 1): it => [
  #v(18pt)
  #box(rect(width: 3.5pt, height: 12pt, fill: accent, radius: 1pt))
  #h(6pt)
  #text(weight: "bold", size: 12.5pt, fill: primary)[#it.body]
  #v(8pt)
]

#show heading.where(level: 2): it => [
  #v(12pt)
  #text(weight: "bold", size: 10.5pt, fill: primary)[#it.body]
  #v(6pt)
]

// ==========================================
// 1. PORTADA MODERNA Y MINIMALISTA
// ==========================================
#page(
  paper: "a4",
  margin: (x: 2.5cm, top: 3.2cm, bottom: 2.5cm),
  header: none,
  footer: none
)[
  // Header Institucional
  #text(size: 11pt, weight: "bold", fill: primary, tracking: 0.05em)[UNIVERSIDAD NACIONAL DEL COMAHUE] \
  #v(2pt)
  #text(size: 9.5pt, weight: "medium", fill: accent)[COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)]
  
  #v(12pt)
  #line(length: 100%, stroke: 0.6pt + border-subtle)
  #v(35pt)
  
  // Tag / Categoría
  #box(
    fill: rgb("#eef2ff"),
    inset: (x: 8pt, y: 4pt),
    radius: 3pt,
    text(size: 8.5pt, weight: "bold", fill: primary, tracking: 0.06em)[PLANEAMIENTO Y CONTROL DE LAS ORGANIZACIONES]
  )
  
  #v(14pt)
  
  // Título Principal (Sin guiones extraños)
  #text(size: 22pt, weight: "bold", fill: primary, hyphenate: false)[
    Avance 1: Contexto, Modelo de Gestión y Gobernanza
  ]
  
  #v(8pt)
  #text(size: 13pt, fill: text-muted, weight: "regular")[
    Análisis Institucional sobre el CURZAS (UNCo)
  ]
  
  #v(45pt)
  
  // Tarjeta de Metadatos Minimalista (Sin bordes rígidos)
  #rect(
    width: 100%,
    fill: bg-card,
    stroke: 0.5pt + border-subtle,
    radius: 6pt,
    inset: (x: 16pt, y: 14pt)
  )[
    #grid(
      columns: (110pt, 1fr),
      row-gutter: 11pt,
      text(size: 9pt, weight: "bold", fill: text-muted)[ALUMNO],
      text(size: 9.5pt, weight: "semibold", fill: text-main)[Héctor Daniel Ayarachi Fuentes],
      
      text(size: 9pt, weight: "bold", fill: text-muted)[CARRERA],
      text(size: 9.5pt, fill: text-main)[Licenciatura en Recursos Humanos],
      
      text(size: 9pt, weight: "bold", fill: text-muted)[ORGANIZACIÓN],
      text(size: 9.5pt, fill: text-main)[CURZAS — Sede Viedma, Río Negro],
      
      text(size: 9pt, weight: "bold", fill: text-muted)[MARCO TEÓRICO],
      text(size: 9.5pt, fill: text-main)[Cao & Blutman (2019), Abal Medina (2014), Oszlak (2020)],
      
      text(size: 9pt, weight: "bold", fill: text-muted)[AÑO ACADÉMICO],
      text(size: 9.5pt, fill: text-main)[2026]
    )
  ]
  
  #align(bottom + center)[
    #text(size: 8.5pt, fill: text-muted)[Viedma, Río Negro — República Argentina]
  ]
]

// ==========================================
// 2. CUERPO DEL INFORME
// ==========================================
#counter(page).update(1)

#set page(
  paper: "a4",
  margin: (x: 2.3cm, top: 2.5cm, bottom: 2.5cm),
  header: [
    #grid(
      columns: (1fr, auto),
      text(size: 8.5pt, fill: text-muted)[Avance 1: Contexto, Modelo de Gestión y Gobernanza | CURZAS],
      text(size: 8.5pt, fill: accent, weight: "bold")[UNCo]
    )
    #v(3pt)
    #line(length: 100%, stroke: 0.4pt + border-subtle)
  ],
  footer: [
    #line(length: 100%, stroke: 0.3pt + border-subtle)
    #v(3pt)
    #grid(
      columns: (1fr, 1fr),
      align: (left, right),
      text(size: 8.5pt, fill: text-muted)[Planeamiento y Control de las Organizaciones],
      text(size: 8.5pt, fill: text-muted)[
        #context [Página #counter(page).display("1") de #counter(page).final().at(0)]
      ]
    )
  ]
)

= 1. Identificación y Marco Institucional de la Organización

El objeto de estudio del presente trabajo es el Complejo Universitario Regional Zona Atlántica y Sur (CURZAS), unidad académica dependiente de la Universidad Nacional del Comahue (UNCo), asentada en la ciudad de Viedma, Provincia de Río Negro. Su estatus institucional responde al mandato constitucional de autonomía y autarquía universitaria (Art. 75 inc. 19 de la Constitución Nacional Argentina y Ley de Educación Superior N° 24.521).

Su marco de creación y funcionamiento se encuentra regido por el Estatuto de la Universidad Nacional del Comahue (Ordenanza N° 470/1993 y sus modificatorias), que establece la estructura organizativa, los órganos co-gobernados de decisión y las misiones fundamentales de docencia, investigación y extensión universitaria.

#callout("Misión y Funciones Institucionales")[
  El CURZAS tiene como misión institucional la generación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte y la Línea Sur rionegrina. Su estructura organizativa combina áreas académicas, departamentos docentes, secretarías administrativas (Académica, de Investigación, de Extensión y de Gestión Administrativa) y órganos de gobierno colegiados.
]

= 2. Identificación del Modelo de Administración Predominante

Para analizar el modelo de administración del CURZAS, se coteja la realidad institucional con la tipología teórica provista por Cao y Blutman (2019) y Abal Medina (2014). Según Cao y Blutman (2019), el modelo burocrático tradicional se enfoca en la formalidad de los procesos, la separación estricta de jerarquías y el apego a la norma legal. En contraste, la Nueva Gestión Pública (NGP) introducida en los años 90 busca flexibilizar estas estructuras, orientando la gestión hacia los resultados y el usuario como "cliente" de la administración.

== A. Rasgos del Modelo Burocrático Tradicional (Weberiano) — PREDOMINANTE

El análisis empírico demuestra la prevalencia estructural de la Burocracia Tradicional Weberiana. Como describen Cao y Blutman (2019), este modelo se asienta en la formalidad y el apego a la norma escrita:

- *Estructura Jerárquica y Centralizada:* La toma de decisiones normativo-administrativas responde a una línea fijada estatutariamente (Decanato -> Secretarías -> Direcciones -> Departamentos).
- *Principio de Legalidad y Procedimentalismo:* Todo acto administrativo debe encuadrarse estrictamente en resoluciones o reglamentos vigentes, supeditando la discrecionalidad a expedientes regulados.
- *Estatuto del Personal y Carrera Administrativa:* Rige un sistema rígido mediante Convenios Colectivos de Trabajo que garantizan estabilidad laboral y concursos de oposición, asegurando la imparcialidad funcionarial.

== B. Elementos Híbridos de la Nueva Gestión Pública (NGP)

A pesar del predominio burocrático, se identifican rasgos procedimentales e instrumentales de la NGP impulsados por la modernización del Estado:

- *Descentralización Operativa:* El CURZAS posee autonomía de gestión presupuestaria a través de su Consejo Directivo.
- *Orientación al Usuario/Estudiante:* Evidente en la digitalización de trámites mediante el ecosistema SIU-Guaraní y ventanillas únicas virtuales.

#callout("Dictamen del Modelo de Gestión")[
  *Conclusión:* El CURZAS presenta un *Modelo Burocrático Tradicional Fuertemente Formalizado con Hibridación Instrumental de NGP*.
]

= 3. Análisis de Mecanismos de Rendición de Cuentas (Accountability)

Tomando las dimensiones desarrolladas por Guillermo O'Donnell y sintetizadas por Abal Medina (2014), la rendición de cuentas puede dividirse conceptualmente en tres ejes: la accountability horizontal (donde agencias estatales controlan a otras agencias del mismo Estado), la vertical (donde la ciudadanía ejerce premio o castigo mediante elecciones) y la social (mecanismos de la sociedad civil para exigir transparencia e información). El CURZAS presenta mecanismos estructurados en estos tres ejes:

#v(4pt)

#table(
  columns: (1.2fr, 2.5fr, 1.8fr),
  fill: (col, row) => if row == 0 { primary } else if calc.even(row) { bg-card } else { white },
  stroke: 0.5pt + border-subtle,
  inset: (x: 9pt, y: 8pt),
  [#text(fill: white, weight: "bold", size: 9pt)[Tipo de Accountability]],
  [#text(fill: white, weight: "bold", size: 9pt)[Mecanismos Vigentes en CURZAS / UNCo]],
  [#text(fill: white, weight: "bold", size: 9pt)[Evidencia Documental / Normativa]],
  
  [
    *Horizontal* \
    #text(size: 8pt, fill: text-muted)[(Controles intra-estatales)]
  ],
  [
    - Auditoría Interna de la UNCo.
    - Auditoría General de la Nación (AGN) y SIGEN.
    - Control institucional entre órganos (Consejo Directivo evalúa las decisiones del Decanato).
  ],
  [
    - Informes periódicos de auditoría pública.
    - Ley 24.156 de Administración Financiera.
    - Memoria y Balance Anual.
  ],
  
  [
    *Vertical* \
    #text(size: 8pt, fill: text-muted)[(Electoral y Representativo)]
  ],
  [
    - Elecciones periódicas, directas y obligatorias para renovar autoridades (Decano/a) y representantes claustrales.
    - Cogobierno universitario integrado por Docentes, Nodocentes, Estudiantes y Graduados.
  ],
  [
    - Estatuto General de la UNCo.
    - Calendario electoral y resoluciones de la Junta Electoral Universidad.
  ],
  
  [
    *Social* \
    #text(size: 8pt, fill: text-muted)[(Ciudadanía e Infra-institucional)]
  ],
  [
    - Portal Institucional de Transparencia Activa.
    - Solicitudes de Acceso a la Información Pública.
    - Publicación de datos presupuestarios, licitaciones y nóminas en la web.
  ],
  [
    - Ley 27.275 de Acceso a la Información Pública.
    - Portal web de Transparencia Abierta UNCo.
  ]
)

= 4. Evaluación de Gobernanza Pública Inteligente (Según Oszlak)

Siguiendo los desarrollos teóricos de Oscar Oszlak (2020) sobre el tránsito desde el Gobierno Electrónico hacia el "Estado Inteligente" y la Gobernanza Algorítmica, se procedió a evaluar la presencia de automatización e Inteligencia Artificial en la organización.

== A. Digitalización e Interoperabilidad Administrativa (Fase Pre-Inteligente)
El CURZAS ha completado de manera satisfactoria la fase de digitalización burocrática mediante la implementación obligatoria del sistema SUDOCU y el ecosistema SIU. Esto permite trazabilidad, firmas digitales y gestión transparente.

== B. Análisis de la Pregunta Guía Específica: Algoritmos e IA en RR.HH.

#callout("Pregunta de Investigación Institucional")[
  _¿Cuenta el área con normativas vigentes sobre la incorporación de algoritmos o software predictivo en la selección o monitoreo de personal?_
]

*Resultado del Relevamiento Normativo e Institucional:*

- *Inexistencia de Sistemas Algorítmicos Predictivos:* Oszlak (2020) señala que la gobernanza algorítmica implica el uso de tecnologías disruptivas y automatizadas (como la Inteligencia Artificial) para la toma de decisiones públicas. En el CURZAS, no existen iniciativas normativas para implementar software predictivo en la selección de personal o el monitoreo disciplinario.
- *Garantía de Control Humano y Paritario:* La adopción de IA en RR.HH. se encuentra bloqueada normativamente. El concurso público se rige 100% por jurados y comisiones paritarias integradas por personas humanas, garantizado por Convenios Colectivos de Trabajo. La evaluación algorítmica está excluida, demostrando que la barrera a la IA no es meramente tecnológica, sino institucional y sindical.
- *Estado Actual en la Escala de Oszlak:* El organismo ha consolidado la fase de "Gobierno Electrónico" y Digitalización Avanzada de Trámites (expediente digital), pero se encuentra aún distante de la fase de "Estado Inteligente" y Gobernanza Algorítmica en el control de sus recursos humanos.

= 5. Conclusión Sintética

El CURZAS constituye un modelo claro de administración pública universitaria donde se conjuga una matriz burocrática tradicional garante de derechos laborales, con herramientas de la Nueva Gestión Pública orientadas a la transparencia y digitalización. La incorporación de la Inteligencia Artificial (Estado Inteligente propuesto por Oszlak) permanece como una asignatura pendiente, fuertemente regulada y limitada por los mecanismos constitucionales y paritarios vigentes.

#pagebreak()

// ==========================================
// 3. HOJA DE FUENTES Y BIBLIOGRAFÍA
// ==========================================

#v(15pt)

#rect(
  width: 100%,
  fill: bg-card,
  stroke: 0.5pt + border-subtle,
  radius: 6pt,
  inset: (x: 18pt, y: 16pt)
)[
  #text(weight: "bold", size: 12pt, fill: primary)[Bibliografía y Fuentes Consultadas]
  #v(8pt)
  #line(length: 100%, stroke: 0.6pt + accent)
  #v(12pt)
  
  #set text(size: 9pt, fill: text-main)
  - *Cao, Horacio y Blutman, Gustavo (2019).* _Continuidades y rupturas en las ideas sobre reforma y modernización del Estado._ Buenos Aires: INAP / Universidad de Buenos Aires.
  - *Abal Medina, Juan Manuel (2014).* _Manual de Administración Pública._ Buenos Aires: Ariel. Capítulos 1 y 5.
  - *Oszlak, Oscar (2020).* _El Estado en la era exponencial: Tecnologías disruptivas y gestión pública._ Buenos Aires: Editorial INAP.
  - *Universidad Nacional del Comahue (1993/2023).* _Estatuto de la Universidad Nacional del Comahue._ Neuquén/Viedma.
  - *Leyes Nacionales y Convenios:* Ley de Educación Superior N° 24.521; Ley de Acceso a la Información Pública N° 27.275; Convenios Colectivos de Trabajo Decretos 366/06 y 1246/15.
]
