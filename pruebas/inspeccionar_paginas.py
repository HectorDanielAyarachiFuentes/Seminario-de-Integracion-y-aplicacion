import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
print(f'Total pages in PDF: {len(reader.pages)}')

for p_num in range(18, 26):
    if p_num < len(reader.pages):
        txt = reader.pages[p_num].extract_text()
        first_line = txt.strip().split('\n')[0] if txt.strip() else 'EMPTY'
        last_line = txt.strip().split('\n')[-1] if txt.strip() else 'EMPTY'
        chars = len(txt.strip())
        print(f"Pág {p_num+1} (chars: {chars}): First: '{first_line[:60]}' | Last: '{last_line[:60]}'")
