# 🧠 Memoria Técnica y Soluciones Docs-as-Code (SIA — CURZAS)

Este documento reúne las soluciones de ingeniería de documentos, trucos de maquetación y configuraciones de bajo nivel implementadas en el pipeline de compilación dual (`compilar_todos.py`), asegurando que todos los Trabajos Prácticos y el TFG cumplan con el estándar institucional y APA 7ma Edición.

---

## 1. Centrado del Logotipo Institucional en Quarto

* **Sintaxis limpia en Quarto puro:**
  Para evitar que Pandoc interprete la imagen como figura y le inserte automáticamente leyendas no deseadas (como *"Figura 1"*), se emplea un bloque de alineación limpio:
  ```markdown
  ::: {align="center"}
  ![](../../assets/img/CURZAS.png){width=135px}
  :::
  ```
* **Post-procesamiento en Word (`.docx`):**
  Pandoc no centra por defecto los objetos de dibujo (`w:drawing`). El compilador `compilar_todos.py` localiza el párrafo que contiene el drawing del logotipo y le asigna `p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER`.
* **Post-procesamiento en PDF (`.pdf`):**
  Mediante PyMuPDF, el compilador verifica las coordenadas de la imagen en la carátula y la centra matemáticamente respecto al ancho de página (`cover.rect.width / 2`).

---

## 2. Paginación Normativa APA 7 (Carátula limpia, inicio en 1)

* **Regla Académica:**
  1. La carátula (página de título) jamás debe mostrar número de página visible.
  2. La página de desarrollo del trabajo (a partir de la Introducción) debe comenzar su numeración visible desde el número **1**.
* **Implementación en Word (`.docx`):**
  * Para documentos con secciones múltiples: desvincular el pie de página (`sec1.footer.is_linked_to_previous = False`), insertar el campo XML dinámico `<w:fldSimple w:instr="PAGE"/>` y configurar `<w:pgNumType w:start="1"/>`.
  * Para documentos de una sola sección: activar `different_first_page_header_footer = True`, insertar el campo `{PAGE}` en el pie de página general y establecer el inicio de sección en `w:start="0"`.
* **Implementación en PDF (`.pdf`):**
  PyMuPDF localiza el bloque de texto con el número "1" en el tercio inferior de la carátula y le aplica una anotación de redacción con relleno blanco, preservando la numeración visible en las hojas siguientes.

---

## 3. Tablas Estilo APA 7ma Edición

* **Regla Normativa:** Prohibición estricta de líneas verticales y cuadrículas enrejadas. Únicamente 3 líneas horizontales principales:
  * Borde superior de la tabla: 1 pt.
  * Borde divisor del encabezado (fila 0): 0.5 pt a 0.75 pt.
  * Borde inferior de la tabla: 1 pt.
* **Implementación en Word (`.docx`):**
  El compilador inyecta OpenXML en las propiedades de la tabla (`tblPr`):
  * `w:insideH="none"` y `w:insideV="none"` para eliminar rejillas internas.
  * `w:top="single" w:sz="8"` y `w:bottom="single" w:sz="8"`.
  * `tcBorders` inferior con `w:sz="6"` en cada celda de la fila de cabecera.
* **Implementación en Typst (`.typ`):**
  Se define en `include-before-body` una regla `#show table` con `stroke: none`, agregando líneas selectivas en la cabecera y el fondo.

---

## 4. Referencias Bibliográficas con Sangría Francesa (*Hanging Indent*)

* **Regla Normativa:** Sangría francesa obligatoria de 1,27 cm (0,5 pulg / 36 pt) en todas las líneas siguientes a la primera en cada entrada bibliográfica.
* **Implementación en Word (`.docx`):**
  El script detecta la sección posterior al encabezado `# Referencias` y aplica a cada párrafo:
  * `paragraph_format.left_indent = Inches(0.5)`
  * `paragraph_format.first_line_indent = Inches(-0.5)`
  * `paragraph_format.space_after = Pt(6)`
* **Implementación en Typst (`.typ`):**
  Se antecede al título de referencias el bloque:
  ````markdown
  ```{=typst}
  #set par(hanging-indent: 1.5em, justify: false)
  ```
  ````

---

## 5. Índice de Contenidos Dinámico y Sin Duplicaciones

* **Regla de Redacción:** En el archivo `.qmd` no se deben anteponer números manuales a los encabezados (escribir `# Introducción` en lugar de `# 1. Introducción`) para evitar que `number-sections: true` duplique la numeración en Word o PDF (ej. *"1. 1. Introducción"*).
* **OpenXML Nativo:** `compilar_todos.py` inserta el campo nativo `<w:instrText> TOC \o "1-3" \h \z \u </w:instrText>` con tabulación dot leader hacia la posición `9026` y activa `<w:updateFields w:val="true"/>` para refresco automático al abrir en Microsoft Word.
