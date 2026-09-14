
#set page(paper: "a4", margin: 2.54cm)
#set text(font: "Segoe UI", size: 10pt)

#set table(
  stroke: (x, y) => if y == 0 { (top: 1pt + black, bottom: 0.5pt + black) } else if y == 12 { (bottom: 1pt + black) } else { none },
  inset: 7pt
)
#show table.cell.where(y: 0): set text(weight: "bold")

#table(
  columns: (35%, 65%),
  [Título:], [Componentes identificados en el artículo científico],
  [Título del artículo y Referencia APA 7], [Impacto de la Inteligencia Artificial...],
  [Tipo de estudio], [Empírico descriptivo...],
  [Tema de Investigación], [Incorporación de herramientas...],
  [Problema de Investigación], [¿De qué manera...?],
  [Objetivo general \ Objetivos específicos], [Analizar la incidencia...],
  [Fundamentación (breve)], [La tecnificación...],
  [Antecedentes (sólo autores y títulos de antecedentes)], [Tambe et al...],
  [Marco teórico (solo autores principales)], [Colquitt...],
  [Tipo de Metodología], [Cuantitativa...],
  [Técnicas de recolección de datos], [Cuestionario...],
  [Población, Muestra, Unidad de Análisis], [1200 trabajadores...],
  [Resultados (brevemente comentar a qué resultados se llegó)], [Se constató...]
)
