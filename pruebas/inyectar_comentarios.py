import fitz

pdf_in = "Entregas/Actividad 3/Correcion/TP3_Ayarachi_Fuentes_Corregido.pdf"
pdf_out = "Entregas/Actividad 3/Correcion/TP3_Ayarachi_Fuentes_Con_Comentarios.pdf"

doc = fitz.open(pdf_in)

anotaciones_data = [
    {
        "num": 1,
        "titulo": "Corrección 1: Denominación de Carrera en CURZAS",
        "docente": "Fijarse si corresponde escribir de esta manera, averiguar. O: y ciclo complementario en la Licenciatura ...",
        "antes": "Tiene a su cargo las carreras de Licenciatura en Administración Pública, Licenciatura en Gestión de Recursos Humanos y ciclos de complementación...",
        "despues": "Tiene a su cargo las carreras de Licenciatura en Administración Pública, el Ciclo de Complementación Curricular de la Licenciatura en Gestión de Recursos Humanos y trayectos formativos...",
        "justificacion": "Ajuste de precisión institucional conforme a la Ordenanza CS N° 0180/2014. En el CURZAS la carrera para técnicos graduados se estructura formalmente bajo la modalidad de Ciclo de Complementación Curricular (CCC).",
        "search_text": "Ciclo de Complementación Curricular de la Licenciatura en Gestión de Recursos Humanos",
        "page_filter": 5
    },
    {
        "num": 2,
        "titulo": "Corrección 2: Tono Institucional Universitario",
        "docente": "impone no es pertinente quizás ofrece. La universidad se encuentra lejos de imponer acciones formativas.",
        "antes": "Esta expansión territorial impone modalidades pedagógicas híbridas...",
        "despues": "Esta expansión territorial promueve y ofrece modalidades pedagógicas híbridas...",
        "justificacion": "Se adoptó la sugerencia de la docente. En la universidad pública autónoma y cogobernada rige la libertad de cátedra y la construcción compartida; el verbo 'promueve y ofrece' refleja adecuadamente la cultura institucional de la UNCo.",
        "search_text": "promueve y ofrece modalidades pedagógicas híbridas",
        "page_filter": 5
    },
    {
        "num": 3,
        "titulo": "Corrección 3: Sangría de Primera Línea (Normas APA 7)",
        "docente": "Sangría",
        "antes": "El primer párrafo posterior al subtítulo no presentaba sangría (iniciaba al ras del margen izquierdo a 72.0 pt).",
        "despues": "Se implementó sangría reglamentaria de 1,27 cm (108.0 pt) en el primer párrafo tras el encabezado.",
        "justificacion": "Normas APA 7ma Edición estipula que todos los párrafos del cuerpo deben llevar sangría de primera línea de 1,27 cm (0,5 pulg). Se programó una regla tipográfica universal en estilos.typ para asegurar la sangría en todos los primeros párrafos.",
        "search_text": "Construir un problema científico exige desnaturalizar",
        "page_filter": 6
    },
    {
        "num": 4,
        "titulo": "Corrección 4: Párrafo de una sola oración y punto seguido",
        "docente": "Punto seguido. Ten presente que los párrafos deben construirse de dos o más oraciones. en este caso el párrafo siguiente es pertinente al señalado.",
        "antes": "Dos párrafos separados; el primero constaba de una sola oración sobre evaluación 360° y el segundo iniciaba en 'En una universidad pública cogobernada...'.",
        "despues": "Se unificaron ambos bloques temáticos mediante punto y seguido en un párrafo integrado de desarrollo argumental completo.",
        "justificacion": "Criterio de redacción científica de la cátedra SIA: un párrafo no debe quedar aislado con una única oración. La fusión otorga cohesión textual entre la propuesta del modelo 360° y las particularidades del régimen estatutario.",
        "search_text": "valoración de las autoridades académicas. En una universidad pública",
        "page_filter": 6
    },
    {
        "num": 5,
        "titulo": "Corrección 5: Sintaxis de Conectores y Fluidez Verbal",
        "docente": "A fin de responder este ..... cambia por la palabra para.",
        "antes": "Fórmula con locución compleja ('A fin de responder a este interrogante...').",
        "despues": "Conector directo y fluido: 'Para responder a este interrogante, la literatura sobre evaluación docente...'",
        "justificacion": "Economía de lenguaje y fluidez sintáctica conforme al estilo de escritura académica recomendado por la cátedra.",
        "search_text": "Para responder a este interrogante, la literatura",
        "page_filter": 6
    },
    {
        "num": 6,
        "titulo": "Corrección 6: Alcance del Diseño Preliminar vs. Metodología",
        "docente": "Esta información es importante pero redundante para el diseño de investigación.",
        "antes": "Tres (3) páginas continuas que incluían matriz exhaustiva de operacionalización con tablas de indicadores empíricos de campo y escalas cerradas de factibilidad.",
        "despues": "Se sintetizó la definición conceptual de factibilidad en 2 párrafos fluidos y se incorporó una nota metodológica que explicita que la matriz de campo se desarrollará en el TP N° 4.",
        "justificacion": "Se atendió plenamente la observación de fondo: en la etapa de planteo del problema (TP2/TP3) la operacionalización detallada resulta prematura y sobrecarga el diseño; corresponde al capítulo metodológico operativo (TP N° 4).",
        "search_text": "Enfoque Analítico de las Dimensiones de Factibilidad",
        "page_filter": 8
    },
    {
        "num": 7,
        "titulo": "Corrección 7: Supresión de Negritas en el Texto Corrido",
        "docente": "evitar negritas, en el párrafo para expresar el rigor científico debe ser claro y preciso, no necesita utilizar este estilo.",
        "antes": "Uso de negritas dentro del cuerpo del párrafo: '...la factibilidad no se reduce a una viabilidad formal o teórica...'.",
        "despues": "Texto corrido en tipografía regular sin resaltados artificiales: '...la factibilidad no se reduce a una viabilidad formal o teórica...'.",
        "justificacion": "Normas APA 7ma Edición prohíbe el uso de negritas en el cuerpo de los párrafos para enfatizar ideas. El rigor argumentativo emana de la claridad expositiva y la estructura oracional, no de artificios tipográficos.",
        "search_text": "la factibilidad no se reduce a una viabilidad formal o teórica",
        "page_filter": 8
    },
    {
        "num": 8,
        "titulo": "Corrección 8: Secuencia Estructural (Problema -> Preguntas -> Objetivos)",
        "docente": "Antes de la pregunta de investigación se encuentran los objetivos",
        "antes": "La Pregunta General quedó desarticulada en la pág. 10 tras la larga tabla de factibilidad, y los Objetivos se ubicaron en la pág. 11.",
        "despues": "Secuencia canónica reordenada: Problematización y delimitación -> Pregunta General -> Justificación y Relevancia -> Definición de Objetivos (General, Específicos y Matriz de consistencia).",
        "justificacion": "Se restableció la articulación secuencial canónica estipulada por la Resolución CD-CURZAS N° 266/23, asegurando la correspondencia unívoca entre la pregunta central y el objetivo general sin interferencias intermedias.",
        "search_text": "¿Cuáles son las condiciones de factibilidad organizacional, técnica",
        "page_filter": 9
    }
]

