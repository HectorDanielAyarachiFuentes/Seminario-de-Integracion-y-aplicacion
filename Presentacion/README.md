# 🎓 Sistema de Presentación Interactiva 3D — Defensa de Tesina (20 Filminas)

**Seminario de Integración y Aplicación (SIA 2025/2026)**  
**Centro Universitario Regional Zona Atlántica y Sur (CURZAS)**  
**Universidad Nacional del Comahue (UNCo)**  

* **Autor:** Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes (Legajo N° 8252 — DNI N° 35.492.138)  
* **Cátedra:** Dra. Deborah Noguera, Esp. Federico Abeiro, Esp. María Cecilia Aguirre  
* **Marco Normativo:** Res. CD-CURZAS N° 266/23 | Normas APA 7ma Edición  
* **Duración estipulada:** 30 minutos cronometrados (~1.5 min por filmina)  

---

## 🌟 Arquitectura y Desacoplamiento de Metadatos

La presentación fue desarrollada con arquitectura **100% desacoplada**: todo el contenido textual, los cronometrajes, los guiones del orador, los diagramas vectoriales SVG y las respuestas al jurado residen en un archivo de datos externo:

```text
Presentacion/
├── index.html                   # Interfaz semántica con visor modal SVG y puntos WebGL
├── README.md                    # Manual de uso, atajos y catálogo de diagramas
├── assets/
│   ├── CURZAS.png               # Emblema oficial en alta resolución
│   ├── Sistemas-longo.svg       # Diagrama oficial de subsistemas (Francisco Longo, 2006)
│   ├── subsistemas_longo.svg    # Desglose operativo de estrategia y subsistemas de RRHH
│   ├── modelo_360.svg           # Arquitectura circular del modelo 360° en CURZAS
│   └── red_territorial.svg      # Mapeo territorial de Viedma y Nodos (Res. 196/2022)
├── css/
│   └── styles.css               # Estilos Glassmorphism de alto contraste, visor modal y HUD
├── data/
│   └── presentacion_data.js     # 📌 20 FILMINAS EDITABLES, GUIONES Y METADATOS
└── js/
    ├── scene3d.js               # Motor Three.js con 6 objetos conceptuales de segundo plano
    └── app.js                   # Controlador de 20 filminas, visor SVG y cronómetro 30 min
```

---

## 📐 Catálogo de Diagramas Vectoriales SVG Oficiales

Los diagramas pueden observarse de forma interactiva en pantalla completa mediante el botón que aparece en la tarjeta o con la tecla **`V`**:

1. **`assets/Sistemas-longo.svg` (Filmina 11):** *Subsistemas de la Gestión de Recursos Humanos (Francisco Longo, 2006)*. Modela la alineación estratégica, la planificación y la retroalimentación continua entre el Rendimiento y el Desarrollo Docente.
2. **`assets/subsistemas_longo.svg`:** *Estrategia y Subsistemas de RRHH (Detalle Operativo)*. Diagrama analítico ampliado con flujos de compensación, empleo y relaciones laborales.
3. **`assets/modelo_360.svg` (Filmina 14):** *Arquitectura Circular del Modelo 360° en CURZAS*. Triangulación formativa de 4 cuadrantes (Autoevaluación, Pares, Estudiantes, Dirección) con blindaje de anonimato criptográfico y desacoplamiento estatutario del Art. 75.
4. **`assets/red_territorial.svg` (Filmina 5):** *Mapeo Territorial y Red de Nodos de Docencia Híbrida*. Distribución de la Sede Cabecera Viedma y los Nodos Territoriales de Sierra Grande, Valcheta, Los Menucos y Ramos Mexía bajo Res. CD-CURZA N° 196/2022.

---

## 📋 Estructura de las 20 Filminas de la Exposición (30 Minutos)

