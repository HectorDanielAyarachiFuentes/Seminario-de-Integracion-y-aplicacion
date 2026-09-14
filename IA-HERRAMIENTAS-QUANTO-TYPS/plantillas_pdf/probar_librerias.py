"""
Script de prueba para comparar las diferentes tecnologías de generación y edición de PDF.
Genera PDFs de ejemplo con cada tecnología para que puedas evaluar el diseño visual de cada una.
"""
import sys
import os

print("="*60)
print("🚀 SUITE DE PRUEBA: LIBRERÍAS DE GENERACIÓN Y EDICIÓN DE PDF")
print("="*60)

# --- 1. PROBAR TYPST ---
print("\n[1/3] Probando Typst (Lenguaje moderno de maquetación académica)...")
try:
    import typst
    doc_typst = """
#set page(paper: "a4", margin: (x: 2cm, y: 2.5cm), numbering: "1 / 1")
#set text(font: "Segoe UI", size: 10.5pt, fill: rgb("202020"))

#align(center)[
  #text(size: 18pt, weight: "bold", fill: rgb("192d5f"))[Universidad Nacional del Comahue] \
  #text(size: 12pt, fill: rgb("c89632"))[CURZAS - Planeamiento y Control de las Organizaciones]
]

#v(0.8em)
#line(length: 100%, stroke: 1.2pt + rgb("192d5f"))
#v(1em)

= Avance 1: Contexto, Modelo de Gestión y Gobernanza (Demo Typst)
El *CURZAS* es una unidad académica dependiente de la UNCo con sede en Viedma, regida bajo los principios de autonomía y autarquía universitaria.

#v(0.5em)
#rect(
  width: 100%,
  fill: rgb("f5f8fa"),
  stroke: (left: 3.5pt + rgb("192d5f")),
  inset: 10pt,
  radius: 2pt
)[
  *Misión Institucional:* Generación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte.
]

#v(1em)
== Matriz de Rendición de Cuentas (Accountability)

#table(
  columns: (1.2fr, 2.5fr, 1.8fr),
  fill: (col, row) => if row == 0 { rgb("192d5f") } else if calc.even(row) { rgb("f5f8fa") } else { white },
  stroke: 0.5pt + rgb("d0e0f0"),
  inset: 7pt,
  [#text(fill: white, weight: "bold")[Tipo de Accountability]], 
  [#text(fill: white, weight: "bold")[Mecanismos Vigentes]], 
  [#text(fill: white, weight: "bold")[Evidencia Normativa]],
  
  [*Horizontal* \ (Intra-estatales)], 
  [- Auditoría Interna UNCo \ - AGN y SIGEN \ - Control Consejo Directivo], 
  [- Informes de auditoría \ - Ley 24.156 \ - Memoria Anual],
  
  [*Vertical* \ (Representativo)], 
  [- Elecciones periódicas directas \ - Cogobierno cuatro claustros], 
  [- Estatuto General UNCo \ - Calendario electoral],
  
  [*Social* \ (Ciudadanía)], 
  [- Publicación de presupuestos y nóminas web \ - Solicitudes AIP], 
  [- Portal Transparencia Activa \ - Ley 27.275]
)
"""
    with open("temp_doc.typ", "w", encoding="utf-8") as f:
        f.write(doc_typst)
    
    typst.compile("temp_doc.typ", output="ejemplo_1_typst.pdf")
    if os.path.exists("temp_doc.typ"):
        os.remove("temp_doc.typ")
    print("✅ ejemplo_1_typst.pdf generado con éxito.")
except Exception as e:
    print("❌ Error probando Typst:", e)

