import pypdf

reader = pypdf.PdfReader('entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf')
print("=== PÁGINA 22 (Body 20) ===")
print(reader.pages[21].extract_text())

print("\n=== PÁGINA 23 (Body 21) ===")
print(reader.pages[22].extract_text())

print("\n=== PÁGINA 24 (Body 22) ===")
print(reader.pages[23].extract_text())
