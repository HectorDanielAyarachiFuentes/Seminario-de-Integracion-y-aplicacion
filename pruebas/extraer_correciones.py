import fitz
import json
import os

pdf_path = "Entregas/Actividad 3/Correcion/TP3_Ayarachi_Fuentes.pdf"
doc = fitz.open(pdf_path)

results = []

for page_idx in range(len(doc)):
    page = doc[page_idx]
    annots = page.annots()
    if not annots:
        continue
    for a in annots:
        info = a.info
        rect = a.rect
        annot_type = a.type[1] if isinstance(a.type, (tuple, list)) else str(a.type)
        
        # Extract text in the annotation rectangle and a slightly expanded box
        rect_text = page.get_textbox(rect).strip().replace("\n", " ")
        expanded_rect = fitz.Rect(max(0, rect.x0 - 50), max(0, rect.y0 - 20), min(page.rect.width, rect.x1 + 50), min(page.rect.height, rect.y1 + 20))
        expanded_text = page.get_textbox(expanded_rect).strip().replace("\n", " ")

        results.append({
            "page": page_idx + 1,
            "author": info.get("title", ""),
            "content": info.get("content", ""),
            "subject": info.get("subject", ""),
            "type": annot_type,
            "date": info.get("modDate", ""),
            "rect_text": rect_text,
            "context": expanded_text
        })

os.makedirs("pruebas", exist_ok=True)
output_json = "pruebas/correciones_extraidas.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total de correcciones encontradas: {len(results)}")
print("=" * 70)
for idx, r in enumerate(results, 1):
    print(f"#{idx} | Página {r['page']} | Autor: {r['author']} | Tipo: {r['type']}")
    print(f"   Comentario: {r['content']}")
    print(f"   Texto referenciado: {r['rect_text']}")
    print(f"   Contexto: {r['context'][:140]}...")
    print("-" * 70)
