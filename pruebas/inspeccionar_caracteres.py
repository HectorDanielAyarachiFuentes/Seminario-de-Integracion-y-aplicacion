import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
# Find page with Lepsinger bibliography entry
for idx, page in enumerate(reader.pages):
    txt = page.extract_text()
    if 'Lepsinger, R.' in txt:
        print(f"Found on PDF page {idx+1}")
        for line in txt.splitlines():
            if 'Lepsinger' in line or '360 degree' in line or 'feedback' in line:
                print("Line:", line)
                for char in line:
                    if char in '0123456789.ªaºed() ':
                        print(f"'{char}' (U+{ord(char):04X})", end=' ')
                print()