* **Bloque I: Apertura y Encuadre Institucional (Filminas 1 a 3):**
  1. Carátula Oficial y Presentación (UNCo - CURZAS - SIA).
  2. Justificación y Línea Temática: Gestión de Personas y Valor Público.
  3. Marco Normativo Oficial: Res. CD-CURZAS N° 266/23 y Docs-as-Code.
* **Bloque II: Esquema N° 1 — El Problema y el Territorio (Filminas 4 a 7):**
  4. El Escenario Territorial Situado: Sede Viedma y Diversidad Regional.
  5. **[SVG]** Mapeo de la Red de Nodos y Docencia Híbrida (Res. 196/2022).
  6. Desnaturalización del Problema: De la Rutina al Objeto Científico (Wainerman & Sautu).
  7. La Tensión Estructural: Carrera Docente Sumativa (Art. 75) vs. Capacitación Continua (Art. 76).
* **Bloque III: Preguntas y Objetivos (Filminas 8 y 9):**
  8. Pregunta Central de Investigación y Preguntas Secundarias.
  9. Matriz de Objetivos: Objetivo General y los 4 Objetivos Específicos.
* **Bloque IV: Esquema N° 2 — Marco Teórico Sustantivo y Modelos (Filminas 10 a 14):**
  10. Marco Teórico Central: El Enfoque Sistémico de Francisco Longo (2006).
  11. **[SVG]** Arquitectura de Subsistemas de Recursos Humanos (Diagrama Oficial de Longo).
  12. Articulación Operativa: Rendimiento, Trabajo, Desarrollo y Relaciones Humanas.
  13. Marco Teórico II: El Dispositivo 360° y Mitigación de Sesgos Unilaterales.
  14. **[SVG]** Arquitectura Circular del Modelo 360° en CURZAS y Blindajes Éticos.
* **Bloque V: Gobernanza, Poder Compartido y Tecnología (Filminas 15 y 16):**
  15. Carlos Matus (1993) y la PES: La Universidad como Arena de Poder Compartido.
  16. Oscar Oszlak (2020) y Cao & Blutman (2023): Estado Plataforma y Poligobernanza.
* **Bloque VI: Esquema N° 3 — Metodología, Factibilidad y Cierre (Filminas 17 a 20):**
  17. Estrategia Metodológica Integral: Diseño Cualitativo, Muestra y Triangulación.
  18. Las Cinco Dimensiones Analíticas de Factibilidad (Normativa, Técnica, Org., Cult., Gob.).
  19. Vacancia Disciplinar Comprobada y Aportes a la Universidad Pública.
  20. Conclusiones, Síntesis de Viabilidad y Apertura al Tribunal Evaluador.

---

## ⌨️ Atajos de Teclado Profesionales

| Tecla | Acción |
| :---: | :--- |
| `→` o `Espacio` o `AvPág` | Avanzar a la siguiente filmina |
| `←` o `RePág` | Retroceder a la filmina anterior |
| `V` | **Observar Diagrama Vectorial SVG** de la filmina actual en pantalla completa |
| `D` | **Modo Enfoque Texto**: Atenuar el fondo 3D al 18% para lectura prioritaria |
| `T` | Iniciar / Pausar el cronómetro de 30 minutos |
| `N` | Abrir / Cerrar el **Guion del Orador** (*teleprompter* con notas de apoyo) |
| `M` | Abrir / Cerrar el panel de **7 Pestañas de Respaldo Metodológico** |
| `F` | Activar / Desactivar pantalla completa |
| `Escape` | Cerrar cualquier visor o panel activo |

---

## 🚀 ¿Cómo Ejecutar la Presentación?

* **Opción Directa:** Haz doble clic sobre [index.html](file:///c:/Users/Ramoncito/.antigravity-ide/Seminario%20de%20Integraci%C3%B3n%20y%20Aplicaci%C3%B3n/Presentacion/index.html) para abrirlo en Edge, Chrome, Brave o Firefox.
* **Opción Servidor Local:** Ejecuta `python -m http.server 8000` en PowerShell y accede a `http://localhost:8000`.
