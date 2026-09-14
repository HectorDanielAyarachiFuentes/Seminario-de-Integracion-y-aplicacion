# 📚 Guía de Librerías de Generación y Edición de PDFs en Python

Esta guía detalla las mejores librerías instaladas en el entorno, sus fortalezas, ejemplos prácticos de código y cuándo elegir cada una para diseñar documentos, reportes y presentaciones de alta calidad estética.

---

## 📋 Resumen Rápido de Herramientas

| Librería | Enfoque Principal | Facilidad de Diseño | Ideal Para |
| :--- | :--- | :--- | :--- |
| **1. WeasyPrint** | HTML5 + CSS Paged Media | ⭐⭐⭐⭐⭐ (Web / CSS) | Informes corporativos, plantillas reutilizables, facturas, catálogos. |
| **2. Typst** | Lenguaje moderno de maquetación (markup) | ⭐⭐⭐⭐⭐ (Minimalista / Markdown) | Trabajos académicos, tesis, papers científicos, reportes ejecutivos. |
| **3. Playwright** | Chromium Headless (HTML + JS + Tailwind) | ⭐⭐⭐⭐⭐ (Pixel-Perfect) | Reportes con gráficos dinámicos (Chart.js, D3.js), diseños ultra-modernos. |
| **4. PyMuPDF (`fitz`)** | Edición y manipulación directa de PDF | ⭐⭐⭐⭐ (Manipulación) | Buscar/reemplazar texto en PDFs existentes, unir/dividir páginas, extraer datos. |
| **5. FPDF2 / ReportLab** | Código imperativo en Python (celdas, líneas) | ⭐⭐⭐ (Manual / Coordenadas) | PDFs ligeros sin dependencias externas pesadas o flujos muy simples. |

---

## 1. 🥇 WeasyPrint (HTML + CSS a PDF)
Convierte cualquier archivo HTML estilizado con CSS a un PDF de calidad editorial. Permite usar variables de Jinja2 para crear plantillas dinámicas.

### 📦 Instalación
```bash
pip install weasyprint jinja2
```

### 💻 Ejemplo de Uso
```python
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
    @page {
        size: A4;
        margin: 20mm;
        @bottom-right {
            content: "Página " counter(page) " de " counter(pages);
            font-size: 9pt;
            color: #888;
        }
    }
    body { font-family: 'Segoe UI', Arial, sans-serif; color: #333; }
    h1 { color: #192d5f; border-bottom: 2px solid #c89632; padding-bottom: 5px; }
    .box { background: #f5f8fa; border-left: 4px solid #192d5f; padding: 12px; border-radius: 4px; }
    table { width: 100%; border-collapse: collapse; margin-top: 15px; }
    th { background: #192d5f; color: white; text-align: left; padding: 8px; }
    td { padding: 8px; border-bottom: 1px solid #ddd; }
    tr:nth-child(even) { background: #f9fbfd; }
</style>
</head>
<body>
    <h1>Reporte de Gestión Institucional</h1>
    <div class="box">
        <p><strong>Estado:</strong> Aprobado y verificado bajo normativas vigentes.</p>
    </div>
    <table>
        <thead>
            <tr><th>Dimensión</th><th>Mecanismo</th></tr>
        </thead>
        <tbody>
            <tr><td>Horizontal</td><td>Auditoría Interna y SIGEN</td></tr>
            <tr><td>Vertical</td><td>Elecciones y Cogobierno</td></tr>
        </tbody>
    </table>
</body>
</html>
"""

HTML(string=html_content).write_pdf("reporte_weasyprint.pdf")
print("PDF generado con WeasyPrint!")
```

---

## 2. ⚡ Typst (El reemplazo moderno de LaTeX)
Typst permite escribir documentos elegantes mediante sintaxis intuitiva similar a Markdown con control tipográfico profesional y soporte para plantillas prehechas.

### 📦 Instalación
```bash
pip install typst
```

