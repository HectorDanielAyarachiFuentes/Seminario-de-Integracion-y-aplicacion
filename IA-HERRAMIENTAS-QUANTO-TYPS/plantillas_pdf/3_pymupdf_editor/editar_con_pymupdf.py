import pymupdf
import os

def demo_edicion_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
    
    source_pdf = os.path.join(workspace_dir, "Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
    output_pdf = os.path.join(script_dir, "documento_sellado_pymupdf.pdf")
    
    if not os.path.exists(source_pdf):
        print(f"❌ No se encontró el archivo base: {source_pdf}")
        return
        
    print(f"Abriendo PDF original ({source_pdf})...")
    doc = pymupdf.open(source_pdf)
    print(f"El documento tiene {len(doc)} páginas.")
    
    # Añadir un sello de agua en la primera página
    page = doc[0]
    rect = pymupdf.Rect(50, 750, 550, 780)
    page.insert_textbox(
        rect, 
        "DOCUMENTO OFICIALIZADO | UNCo - CURZAS (Verificado con PyMuPDF)", 
        fontsize=9, 
        color=(0.1, 0.2, 0.5), 
        align=pymupdf.TEXT_ALIGN_CENTER
    )
    
    doc.save(output_pdf)
    print(f"✅ PDF modificado y guardado en: {output_pdf}")

if __name__ == "__main__":
    demo_edicion_pdf()
