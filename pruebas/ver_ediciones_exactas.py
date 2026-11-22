import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
txt = reader.pages[30].extract_text()
for line in txt.splitlines():
    if 'Lepsinger' in line or 'Hernández' in line or 'Chiavenato' in line or 'Wainerman' in line or 'ed.' in line:
        print(repr(line))
