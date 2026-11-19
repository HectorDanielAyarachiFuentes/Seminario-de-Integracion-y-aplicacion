import docx
from docx.shared import Inches, Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document(r"TP Alejandra\entregas\TP_Alejandra_Proyecto_TFG_SIA_2026.docx")

# Inspeccionar párrafos de la portada
pb_idx = 8
for i, p in enumerate(doc.paragraphs[:pb_idx+1]):
    print(f"P{i:02d}: {p.text[:35]}")
