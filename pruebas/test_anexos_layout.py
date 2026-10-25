import subprocess
from pathlib import Path
import pymupdf

nota_qmd = """
{{< pagebreak >}}

### Anexo III: Modelo de Nota Institucional de Solicitud de Aval Académico {.unnumbered}

::: {align="center"}
**SOLICITUD DE AVAL ACADÉMICO PARA INVESTIGACIÓN DE TFG**
:::

Viedma, Río Negro, ______ de ________________ de 202___

**A la Dirección del Departamento de Administración Pública**  
**Complejo Universitario Regional Zona Atlántica y Sur (CURZAS — UNCo)**  

De mi mayor consideración:  

Me dirijo a Usted como estudiante regular del Ciclo de Complementación Curricular de la Licenciatura en Gestión de Recursos Humanos (Legajo N° 8252 — DNI N° 35.492.138), en el marco de la formulación de mi Trabajo Final de Graduación para la asignatura *Seminario de Integración y Aplicación* (SIA 2025/2026), titulado:  

> **"Evaluación del Desempeño Docente y Factibilidad de Implementación de un Modelo de Retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo (2027)"**  

Por la presente, solicito formalmente el correspondiente **aval institucional y autorización de acceso al campo** para llevar adelante las tareas de relevamiento previstas en el diseño:  

* a) Consulta de documentación reglamentaria y programas de capacitación docente;  
* b) Realización de entrevistas a informantes clave (autoridades, docentes y representantes gremiales);  
* c) Administración de un sondeo digital anónimo y voluntario a docentes y estudiantes en sede Viedma y Nodos Territoriales.  

Se garantiza que toda la información se tratará bajo estricto secreto estadístico (Ley N° 25.326) con fines exclusivamente diagnósticos y académicos, sin generar consecuencias laborales ni sumativas.  

Agradeciendo su atención, saludo a Usted atentamente.  

<br>

::: {align="center"}
______________________________________________  
**Tec. Sup. Héctor Daniel Ayarachi Fuentes**  
Legajo N° 8252 — DNI N° 35.492.138  
Departamento de Administración Pública — CURZAS-UNCo  
:::

{{< pagebreak >}}

### Anexo IV: Formulario de Consentimiento Informado {.unnumbered}

::: {align="center"}
**FORMULARIO DE CONSENTIMIENTO INFORMADO**
:::

1. **Proyecto:** *Evaluación del Desempeño Docente y Factibilidad de Implementación de un Modelo de Retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo (2027)*.
2. **Investigador:** Tec. Sup. Héctor Daniel Ayarachi Fuentes (CURZAS-UNCo).
3. **Propósito:** Diagnosticar las condiciones de factibilidad para un circuito formativo de retroalimentación docente.
4. **Constancia y Declaración del Participante:**
   - Declaro haber recibido información clara y detallada sobre los objetivos y alcances de la investigación.
   - Mi participación es libre, voluntaria y no remunerada, pudiendo retirarme en cualquier momento sin perjuicio alguno.
   - Se me garantiza el anonimato estricto y la confidencialidad de mis respuestas (Ley N° 25.326 de Protección de los Datos Personales).
   - Se me informa que los resultados no afectarán bajo ninguna circunstancia mi situación laboral estatutaria ni mi condición académica.

<br>

| Campo | Registro |
| :--- | :--- |
| **Lugar y Fecha:** | __________________________________________________ |
| **Firma (o validación digital):** | __________________________________________________ |
| **Aclaración de Firma:** | __________________________________________________ |
| **Estamento / Rol:** | [ ] Docente &nbsp;&nbsp;&nbsp;&nbsp; [ ] Estudiante &nbsp;&nbsp;&nbsp;&nbsp; [ ] Autoridad |

"""

test_doc = f"""---
title: Test Anexos
format:
  typst:
    paper: a4
    margin:
      top: 2.54cm
      bottom: 2.54cm
      left: 2.54cm
      right: 2.54cm
    mainfont: "Arial"
    fontsize: 11pt
---

{nota_qmd}
"""

p = Path("pruebas/test_anexos.qmd")
p.write_text(test_doc, encoding="utf-8")
res = subprocess.run(["quarto", "render", "pruebas/test_anexos.qmd", "--to", "typst"], capture_output=True, text=True)
print("Quarto exit:", res.returncode)
if res.returncode == 0:
    doc = pymupdf.open("pruebas/test_anexos.pdf")
    print(f"Total pages rendered: {len(doc)}")
    for i, page in enumerate(doc):
        txt = page.get_text().strip()
        first_line = txt.splitlines()[0] if txt else "EMPTY"
        last_line = txt.splitlines()[-1] if txt else "EMPTY"
        print(f"Page {i+1}: first='{first_line[:50]}' ... last='{last_line[:50]}'")
else:
    print(res.stderr)
