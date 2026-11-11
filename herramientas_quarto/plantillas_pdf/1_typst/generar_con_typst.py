import typst
import os

def compilar_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_typ = os.path.join(script_dir, "documento.typ")
    output_pdf = os.path.join(script_dir, "ejemplo_typst.pdf")
    
    print("Compilando documento con Typst...")
    typst.compile(input_typ, output=output_pdf)
    print(f"✅ PDF generado exitosamente en: {output_pdf}")

if __name__ == "__main__":
    compilar_pdf()
