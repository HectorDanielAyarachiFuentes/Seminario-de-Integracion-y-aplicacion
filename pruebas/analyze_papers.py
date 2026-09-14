import re

def analyze_doc(filename, doc_num):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"==================================================")
    print(f"ANÁLISIS DOCUMENTO {doc_num}: {filename}")
    print(f"==================================================")

    # Search for key sections
    keywords = [
        "METODOLOGÍA", "MÉTODO", "TIPO DE INVESTIGACIÓN", "DISEÑO",
        "POBLACIÓN", "MUESTRA", "INSTRUMENTO", "RESULTADOS",
        "DISCUSIÓN", "CONCLUSIONES", "OBJETIVO", "PROBLEMA"
    ]

    for kw in keywords:
        matches = [m.start() for m in re.finditer(rf'(?i)\b{kw}\b', text)]
        print(f"Keyword '{kw}': {len(matches)} apariciones")

    # Extract abstract and methodology
    print("\n--- RESUMEN ---")
    resumen_match = re.search(r'(?i)resumen[\s\S]*?(?=abstract|introducción)', text)
    if resumen_match:
        print(resumen_match.group(0)[:1200])

    print("\n--- METODOLOGÍA (primeros 1500 caracteres) ---")
    metod_match = re.search(r'(?i)(?:metodología|método|materiales y métodos)[\s\S]*?(?=resultados|discusión|análisis)', text)
    if metod_match:
        print(metod_match.group(0)[:1500])

    print("\n--- CONCLUSIONES / RESULTADOS (resumen) ---")
    concl_match = re.search(r'(?i)(?:conclusiones|conclusión)[\s\S]*?(?=referencias|bibliografía|$)', text)
    if concl_match:
        print(concl_match.group(0)[:1500])

analyze_doc('pruebas/doc1_full.txt', 1)
analyze_doc('pruebas/doc2_full.txt', 2)