total_inyectadas = 0

for item in anotaciones_data:
    p_num = item["page_filter"] - 1 # 0-indexed
    page = doc[p_num]
    rects = page.search_for(item["search_text"])
    
    if not rects:
        # Fallback search across pages
        for idx_page, p_alt in enumerate(doc):
            if idx_page < 2:
                continue
            r_alt = p_alt.search_for(item["search_text"][:25])
            if r_alt:
                page = p_alt
                rects = r_alt
                p_num = idx_page
                break

    if rects:
        r = rects[0]
        # Crear resaltado visual sutil en color verde esmeralda / turquesa suave
        highlight = page.add_highlight_annot(r)
        highlight.set_colors(stroke=[0.2, 0.72, 0.45]) # verde esmeralda suave
        
        # Redactar contenido enriquecido del popup
        contenido_popup = (
            f"✅ {item['titulo']}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👩‍🏫 OBSERVACIÓN DOCENTE (Esp. María Cecilia Aguirre):\n"
            f"«{item['docente']}»\n\n"
            f"🔴 ANTES (Versión evaluada):\n"
            f"{item['antes']}\n\n"
            f"🟢 DESPUÉS (Versión corregida):\n"
            f"{item['despues']}\n\n"
            f"💡 JUSTIFICACIÓN METODOLÓGICA Y NORMATIVA:\n"
            f"{item['justificacion']}"
        )
        
        highlight.set_info({
            "title": "Héctor Daniel Ayarachi Fuentes (Respuesta a Cátedra)",
            "content": contenido_popup,
            "subject": item["titulo"]
        })
        highlight.update()

        # También agregar un icono de comentario sutil en el margen izquierdo
        icon_point = fitz.Point(max(35, r.x0 - 25), r.y0 + 2)
        text_annot = page.add_text_annot(icon_point, contenido_popup, icon="Comment")
        text_annot.set_info({
            "title": f"Ayarachi Fuentes — {item['titulo']}",
            "content": contenido_popup,
            "subject": item["titulo"]
        })
        text_annot.set_colors(stroke=[0.1, 0.6, 0.35])
        text_annot.update()
        
        total_inyectadas += 1
        print(f"[{item['num']}/8] Inyectada en Página {p_num + 1}: {item['titulo']}")
    else:
        print(f"[!] No encontrada para inyectar: {item['titulo']}")

doc.save(pdf_out)
doc.close()
print(f"\nProceso finalizado. Total de anotaciones inyectadas: {total_inyectadas}")
print(f"Archivo guardado: {pdf_out}")
