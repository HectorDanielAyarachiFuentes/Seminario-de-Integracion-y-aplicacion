import pymupdf
import docx

print("=== VERIFICACIÓN DE VARIABLES EN PDF ===")
doc_pdf = pymupdf.open("Entregas/Actividad 1/TP1_Ayarachi_Fuentes.pdf")
full_text = "\n".join([doc_pdf[i].get_text() for i in range(2, 6)])

labels = [
    "DATOS DEL ARTÍCULO CIENTÍFICO",
    "Título:",
    "Componentes identificados en el artículo científico",
    "Tipo de estudio",
    "Tema de Investigación",
    "Problema de Investigación",
    "Objetivo general",
    "Objetivos específicos",
    "Fundamentación (breve)",
    "Antecedentes (sólo autores y títulos de antecedentes)",
    "Marco teórico (solo autores principales)",
    "Tipo de Metodología",
    "Técnicas de recolección de datos",
    "Población, Muestra, Unidad de Análisis",
    "Resultados (brevemente comentar a qué resultados se llegó)"
]

for l in labels:
    presente = l in full_text
    print(f"  [{'OK' if presente else 'FALTA'}] {l}")

print("\n=== VERIFICACIÓN EN WORD ===")
doc_word = docx.Document("Entregas/Actividad 1/TP1_Ayarachi_Fuentes.docx")
word_text = "\n".join([c.text for t in doc_word.tables for row in t.rows for c in row.cells])
for l in labels[1:]:  # skip heading DATOS DEL ARTICULO
    presente = l in word_text
    print(f"  [{'OK' if presente else 'FALTA'}] {l}")
