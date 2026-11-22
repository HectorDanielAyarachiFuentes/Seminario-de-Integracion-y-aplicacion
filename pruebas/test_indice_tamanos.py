import subprocess
import fitz

test_qmd = """# Primera parte de la estructura
## Tema de Investigación
### Encuadre Conceptual
### Contexto Institucional
## Delimitación del Objeto Problema
### Problematización
### Delimitaciones Metodológicas
## Justificación y Relevancia
## Definición de Objetivos
### Objetivo General
### Objetivos Específicos
## Matriz de Consistencia

# Segunda parte de la estructura
## Marco Teórico: Posicionamiento Teórico
### Posicionamiento Epistemológico
### El Enfoque Sistémico de Longo
### El Modelo de Retroalimentación 360
### Gobernanza Universitaria Multinivel
### Precisión Categorial
### Las Condiciones de Viabilidad
## Antecedentes de Investigación Empírica
### Antecedentes Internacionales
### Antecedentes Nacionales
### Marco Normativo e Institucional Situado
## Síntesis Integradora y Vacancia

# Tercera parte de la estructura
## Metodología / Materiales, Técnicas y Métodos
### Enfoque y Diseño
### Población y Muestra
### Técnicas e Instrumentos
### Matriz de Operacionalización
### Procedimiento y Fases
### Procesamiento y Análisis
### Consideraciones Éticas
## Cronograma de Actividades
## Viabilidad del Proyecto
### Recursos Económicos
### Recursos Humanos
### Recursos Técnicos
### Viabilidad Institucional

# Referencias Bibliográficas

# Anexos Metodológicos
## Anexo I: Guía de Entrevista
### Bloque A
### Bloque B
### Bloque C
## Anexo II: Cuestionarios Exploratorios
### Formulario A
### Formulario B
## Anexo III: Solicitud de Aval
## Anexo IV: Consentimiento Informado
"""

def compilar_y_verificar(nombre, depth, size, spacing, indent):
    qmd = f"""---
lang: es
format:
  typst:
    paper: a4
    margin:
      top: 2.54cm
      bottom: 2.54cm
      left: 2.54cm
      right: 2.54cm
    mainfont: "Arial"
    fontsize: 12pt
---

#set page(numbering: none)
#show outline.entry: set text(size: {size})
#show outline.entry: set block(spacing: {spacing})
#show outline.entry.where(level: 1): set text(weight: "bold")
#outline(title: [Índice de Contenidos], indent: {indent}, depth: {depth})

{{{{< pagebreak >}}}}

# Cuerpo del documento (Página 1 del texto)
Texto de prueba.
""" + test_qmd

    with open(f"pruebas/{nombre}.qmd", "w", encoding="utf-8") as f:
        f.write(qmd)
    
    cmd = f"quarto render pruebas/{nombre}.qmd --to typst"
    subprocess.run(cmd, shell=True, capture_output=True)
    
    pdf_path = f"pruebas/{nombre}.pdf"
    doc = fitz.open(pdf_path)
    print(f"[{nombre}] Total páginas: {doc.page_count}")
    # Renderizar página 1 (índice)
    page1 = doc.load_page(0)
    pix = page1.get_pixmap(dpi=150)
    pix.save(f"pruebas/{nombre}_page1.png")

print("Probando variantes...")
compilar_y_verificar("opcion_depth2_11pt", 2, "11pt", "0.75em", "1.5em")
compilar_y_verificar("opcion_depth2_10pt", 2, "10.5pt", "0.65em", "1.5em")
compilar_y_verificar("opcion_depth3_9pt", 3, "9pt", "0.45em", "1.2em")
