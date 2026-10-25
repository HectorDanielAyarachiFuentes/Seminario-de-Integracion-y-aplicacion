import pymupdf
from pathlib import Path

pdf_path = Path("Entregas/Actividad 4/TP4_Ayarachi_Fuentes.pdf")
doc = pymupdf.open(str(pdf_path))
print(f"Total pages in PDF: {len(doc)}")

headers = [
    "Viabilidad del Proyecto",
    "Referencias Bibliográficas",
    "Anexos Metodológicos",
    "Anexo I: Guía Temática",
    "Anexo II: Cuestionario Exploratorio",
    "Anexo III: Modelo de Nota Institucional",
    "Anexo IV: Formulario de Consentimiento",
]

for i, page in enumerate(doc):
    txt = page.get_text()
    found = [h for h in headers if h in txt]
    if found:
        # get bottom page number if present
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        last_line = lines[-1] if lines else ""
        print(f"Página física {i+1:2d} (número pie: {last_line:3s}): {', '.join(found)}")

print("\n--- DETALLE DE LAS ÚLTIMAS PÁGINAS ---")
for p in range(len(doc)-6, len(doc)):
    txt = doc[p].get_text()
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_few = " // ".join(lines[:2])
    last_few = " // ".join(lines[-2:])
    print(f"Pág {p+1}: INICIO: {first_few[:80]} | FIN: {last_few[:80]}")