### 💻 Ejemplo de Uso en Python
```python
import typst

typst_content = """
#set page(paper: "a4", margin: (x: 2cm, y: 2.5cm), numbering: "1 / 1")
#set text(font: "Segoe UI", size: 10.5pt, fill: rgb("202020"))

#align(center)[
  #text(size: 18pt, weight: "bold", fill: rgb("192d5f"))[Universidad Nacional del Comahue] \
  #text(size: 13pt, fill: rgb("c89632"))[CURZAS - Planeamiento y Control]
]

#v(1em)
#line(length: 100%, stroke: 1pt + rgb("192d5f"))
#v(1em)

= 1. Identificación y Marco Institucional
El *CURZAS* es una unidad académica que goza de autonomía y autarquía universitaria.

#rect(
  width: 100%,
  fill: rgb("f5f8fa"),
  stroke: (left: 3pt + rgb("192d5f")),
  inset: 10pt,
  radius: 2pt
)[
  *Misión Institucional:* Formación y democratización del conocimiento en la Patagonia Norte.
]

#v(1em)
== Cuadro de Rendición de Cuentas

#table(
  columns: (1fr, 2fr),
  fill: (col, row) => if row == 0 { rgb("192d5f") } else if calc.even(row) { rgb("f5f8fa") } else { white },
  stroke: 0.5pt + rgb("d0e0f0"),
  inset: 7pt,
  [#text(fill: white, weight: "bold")[Tipo]], [#text(fill: white, weight: "bold")[Mecanismos]],
  [*Horizontal*], [- Auditoría Interna UNCo \ - AGN y SIGEN],
  [*Vertical*], [- Elecciones directas \ - Cogobierno universitario]
)
"""

typst.compile(typst_content, output="reporte_typst.pdf")
print("PDF generado con Typst!")
```

---

## 3. 🌐 Playwright (Chromium Headless)
Renderiza código HTML/CSS/JS exactamente como se vería en Google Chrome y lo guarda en PDF con soporte completo para TailwindCSS, Google Fonts, gráficos interactivos e imágenes.

### 📦 Instalación
```bash
pip install playwright
playwright install chromium
```

### 💻 Ejemplo de Uso
```python
from playwright.sync_api import sync_playwright

html = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="p-10 font-sans text-gray-800">
  <div class="border-b-4 border-blue-900 pb-4 mb-6">
    <h1 class="text-3xl font-bold text-blue-900">Informe de Gobernanza y Modelos de Gestión</h1>
    <p class="text-amber-600 font-semibold mt-1">CURZAS - Universidad Nacional del Comahue</p>
  </div>
  
  <div class="bg-blue-50 border-l-4 border-blue-900 p-4 rounded-r shadow-sm mb-6">
    <p class="text-sm text-gray-700"><strong>Dictamen:</strong> Burocracia Weberiana con hibridación NGP.</p>
  </div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html)
    page.pdf(path="reporte_playwright.pdf", format="A4", print_background=True)
    browser.close()

print("PDF generado con Playwright!")
```

---

## 4. ✏️ PyMuPDF (`fitz` - Modificación Directa de PDFs)
Ideal para modificar PDFs ya existentes sin tener que volver a generarlos desde cero.

### 📦 Instalación
```bash
pip install pymupdf
```

### 💻 Ejemplo de Uso (Inspección y Reemplazo)
```python
import fitz  # PyMuPDF

# Abrir un PDF existente
doc = fitz.open("Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
print(f"Total de páginas: {len(doc)}")

# Leer texto de la primera página
page1 = doc[0]
print(page1.get_text()[:200])

# Guardar una copia o exportar páginas
doc.save("copia_reporte.pdf")
```

---

## 🎯 ¿Cuál usar para tus próximos trabajos?

1. **Si quieres diseñar en HTML/CSS como una página web:** Usa **WeasyPrint** o **Playwright**. Te permite separar el diseño (`.css`) del contenido (`.html`).
2. **Si buscas rapidez, elegancia y formato tipo Markdown/Paper:** Usa **Typst**. Es moderno, rápido y tiene una sintaxis muy limpia.
3. **Si necesitas editar/manipular un PDF ya cerrado:** Usa **PyMuPDF**.
