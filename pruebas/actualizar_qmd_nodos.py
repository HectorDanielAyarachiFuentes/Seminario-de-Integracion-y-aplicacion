# -*- coding: utf-8 -*-
"""
Actualiza las referencias a los 10 Nodos e inserta la Figura 2 (red_territorial.svg) en tp4_proyecto_tfg_integral.qmd
"""

qmd_path = 'Entregas/Actividad 4/quarto/tp4_proyecto_tfg_integral.qmd'
with open(qmd_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Párrafo de Contexto Institucional (Línea 177 aprox)
old_context = """A ello se suma la expansión territorial a través de la Red de Nodos Universitarios en localidades de la Línea Sur y la Costa Atlántica rionegrina (Sierra Grande, Valcheta, Los Menucos y Ramos Mexía), donde se implementan modalidades de cursada híbrida reguladas por la Resolución CD-CURZA N° 196/2022 [@curza2022]."""

new_context = """A ello se suma la expansión territorial a través de la Red Territorial de Nodos Universitarios distribuida en 10 localidades rionegrinas (Los Menucos, Sierra Colorada, Valcheta, Ramos Mexía, San Antonio Oeste, General Conesa, Lamarque, Maquinchao, Comallo y Sierra Grande), articuladas desde la sede central de Viedma bajo modalidades de cursada híbrida reguladas por la Resolución CD-CURZA N° 196/2022 [@curza2022] (ver Figura 2).

::: {align="center"}
![*Red Territorial de Nodos Universitarios del CURZAS-UNCo (Resolución CD-CURZA N° 196/2022).*](assets/red_territorial.svg){width=92%}
:::"""

assert old_context in text, 'old_context not found'
text = text.replace(old_context, new_context)

# 2. Delimitación Espacial (Línea 200 aprox)
old_espacial = """* **Delimitación Espacial:** Sede central del CURZAS (Viedma) y Red de Nodos Universitarios (Sierra Grande, Valcheta, Los Menucos y Ramos Mexía) donde el Departamento dicta asignaturas con mediación tecnológica y presencialidad distribuida."""

new_espacial = """* **Delimitación Espacial:** Sede central del CURZAS (Viedma) y Red Territorial de Nodos Universitarios en sus 10 localidades (Los Menucos, Sierra Colorada, Valcheta, Ramos Mexía, San Antonio Oeste, General Conesa, Lamarque, Maquinchao, Comallo y Sierra Grande), donde el Departamento dicta asignaturas bajo modalidades presenciales e híbridas con mediación tecnológica y presencialidad distribuida."""

assert old_espacial in text, 'old_espacial not found'
text = text.replace(old_espacial, new_espacial)

# 3. Nivel Micro Territorial en Gobernanza
old_micro = """3. *Nivel Micro (Territorial):* La Red de Nodos Universitarios (Sierra Grande, Valcheta, Los Menucos y Ramos Mexía), donde las prácticas híbridas demandan acompañamiento tutorial virtual específico [@curza2022]."""

new_micro = """3. *Nivel Micro (Territorial):* La Red Territorial de Nodos Universitarios (10 localidades distribuidas en la Línea Sur, Valle Medio y Costa Atlántica), donde las prácticas híbridas demandan acompañamiento tutorial virtual específico [@curza2022]."""

assert old_micro in text, 'old_micro not found'
text = text.replace(old_micro, new_micro)

# 4. Antecedentes Institucionales (Resolución CD-CURZA N° 196/2022)
old_antecedentes = """* **Red de Nodos y Docencia Híbrida (Resolución CD-CURZA N° 196/2022):** Valida las mediaciones pedagógicas híbridas en las localidades de la Línea Sur y Costa Atlántica rionegrina [@curza2022], demandando competencias de tutoría virtual que actualmente no son ponderadas formativamente por los instrumentos evaluativos vigentes."""

new_antecedentes = """* **Red de Nodos y Docencia Híbrida (Resolución CD-CURZA N° 196/2022):** Valida las mediaciones pedagógicas híbridas en las 10 localidades que integran la red territorial en la Línea Sur, Valle Medio y Costa Atlántica rionegrina [@curza2022], demandando competencias de tutoría virtual que actualmente no son ponderadas formativamente por los instrumentos evaluativos vigentes."""

assert old_antecedentes in text, 'old_antecedentes not found'
text = text.replace(old_antecedentes, new_antecedentes)

# 5. Población Docente en Metodología
old_pob_doc = """* **Población Docente (*N*~doc~ ≈ 38 docentes):** Totalidad de los profesores y auxiliares docentes (regulares e interinos) con designación activa frente a cátedra en el Departamento de Administración Pública, distribuidos entre las asignaturas presenciales de sede Viedma y los espacios con mediación tecnológica y tutoría en la Red de Nodos Universitarios (Sierra Grande, Valcheta, Los Menucos y Ramos Mexía)."""

new_pob_doc = """* **Población Docente (*N*~doc~ ≈ 38 docentes):** Totalidad de los profesores y auxiliares docentes (regulares e interinos) con designación activa frente a cátedra en el Departamento de Administración Pública, distribuidos entre las asignaturas presenciales de sede Viedma y los espacios con mediación tecnológica y tutoría en los 10 Nodos Universitarios de la red territorial (Los Menucos, Sierra Colorada, Valcheta, Ramos Mexía, San Antonio Oeste, General Conesa, Lamarque, Maquinchao, Comallo y Sierra Grande)."""

assert old_pob_doc in text, 'old_pob_doc not found'
text = text.replace(old_pob_doc, new_pob_doc)

# 6. Presupuesto (Nota explicativa)
old_presupuesto = """*Nota.* El relevamiento en los Nodos Universitarios (Sierra Grande, Valcheta, Los Menucos y Ramos Mexía) se realizará mediante formularios digitales y salas de videoconferencia institucionales, sin generar costos extraordinarios de traslado físico."""

new_presupuesto = """*Nota.* El relevamiento en los 10 Nodos Universitarios de la red territorial se realizará mediante formularios digitales autoadministrados y salas de videoconferencia institucionales, sin generar costos extraordinarios de traslado físico."""

assert old_presupuesto in text, 'old_presupuesto not found'
text = text.replace(old_presupuesto, new_presupuesto)

with open(qmd_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('[OK] tp4_proyecto_tfg_integral.qmd actualizado con los 10 Nodos y la Figura 2.')

