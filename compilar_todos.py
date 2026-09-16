"""
=============================================================================
BUILD AUTOMATION: Seminario de Integración y Aplicación (SIA 2025/2026)
CURZAS — Universidad Nacional del Comahue
Autor: Héctor Daniel Ayarachi Fuentes
=============================================================================
Flujo unificado basado en Quarto (.qmd):
Genera automáticamente tanto la versión en formato Word (.docx) como la versión
en formato PDF (.pdf) directamente hacia la carpeta Entregas/.

Uso:
    python compilar_todos.py            # Compila TP1 (o todos los activos) a PDF y Word (.docx)
    python compilar_todos.py --pdf      # Solo compila PDF
    python compilar_todos.py --word     # Solo compila Word (.docx)
    python compilar_todos.py --watch    # Monitorea cambios en vivo y recompila automáticamente
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
ENTREGAS_DIR = ROOT_DIR / "Entregas"
ACTIVIDAD1_DIR = ENTREGAS_DIR / "Actividad 1"
ACTIVIDAD2_DIR = ENTREGAS_DIR / "Actividad 2"

DOCUMENTOS = [
    {
        "id": "TP1",
        "nombre": "Trabajo Práctico N° 1 (Análisis Metodológico)",
        "qmd": ROOT_DIR / "1 - Introducción" / "Trabajo Práctico 1" / "tp1_analisis_articulos.qmd",
        "pdf_entrega": ACTIVIDAD1_DIR / "TP1_Ayarachi_Fuentes.pdf",
        "docx_entrega": ACTIVIDAD1_DIR / "TP1_Ayarachi_Fuentes.docx",
        "qmd_entrega": ACTIVIDAD1_DIR / "tp1_analisis_articulos.qmd",
        "activo": False
    },
    {
        "id": "TP2",
        "nombre": "Trabajo Práctico N° 2 (Tema, Problema y Objetivos)",
        "qmd": ROOT_DIR / "2 - El problema" / "Trabajo Práctico n° 2" / "tp2_diseno_problema.qmd",
        "pdf_entrega": ACTIVIDAD2_DIR / "TP2_Ayarachi_Fuentes.pdf",
        "docx_entrega": ACTIVIDAD2_DIR / "TP2_Ayarachi_Fuentes.docx",
        "qmd_entrega": ACTIVIDAD2_DIR / "quarto" / "tp2_diseno_problema.qmd",
        "activo": True
    },
    {
        "id": "TP3",
        "nombre": "Trabajo Práctico N° 3 (Marco Teórico y Antecedentes)",
        "qmd": ROOT_DIR / "3 - Estado de la cuestión y marco teórico" / "Trabajo Práctico n° 3" / "tp3_marco_teorico_antecedentes.qmd",
        "pdf_entrega": ENTREGAS_DIR / "TP3_Ayarachi_Fuentes.pdf",
        "docx_entrega": ENTREGAS_DIR / "TP3_Ayarachi_Fuentes.docx",
        "activo": False
    },
    {
        "id": "TP4",
        "nombre": "Trabajo Práctico N° 4 (Proyecto Integral de TFG)",
        "qmd": ROOT_DIR / "4 - Metodología" / "Trabajo Práctico n° 4" / "tp4_proyecto_tfg_integral.qmd",
        "pdf_entrega": ENTREGAS_DIR / "TP4_Proyecto_TFG_Ayarachi_Fuentes.pdf",
        "docx_entrega": ENTREGAS_DIR / "TP4_Proyecto_TFG_Ayarachi_Fuentes.docx",
        "activo": False
    }
]

def obtener_info_archivo(filepath):
    """Devuelve tamaño y páginas/características del archivo."""
    if not filepath.exists():
        return "No encontrado"
    size_kb = filepath.stat().st_size / 1024
    if filepath.suffix == ".pdf":
        try:
            import pymupdf
            doc = pymupdf.open(str(filepath))
            return f"{len(doc)} págs, {size_kb:.1f} KB"
        except Exception:
            pass
    return f"{size_kb:.1f} KB"

def compilar_quarto_pdf(doc):
    """Compila Quarto a PDF (vía motor Typst interno de Quarto) hacia Entregas/."""
    qmd_path = doc["qmd"]
    pdf_out = doc["pdf_entrega"]
    
    if not qmd_path.exists():
        print(f"  [!] No existe el archivo: {qmd_path}")
        return False

    cmd = ["quarto", "render", str(qmd_path), "--to", "typst"]
    try:
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(ROOT_DIR))
        dt = time.time() - t0
        
        # Mover archivo generado por Quarto hacia Entregas/
        tmp_pdf = qmd_path.with_suffix(".pdf")
        if tmp_pdf.exists():
            pdf_out.parent.mkdir(parents=True, exist_ok=True)
            
            # 1. Centrar logotipo en portada, quitar número de portada y renumerar páginas desde 1
            try:
                import pymupdf
                doc_pdf = pymupdf.open(str(tmp_pdf))
                if len(doc_pdf) > 0:
                    cover = doc_pdf[0]
                    # Centrar el logotipo del CURZAS en la carátula si no estuviera centrado
                    imgs = cover.get_images(full=True)
                    if imgs:
                        img_bbox = cover.get_image_bbox(imgs[0])
                        center_x = cover.rect.width / 2
                        if abs((img_bbox.x0 + img_bbox.x1) / 2 - center_x) > 10:
                            cover.add_redact_annot(img_bbox, fill=(1, 1, 1))
                            cover.apply_redactions()
                            new_rect = pymupdf.Rect(
                                (cover.rect.width - img_bbox.width) / 2,
                                img_bbox.y0,
                                (cover.rect.width + img_bbox.width) / 2,
                                img_bbox.y1
                            )
                            logo_path = ROOT_DIR / "assets" / "img" / "CURZAS.png"
                            cover.insert_image(new_rect, filename=str(logo_path))

                    # Quitar número en la carátula (página 0)
                    for b in cover.get_text("blocks"):
                        if b[4].strip() == "1" and b[1] > cover.rect.height * 0.85:
                            r = pymupdf.Rect(b[0] - 5, b[1] - 5, b[2] + 5, b[3] + 5)
                            cover.add_redact_annot(r, fill=(1, 1, 1))
                            cover.apply_redactions()
                            break

                    doc_pdf.save(str(pdf_out), incremental=False, encryption=0)
                doc_pdf.close()
                tmp_pdf.unlink(missing_ok=True)
            except Exception:
                shutil.copy2(str(tmp_pdf), str(pdf_out))
                tmp_pdf.unlink(missing_ok=True)

            info = obtener_info_archivo(pdf_out)
            rel_path = pdf_out.relative_to(ENTREGAS_DIR)
            print(f"  [OK] PDF  -> Entregas/{rel_path} ({info}) en {dt:.2f}s")
            return True
        else:
            print(f"  [!] No se generó el archivo esperado: {tmp_pdf}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Fallo al generar PDF de {qmd_path.name}:")
        print(f"     {e.stderr.strip() or e.stdout.strip()}")
        return False

def compilar_quarto_word(doc):
    """Compila Quarto a Word (.docx) hacia Entregas/."""
    qmd_path = doc["qmd"]
    docx_out = doc["docx_entrega"]
    
    if not qmd_path.exists():
        print(f"  [!] No existe el archivo: {qmd_path}")
        return False

    cmd = ["quarto", "render", str(qmd_path), "--to", "docx"]
    try:
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(ROOT_DIR))
        dt = time.time() - t0
        
        tmp_docx = qmd_path.with_suffix(".docx")
        if tmp_docx.exists():
            docx_out.parent.mkdir(parents=True, exist_ok=True)
            try:
                import docx
                from docx.oxml import parse_xml
                from docx.oxml.ns import nsdecls
                from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
                from docx.shared import Inches, Pt, Cm

                doc_word = docx.Document(str(tmp_docx))
                
                # 0. Configurar márgenes de 2.5 cm, tipografía Arial 12pt e interlineado 1.5 en Word (Normas APA 7)
                for sec in doc_word.sections:
                    sec.top_margin = Cm(2.5)
                    sec.bottom_margin = Cm(2.5)
                    sec.left_margin = Cm(2.5)
                    sec.right_margin = Cm(2.5)

                for s_name in ['Normal', 'Body Text', 'First Paragraph', 'Compact']:
                    try:
                        st = doc_word.styles[s_name]
                        st.font.name = 'Arial'
                        st.font.size = Pt(12)
                        st.paragraph_format.line_spacing = 1.5
                    except Exception:
                        pass

                # Heading 1 (# ...): 14pt negrita con espacio antes/después
                try:
                    h1 = doc_word.styles['Heading 1']
                    h1.font.name = 'Arial'
                    h1.font.size = Pt(14)
                    h1.font.bold = True
                    h1.paragraph_format.space_before = Pt(20)
                    h1.paragraph_format.space_after = Pt(10)
                    h1.paragraph_format.line_spacing = 1.2
                    h1.paragraph_format.keep_with_next = True
                except Exception:
                    pass

                # Heading 2 (## ...): 12pt negrita con espacio antes/después
                try:
                    h2 = doc_word.styles['Heading 2']
                    h2.font.name = 'Arial'
                    h2.font.size = Pt(12)
                    h2.font.bold = True
                    h2.paragraph_format.space_before = Pt(14)
                    h2.paragraph_format.space_after = Pt(6)
                    h2.paragraph_format.line_spacing = 1.2
                    h2.paragraph_format.keep_with_next = True
                except Exception:
                    pass

                # Heading 3 (### ...): 12pt negrita y cursiva
                try:
                    h3 = doc_word.styles['Heading 3']
                    h3.font.name = 'Arial'
                    h3.font.size = Pt(12)
                    h3.font.bold = True
                    h3.font.italic = True
                    h3.paragraph_format.space_before = Pt(10)
                    h3.paragraph_format.space_after = Pt(4)
                    h3.paragraph_format.line_spacing = 1.2
                    h3.paragraph_format.keep_with_next = True
                except Exception:
                    pass

                # Aplicar directamente formato de margen y tamaño a cada encabezado
                for p in doc_word.paragraphs:
                    sname = p.style.name
                    if sname in ['Heading 1', 'Encabezado 1']:
                        p.paragraph_format.space_before = Pt(12)
                        p.paragraph_format.space_after = Pt(6)
                        p.paragraph_format.line_spacing = 1.25
                        p.paragraph_format.keep_with_next = True
                        for r in p.runs:
                            r.font.name = 'Arial'
                            r.font.size = Pt(14)
                            r.font.bold = True
                    elif sname in ['Heading 2', 'Encabezado 2']:
                        p.paragraph_format.space_before = Pt(10)
                        p.paragraph_format.space_after = Pt(4)
                        p.paragraph_format.line_spacing = 1.25
                        p.paragraph_format.keep_with_next = True
                        for r in p.runs:
                            r.font.name = 'Arial'
                            r.font.size = Pt(12)
                            r.font.bold = True
                    elif sname in ['Heading 3', 'Encabezado 3']:
                        p.paragraph_format.space_before = Pt(8)
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.line_spacing = 1.25
                        p.paragraph_format.keep_with_next = True
                        for r in p.runs:
                            r.font.name = 'Arial'
                            r.font.size = Pt(12)
                            r.font.bold = True
                            r.font.italic = True

                # Formatear y centrar el bloque del Título Principal y Subtítulo al inicio del cuerpo (Página 3)
                for p in doc_word.paragraphs:
                    txt = p.text.strip()
                    if txt.startswith("Evaluación del Desempeño Docente") and "Factibilidad" in txt:
                        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        p.paragraph_format.space_before = Pt(0)
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.line_spacing = 1.15
                        
                        if "\n" in txt:
                            parts = txt.split("\n", 1)
                            title_text = parts[0].strip()
                            subtitle_text = parts[1].strip()
                            
                            p.text = ""
                            r_title = p.add_run(title_text)
                            r_title.bold = True
                            r_title.font.name = "Arial"
                            r_title.font.size = Pt(13)
                            
                            p_sub = doc_word.add_paragraph()
                            p._p.addnext(p_sub._p)
                            p_sub.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                            p_sub.paragraph_format.space_before = Pt(0)
                            p_sub.paragraph_format.space_after = Pt(6)
                            p_sub.paragraph_format.line_spacing = 1.15
                            
                            r_sub = p_sub.add_run(subtitle_text)
                            r_sub.italic = True
                            r_sub.font.name = "Arial"
                            r_sub.font.size = Pt(11)

                            # Eliminar párrafos vacíos entre el subtítulo y el primer encabezado
                            next_p = p_sub._p.getnext()
                            while next_p is not None:
                                try:
                                    from lxml import etree
                                    txt_p = etree.tostring(next_p, method="text", encoding="unicode").strip()
                                except Exception:
                                    txt_p = ""
                                if not txt_p:
                                    temp = next_p.getnext()
                                    next_p.getparent().remove(next_p)
                                    next_p = temp
                                else:
                                    break
                        else:
                            for r in p.runs:
                                r.font.name = "Arial"
                                r.font.size = Pt(13)
                                r.font.bold = True
                        break

                # 1. Asegurar alineación centrada del logotipo y reconstruir la carátula oficial SIA
                p_logo = None
                for p in doc_word.paragraphs:
                    if len(p._element.xpath('.//w:drawing')) > 0:
                        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        p_logo = p
                        break

                # Reconstruir la carátula según el modelo oficial SIA (Recursos TFG/Modelo de Carátula SIA 2025.docx) solo para TP2
                if p_logo is not None and doc.get("id") == "TP2":
                    pb_idx = None
                    for i, p in enumerate(doc_word.paragraphs):
                        if 'type="page"' in p._p.xml or p.text.strip() == "Índice de Contenidos":
                            pb_idx = i if 'type="page"' in p._p.xml else i - 1
                            break

                    if pb_idx is not None and pb_idx > 0:
                        p_pb = doc_word.paragraphs[pb_idx]
                        
                        # Eliminar párrafos intermedios entre el logo y el salto de página
                        current_p = p_logo._p.getnext()
                        while current_p is not None and current_p != p_pb._p:
                            temp = current_p.getnext()
                            current_p.getparent().remove(current_p)
                            current_p = temp

                        # Párrafos idénticos al archivo oficial Modelo de Carátula SIA 2025.docx
                        cover_data = [
                            ("", False, WD_PARAGRAPH_ALIGNMENT.CENTER, None),
                            ("Universidad Nacional del Comahue", True, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("Complejo Universitario Regional Zona Atlántica y Sur", True, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("Departamento de Administración Pública", True, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.5),
                            ("Licenciatura en Gestión de Recursos Humanos", True, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.0),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.CENTER, 1.0),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("Materia: Seminario de Integración y Aplicación", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("Profesores: Dra. Deborah Noguera", False, None, None),
                            ("                   Esp. Federico Abeiro", False, None, None),
                            ("                   Esp. María Cecilia Aguirre", False, None, None),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("Estudiante: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("DNI y LEGAJO: DNI N° 35.492.138 — Legajo N° 8252", False, None, None),
                            ("Email: hectordanielayarachifuentes@gmail.com", False, None, None),
                            ("", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("Director/a: (A designar antes de finalizar el cursado del SIA)", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("Codirector/a: (A designar antes de finalizar el cursado del SIA)", False, WD_PARAGRAPH_ALIGNMENT.JUSTIFY, 1.5),
                            ("", False, None, None),
                            ("", False, None, None),
                            ("Viedma, Río Negro — Año 2026", False, WD_PARAGRAPH_ALIGNMENT.CENTER, None)
                        ]

                        for text, bold, align, ls in cover_data:
                            new_p = doc_word.add_paragraph()
                            p_pb._p.addprevious(new_p._p)
                            if align is not None:
                                new_p.alignment = align
                            if ls is not None:
                                new_p.paragraph_format.line_spacing = ls
                            new_p.paragraph_format.space_before = Pt(0)
                            new_p.paragraph_format.space_after = Pt(0)
                            if text:
                                run = new_p.add_run(text)
                                run.bold = bold
                                run.font.name = "Arial"
                                run.font.size = Pt(12)

                # Ajustar espaciado de carátula para TP1 para que entre exactamente en una sola página en Word
                if p_logo is not None and doc.get("id") == "TP1":
                    pb_idx = None
                    for i, p in enumerate(doc_word.paragraphs):
                        if 'type="page"' in p._p.xml or p.text.strip() == "Índice de Contenidos":
                            pb_idx = i if 'type="page"' in p._p.xml else i - 1
                            break

                    if pb_idx is not None:
                        for p in list(doc_word.paragraphs[:pb_idx]):
                            txt = p.text.strip()
                            if not txt and len(p._element.xpath('.//w:drawing')) == 0:
                                p._p.getparent().remove(p._p)
                            else:
                                p.paragraph_format.space_before = Pt(0)
                                if "Universidad" in txt:
                                    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                                    p.paragraph_format.space_after = Pt(10)
                                    p.paragraph_format.line_spacing = 1.15
                                elif "TRABAJO PRÁCTICO" in txt:
                                    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                                    p.paragraph_format.space_after = Pt(12)
                                    p.paragraph_format.line_spacing = 1.15
                                elif "Materia" in txt or "Estudiante" in txt:
                                    p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
                                    p.paragraph_format.left_indent = Inches(0.4)
                                    p.paragraph_format.space_after = Pt(12)
                                    p.paragraph_format.line_spacing = 1.15
                                elif "Año Académico" in txt:
                                    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                                    p.paragraph_format.space_after = Pt(0)
                                    p.paragraph_format.line_spacing = 1.15
                                else:
                                    p.paragraph_format.space_after = Pt(6)

                # 2. Configurar pie de página: Portada e Índice sin número, contenido inicia en 1
                p_body = None
                found_toc = False
                for p in doc_word.paragraphs:
                    txt = p.text.strip()
                    if txt == "Índice de Contenidos":
                        found_toc = True
                        continue
                    if found_toc and txt:
                        if txt.startswith(('1.', '2.', '3.', '4.', '5.')) and '\t' in txt:
                            continue
                        if p.style.name.startswith(('Heading', 'First Paragraph', 'Title', 'Encabezado')) or txt.startswith(('1.', 'Evaluación', 'Tema', 'Introducción')):
                            p_body = p
                            break

                if not p_body and len(doc_word.paragraphs) > 0:
                    for p in doc_word.paragraphs:
                        txt = p.text.strip()
                        if txt.startswith(('1.', 'Evaluación', 'Tema', 'Introducción')) and not txt.startswith('Materia'):
                            p_body = p
                            break

                if p_body is not None:
                    p_prev = p_body._p.getprevious()
                    if p_prev is not None:
                        if len(p_prev.xpath('.//w:sectPr')) == 0:
                            sect_pr = parse_xml(f'<w:sectPr {nsdecls("w")}><w:type w:val="nextPage"/></w:sectPr>')
                            p_prev.get_or_add_pPr().append(sect_pr)

                sections = doc_word.sections
                if len(sections) >= 2:
                    sec0 = sections[0]
                    sec0.footer.is_linked_to_previous = False
                    for p in sec0.footer.paragraphs:
                        p.text = ""

                    sec1 = sections[1]
                    sec1.footer.is_linked_to_previous = False
                    fp = sec1.footer.paragraphs[0] if sec1.footer.paragraphs else sec1.footer.add_paragraph()
                    fp.text = ""
                    fp.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                    xml_fld = f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>'
                    fp._p.append(parse_xml(xml_fld))
                    xml_pg = f'<w:pgNumType {nsdecls("w")} w:start="1"/>'
                    sec1._sectPr.append(parse_xml(xml_pg))
                elif len(sections) == 1:
                    sec = sections[0]
                    sec.different_first_page_header_footer = True
                    fp = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
                    fp.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                    xml_fld = f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>'
                    fp._p.append(parse_xml(xml_fld))
                    xml_pg = f'<w:pgNumType {nsdecls("w")} w:start="0"/>'
                    sec._sectPr.append(parse_xml(xml_pg))

                # 3. Aplicar estilo de tablas APA 7 (solo 3 líneas horizontales: top, header-bottom, table-bottom)
                for table in doc_word.tables:
                    xml_borders = (
                        f'<w:tblBorders {nsdecls("w")}>'
                        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
                        f'<w:left w:val="none"/>'
                        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>'
                        f'<w:right w:val="none"/>'
                        f'<w:insideH w:val="none"/>'
                        f'<w:insideV w:val="none"/>'
                        f'</w:tblBorders>'
                    )
                    table._tbl.tblPr.append(parse_xml(xml_borders))
                    if len(table.rows) > 0:
                        for cell in table.rows[0].cells:
                            tcPr = cell._tc.get_or_add_tcPr()
                            tcBorders = parse_xml(
                                f'<w:tcBorders {nsdecls("w")}>'
                                f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
                                f'</w:tcBorders>'
                            )
                            tcPr.append(tcBorders)

                # 4. Generar e insertar Tabla de Contenidos completa y visible en Word
                p_toc = None
                for p in doc_word.paragraphs:
                    if p.text.strip() == "Índice de Contenidos":
                        p_toc = p
                        break

                if p_toc:
                    # Limpiar párrafos de TOC previos si estuvieran vacíos
                    next_p = p_toc._p.getnext()
                    while next_p is not None:
                        try:
                            from lxml import etree
                            xml_s = etree.tostring(next_p, encoding="unicode")
                        except Exception:
                            xml_s = ""
                        if 'TOC' in xml_s or 'fldChar' in xml_s:
                            parent = next_p.getparent()
                            temp = next_p.getnext()
                            parent.remove(next_p)
                            next_p = temp
                        else:
                            break

                    # Extraer entradas y números de página desde el PDF o desde los encabezados
                    items_toc = []
                    pdf_path = doc.get("pdf_entrega")
                    if pdf_path and pdf_path.exists():
                        try:
                            import pymupdf
                            doc_pdf = pymupdf.open(str(pdf_path))
                            if len(doc_pdf) > 1:
                                txt_toc = doc_pdf[1].get_text()
                                for line in txt_toc.split('\n'):
                                    line = line.strip()
                                    if not line or line.startswith('Índice') or line == '1':
                                        continue
                                    parts = line.split(' .')
                                    if len(parts) >= 2:
                                        title = parts[0].strip()
                                        pag = parts[-1].replace('.', '').replace('\u2060', '').strip()
                                        if pag.isdigit():
                                            level = 2 if title == 'Objetivos' or title.startswith('1.1') else 1
                                            items_toc.append((title, level, pag))
                        except Exception:
                            pass

                    # Títulos detectados en Word
                    headings_word = []
                    for p in doc_word.paragraphs:
                        txt = p.text.strip()
                        if txt == "Índice de Contenidos":
                            continue
                        if p.style.name.startswith(('Heading', 'Encabezado')) or txt.startswith(('1.', '2.', '3.', '4.', '5.')):
                            headings_word.append(txt)

                    final_items = []
                    if items_toc:
                        for title_pdf, level, pag in items_toc:
                            matched = title_pdf
                            for hw in headings_word:
                                hw_clean = hw
                                parts = hw.split(' ', 1)
                                if len(parts) > 1 and parts[0].replace('.', '').isdigit():
                                    hw_clean = parts[1]
                                if hw_clean.strip().lower() == title_pdf.strip().lower():
                                    matched = hw
                                    break
                            final_items.append((matched, level, pag))
                    else:
                        for hw in headings_word:
                            level = 2 if hw.startswith('1.1') else 1
                            final_items.append((hw, level, "1"))

                    # Construir estructura nativa OpenXML para el TOC de Word
                    tab_pos = "9026"
                    curr = p_toc._p

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

                    for texto, nivel, num_pag in final_items:
                        style_name = f"TOC{nivel}"
                        left_indent = "280" if nivel == 2 else "0"
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
                            f'<w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
                            f'<w:sz w:val="22"/>'
                            f'</w:rPr>'
                            f'<w:t>{texto}</w:t>'
                            f'</w:r>'
                            f'<w:r>'
                            f'<w:tab/>'
                            f'</w:r>'
                            f'<w:r>'
                            f'<w:rPr>'
                            f'<w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
                            f'<w:sz w:val="22"/>'
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

                    # Habilitar actualización automática al abrir en Word
                    try:
                        settings = doc_word.settings.element
                        update_fields = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
                        settings.append(update_fields)
                    except Exception:
                        pass

                # 5. Aplicar sangría francesa APA 7 a las referencias y centrar su título en Word
                is_ref = False
                for p in doc_word.paragraphs:
                    txt = p.text.strip()
                    if (txt == "Referencias" or txt.startswith("Referencias Bibliográficas") or txt.startswith("Referencias")) and "\t" not in txt:
                        is_ref = True
                        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        continue
                    if is_ref and txt:
                        p.paragraph_format.left_indent = Inches(0.5)
                        p.paragraph_format.first_line_indent = Inches(-0.5)
                        p.paragraph_format.space_after = docx.shared.Pt(6)
                        p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

                doc_word.save(str(tmp_docx))
            except Exception as e:
                import traceback
                print(f"  [AVISO] Post-procesamiento Word omitido: {e}")
                traceback.print_exc()

            try:
                shutil.copy2(str(tmp_docx), str(docx_out))
                tmp_docx.unlink(missing_ok=True)
            except PermissionError:
                print(f"  [AVISO] No se pudo sobrescribir Entregas/{docx_out.name} porque está abierto en Microsoft Word. Por favor cerralo para actualizar la entrega.")
                tmp_docx.unlink(missing_ok=True)
                return False

            info = obtener_info_archivo(docx_out)
            rel_path = docx_out.relative_to(ENTREGAS_DIR)
            print(f"  [OK] WORD -> Entregas/{rel_path} ({info}) en {dt:.2f}s")
            return True
        else:
            print(f"  [!] No se generó el archivo esperado: {tmp_docx}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Fallo al generar Word de {qmd_path.name}:")
        print(f"     {e.stderr.strip() or e.stdout.strip()}")
        return False

def sincronizar_documento(doc):
    """Sincroniza bidireccionalmente el archivo origen y la copia en Entregas según la última modificación."""
    if "qmd_entrega" not in doc:
        return
    qmd_orig = doc["qmd"]
    qmd_entr = doc["qmd_entrega"]
    
    if qmd_orig.exists() and qmd_entr.exists():
        mtime_orig = qmd_orig.stat().st_mtime
        mtime_entr = qmd_entr.stat().st_mtime
        if mtime_entr > mtime_orig + 0.1:
            shutil.copy2(str(qmd_entr), str(qmd_orig))
            print(f"  [SYNC] Copiado desde {qmd_entr.name} (Entregas) -> {qmd_orig.parent.name}")
        elif mtime_orig > mtime_entr + 0.1:
            shutil.copy2(str(qmd_orig), str(qmd_entr))
            print(f"  [SYNC] Copiado desde {qmd_orig.parent.name} -> {qmd_entr.name} (Entregas)")
    elif qmd_orig.exists() and not qmd_entr.exists():
        qmd_entr.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(qmd_orig), str(qmd_entr))
        print(f"  [SYNC] Copiado inicial a Entregas: {qmd_entr.name}")
    elif qmd_entr.exists() and not qmd_orig.exists():
        qmd_orig.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(qmd_entr), str(qmd_orig))
        print(f"  [SYNC] Restaurado archivo origen desde Entregas: {qmd_orig.name}")

    local_assets = qmd_orig.parent / "assets"
    if local_assets.exists():
        entrega_assets = qmd_entr.parent / "assets"
        entrega_assets.mkdir(parents=True, exist_ok=True)
        shutil.copytree(str(local_assets), str(entrega_assets), dirs_exist_ok=True)

    # Sincronizar archivos auxiliares (.bib, .csl, .typ) de la carpeta origen hacia Entregas
    for ext in ["*.bib", "*.csl", "*.typ"]:
        for aux_file in qmd_orig.parent.glob(ext):
            if not aux_file.name.endswith("_typst.typ") and aux_file.name != qmd_orig.with_suffix(".typ").name:
                dst = qmd_entr.parent / aux_file.name
                if not dst.exists() or aux_file.stat().st_mtime > dst.stat().st_mtime + 0.1:
                    shutil.copy2(str(aux_file), str(dst))

def compilar_todo(solo_pdf=False, solo_word=False, todos_los_tps=False, tp_id=None):
    """Ejecuta el pipeline para los TPs (por defecto el TP activo actual o tp_id especificado)."""
    ENTREGAS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "=" * 70)
    print(" 🏛️ COMPILACIÓN QUARTO A WORD (.docx) Y PDF — SIA (UNCo CURZAS)")
    print(" Estudiante: Héctor Daniel Ayarachi Fuentes")
    print("=" * 70)
    
    start_total = time.time()
    exitos = 0
    total_tareas = 0

    if tp_id:
        lista_docs = [d for d in DOCUMENTOS if d["id"].upper() == tp_id.upper()]
    elif todos_los_tps:
        lista_docs = DOCUMENTOS
    else:
        lista_docs = [d for d in DOCUMENTOS if d["activo"]]

    for doc in lista_docs:
        print(f"\n>> Procesando [{doc['id']}] {doc['nombre']}:")
        
        # Sincronizar antes de compilar
        sincronizar_documento(doc)

        if not solo_word:
            total_tareas += 1
            if compilar_quarto_pdf(doc):
                exitos += 1

        if not solo_pdf:
            total_tareas += 1
            if compilar_quarto_word(doc):
                exitos += 1

        # Confirmar sincronización de código y assets hacia Entregas
        if "qmd_entrega" in doc and doc["qmd"].exists():
            sincronizar_documento(doc)
            print(f"  [OK] CÓDIGO QUARTO -> {doc['qmd_entrega'].parent.name}/{doc['qmd_entrega'].name}")

    dt_total = time.time() - start_total
    print("\n" + "-" * 70)
    print(f" Resumen: {exitos}/{total_tareas} tareas exitosas en {dt_total:.2f} segundos.")
    print(f" Carpeta de Entregas: {ENTREGAS_DIR}")
    print("-" * 70 + "\n")

def modo_vigilante():
    """Vigila el archivo Quarto (.qmd) activo y recompila automáticamente al guardar.
    
    Detecta cambios en AMBAS copias del QMD (original y Entregas/).
    Al detectar un guardado, fuerza la copia al otro archivo SIN comparar timestamps
    y recompila PDF + Word de inmediato.
    """
    print("\n" + "=" * 70)
    print(" 👁️ MODO VIGILANTE QUARTO ACTIVO — Recompila PDF y Word al guardar")
    print(" Edita desde cualquiera de las dos ubicaciones del .qmd.")
    print(" Presiona Ctrl+C para detener.")
    print("=" * 70 + "\n")

    activos = [d for d in DOCUMENTOS if d["activo"]]
    archivos_mtime = {}

    for d in activos:
        # Al arrancar, la copia en Entregas manda: forzar sincronización inicial
        if d.get("qmd_entrega") and d["qmd_entrega"].exists():
            shutil.copy2(str(d["qmd_entrega"]), str(d["qmd"]))
            print(f"  [SYNC INICIAL] Entregas/{d['qmd_entrega'].name} → {d['qmd'].parent.name}/")
        if d["qmd"].exists():
            archivos_mtime[d["qmd"]] = d["qmd"].stat().st_mtime
        if d.get("qmd_entrega") and d["qmd_entrega"].exists():
            archivos_mtime[d["qmd_entrega"]] = d["qmd_entrega"].stat().st_mtime

    compilar_todo()

    try:
        while True:
            time.sleep(1.5)
            cambios = []
            for p, mtime_ant in list(archivos_mtime.items()):
                if p.exists():
                    mtime_act = p.stat().st_mtime
                    if mtime_act > mtime_ant + 0.05:
                        archivos_mtime[p] = mtime_act
                        cambios.append(p)

            if cambios:
                for c in cambios:
                    print(f"\n[CAMBIO DETECTADO] {c.parent.name}/{c.name}")
                    for doc in activos:
                        if doc["qmd"] == c or doc.get("qmd_entrega") == c:
                            # Fuerza copia sin comparar timestamps
                            if doc.get("qmd_entrega") == c and c.exists():
                                # Guardó en Entregas/ → copiar al original
                                shutil.copy2(str(c), str(doc["qmd"]))
                                print(f"  [SYNC ▶] Entregas/{c.name} → {doc['qmd'].parent.name}/")
                            elif doc["qmd"] == c and c.exists() and doc.get("qmd_entrega"):
                                # Guardó en original → copiar a Entregas/
                                doc["qmd_entrega"].parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(str(c), str(doc["qmd_entrega"]))
                                print(f"  [SYNC ▶] {doc['qmd'].parent.name}/{c.name} → Entregas/")

                            compilar_quarto_pdf(doc)
                            compilar_quarto_word(doc)

                            # Refrescar timestamps para evitar doble disparo
                            if doc["qmd"].exists():
                                archivos_mtime[doc["qmd"]] = doc["qmd"].stat().st_mtime
                            if doc.get("qmd_entrega") and doc["qmd_entrega"].exists():
                                archivos_mtime[doc["qmd_entrega"]] = doc["qmd_entrega"].stat().st_mtime
    except KeyboardInterrupt:
        print("\n[Vigilante finalizado por el usuario].")

if __name__ == "__main__":
    args = sys.argv[1:]
    tp_target = None
    if "--tp1" in args:
        tp_target = "TP1"
    elif "--tp2" in args:
        tp_target = "TP2"
    elif "--tp3" in args:
        tp_target = "TP3"
    elif "--tp4" in args:
        tp_target = "TP4"
    else:
        for arg in args:
            if not arg.startswith("-"):
                norm_arg = arg.replace("/", "\\").lower()
                for d in DOCUMENTOS:
                    qmd_str = str(d.get("qmd", "")).lower()
                    entr_str = str(d.get("qmd_entrega", "")).lower()
                    if norm_arg in qmd_str or norm_arg in entr_str or d["id"].lower() in norm_arg or Path(arg).name.lower() == d["qmd"].name.lower():
                        tp_target = d["id"]
                        break
                if tp_target:
                    break

    if "--watch" in args or "-w" in args:
        modo_vigilante()
    elif "--pdf" in args:
        compilar_todo(solo_pdf=True, tp_id=tp_target)
    elif "--word" in args:
        compilar_todo(solo_word=True, tp_id=tp_target)
    elif "--all" in args:
        compilar_todo(todos_los_tps=True)
    else:
        compilar_todo(tp_id=tp_target)
