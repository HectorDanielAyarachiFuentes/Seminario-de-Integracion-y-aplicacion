import re
import os
import pypdf

# 1. Cargar PDF
pdf_path = "entregas/actividad_4/TP4_Ayarachi_Fuentes.pdf"
reader = pypdf.PdfReader(pdf_path)
total_pages = len(reader.pages)
full_text = ""
page_texts = {}
for i, page in enumerate(reader.pages):
    t = page.extract_text()
    page_texts[i+1] = t
    full_text += f"\n--- PÁGINA {i+1} ---\n" + t

print(f"PDF cargado: {total_pages} páginas, {len(full_text)} caracteres.")

# 2. Cargar referencias.bib
bib_path = "entregas/actividad_4/quarto/referencias.bib"
with open(bib_path, "r", encoding="utf-8") as f:
    bib_content = f.read()

bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))
print(f"Total entradas en .bib: {len(bib_keys)}")

# 3. Cargar Quarto fuente para cruce de citas
qmd_path = "entregas/actividad_4/TP4_Ayarachi_Fuentes_COMPLETO.qmd"
with open(qmd_path, "r", encoding="utf-8") as f:
    qmd_content = f.read()

cited_keys = set(re.findall(r'@([a-zA-Z0-9_\-]+)', qmd_content))
# Filtrar posibles falsos positivos
cited_keys = {k for k in cited_keys if not k.startswith('fig') and not k.startswith('tbl') and not k.startswith('sec')}
print(f"Total claves citadas en QMD: {len(cited_keys)}")

# Citas huérfanas (citadas pero no en bib)
orphans = cited_keys - bib_keys
# Bibliografía no citada (en bib pero no en QMD)
uncited = bib_keys - cited_keys

print(f"\n[AUDITORÍA DE CITAS]")
print(f" - Citas huérfanas en texto: {orphans if orphans else 'NINGUNA (100% integradas)'}")
print(f" - Entradas en .bib sin citar: {uncited if uncited else 'NINGUNA (100% referenciadas)'}")

# 4. Auditoría de Cifras y Aritmética (Numbers Audit)
print(f"\n[AUDITORÍA DE NÚMEROS Y ARITMÉTICA]")

# Presupuesto: buscar cifras y sumas
print("\n--- Presupuesto (Tabla 4) ---")
m_presupuesto = re.search(r'Rubro.*?Total General.*?(\n|$)', qmd_content, re.DOTALL)
if m_presupuesto:
    lineas_tabla = m_presupuesto.group(0).splitlines()
    for l in lineas_tabla:
        if '|' in l:
            print("  ", l)

# Cronograma: meses
print("\n--- Cronograma (Tabla 3) ---")
m_crono = re.search(r'\| Etapa / Actividad Metodológica.*?(\n\n|\Z)', qmd_content, re.DOTALL)
if m_crono:
    print("  Cabecera cronograma:")
    print("  ", m_crono.group(0).splitlines()[0])

# Muestra y Población
print("\n--- Muestra N ---")
m_muestra = re.findall(r'(\b[Nn]\s*=\s*\d+|\bN\s*estimad[oa][^\.]*\.)', qmd_content)
for m in m_muestra[:10]:
    print("  ", m)

# 5. Auditoría de Figuras y Tablas
print(f"\n[AUDITORÍA DE TABLAS Y FIGURAS]")
tablas = re.findall(r'\*\*Tabla\s+(\d+)[^\*]*\*\*', qmd_content)
figuras = re.findall(r'\*\*Figura\s+(\d+)[^\*]*\*\*', qmd_content)
print(f" - Tablas detectadas: {sorted(list(set(tablas)))}")
print(f" - Figuras detectadas: {sorted(list(set(figuras)))}")

# Verificar menciones en el texto
for t in sorted(list(set(tablas))):
    count = len(re.findall(rf'Tabla\s+{t}\b', qmd_content))
    print(f"   Tabla {t}: {count} menciones en el texto")

for f in sorted(list(set(figuras))):
    count = len(re.findall(rf'Figura\s+{f}\b', qmd_content))
    print(f"   Figura {f}: {count} menciones en el texto")
