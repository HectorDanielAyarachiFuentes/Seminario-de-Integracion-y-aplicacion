"""
=============================================================================
BUILD AUTOMATION: Proyecto TFG-SIA (2026) — Estudiante: Andrea Alejandra Díaz
CURZAS — Universidad Nacional del Comahue
Pipeline Docs-as-Code Quarto (.qmd) -> PDF y Word (.docx) con Normas APA 7
=============================================================================
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

# Importaciones lazy / seguras
try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        pymupdf = None

try:
    import docx
    from docx.shared import Pt, Cm, Inches
    from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls
except ImportError:
    docx = None
    Pt = Cm = Inches = WD_PARAGRAPH_ALIGNMENT = parse_xml = nsdecls = None

try:
    from lxml import etree
except ImportError:
    etree = None

# Rutas
BASE_DIR = Path(__file__).resolve().parent
QUARTO_DIR = BASE_DIR / "quarto"
ENTREGAS_DIR = BASE_DIR / "entregas"
QMD_FILE = QUARTO_DIR / "tp_alejandra_proyecto_tfg.qmd"
PDF_OUT = ENTREGAS_DIR / "TP_Alejandra_Proyecto_TFG_SIA_2026.pdf"
DOCX_OUT = ENTREGAS_DIR / "TP_Alejandra_Proyecto_TFG_SIA_2026.docx"
LOGO_PATH = QUARTO_DIR / "assets" / "img" / "curzas.png"


def obtener_info_archivo(filepath):
    if not filepath.exists():
        return "No encontrado"
    size_kb = filepath.stat().st_size / 1024
    if filepath.suffix == ".pdf" and pymupdf is not None:
        try:
            with pymupdf.open(str(filepath)) as doc:
                return f"{len(doc)} págs, {size_kb:.1f} KB"
        except Exception:
            pass
    return f"{size_kb:.1f} KB"


def compilar_quarto_pdf():
    print(">> Compilando versión PDF (Typst)...")
    ENTREGAS_DIR.mkdir(parents=True, exist_ok=True)
    cmd = ["quarto", "render", str(QMD_FILE), "--to", "typst"]
    try:
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(BASE_DIR))
        dt = time.time() - t0
        tmp_pdf = QMD_FILE.with_suffix(".pdf")
        if tmp_pdf.exists():
            processed_bytes = None
            if pymupdf is not None:
                try:
                    with pymupdf.open(str(tmp_pdf)) as doc_pdf:
                        if len(doc_pdf) > 0:
                            cover = doc_pdf[0]
                            # Quitar número en la carátula si existiera
                            for b in cover.get_text("blocks"):
                                if b[4].strip() == "1" and b[1] > cover.rect.height * 0.85:
                                    r = pymupdf.Rect(b[0] - 5, b[1] - 5, b[2] + 5, b[3] + 5)
                                    cover.add_redact_annot(r, fill=(1, 1, 1))
                                    cover.apply_redactions()
                                    break
                            processed_bytes = doc_pdf.tobytes(deflate=True)
                except Exception:
                    processed_bytes = None

            if processed_bytes:
                with open(PDF_OUT, "wb") as f_out:
                    f_out.write(processed_bytes)
            else:
                shutil.copy2(str(tmp_pdf), str(PDF_OUT))
            tmp_pdf.unlink(missing_ok=True)
            print(f"  [OK] PDF  -> {PDF_OUT.name} ({obtener_info_archivo(PDF_OUT)}) en {dt:.2f}s")
            return True
        else:
            print(f"  [!] No se generó el PDF esperado: {tmp_pdf}")
            return False
    except subprocess.CalledProcessError as e:
        print("  [ERROR] Falló compilación a PDF:")
        print(e.stderr.strip() or e.stdout.strip())
        return False


def aplicar_estilos_base_apa7(doc_word):
    if doc_word is None or Cm is None:
        return
    for sec in doc_word.sections:
        sec.top_margin = Cm(2.54)
        sec.bottom_margin = Cm(2.54)
        sec.left_margin = Cm(2.54)
        sec.right_margin = Cm(2.54)

    for s_name in ['Normal', 'Body Text', 'First Paragraph', 'Compact']:
        try:
            st = doc_word.styles[s_name]
            st.font.name = 'Arial'
            st.font.size = Pt(12)
            st.paragraph_format.line_spacing = 1.5
            st.paragraph_format.first_line_indent = Inches(0.5)
        except (KeyError, AttributeError):
            pass

    try:
        h1 = doc_word.styles['Heading 1']
        h1.font.name = 'Arial'
        h1.font.size = Pt(14)
        h1.font.bold = True
        h1.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        h1.paragraph_format.first_line_indent = Inches(0)
        h1.paragraph_format.space_before = Pt(20)
        h1.paragraph_format.space_after = Pt(10)
        h1.paragraph_format.line_spacing = 1.2
        h1.paragraph_format.keep_with_next = True
    except (KeyError, AttributeError):
        pass

    try:
        h2 = doc_word.styles['Heading 2']
        h2.font.name = 'Arial'
        h2.font.size = Pt(12)
        h2.font.bold = True
        h2.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        h2.paragraph_format.first_line_indent = Inches(0)
        h2.paragraph_format.space_before = Pt(14)
        h2.paragraph_format.space_after = Pt(6)
        h2.paragraph_format.line_spacing = 1.2
        h2.paragraph_format.keep_with_next = True
    except (KeyError, AttributeError):
        pass

    try:
        h3 = doc_word.styles['Heading 3']
        h3.font.name = 'Arial'
        h3.font.size = Pt(12)
        h3.font.bold = True
        h3.font.italic = True
        h3.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        h3.paragraph_format.first_line_indent = Inches(0)
        h3.paragraph_format.space_before = Pt(10)
        h3.paragraph_format.space_after = Pt(4)
        h3.paragraph_format.line_spacing = 1.2
        h3.paragraph_format.keep_with_next = True
    except (KeyError, AttributeError):
        pass


def formatear_parrafos_y_encabezados(doc_word):
    if doc_word is None or Pt is None:
        return

    for p in doc_word.paragraphs:
        sname = p.style.name if p.style else ""
        if sname in ['Heading 1', 'Encabezado 1']:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(8)
            p.paragraph_format.line_spacing = 1.25
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.font.name = 'Arial'
                r.font.size = Pt(14)
                r.font.bold = True
        elif sname in ['Heading 2', 'Encabezado 2']:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.25
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.font.name = 'Arial'
                r.font.size = Pt(12)
                r.font.bold = True
        elif sname in ['Heading 3', 'Encabezado 3']:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.25
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.font.name = 'Arial'
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.italic = True
        else:
            txt_clean = p.text.strip()
            if txt_clean.startswith(("Nota.", "*Nota.*")):
                p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
                p.paragraph_format.first_line_indent = Inches(0)
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(6)
                p.paragraph_format.line_spacing = 1.15
                for r in p.runs:
                    r.font.size = Pt(10)

    # Formatear título principal al inicio del cuerpo
    for p in doc_word.paragraphs:
        txt = p.text.strip()
        if txt.startswith("Transformaciones en la Organización del Trabajo") and "ESRN N° 154" in txt:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(13)
                r.font.bold = True
            break


def configurar_paginacion_dinamica(doc_word):
    if doc_word is None or parse_xml is None:
        return

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
            if p.style and (p.style.name.startswith(('Heading', 'First Paragraph', 'Title', 'Encabezado')) or txt.startswith(('Primera', 'Transformaciones', 'Tema'))):
                p_body = p
                break

    if not p_body and len(doc_word.paragraphs) > 0:
        for p in doc_word.paragraphs:
            txt = p.text.strip()
            if txt.startswith(('Primera', 'Transformaciones', 'Tema')) and not txt.startswith('Materia'):
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


def formatear_tablas_apa7(doc_word):
    if doc_word is None or parse_xml is None:
        return
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

        for row_idx, row in enumerate(table.rows):
            for cell in row.cells:
                for cp in cell.paragraphs:
                    cp.paragraph_format.first_line_indent = Inches(0)
                    cp.paragraph_format.line_spacing = 1.15
                    cp.paragraph_format.space_before = Pt(1)
                    cp.paragraph_format.space_after = Pt(1)
                    for cr in cp.runs:
                        cr.font.name = 'Arial'
                        cr.font.size = Pt(9)
                        if row_idx == 0:
                            cr.bold = True


def insertar_tabla_contenidos_word(doc_word):
    if doc_word is None or parse_xml is None:
        return

    p_toc = None
    for p in doc_word.paragraphs:
        if p.text.strip() == "Índice de Contenidos":
            p_toc = p
            break

    if not p_toc:
        return

    next_p = p_toc._p.getnext()
    while next_p is not None:
        try:
            xml_s = etree.tostring(next_p, encoding="unicode") if etree else ""
        except Exception:
            xml_s = ""
        if 'TOC' in xml_s or 'fldChar' in xml_s:
            parent = next_p.getparent()
            temp = next_p.getnext()
            parent.remove(next_p)
            next_p = temp
        else:
            break

    # Extraer entradas desde el PDF o encabezados
    items_toc = []
    if PDF_OUT.exists() and pymupdf is not None:
        try:
            with pymupdf.open(str(PDF_OUT)) as doc_pdf:
                toc = doc_pdf.get_toc()
                if toc:
                    offset = toc[0][2] - 1
                    for lvl, title, phys_pag in toc:
                        if lvl <= 2:
                            vis_pag = str(max(1, phys_pag - offset))
                            items_toc.append((title, lvl, vis_pag))
                elif len(doc_pdf) > 1:
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
                                # Solo niveles 1 y 2 para que el TOC ocupe exactamente 1 página
                                if any(title.startswith(pfx) for pfx in [
                                    'Primera parte', 'Tema de Investigación', 'Delimitación', 'Planteamiento', 'Justificación', 'Definición de Objetivos',
                                    'Segunda parte', 'Marco Teórico', 'Marco Normativo', 'Estado del Arte',
                                    'Tercera parte', 'Metodología', 'Cronograma', 'Viabilidad',
                                    'Referencias Bibliográficas'
                                ]):
                                    level = 1 if title.startswith(('Primera', 'Segunda', 'Tercera', 'Referencias')) else 2
                                    items_toc.append((title, level, pag))
        except Exception:
            pass

    if not items_toc:
        for p in doc_word.paragraphs:
            txt = p.text.strip()
            if txt == "Índice de Contenidos":
                continue
            if p.style and p.style.name.startswith(('Heading 1', 'Encabezado 1')):
                items_toc.append((txt, 1, "1"))
            elif p.style and p.style.name.startswith(('Heading 2', 'Encabezado 2')):
                items_toc.append((txt, 2, "1"))

    tab_pos = "9026"
    curr = p_toc._p

    begin_xml = (
        f'<w:p {nsdecls("w")}>'
        f'<w:pPr><w:spacing w:after="80"/></w:pPr>'
        f'<w:r>'
        f'<w:fldChar w:fldCharType="begin"/>'
        f'<w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText>'
        f'<w:fldChar w:fldCharType="separate"/>'
        f'</w:r>'
        f'</w:p>'
    )
    p_begin = parse_xml(begin_xml)
    curr.addnext(p_begin)
    curr = p_begin

    for texto, nivel, num_pag in items_toc:
        style_name = f"TOC{min(nivel, 2)}"
        left_indent = "0" if nivel <= 1 else "280"
        bold_tag = '<w:b/>' if nivel == 1 else ''

        item_xml = (
            f'<w:p {nsdecls("w")}>'
            f'<w:pPr>'
            f'<w:pStyle w:val="{style_name}"/>'
            f'<w:tabs>'
            f'<w:tab w:val="right" w:leader="dot" w:pos="{tab_pos}"/>'
            f'</w:tabs>'
            f'<w:ind w:left="{left_indent}"/>'
            f'<w:spacing w:before="20" w:after="25" w:line="240" w:lineRule="auto"/>'
            f'</w:pPr>'
            f'<w:r>'
            f'<w:rPr>'
            f'<w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
            f'{bold_tag}'
            f'<w:sz w:val="20"/>'
            f'</w:rPr>'
            f'<w:t>{texto}</w:t>'
            f'</w:r>'
            f'<w:r>'
            f'<w:tab/>'
            f'</w:r>'
            f'<w:r>'
            f'<w:rPr>'
            f'<w:rFonts w:ascii="Arial" w:hAnsi="Arial"/>'
            f'{bold_tag}'
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

    try:
        settings = doc_word.settings.element
        update_fields = parse_xml(f'<w:updateFields {nsdecls("w")} w:val="true"/>')
        settings.append(update_fields)
    except Exception:
        pass


def aplicar_sangria_francesa_referencias(doc_word):
    if doc_word is None or Inches is None:
        return
    is_ref = False
    for p in doc_word.paragraphs:
        txt = p.text.strip()
        if (txt == "Referencias" or txt.startswith("Referencias Bibliográficas")) and "\t" not in txt:
            is_ref = True
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            continue
        if is_ref and txt.startswith(("Anexo", "Anexos")):
            is_ref = False
            continue
        if is_ref and txt:
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.first_line_indent = Inches(-0.5)
            p.paragraph_format.space_after = Pt(6)
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT


def centrar_caratula_oficial(doc_word):
    """Centra el logotipo del CURZAS y distribuye armónicamente la carátula para ocupar exactamente 1 página en Word."""
    if doc_word is None or parse_xml is None:
        return

    pb_idx = len(doc_word.paragraphs)
    for i, p in enumerate(doc_word.paragraphs):
        if p.text.strip() == "Índice de Contenidos" or 'type="page"' in p._p.xml:
            pb_idx = i
            break

    # 1. Eliminar párrafos vacíos redundantes en la carátula
    for p in list(doc_word.paragraphs[:pb_idx]):
        txt = p.text.strip()
        has_draw = len(p._element.xpath('.//w:drawing')) > 0
        if not txt and not has_draw:
            p._p.getparent().remove(p._p)

    # Recalcular índice tras eliminar párrafos vacíos
    pb_idx = len(doc_word.paragraphs)
    for i, p in enumerate(doc_word.paragraphs):
        if p.text.strip() == "Índice de Contenidos" or 'type="page"' in p._p.xml:
            pb_idx = i
            break

    # 2. Formatear y calibrar verticalmente cada bloque de la portada
    for p in doc_word.paragraphs[:pb_idx]:
        p.paragraph_format.line_spacing = 1.25

        # Párrafo del Logo
        if len(p._element.xpath('.//w:drawing')) > 0:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.left_indent = Inches(0)
            p.paragraph_format.right_indent = Inches(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(22)
            pPr = p._p.get_or_add_pPr()
            for jc in pPr.findall(docx.oxml.ns.qn('w:jc')):
                pPr.remove(jc)
            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
            pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="0" w:right="0" w:firstLine="0"/>'))
            continue

        txt = p.text.strip()
        # Textos institucionales centrados
        if any(keyword in txt for keyword in [
            "Universidad Nacional del Comahue",
            "Complejo Universitario Regional",
            "Departamento de Administración Pública"
        ]):
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.left_indent = Inches(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(36)
            pPr = p._p.get_or_add_pPr()
            for jc in pPr.findall(docx.oxml.ns.qn('w:jc')):
                pPr.remove(jc)
            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
            pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="0" w:right="0" w:firstLine="0"/>'))
        elif "Licenciatura en Gestión de Recursos Humanos" in txt:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.left_indent = Inches(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(36)
            pPr = p._p.get_or_add_pPr()
            for jc in pPr.findall(docx.oxml.ns.qn('w:jc')):
                pPr.remove(jc)
            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
            pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="0" w:right="0" w:firstLine="0"/>'))
        elif "Transformaciones en la Organización" in txt:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.left_indent = Inches(0)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(38)
            pPr = p._p.get_or_add_pPr()
            for jc in pPr.findall(docx.oxml.ns.qn('w:jc')):
                pPr.remove(jc)
            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
            pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="0" w:right="0" w:firstLine="0"/>'))
        elif any(keyword in txt for keyword in ["Materia:", "Profesores:"]):
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(14)
            pPr = p._p.get_or_add_pPr()
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
        elif any(keyword in txt for keyword in ["Estudiante:", "Email:"]):
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(14)
            pPr = p._p.get_or_add_pPr()
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
        elif any(keyword in txt for keyword in ["Director", "Codirector"]):
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(18)
            pPr = p._p.get_or_add_pPr()
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
        elif "Año 2026" in txt:
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.first_line_indent = Inches(0)
            p.paragraph_format.left_indent = Inches(0)
            p.paragraph_format.space_before = Pt(50)
            p.paragraph_format.space_after = Pt(0)
            pPr = p._p.get_or_add_pPr()
            for jc in pPr.findall(docx.oxml.ns.qn('w:jc')):
                pPr.remove(jc)
            pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for ind in pPr.findall(docx.oxml.ns.qn('w:ind')):
                pPr.remove(ind)
            pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="0" w:right="0" w:firstLine="0"/>'))


def postprocesar_word(tmp_docx):
    if docx is None:
        return
    doc_word = docx.Document(str(tmp_docx))
    aplicar_estilos_base_apa7(doc_word)
    centrar_caratula_oficial(doc_word)
    formatear_parrafos_y_encabezados(doc_word)
    configurar_paginacion_dinamica(doc_word)
    formatear_tablas_apa7(doc_word)
    insertar_tabla_contenidos_word(doc_word)
    aplicar_sangria_francesa_referencias(doc_word)

    # Asegurar 2.54 cm en todas las secciones
    if Cm is not None:
        for sec in doc_word.sections:
            sec.top_margin = Cm(2.54)
            sec.bottom_margin = Cm(2.54)
            sec.left_margin = Cm(2.54)
            sec.right_margin = Cm(2.54)

    doc_word.save(str(tmp_docx))


def compilar_quarto_word():
    print(">> Compilando versión Word (.docx)...")
    ENTREGAS_DIR.mkdir(parents=True, exist_ok=True)
    cmd = ["quarto", "render", str(QMD_FILE), "--to", "docx"]
    try:
        t0 = time.time()
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(BASE_DIR))
        dt = time.time() - t0
        tmp_docx = QMD_FILE.with_suffix(".docx")
        if tmp_docx.exists():
            postprocesar_word(tmp_docx)
            shutil.copy2(str(tmp_docx), str(DOCX_OUT))
            tmp_docx.unlink(missing_ok=True)
            print(f"  [OK] WORD -> {DOCX_OUT.name} ({obtener_info_archivo(DOCX_OUT)}) en {dt:.2f}s")
            return True
        else:
            print(f"  [!] No se generó el archivo Word esperado: {tmp_docx}")
            return False
    except subprocess.CalledProcessError as e:
        print("  [ERROR] Falló compilación a Word:")
        print(e.stderr.strip() or e.stdout.strip())
        return False


def main():
    print("=" * 70)
    print(" 🏛️ COMPILACIÓN TFG-SIA (2026) — DOCS-AS-CODE (APA 7)")
    print(" Estudiante: Andrea Alejandra Díaz")
    print(" Caso: ESRN N° 154 de Viedma (Modelo CEM-ESRN)")
    print("=" * 70)

    ok_pdf = compilar_quarto_pdf()
    ok_word = compilar_quarto_word()

    print("-" * 70)
    if ok_pdf and ok_word:
        print("  ✨ ¡Compilación completada exitosamente!")
        print(f"  📁 Entregas generadas en: {ENTREGAS_DIR}")
        print(f"     - PDF:  {PDF_OUT.name}")
        print(f"     - Word: {DOCX_OUT.name}")
    else:
        print("  ⚠️ Hubo advertencias o fallos durante la compilación.")
    print("=" * 70)


if __name__ == "__main__":
    main()
