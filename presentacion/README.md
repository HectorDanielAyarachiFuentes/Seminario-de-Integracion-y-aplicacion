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

## 🏛️ Catálogo de las 20 Esculturas Académicas 3D (Galería Institucional)

Cada filmina posee una pieza escultórica tridimensional inspirada en la tradición universitaria y las artes plásticas clásicas (mármol de Carrara, latón dorado cepillado, bronce escultórico, cristal esmerilado y plintos de granito pulido bajo iluminación de museo):
1. **Filmina 1:** *Esfera Armilar Renacentista*: base clásica con tres aros meridiano y eclíptica graduados de latón girando en torno al orbe universitario de marfil.
2. **Filmina 2:** *Monumento al Valor Social*: pedestal de mármol con tres anillos horizontales concéntricos de bronce ascendiendo armónicamente y gema de cristal.
3. **Filmina 3:** *Frontispicio Normativo (Res. 266/23)*: estilóbato de granito con 3 columnas jónicas de mármol, arquitrabe y frontón clásico de latón.
4. **Filmina 4:** *Maqueta Geodésica de Río Negro*: plinto de bronce patinado con 5 obeliscos geodésicos monumentales en mármol y piramidones dorados (Viedma y Nodos).
5. **Filmina 5:** *Red Tensada de Nodos Territoriales*: esferas perladas de alabastro unidas por finos filamentos tensores de latón (Res. CD-CURZA N° 196/2022).
6. **Filmina 6:** *Escultura Cinética de Péndulos Armónicos*: 7 esferas de mármol y bronce suspendidas que transitan del desorden a la alineación epistemológica (Wainerman & Sautu).
7. **Filmina 7:** *Balanza de la Justicia Universitaria*: fuste de mármol con balancín de latón y dos platillos en solemne equilibrio (Art. 75 vs. Art. 76 Estatuto UNCo).
8. **Filmina 8:** *Astrolabio Geodésico de Precisión*: limbo graduado de bronce con disco de cristal y alidada rotatoria para la delimitación del problema.
9. **Filmina 9:** *Tétrada Monumental de Placas*: cuatro placas de bronce con pátina y biseles dorados que se abren en compás ordenado (Objetivo General + 3 Específicos).
10. **Filmina 10:** *Heptágono Escultórico de los 7 Subsistemas*: prisma regular de 7 caras de mármol blanco de Carrara coronado por estrella heptagonal y anillo orbital (Francisco Longo).
11. **Filmina 11:** *Atril de Honor Académico*: marco ceremonial de bronce y columna de mármol que enmarca el diagrama oficial SVG de Longo.
12. **Filmina 12:** *Escalera Monumental de la Carrera Docente*: cuatro pedestales de mármol ascendentes con molduras de latón (Planificación, Organización, Rendimiento, Desarrollo).
13. **Filmina 13:** *Giroscopio Cuádruple de Bronce y Alabastro*: cuatro aros cardinales girando en rotación solemne con las 4 esferas de los claustros evaluativos (Modelo 360°).
14. **Filmina 14:** *Cúpula Geodésica de Cristal y Tracería de Bronce*: cúpula protectora arquitectónica de cristal esmerilado cobijando la libertad de cátedra y confidencialidad.
15. **Filmina 15:** *Triángulo de Matus en Granito y Latón*: tríada monumental conectada por barras de tensión (Proyecto, Capacidad y Gobernabilidad).
16. **Filmina 16:** *Estructura Tensada de Tensegridad*: barras de latón suspendidas en equilibrio flotante sin tocarse, metáfora de la poligobernanza (Cao & Blutman).
17. **Filmina 17:** *Teodolito y Prisma Óptico de Triangulación*: prisma de cristal puro tallado sobre montura clásica de latón y trípode geodésico.
18. **Filmina 18:** *Pentagrama Armónico de Vitral y Latón*: escultura pentagonal con 5 radios de latón sosteniendo cristales biselados para las 5 dimensiones de factibilidad.
19. **Filmina 19:** *Linterna de la Biblioteca del Saber*: faro cilíndrico de mampostería clásica y cúpula de bronce con celosía renacentista.
20. **Filmina 20:** *Gran Medallón de Honor CURZAS - UNCo*: medalla conmemorativa de bronce patinado y oro con corona de laureles sobre plinto de mármol blanco.

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
