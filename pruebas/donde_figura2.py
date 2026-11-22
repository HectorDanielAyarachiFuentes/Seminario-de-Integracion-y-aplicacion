import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    if 'Figura 2' in txt:
        print(f"Figura 2 is on PDF Page {i+1}")
        print(txt[:300])
