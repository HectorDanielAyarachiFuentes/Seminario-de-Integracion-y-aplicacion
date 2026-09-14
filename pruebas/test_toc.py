import docx
import shutil
from pathlib import Path
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

src = Path('Entregas/Actividad 1/TP1_Ayarachi_Fuentes.docx')
dst = Path('pruebas/test_output.docx')
shutil.copy2(src, dst)

doc = docx.Document(str(dst))

p_toc = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip() == 'Índice de Contenidos':
        p_toc = p
        print(f'Encontrado en parrafo {i}')
        break

if p_toc:
    next_p = p_toc._p.getnext()
    if next_p is not None and 'TOC' in next_p.xml:
        next_p.getparent().remove(next_p)
        print('TOC viejo removido')

items = [
    ('1. Introducción y Objetivos de la Actividad', 1, 2),
    ('1.1 Objetivos', 2, 2),
    ('2. Matriz Metodológica: Artículo Científico N° 1', 1, 3),
    ('3. Matriz Metodológica: Artículo Científico N° 2', 1, 6),
    ('4. Síntesis Comparativa y Aportes al Proyecto de TFG', 1, 9),
    ('Referencias Bibliográficas', 1, 10),
]

curr = p_toc._p
tab_pos = '9026'

begin_xml = (
    f'<w:p {nsdecls("w")}>'
    f'<w:pPr><w:spacing w:after="120"/></w:pPr>'
    f'<w:r>'
    f'<w:fldChar w:fldCharType="begin"/>'
    f'<w:instrText xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>'
    f'<w:fldChar w:fldCharType="separate"/>'
    f'</w:r>'
    f'</w:p>'
)
p_begin = parse_xml(begin_xml)
curr.addnext(p_begin)
curr = p_begin

for texto, nivel, num_pag in items:
    style_name = f'TOC{nivel}'
    left_indent = '280' if nivel == 2 else '0'
    item_xml = (
        f'<w:p {nsdecls("w")}>'
        f'<w:pPr>'
        f'<w:pStyle w:val="{style_name}"/>'
        f'<w:tabs>'
        f'<w:tab w:val="right" w:leader="dot" w:pos="{tab_pos}"/>'
        f'</w:tabs>'
        f'<w:ind w:left="{left_indent}"/>'
        f'<w:spacing w:after="60"/>'
        f'</w:pPr>'
        f'<w:r>'
        f'<w:rPr>'
        f'<w:rFonts w:ascii="Segoe UI" w:hAnsi="Segoe UI"/>'
        f'<w:sz w:val="20"/>'
        f'</w:rPr>'
        f'<w:t>{texto}</w:t>'
        f'</w:r>'
        f'<w:r>'
        f'<w:tab/>'
        f'</w:r>'
        f'<w:r>'
        f'<w:rPr>'
        f'<w:rFonts w:ascii="Segoe UI" w:hAnsi="Segoe UI"/>'
        f'<w:sz w:val="20"/>'
        f'</w:rPr>'
        f'<w:t>{num_pag}</w:t>'
        f'</w:r>'
        f'</w:p>'
    )
    p_item = parse_xml(item_xml)
    curr.addnext(p_item)
    curr = p_item

end_xml = (
    f'<w:p {nsdecls("w")}>'
    f'<w:r>'
    f'<w:fldChar w:fldCharType="end"/>'
    f'</w:r>'
    f'</w:p>'
)
p_end = parse_xml(end_xml)
curr.addnext(p_end)

# Configurar w:updateFields en settings.xml
try:
    settings = doc.settings.element
    update_fields = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
    settings.append(update_fields)
    print("w:updateFields activado en settings.xml")
except Exception as e:
    print(f"No se pudo agregar updateFields: {e}")

doc.save(str(dst))
print('Guardado test_output.docx exitosamente')
