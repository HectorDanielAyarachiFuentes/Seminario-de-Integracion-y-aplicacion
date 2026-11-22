import os
import re

print("=== 5. REESTRUCTURANDO TABLA 2 EN _04 ===")
p4_path = "entregas/actividad_4/quarto/secciones/_04_metodologia_y_cronograma.qmd"
with open(p4_path, "r", encoding="utf-8") as f:
    p4 = f.read()

tabla2_nueva = """**Tabla 2**  
*Matriz de Operacionalización de Variables y Dimensiones de Factibilidad (Parte 1: Dimensiones 1 y 2)*

| Dimensión | Variable | Definición Operacional | Indicadores Empíricos | Fuentes e Instrumentos |
| :--- | :--- | :--- | :--- | :--- |
| **1. Normativa y Estatutaria** | Compatibilidad jurídica | Adecuación al Estatuto UNCo, Carrera Docente y CCT Docente (Decreto N° 1246/2015). | • Articulación con informes anuales y evaluaciones cuatrienales.<br>• Preservación de la estabilidad y libertad de cátedra. | Estatuto UNCo, Ord. CS N° 0910/1997 y CCT.<br>*Ficha de análisis documental.* |
| | No sumatividad estatutaria | Resguardo de que el dispositivo carezca de consecuencias punitivas o contractuales. | • Cláusula de destino formativo exclusivo.<br>• Desvinculación de jurados de permanencia. | Normativa de carrera y actas paritarias.<br>*Ficha documental y entrevista gremial.* |
| **2. Técnica e Instrumental** | Plataforma y usabilidad | Accesibilidad de plataformas institucionales (Moodle/SIU) para formularios estructurados. | • Disponibilidad de servidores en Viedma y Nodos.<br>• Tiempo de respuesta menor a 15 minutos. | Personal informático y usuarios.<br>*Ficha técnica y sondeo exploratorio.* |
| | Confidencialidad y anonimato | Medidas de diseño para evitar la reidentificación de los participantes. | • Inhabilitación de registro de IP y metadatos.<br>• Protocolo de anonimización en origen (tokens aleatorios de un solo uso) en sondeos.<br>• Seudonimización estricta (claves alfanuméricas) en entrevistas cualitativas.<br>• Custodia técnica neutral externa a la Dirección ejecutiva.<br>• Regla de umbral mínimo de protección: emisión de reportes individuales únicamente en asignaturas con 5 o más respuestas ($n \\ge 5$); en cursos con menor participación se suprimen reportes desagregados y los datos se integran exclusivamente al informe agregado del área. | Plataforma digital, prueba piloto y protocolos éticos.<br>*Auditoría técnica y matriz de resguardo.* |
| | Mitigación de fatiga | Criterios de brevedad para evitar sobrecarga en asignaturas compartidas. | • Límite estricto de reactivos (hasta 15 ítems).<br>• Frecuencia diagnóstica anual. | Respondientes en prueba piloto.<br>*Cuestionario exploratorio.* |

{{< pagebreak >}}

**Tabla 2 (Continuación)**  
*Matriz de Operacionalización de Variables y Dimensiones de Factibilidad (Parte 2: Dimensiones 3 a 5)*

| Dimensión | Variable | Definición Operacional | Indicadores Empíricos | Fuentes e Instrumentos |
| :--- | :--- | :--- | :--- | :--- |
| **3. Organizacional y Procedimental** | Capacidad departamental | Circuitos y tiempos de gestión para procesar información y coordinar devoluciones. | • Circuitos internos de procesamiento.<br>• Plazos de emisión de reportes globales. | Dirección departamental y docentes.<br>*Entrevistas y revisión de circuitos.* |
| | Articulación con Art. 76 | Canalización de demandas hacia el Programa Anual de Capacitación Docente. | • Registro temático de necesidades prioritarias.<br>• Transferencia formal de insumos al plan anual. | Programas anuales de formación y actas.<br>*Ficha documental y entrevistas.* |
| **4. Cultural y Actitudinal** | Confianza institucional | Predisposición favorable y percepción de seguridad frente a la retroalimentación. | • Nivel de confianza declarado en el fin formativo.<br>• Disposición a recibir comentarios de pares. | Docentes del Departamento.<br>*Cuestionario exploratorio y entrevistas.* |
| | Autorreflexión docente | Valoración de la autoevaluación como herramienta de perfeccionamiento pedagógico. | • Práctica habitual de reflexión sobre la enseñanza.<br>• Interés en confrontar autopercepción con pares. | Docentes del Departamento.<br>*Cuestionario exploratorio y entrevistas.* |
| | Pertinencia del juicio estudiantil | Criterio y seriedad en la valoración estudiantil del acompañamiento pedagógico. | • Percepción docente sobre el juicio estudiantil.<br>• Valoración estudiantil de su propio rol. | Estudiantes regulares y docentes.<br>*Cuestionario a estudiantes y entrevistas.* |
| **5. Gobernanza Multinivel** | Legitimación en cogobierno | Viabilidad para deliberar la propuesta en los órganos colegiados del CURZAS. | • Tratamiento en Consejo Departamental y Directivo.<br>• Búsqueda de consensos interclaustros. | Consejeros departamentales y directivos.<br>*Entrevistas y actas de cogobierno.* |
| | Concertación paritaria | Negociación con la representación gremial (ADUNC) sobre variables de control compartido. | • Criterios gremiales sobre voluntariedad.<br>• Previsión de acuerdos paritarios para pilotaje. | Representantes paritarios de ADUNC.<br>*Guía de entrevista paritaria.* |

*Nota.* Elaboración propia sobre la base de Longo (2006), Cao y Blutman (2019), Estatuto UNCo (Ord. CS N° 0988/2025), Ord. CS N° 0910/1997 y CCT Docente (Decreto N° 1246/2015)."""

