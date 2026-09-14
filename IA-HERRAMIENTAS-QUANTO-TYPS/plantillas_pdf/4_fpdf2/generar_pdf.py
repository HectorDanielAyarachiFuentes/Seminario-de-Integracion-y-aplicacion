from fpdf import FPDF
from fpdf.fonts import FontFace

# Colors
DARK_BLUE = (25, 45, 95)
GOLDEN = (200, 150, 50)
LIGHT_GREY = (240, 240, 240)
GREY_TEXT = (100, 100, 100)
LIGHT_BLUE_BG = (245, 248, 250)
LIGHT_BLUE_LINE = (100, 150, 200)

class PDF(FPDF):
    def __init__(self, total_pages_count=None):
        super().__init__()
        self.total_pages_count = total_pages_count

    def header(self):
        if self.page_no() == 1:
            return
            
        self.set_y(15)
        self.set_x(15)
        self.set_font("helvetica", "I", 9)
        self.set_text_color(*GREY_TEXT)
        self.cell(180, 5, "Avance 1: Contexto, Modelo de Gestión y Gobernanza | CURZAS", align="R")
        self.ln(6)
        
        # Thin golden line to give it an elegant touch
        self.set_draw_color(*GOLDEN)
        self.set_line_width(0.3)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(8)

    def footer(self):
        if self.page_no() == 1:
            return
            
        self.set_y(-15)
        self.set_font("helvetica", "", 9)
        self.set_text_color(*GREY_TEXT)
        current_page = self.page_no() - 1
        total = self.total_pages_count if self.total_pages_count else "{nb}"
        self.set_x(15)
        self.cell(0, 10, "Planeamiento y Control de las Organizaciones", new_x="RIGHT", new_y="TOP", align="L")
        self.set_x(15)
        self.cell(180, 10, f"Página {current_page} de {total}", new_x="RIGHT", new_y="TOP", align="R")

    def section_title(self, text):
        self.ln(5)
        start_y = self.get_y()
        self.set_draw_color(*GOLDEN)
        self.set_line_width(1.5)
        self.line(15, start_y + 1, 15, start_y + 7)
        
        self.set_x(18)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*DARK_BLUE)
        self.multi_cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        
        # Reset font to regular for following text
        self.set_font("helvetica", "", 10)
        self.set_text_color(40, 40, 40)

    def blue_box(self, title, content):
        self.ln(3)
        start_y = self.get_y()
        self.set_fill_color(*LIGHT_BLUE_BG)
        # We calculate height first
        self.set_font("helvetica", "", 10)
        lines = len(self.multi_cell(172, 6, content, dry_run=True, output="LINES"))
        box_h = 10 + (lines * 6) + 5
        
        # Check page break
        if self.get_y() + box_h > 270:
            self.add_page()
            start_y = self.get_y()
            
        self.rect(15, start_y, 180, box_h, 'F')
        
        self.set_draw_color(*DARK_BLUE)
        self.set_line_width(1.2)
        self.line(15, start_y, 15, start_y + box_h)
        
        self.set_xy(20, start_y + 5)
        self.set_font("helvetica", "B", 10)
        self.set_text_color(*DARK_BLUE)
        self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        
        self.set_x(20)
        self.set_font("helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(172, 6, content, new_x="LMARGIN", new_y="NEXT")
        self.set_y(start_y + box_h + 5)


def build_pdf(total_pages=None):
    pdf = PDF(total_pages_count=total_pages)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # --- COVER PAGE ---
    pdf.set_y(30)
    pdf.set_x(15)
    pdf.set_font("helvetica", "", 14)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 8, "UNIVERSIDAD NACIONAL DEL COMAHUE", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_x(15)
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(*GOLDEN)
    pdf.cell(0, 8, "COMPLEJO UNIVERSITARIO REGIONAL ZONA ATLÁNTICA Y SUR (CURZAS)", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(10)
    pdf.set_draw_color(*DARK_BLUE)
    pdf.set_line_width(0.8)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(10)
    
    # Vertical line block
    start_y = pdf.get_y()
    pdf.set_font("helvetica", "I", 10)
    pdf.set_text_color(*GREY_TEXT)
    pdf.set_x(20)
    pdf.cell(0, 8, "PLANEAMIENTO Y CONTROL DE LAS ORGANIZACIONES", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(*DARK_BLUE)
    pdf.set_x(20)
    pdf.multi_cell(175, 10, "Avance 1: Contexto, Modelo de Gestión y Gobernanza", new_x="LMARGIN", new_y="NEXT")
    
    pdf.ln(2)
    pdf.set_font("helvetica", "", 14)
    pdf.set_text_color(40, 80, 130)
    pdf.set_x(20)
    pdf.cell(0, 8, "Análisis Institucional sobre el CURZAS (UNCo)", new_x="LMARGIN", new_y="NEXT")
    
    end_y = pdf.get_y()
    
    # Draw the thick vertical line
    pdf.set_draw_color(*DARK_BLUE)
    pdf.set_line_width(2)
    pdf.line(15, start_y + 2, 15, end_y - 2)
    
    pdf.ln(30)
    
    # Metadata for cover
    pdf.set_text_color(*DARK_BLUE)
    metadata = [
        ("Alumno:", "Héctor Daniel Ayarachi Fuentes"),
        ("Carrera:", "Licenciatura en Recursos Humanos"),
        ("Institución:", "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)"),
        ("Sede Académica:", "Viedma, Provincia de Río Negro"),
        ("Marco Teórico:", "Cao & Blutman, Abal Medina, Oszlak"),
        ("Año Académico:", "2026")
    ]
    
    pdf.set_draw_color(*LIGHT_GREY)
    pdf.set_line_width(0.2)
    
    for label, value in metadata:
        pdf.set_x(15)
        pdf.set_font("helvetica", "B", 10)
        pdf.cell(40, 10, label, border=0)
        pdf.set_font("helvetica", "", 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(0, 10, value, border=0, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(*DARK_BLUE)
        # Draw light grey line under row
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        
    pdf.ln(40)
    
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 10, "Viedma, Río Negro - República Argentina", align="C", new_x="LMARGIN", new_y="NEXT")

    # --- CONTENT PAGES ---
    pdf.add_page() # Page 2
    
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    text_sec1 = """El objeto de estudio del presente trabajo es el Complejo Universitario Regional Zona Atlántica y Sur (CURZAS), unidad académica dependiente de la Universidad Nacional del Comahue (UNCo), asentada en la ciudad de Viedma, Provincia de Río Negro. Su estatus institucional responde al mandato constitucional de autonomía y autarquía universitaria (Art. 75 inc. 19 de la Constitución Nacional Argentina y Ley de Educación Superior N° 24.521).

Su marco de creación y funcionamiento se encuentra regido por el Estatuto de la Universidad Nacional del Comahue (Ordenanza N° 470/1993 y sus modificatorias), que establece la estructura organizativa, los órganos co-gobernados de decisión y las misiones fundamentales de docencia, investigación y extensión universitaria."""
    
    pdf.section_title("1. Identificación y Marco Institucional de la Organización")
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec1, new_x="LMARGIN", new_y="NEXT")
    
    box_content = """El CURZAS tiene como misión institucional la generación, formación y democratización del conocimiento científico, técnico y humanístico en el territorio de la Patagonia Norte y la Línea Sur rionegrina. Su estructura organizativa combina áreas académicas, departamentos docentes, secretarías administrativas (Académica, de Investigación, de Extensión y de Gestión Administrativa) y órganos de gobierno colegiados."""
    pdf.blue_box("MISIÓN Y FUNCIONES INSTITUCIONALES", box_content)
    
    pdf.section_title("2. Identificación del Modelo de Administración Predominante")
    text_sec2_intro = """Para analizar el modelo de administración del CURZAS, se coteja la realidad institucional con la tipología teórica provista por Cao y Blutman (2019) y Abal Medina (2014). Según Cao y Blutman (2019), el modelo burocrático tradicional se enfoca en la formalidad de los procesos, la separación estricta de jerarquías y el apego a la norma legal. En contraste, la Nueva Gestión Pública (NGP) introducida en los años 90 busca flexibilizar estas estructuras, orientando la gestión hacia los resultados y el usuario como "cliente" de la administración."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec2_intro, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_x(15)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 6, "A. Rasgos del Modelo Burocrático Tradicional (Weberiano) - PREDOMINANTE", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    text_sec2_a = """El análisis empírico demuestra la prevalencia estructural de la Burocracia Tradicional Weberiana. Como describen Cao y Blutman (2019), este modelo se asienta en la formalidad y el apego a la norma escrita. En primer lugar, la toma de decisiones normativo-administrativas responde a una Estructura Jerárquica y Centralizada fijada estatutariamente (Decanato -> Secretarías -> Direcciones -> Departamentos). En segundo lugar, rige un fuerte Principio de Legalidad y Procedimentalismo: todo acto administrativo debe encuadrarse estrictamente en resoluciones o reglamentos vigentes. Finalmente, la gestión de personal se rige por un Estatuto del Personal y Carrera Administrativa rígida mediante Convenios Colectivos de Trabajo que garantizan la estabilidad laboral y concursos de oposición, rasgos típicos del modelo weberiano para asegurar la imparcialidad."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec2_a, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_x(15)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 6, "B. Elementos Híbridos de la Nueva Gestión Pública (NGP)", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    text_sec2_b = """A pesar del predominio burocrático, se identifican rasgos procedimentales e instrumentales de la NGP, impulsados por la modernización. Existe una Descentralización Operativa, ya que el CURZAS posee autonomía de gestión presupuestaria a través de su Consejo Directivo. Asimismo, se observa una Orientación al Usuario/Estudiante, evidente en la digitalización de trámites a través del sistema SIU-Guaraní y ventanillas únicas."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec2_b, new_x="LMARGIN", new_y="NEXT")
    
    concl_box = "Conclusión: El CURZAS presenta un Modelo Burocrático Tradicional Fuertemente Formalizado con Hibridación Instrumental de NGP."
    pdf.blue_box("DICTAMEN DEL MODELO DE GESTIÓN", concl_box)

    pdf.section_title("3. Análisis de Mecanismos de Rendición de Cuentas (Accountability)")
    text_sec3 = """Tomando las dimensiones desarrolladas por Guillermo O'Donnell y sintetizadas por Abal Medina (2014), la rendición de cuentas puede dividirse conceptualmente en tres ejes: la accountability horizontal (donde agencias estatales controlan a otras agencias del mismo Estado), la vertical (donde la ciudadanía ejerce premio o castigo mediante elecciones) y la social (mecanismos de la sociedad civil para exigir transparencia e información). El CURZAS presenta mecanismos estructurados en estos tres ejes:"""
    pdf.set_x(15)
    pdf.set_x(15)
    
    # Table using FPDF2 Native API with FontFace and Markdown
    pdf.set_draw_color(210, 225, 240)
    pdf.set_line_width(0.3)
    
    table_data = [
        ["Tipo de Accountability", "Mecanismos Vigentes en CURZAS / UNCo", "Evidencia Documental / Normativa"],
        [
            "**Horizontal**\n(Controles intra-estatales)",
            "- Auditoría Interna de la UNCo.\n- Auditoría General de la Nación (AGN) y SIGEN.\n- Control institucional entre órganos (Consejo Directivo evalúa las decisiones del Decanato).",
            "- Informes periódicos de auditoría pública.\n- Ley 24.156 de Administración Financiera.\n- Memoria y Balance Anual."
        ],
        [
            "**Vertical**\n(Electoral y Representativo)",
            "- Elecciones periódicas, directas y obligatorias para renovar autoridades (Decano/a) y representantes claustrales.\n- Cogobierno universitario integrado por Docentes, Nodocentes, Estudiantes y Graduados.",
            "- Estatuto General de la UNCo.\n- Calendario electoral y resoluciones de la Junta Electoral Universidad."
        ],
        [
            "**Social**\n(Ciudadanía e Infra-institucional)",
            "- Portal Institucional de Transparencia Activa.\n- Solicitudes de Acceso a la Información Pública.\n- Publicación de datos presupuestarios, licitaciones y nóminas en la web.",
            "- Ley 27.275 de Acceso a la Información Pública.\n- Portal web de Transparencia Abierta UNCo."
        ]
    ]

    with pdf.table(
        col_widths=(45, 80, 55),
        line_height=4.8,
        text_align="LEFT",
        width=180,
        first_row_as_headings=True,
        headings_style=FontFace(color=(255, 255, 255), fill_color=DARK_BLUE, size_pt=9.5),
        cell_fill_color=LIGHT_BLUE_BG,
        cell_fill_mode="ROWS",
        markdown=True,
        padding=(2.5, 2.5, 2.5, 2.5)
    ) as table:
        for row_data in table_data:
            row = table.row()
            for cell_data in row_data:
                row.cell(cell_data)
        
    pdf.ln(5)

    pdf.section_title("4. Evaluación de Gobernanza Pública Inteligente (Según Oszlak)")
    text_sec4_intro = """Siguiendo los desarrollos teóricos de Oscar Oszlak (2020) sobre el tránsito desde el Gobierno Electrónico hacia el "Estado Inteligente" y la Gobernanza Algorítmica, se procedió a evaluar la presencia de automatización e Inteligencia Artificial en la organización."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec4_intro, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_x(15)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 6, "A. Digitalización e Interoperabilidad Administrativa (Fase Pre-Inteligente)", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(0, 0, 0)
    text_sec4_a = """El CURZAS ha completado de manera satisfactoria la fase de digitalización burocrática mediante la implementación obligatoria del sistema SUDOCU y el ecosistema SIU. Esto permite trazabilidad, firmas digitales y gestión transparente."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec4_a, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    pdf.set_x(15)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 6, "B. Análisis de la Pregunta Guía Específica: Algoritmos e IA en RR.HH.", new_x="LMARGIN", new_y="NEXT")
    
    pregunta_box = "¿Cuenta el área con normativas vigentes sobre la incorporación de algoritmos o software predictivo en la selección o monitoreo de personal?"
    pdf.blue_box("PREGUNTA DE INVESTIGACIÓN INSTITUCIONAL", pregunta_box)

    pdf.set_x(15)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 6, "Resultado del Relevamiento Normativo e Institucional:", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 10)
    text_sec4_b = """- Inexistencia de Sistemas Algorítmicos Predictivos: Oszlak (2020) señala que la gobernanza algorítmica implica el uso de tecnologías disruptivas y automatizadas (como la Inteligencia Artificial) para la toma de decisiones públicas. En el CURZAS, no existen iniciativas normativas para implementar software predictivo en la selección de personal o el monitoreo disciplinario.
- Garantía de Control Humano y Paritario: La adopción de IA en RR.HH. se encuentra bloqueada normativamente. El concurso público se rige 100% por jurados y comisiones paritarias integradas por personas humanas, garantizado por Convenios Colectivos de Trabajo. La evaluación algorítmica está excluida, demostrando que la barrera a la IA no es meramente tecnológica, sino institucional y sindical.
- Estado Actual en la Escala de Oszlak: El organismo ha consolidado la fase de "Gobierno Electrónico" y Digitalización Avanzada de Trámites (expediente digital), pero se encuentra aún distante de la fase de "Estado Inteligente" y Gobernanza Algorítmica en el control de sus recursos humanos."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec4_b, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.section_title("5. Conclusión Sintética")
    text_sec5 = """El CURZAS constituye un modelo claro de administración pública universitaria donde se conjuga una matriz burocrática tradicional garante de derechos laborales, con herramientas de la Nueva Gestión Pública orientadas a la transparencia y digitalización. La incorporación de la Inteligencia Artificial (Estado Inteligente propuesto por Oszlak) permanece como una asignatura pendiente, fuertemente regulada y limitada por los mecanismos constitucionales y paritarios vigentes."""
    pdf.set_x(15)
    pdf.multi_cell(180, 6, text_sec5, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    pdf.add_page()
    pdf.set_y(30)
    pdf.set_fill_color(*LIGHT_BLUE_BG)
    pdf.rect(15, pdf.get_y(), 180, 70, 'F')
    pdf.set_xy(20, pdf.get_y() + 5)
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(*DARK_BLUE)
    pdf.cell(0, 6, "Bibliografía y Fuentes Consultadas", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    bibliografia = [
        "- Cao, Horacio y Blutman, Gustavo (2019). Continuidades y rupturas en las ideas sobre reforma y modernización del Estado. Buenos Aires: INAP / Universidad de Buenos Aires.",
        "- Abal Medina, Juan Manuel (2014). Manual de Administración Pública. Buenos Aires: Ariel. Capítulos 1 y 5.",
        "- Oszlak, Oscar (2020). El Estado en la era exponencial: Tecnologías disruptivas y gestión pública. Buenos Aires: Editorial INAP.",
        "- Universidad Nacional del Comahue (1993/2023). Estatuto de la Universidad Nacional del Comahue. Neuquén/Viedma.",
        "- Leyes Nacionales: Ley de Educación Superior N° 24.521; Ley de Acceso a la Información Pública N° 27.275; Convenios Colectivos de Trabajo Decretos 366/06 y 1246/15."
    ]
    for item in bibliografia:
        pdf.set_x(20)
        pdf.multi_cell(170, 5, item, new_x="LMARGIN", new_y="NEXT")

    return pdf

# First pass
temp_pdf = build_pdf()
total_content_pages = temp_pdf.page_no() - 1

# Second pass
final_pdf = build_pdf(total_pages=total_content_pages)
final_pdf.output("Avance_1_Contexto_Modelo_Gestion_Gobernanza_CURZAS_Hector_Ayarachi_Mejorado.pdf")
print("PDF generado con éxito.")
