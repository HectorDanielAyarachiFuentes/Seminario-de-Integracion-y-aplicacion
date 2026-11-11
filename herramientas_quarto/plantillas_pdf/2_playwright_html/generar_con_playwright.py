from playwright.sync_api import sync_playwright
import os

def generar_pdf_desde_html():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_html = os.path.join(script_dir, "plantilla.html")
    output_pdf = os.path.join(script_dir, "ejemplo_playwright.pdf")
    
    print("Leyendo plantilla HTML...")
    with open(input_html, "r", encoding="utf-8") as f:
        html_content = f.read()

    print("Renderizando PDF con Chromium...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        page.pdf(path=output_pdf, format="A4", print_background=True)
        browser.close()
        
    print(f"✅ PDF generado exitosamente en: {output_pdf}")

if __name__ == "__main__":
    generar_pdf_desde_html()