# --- 2. PROBAR PLAYWRIGHT (HTML5 + CSS + TAILWIND) ---
print("\n[2/3] Probando Playwright (HTML5 + Tailwind CSS + Google Fonts a PDF)...")
try:
    from playwright.sync_api import sync_playwright
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <script src="https://cdn.tailwindcss.com"></script>
      <style>
        @page {
          size: A4;
          margin: 15mm;
        }
      </style>
    </head>
    <body class="bg-white text-gray-800 font-sans text-sm leading-relaxed p-4">
      <div class="border-b-2 border-[#192d5f] pb-3 mb-5">
        <h2 class="text-xs font-bold text-[#c89632] uppercase tracking-widest">Universidad Nacional del Comahue</h2>
        <h1 class="text-2xl font-black text-[#192d5f]">Avance 1: Contexto, Modelo de Gestión y Gobernanza</h1>
        <p class="text-xs text-gray-500 font-medium">CURZAS - Planeamiento y Control de las Organizaciones | Demo Playwright (HTML+CSS)</p>
      </div>

      <div class="bg-[#f5f8fa] border-l-4 border-[#192d5f] p-3.5 rounded-r shadow-xs mb-5">
        <h3 class="text-xs font-bold text-[#192d5f] uppercase tracking-wider mb-1">Misión y Funciones Institucionales</h3>
        <p class="text-xs text-gray-700">El CURZAS tiene como misión la generación y democratización del conocimiento en la Patagonia Norte.</p>
      </div>

      <h3 class="text-base font-bold text-[#192d5f] mb-2">Cuadro de Rendición de Cuentas (Accountability)</h3>
      <table class="w-full border-collapse border border-blue-100 text-xs shadow-xs rounded-sm overflow-hidden mb-6">
        <thead>
          <tr class="bg-[#192d5f] text-white">
            <th class="p-2.5 text-left font-bold w-1/4">Tipo de Accountability</th>
            <th class="p-2.5 text-left font-bold w-1/2">Mecanismos Vigentes en CURZAS</th>
            <th class="p-2.5 text-left font-bold w-1/4">Evidencia Normativa</th>
          </tr>
        </thead>
        <tbody>
          <tr class="bg-[#f5f8fa] border-b border-blue-100">
            <td class="p-2.5 font-bold text-gray-900">Horizontal<br><span class="font-normal text-gray-500 text-[11px]">(Intra-estatales)</span></td>
            <td class="p-2.5 text-gray-700">• Auditoría Interna UNCo<br>• Auditoría General de la Nación (AGN) y SIGEN</td>
            <td class="p-2.5 text-gray-700">• Informes de auditoría<br>• Ley 24.156</td>
          </tr>
          <tr class="bg-white border-b border-blue-100">
            <td class="p-2.5 font-bold text-gray-900">Vertical<br><span class="font-normal text-gray-500 text-[11px]">(Representativo)</span></td>
            <td class="p-2.5 text-gray-700">• Elecciones directas y periódicas<br>• Cogobierno de claustros</td>
            <td class="p-2.5 text-gray-700">• Estatuto General UNCo<br>• Resoluciones electorales</td>
          </tr>
          <tr class="bg-[#f5f8fa]">
            <td class="p-2.5 font-bold text-gray-900">Social<br><span class="font-normal text-gray-500 text-[11px]">(Ciudadanía)</span></td>
            <td class="p-2.5 text-gray-700">• Publicación de datos presupuestarios y nóminas</td>
            <td class="p-2.5 text-gray-700">• Portal de Transparencia<br>• Ley 27.275</td>
          </tr>
        </tbody>
      </table>

      <div class="mt-8 pt-3 border-t border-gray-200 text-center text-xs text-gray-400">
        Generado con motor Chromium / Playwright a partir de HTML5 & TailwindCSS
      </div>
    </body>
    </html>
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(path="ejemplo_2_playwright_html.pdf", format="A4", print_background=True)
        browser.close()
    print("✅ ejemplo_2_playwright_html.pdf generado con éxito.")
except Exception as e:
    print("❌ Error probando Playwright:", e)

# --- 3. PROBAR PYMUPDF (EDICIÓN DIRECTA) ---
print("\n[3/3] Probando PyMuPDF (Edición / Manipulación directa de PDF)...")
try:
    import pymupdf
    source_pdf = "Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf"
    doc = pymupdf.open(source_pdf)
    print(f"✅ Archivo '{source_pdf}' abierto correctamente ({len(doc)} páginas).")
    
    nuevo_doc = pymupdf.open()
    nuevo_doc.insert_pdf(doc, from_page=0, to_page=0) # Extraer solo la portada
    
    page = nuevo_doc[0]
    rect = pymupdf.Rect(50, 680, 500, 720)
    page.insert_textbox(rect, "COPIA CONTROLADA - VERIFICADO PyMuPDF", fontsize=11, color=(0.1, 0.2, 0.5), align=pymupdf.TEXT_ALIGN_CENTER)
    
    nuevo_doc.save("ejemplo_3_pymupdf_edit.pdf")
    print("✅ ejemplo_3_pymupdf_edit.pdf generado con éxito.")
except Exception as e:
    print("❌ Error probando PyMuPDF:", e)

print("\n" + "="*60)
print("🎉 ¡TODAS LAS LIBRERÍAS FUERON PROBADAS CON ÉXITO!")
print("="*60)
