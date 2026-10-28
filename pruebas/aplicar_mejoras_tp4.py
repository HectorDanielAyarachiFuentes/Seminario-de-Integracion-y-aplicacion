# -*- coding: utf-8 -*-
"""
Aplica todas las mejoras metodológicas y de maquetación al archivo tp4_proyecto_tfg_integral.qmd
"""
import re
from pathlib import Path

qmd_path = Path("Entregas/Actividad 4/quarto/tp4_proyecto_tfg_integral.qmd")
with open(qmd_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ajustar el ancho del gráfico de Longo de 50% a 95%
content = content.replace(
    'assets/Sistemas-longo.svg){width=50%}',
    'assets/Sistemas-longo.svg){width=95%}'
)

# 2. Agregar saltos de línea antes de listas que quedaron pegadas
replacements_lists = [
    (
        "En el plano regulatorio, la labor docente en la institución se encuentra regida por:\n1. El Estatuto",
        "En el plano regulatorio, la labor docente en la institución se encuentra regida por:\n\n1. El Estatuto"
    ),
    (
        "En el CURZAS-UNCo, esta evaluación preliminar abarca cinco dimensiones analíticas:\n1. *Factibilidad",
        "En el CURZAS-UNCo, esta evaluación preliminar abarca cinco dimensiones analíticas:\n\n1. *Factibilidad"
    ),
    (
        "### Objetivos Específicos\n1. Relevar y caracterizar",
        "### Objetivos Específicos\n\n1. Relevar y caracterizar"
    ),
    (
        "Esta perspectiva resulta fértil para el estudio de la factibilidad organizacional:\n1. *La realidad social",
        "Esta perspectiva resulta fértil para el estudio de la factibilidad organizacional:\n\n1. *La realidad social"
    ),
    (
        "interdependencia con otros tres subsistemas:\n* **Gestión del Rendimiento:**",
        "interdependencia con otros tres subsistemas:\n\n* **Gestión del Rendimiento:**"
    ),
    (
        "cuatro miradas sobre la práctica educativa:\n1. *Autoevaluación docente:*",
        "cuatro miradas sobre la práctica educativa:\n\n1. *Autoevaluación docente:*"
    ),
    (
        "enfoque sociocéntrico y relacional:\n* *El Estado plataforma",
        "enfoque sociocéntrico y relacional:\n\n* *El Estado plataforma"
    ),
    (
        "cuatro planos interdependientes:\n1. *Nivel Macro (Central):*",
        "cuatro planos interdependientes:\n\n1. *Nivel Macro (Central):*"
    ),
    (
        "Carlos Matus y Oscar Oszlak:\n* *Carlos Matus",
        "Carlos Matus y Oscar Oszlak:\n\n* *Carlos Matus"
    ),
    (
        "dos categorías conceptuales:\n* *Claustros (categoría",
        "dos categorías conceptuales:\n\n* *Claustros (categoría"
    ),
    (
        "descriptivo, exploratorio y propositivo:\n* *Descriptivo:*",
        "descriptivo, exploratorio y propositivo:\n\n* *Descriptivo:*"
    ),
    (
        "tres técnicas complementarias:\n1. **Análisis documental",
        "tres técnicas complementarias:\n\n1. **Análisis documental"
    ),
    (
        "garantías institucionales y éticas:\n1. **Protección de datos",
        "garantías institucionales y éticas:\n\n1. **Protección de datos"
    ),
    (
        "previstas en el diseño:  \na) Consulta de documentación",
        "previstas en el diseño:\n\na) Consulta de documentación"
    ),
    (
        "4. **Constancia y Declaración del Participante:**\n   - Declaro haber",
        "4. **Constancia y Declaración del Participante:**\n\n   - Declaro haber"
    ),
]

for orig, repl in replacements_lists:
    # Normalizar saltos de línea para que matchee
    orig_crlf = orig.replace("\n", "\r\n")
    if orig in content:
        content = content.replace(orig, repl)
    elif orig_crlf in content:
        content = content.replace(orig_crlf, repl.replace("\n", "\r\n"))

# 3. Dilema de las Cátedras Unipersonales en el Modelo 360° y en los Objetivos
# En Objetivo Específico 3:
orig_obj3 = "3. Identificar los condicionantes técnico-organizacionales, normativos y de gobernanza multinivel (acuerdos paritarios, carrera docente, confidencialidad y cogobierno) que inciden en la factibilidad del modelo en el marco de la poligobernanza institucional."
repl_obj3 = "3. Identificar los condicionantes técnico-organizacionales (incluyendo la resolución de la coevaluación en cátedras unipersonales mediante pares horizontales por área o tramo curricular), normativos y de gobernanza multinivel (acuerdos paritarios, carrera docente, confidencialidad y cogobierno) que inciden en la factibilidad del modelo en el marco de la poligobernanza institucional."
content = content.replace(orig_obj3, repl_obj3)

# En la definición del modelo 360° (coevaluación de pares):
orig_coeval = "2. *Coevaluación de pares:* Valoración colegiada realizada por docentes del mismo equipo de cátedra o área disciplinar, focalizada en la pertinencia conceptual, la rigurosidad disciplinar y el trabajo colaborativo."
repl_coeval = "2. *Coevaluación de pares:* Valoración colegiada realizada por docentes del mismo equipo de cátedra o área disciplinar, focalizada en la pertinencia conceptual, la rigurosidad disciplinar y el trabajo colaborativo. Para las asignaturas de cátedra unipersonal (frecuentes en el Departamento de Administración Pública y en el CCC de RRHH, donde una materia cuenta con un único docente sin auxiliares ni adjuntos), la investigación indagará la viabilidad de instrumentar una **coevaluación horizontal por área o tramo curricular** (articulando docentes de materias afines del mismo año o ciclo), evitando que el anillo de pares del dispositivo 360° quede vacante."
content = content.replace(orig_coeval, repl_coeval)

# 4. Custodia del anonimato en la Matriz de Operacionalización y en Consideraciones Éticas
# Matriz:
orig_matriz_anon = "• Inhabilitación de registro de IP y metadatos.<br>• Agrupamiento de variables sociodemográficas."
repl_matriz_anon = "• Inhabilitación de registro de IP y metadatos.<br>• Agrupamiento de variables sociodemográficas.<br>• Protocolo de anonimización en origen (tokens aleatorios de un solo uso).<br>• Custodia técnica neutral: procesamiento a cargo de una comisión ad-hoc o área pedagógica neutral externa a la Dirección, que entrega al Departamento reportes consolidados y al docente su reporte individual confidencial."
content = content.replace(orig_matriz_anon, repl_matriz_anon)

# Consideraciones Éticas:
orig_etica = """1. **Protección de datos y resguardo de identidad:** Conforme a la Ley Nacional N° 25.326 de Protección de los Datos Personales [@ley25326], se garantiza la estricta disociación entre las respuestas y la identidad de los participantes. El cuestionario digital se administra sin registrar correos electrónicos ni direcciones IP, y las variables sociodemográficas se agrupan en categorías amplias para impedir la identificación por deducción en cátedras con pocos integrantes."""
repl_etica = """1. **Protección de datos y resguardo de identidad (Custodia del Anonimato):** Conforme a la Ley Nacional N° 25.326 de Protección de los Datos Personales [@ley25326], se garantiza la estricta disociación entre las respuestas y la identidad de los participantes. El cuestionario digital se administra bajo un protocolo de **anonimización en origen** mediante tokens aleatorios de un solo uso, sin registrar correos electrónicos ni direcciones IP. Para disipar cualquier incertidumbre sobre cruce de horarios o permisos de administrador en servidores institucionales, la custodia y administración técnica del instrumento será gestionada por un área pedagógica neutral o comisión técnica ad-hoc independiente de la conducción ejecutiva del Departamento. Dicha custodia garantiza que el Departamento solo reciba informes diagnósticos agregados y globales, mientras que cada docente recibe de forma directa y confidencial su reporte individual de retroalimentación pedagógica, impidiendo cualquier reidentificación por deducción en cátedras unipersonales o con reducida matrícula."""

# Reemplazo flexible de consideraciones éticas
if orig_etica in content:
    content = content.replace(orig_etica, repl_etica)
else:
    orig_etica_crlf = orig_etica.replace("\n", "\r\n")
    if orig_etica_crlf in content:
        content = content.replace(orig_etica_crlf, repl_etica.replace("\n", "\r\n"))

# 5. Precisar los instrumentos por perfil en el Anexo I (Entrevistas)
anexo1_pat = r"### Anexo I: Guía Temática de Entrevista Semiestructurada \{.unnumbered\}.*?(?=\{\{< pagebreak >\}\})"
repl_anexo1 = """### Anexo I: Guía Temática de Entrevista Semiestructurada {.unnumbered}

**Proyecto:** *Evaluación del Desempeño Docente y Factibilidad de un Modelo de Retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo (2027)*  
**Investigador:** Tec. Sup. Héctor Daniel Ayarachi Fuentes  

*Objetivo:* Relevar opiniones, percepciones y juicios críticos sobre los mecanismos actuales de evaluación docente y las condiciones de factibilidad para un circuito formativo 360° adaptado a la singularidad institucional.

#### Bloque A: Guía Temática para Docentes de Cátedra y Autoridades Académicas {.unnumbered}

1. **Evaluación vigente:** ¿Qué balance realiza de los instrumentos actuales (informes anuales, encuestas estudiantiles y evaluaciones cuatrienales de permanencia)?
2. **Uso pedagógico:** ¿En qué medida considera que las opiniones estudiantiles actuales se traducen en mejoras de la enseñanza o en planes de capacitación?
3. **Autoevaluación:** ¿Realiza habitualmente instancias de autorreflexión sobre su práctica pedagógica? ¿Qué utilidad le asigna a formalizar dicha instancia?
4. **Mirada de pares y cátedras unipersonales:** ¿Qué condiciones de confianza institucional considera necesarias para que la coevaluación entre colegas sea constructiva? En asignaturas de docente único, ¿ve viable la coevaluación horizontal entre pares de materias afines del mismo tramo curricular?
5. **Nodos Territoriales:** En asignaturas con modalidad híbrida en la Línea Sur y Costa Atlántica, ¿qué aspectos de la labor docente (tutoría virtual, diseño de recursos) deberían valorarse de forma diferenciada?
6. **Resguardos necesarios:** ¿Qué salvaguardas (anonimato, voluntariedad, desvinculación de legajos sumativos) considera indispensables para legitimar una propuesta de este tipo?
7. **Articulación departamental:** ¿De qué forma deberían vincularse los resultados con el Programa Anual de Capacitación Docente (Art. 76 del Estatuto UNCo)?

#### Bloque B: Preguntas Específicas para la Representación Gremial Paritaria (ADUNC) {.unnumbered}

1. **Compatibilidad normativa y estabilidad laboral:** ¿Qué condiciones y salvaguardas paritarias considera prioritario establecer para asegurar la plena compatibilidad con los Arts. 74 y 75 del Estatuto UNCo y el Convenio Colectivo de Trabajo Docente (Decreto N° 1246/2015), blindando el carácter estrictamente formativo del modelo frente a cualquier uso sumativo o punitivo?
2. **Veeduría y custodia de datos:** ¿Qué mecanismos de veeduría y gobernanza gremial deberían incorporarse en la administración y custodia técnica de los formularios para otorgar plena certeza de que los datos diagnósticos no serán transferidos a legajos ni utilizados por jurados de permanencia o acreditación?

#### Bloque C: Preguntas Específicas para Estudiantes Avanzados {.unnumbered}

1. **Utilidad percibida de la evaluación actual:** En base a su trayectoria, ¿qué balance realiza de la utilidad pedagógica real de las encuestas estudiantiles obligatorias que se completan en SIU-Guaraní al término de cada cursada? ¿Considera que sus aportes inciden efectivamente en cambios o mejoras en la enseñanza?
2. **Condiciones para la retroalimentación constructiva:** ¿Qué condiciones de anonimato y qué tipo de aspectos de la enseñanza (ej. claridad didáctica, acompañamiento tutorial virtual en Nodos, criterios de evaluación y devoluciones) considera más relevantes de incorporar en una retroalimentación formativa para opinar con sinceridad y compromiso?

"""

content = re.sub(anexo1_pat, repl_anexo1, content, flags=re.DOTALL)

# 6. Tabla del Anexo II con proporciones de columnas relativas y las 2 Preguntas Abiertas
anexo2_pat = r"### Anexo II: Cuestionario Exploratorio de Factibilidad \(Escala Likert\) \{.unnumbered\}.*?(?=\{\{< pagebreak >\}\})"
repl_anexo2 = """### Anexo II: Cuestionario Exploratorio de Factibilidad (Escala Likert) {.unnumbered}

*Instrucciones:* Indique su nivel de acuerdo marcando del 1 al 5 (1: Totalmente en desacuerdo; 2: En desacuerdo; 3: Ni de acuerdo ni en desacuerdo; 4: De acuerdo; 5: Totalmente de acuerdo).

| N° | Reactivo | 1 | 2 | 3 | 4 | 5 |
|:----:|:----------------------------------------------------------|:---:|:---:|:---:|:---:|:---:|
| 1 | La evaluación docente debería orientarse prioritariamente al aprendizaje pedagógico continuo y no al control formal. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | Es indispensable que los reportes individuales no integren legajos de permanencia ni concursos laborales. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 3 | Las plataformas institucionales (Moodle/SIU) son adecuadas para administrar cuestionarios anónimos. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 4 | Confío en que el sistema informático puede garantizar el anonimato técnico de las respuestas. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 5 | Un cuestionario breve (hasta 15 preguntas) es suficiente para evaluar la labor docente sin generar sobrecarga. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 6 | El Departamento dispone de capacidad organizativa para coordinar devoluciones diagnósticas oportunas. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 7 | Los resultados consolidados deberían alimentar el Programa Anual de Capacitación Docente (Art. 76). | [ ] | [ ] | [ ] | [ ] | [ ] |
| 8 | Estaría dispuesto/a a participar voluntariamente de una autoevaluación reflexiva sobre mi enseñanza. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 9 | Considero enriquecedor recibir comentarios constructivos de colegas de cátedra sobre la labor docente. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 10 | Los estudiantes cuentan con criterio suficiente para opinar con seriedad sobre el acompañamiento pedagógico. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 11 | En el Departamento existe un clima de confianza que permite dialogar sobre fortalezas y dificultades didácticas. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 12 | Una propuesta evaluativa formativa debe ser debatida previamente en el Consejo Departamental. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 13 | El acuerdo de la representación gremial docente (ADUNC) es un requisito central para su viabilidad. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 14 | En los Nodos Territoriales deben evaluarse aspectos específicos de tutoría y comunicación virtual. | [ ] | [ ] | [ ] | [ ] | [ ] |
| 15 | Estaría dispuesto/a a participar de una experiencia piloto voluntaria de retroalimentación multiactoral. | [ ] | [ ] | [ ] | [ ] | [ ] |

<br>

**Preguntas Abiertas Complementarias:**

* **Pregunta abierta 1:** ¿Qué condición o resguardo considera prioritario garantizar para participar con confianza en una instancia de retroalimentación docente?  
  *Respuesta:* `...........................................................................................................................................................`  
  `...........................................................................................................................................................`

* **Pregunta abierta 2:** ¿Qué aspectos específicos de la cursada (presencial en sede o híbrida en Nodos Territoriales) cree que no están siendo captados por las encuestas actuales?  
  *Respuesta:* `...........................................................................................................................................................`  
  `...........................................................................................................................................................`

"""

content = re.sub(anexo2_pat, repl_anexo2, content, flags=re.DOTALL)

# 7. Espacio de firma en la Nota de Aval (Anexo III)
anexo3_pat = r"Agradeciendo su atención, saludo a Usted atentamente\..*?(?=\{\{< pagebreak >\}\})"
repl_anexo3 = """Agradeciendo su atención, saludo a Usted atentamente.

<br>
<br>

::: {.content-visible when-format="typst"}
```{=typst}
#v(2.5cm)
#align(center)[
  #line(length: 65%, stroke: 0.5pt + black)
  #v(0.6em)
  #text(weight: "bold")[Tec. Sup. Héctor Daniel Ayarachi Fuentes] \
  Legajo N° 8252 — DNI N° 35.492.138 \
  Estudiante del CCC de la Licenciatura en Gestión de Recursos Humanos \
  Departamento de Administración Pública — CURZAS-UNCo
]
```
:::

::: {.content-visible when-format="docx"}
<br>
<br>

::: {align="center"}
................................................................................................................  
**Tec. Sup. Héctor Daniel Ayarachi Fuentes**  
Legajo N° 8252 — DNI N° 35.492.138  
Estudiante del CCC de la Licenciatura en Gestión de Recursos Humanos  
Departamento de Administración Pública — CURZAS-UNCo  
:::
:::

"""

content = re.sub(anexo3_pat, repl_anexo3, content, flags=re.DOTALL)

with open(qmd_path, "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] Mejoras aplicadas exitosamente en tp4_proyecto_tfg_integral.qmd")