# Usar lambda para evitar problemas con secuencias de escape en la sustitución
patron_tabla2 = r'\*\*Tabla 2\*\*.*?\*Nota\.\* Elaboración propia sobre la base de Longo \(2006\)[^\n]*'
p4 = re.sub(patron_tabla2, lambda _: tabla2_nueva, p4, flags=re.DOTALL)

with open(p4_path, "w", encoding="utf-8") as f:
    f.write(p4)
print("Tabla 2 balanceada con éxito en _04!")

# === 6. REENSAMBLAR ARCHIVO COMPLETO Y ARTEFACTOS ===
print("\n=== 6. REENSAMBLANDO ARCHIVO COMPLETO Y ARTEFACTOS ===")
base_dir = "entregas/actividad_4/quarto"
with open(os.path.join(base_dir, "tp4_proyecto_tfg_integral.qmd"), "r", encoding="utf-8") as f:
    master = f.read()

yaml_header = master.split("{{< include")[0].strip() + "\n\n"

secciones = [
    "_01_caratula_e_indice.qmd",
    "_02_problema_y_objetivos.qmd",
    "_03_marco_teorico_y_antecedentes.qmd",
    "_04_metodologia_y_cronograma.qmd",
    "_05_referencias_y_anexos.qmd"
]

partes = [yaml_header]
for sec in secciones:
    ruta = os.path.join(base_dir, "secciones", sec)
    with open(ruta, "r", encoding="utf-8") as f:
        partes.append(f.read().strip() + "\n\n")

contenido_completo = "".join(partes)

completo_path = "entregas/actividad_4/TP4_Ayarachi_Fuentes_COMPLETO.qmd"
with open(completo_path, "w", encoding="utf-8") as f:
    f.write(contenido_completo)
print(f"Actualizado {completo_path} ({len(contenido_completo.splitlines())} líneas)")

artifact_dir = r"C:\Users\Ramoncito\.gemini\antigravity\brain\f7af82bd-a93f-4f81-9ca9-668a3068acb5"
if os.path.exists(artifact_dir):
    with open(os.path.join(artifact_dir, "tp4_codigo_completo.qmd"), "w", encoding="utf-8") as f:
        f.write(contenido_completo)
    with open(os.path.join(artifact_dir, "tp4_codigo_completo.md"), "w", encoding="utf-8") as f:
        f.write("# Código Fuente Completo e Integrado — TP N° 4\n\n```markdown\n" + contenido_completo + "\n```\n")
    print("Artifacts actualizados con éxito.")
