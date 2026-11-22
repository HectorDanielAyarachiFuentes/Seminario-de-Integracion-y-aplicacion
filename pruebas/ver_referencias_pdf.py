import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    if 'Lepsinger' in txt:
        print(f"Lepsinger found on PDF Page {i+1}:")
        for line in txt.splitlines():
            if 'Lepsinger' in line or 'Chiavenato' in line or 'Wainerman' in line or 'Hernández' in line:
                print("  ", line)
