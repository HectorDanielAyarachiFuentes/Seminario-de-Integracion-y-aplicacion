/**
 * =============================================================================
 * METADATOS Y CONTENIDO DE LA PRESENTACIÓN FINAL — TFG / TESINA (20 FILMINAS)
 * Universidad Nacional del Comahue — CURZAS
 * Seminario de Integración y Aplicación (SIA 2025/2026)
 * Autor: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes
 * =============================================================================
 * Centraliza las 20 estaciones de la defensa, los enlaces a los diagramas SVG,
 * los guiones para el orador y las 6 pestañas de respaldo metodológico para el jurado.
 */

const PRESENTACION_DATA = {
  meta: {
    institucion: "Universidad Nacional del Comahue",
    sede: "Complejo Universitario Regional Zona Atlántica y Sur (CURZAS)",
    departamento: "Departamento de Administración Pública",
    carrera: "Ciclo de Complementación Curricular de la Licenciatura en Gestión de Recursos Humanos",
    materia: "Seminario de Integración y Aplicación (SIA)",
    titulo: "Evaluación del Desempeño Docente y Factibilidad de Implementación de un Modelo de Retroalimentación 360°",
    subtitulo: "Enfoque formativo situado en el Departamento de Administración Pública del CURZAS-UNCo (2025–2026)",
    autor: "Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes",
    legajo: "Legajo N° 8252 — DNI N° 35.492.138",
    docentes: [
      { nombre: "Dra. Deborah Noguera", rol: "Docente Responsable de Cátedra" },
      { nombre: "Esp. Federico Abeiro", rol: "Ayudante de Cátedra" },
      { nombre: "Esp. María Cecilia Aguirre", rol: "Ayudante de Cátedra" }
    ],
    normativaMarco: "Resolución CD-CURZAS N° 266/23 (Reglamento de TFG)",
    ano: "2026",
    lugar: "Viedma, Río Negro — República Argentina"
  },

  timing: {
    totalMinutos: 30,
    alertaAmarillaMinutos: 20, // Minuto en que cambia a color de advertencia
    alertaRojaMinutos: 27,     // Minuto en que avisa cierre inminente
    promedioPorSlideMin: 1.5   // ~1.5 minutos por filmina para completar 30 minutos
  },

  // 6 Pestañas de Respaldo Metodológico para el Tribunal Evaluador (Atajo: Tecla 'M')
  fichasRespaldo: {
    autores: [
      {
        autor: "Francisco Longo (2006)",
        concepto: "Modelo analítico de 7 subsistemas para el empleo público: rendimiento, desarrollo, organización del trabajo, relaciones humanas y sociales. Fundamento para superar la auditoría punitiva y orientar la gestión pública a la generación de valor social."
      },
      {
        autor: "Carlos Matus (1993)",
        concepto: "Planificación Estratégica Situacional (PES): las organizaciones públicas operan en 'arenas de poder compartido'. La viabilidad de una innovación no se decreta; se construye concertando sobre variables de control compartido en cogobierno."
      },
      {
        autor: "Oscar Oszlak (2020)",
        concepto: "El Estado en la era exponencial: incorporación inteligente de tecnologías y algoritmos para expandir capacidades estatales sin vulnerar la privacidad ni caer en automatismos autoritarios despersonalizados."
      },
      {
        autor: "Horacio Cao & Gustavo Blutman (2023)",
        concepto: "Poligobernanza y Estado plataforma: redes horizontales y gestión de la complejidad que superan el modelo burocrático weberiano y el gerencialismo ciego en la administración pública argentina."
      },
      {
        autor: "Catalina Wainerman & Ruth Sautu (2011)",
        concepto: "Desnaturalización de las rutinas cotidianas para formular un problema científico genuino, evitando confundir el problema de gestión empírico con el objeto de investigación teórica."
      },
      {
        autor: "Obando Freire et al. (2014) & Sifuentes (2016)",
        concepto: "Estudios empíricos sobre evaluación 360° en universidades: demuestran que la triangulación multiactoral reduce sesgos subjetivos de las encuestas unilaterales si se garantiza 100% de confidencialidad."
      },
      {
        autor: "Idalberto Chiavenato (2019)",
        concepto: "Gestión del talento humano: la evaluación circular como ciclo continuo de retroalimentación reflexiva que alinea los objetivos individuales con la misión estratégica institucional."
      }
    ],

    normativa: [
      {
        norma: "Resolución CD-CURZAS N° 266/23",
        descripcion: "Reglamento formal de Trabajos Finales de Graduación del CURZAS-UNCo. Define la estructura canónica de 10 apartados y los criterios de viabilidad del proyecto de TFG."
      },
      {
        norma: "Ordenanza CS N° 0988/2025 (Estatuto UNCo)",
        descripcion: "Título X: Carrera Docente. El Art. 75 establece que dos evaluaciones negativas consecutivas causan la vacancia del cargo. El Art. 76 instituye el Programa Anual de Formación Docente Continua, anclaje central de nuestra propuesta."
      },
      {
        norma: "Decreto PEN N° 1246/2015 (CCT Docente Universitario)",
        descripcion: "Convenio Colectivo de Trabajo Docente. Protege la estabilidad, libertad de cátedra y establece garantías de debido proceso y tutela gremial contra instrumentos de evaluación punitiva unilateral."
      },
      {
        norma: "Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)",
        descripcion: "Reglamenta las mediaciones tecnológicas, la presencialidad remota sincrónica y las tutorías virtuales en la Red de Nodos Territoriales del CURZAS, exigiendo evaluar nuevas competencias docentes."
      },
      {
        norma: "Ordenanza CS N° 0910/1997 y modif.",
        descripcion: "Reglamento de Carrera Docente de la UNCo: fija los procedimientos históricos de informes de cátedra y encuestas estudiantiles sumativas."
      },
      {
        norma: "Ordenanza CS N° 0180/2014",
        descripcion: "Plan de Estudios del Ciclo de Licenciatura en Gestión de Recursos Humanos del CURZAS, marco de pertenencia académica de esta graduación."
      }
    ],

    objetivos: [
      {
        nivel: "Objetivo General",
        texto: "Determinar las condiciones de factibilidad organizacional, técnica, normativa y de gobernanza multinivel para la implementación de un modelo de retroalimentación multiactoral (360°) en la evaluación del desempeño docente en el Departamento de Administración Pública del CURZAS-UNCo (2025–2026)."
      },
      {
        nivel: "Objetivo Específico 1 (Relevamiento Normativo-Operativo)",
        texto: "Relevar y caracterizar los instrumentos normativos, procedimientos y prácticas vigentes aplicadas a la evaluación del desempeño docente en el Departamento, distinguiendo prescripciones estatutarias de su aplicación empírica real."
      },
      {
        nivel: "Objetivo Específico 2 (Percepciones de Actores)",
        texto: "Explorar las percepciones, disposiciones y representaciones de docentes, estudiantes y autoridades departamentales respecto a la retroalimentación 360° y las condiciones de confianza institucional requeridas."
      },
      {
        nivel: "Objetivo Específico 3 (Condicionantes de Gobernanza)",
        texto: "Identificar los condicionantes técnico-organizacionales, normativos y de gobernanza multinivel (acuerdos paritarios, confidencialidad algorítmica, carrera docente y cogobierno) que inciden en la factibilidad del modelo."
      },
      {
        nivel: "Objetivo Específico 4 (Lineamientos Formativos)",
        texto: "Proponer lineamientos orientativos para una eventual implementación formativa del modelo 360°, en función de las condiciones y límites de factibilidad identificados empíricamente."
      }
    ],

    dimensiones: [
      {
        dim: "1. Dimensión Normativa y Gremial",
        detalle: "Resguardo del CCT (Dec. 1246/15) y del Estatuto UNCo. El modelo debe operar en estricta desconexión del legajo sumativo del Art. 75 para no violar garantías laborales, anclándose exclusivamente en el Art. 76 (capacitación)."
      },
      {
        dim: "2. Dimensión Técnica e Informática",
        detalle: "Garantía criptográfica y algorítmica de anonimato en plataformas institucionales (Moodle / SIU-Guaraní). Ponderación mínima de respuestas para evitar la trazabilidad de opiniones en cátedras con pocos alumnos."
      },
      {
        dim: "3. Dimensión Organizacional y Administrativa",
        detalle: "Capacidad de la Secretaría Académica y del Departamento para procesar diagnósticos 360° y transformarlos en planes anuales de capacitación pedagógica situada y oportuna."
      },
      {
        dim: "4. Dimensión Cultural y Clima Laboral",
        detalle: "Superación del ritualismo defensivo y la desconfianza histórica mediante procesos de sensibilización previa que desmitifiquen la evaluación como mecanismo de persecución ideológica o laboral."
      },
      {
        dim: "5. Dimensión de Gobernanza Cogobernada",
        detalle: "Acuerdo situacional en Consejo Directivo paritario con representación docente, estudiantil, nodocente y de graduados (Matus, 1993; Cao & Blutman, 2023)."
      }
    ],

    territorio: [
      {
        sede: "Sede Cabecera: Viedma (Valle Inferior)",
        detalle: "Sede central académica y administrativa del CURZAS, conurbada con Carmen de Patagones. Concentra los claustros docentes, la dirección departamental y los órganos de cogobierno."
      },
      {
        sede: "Nodo Territorial: Sierra Grande (Costa Atlántica)",
        detalle: "Vinculación con comunidades costeras y mineras. Demanda docencia híbrida sincrónica con fuerte necesidad de acompañamiento virtual continuo."
      },
      {
        sede: "Nodo Territorial: Valcheta (Portal de la Línea Sur)",
        detalle: "Población estudiantil que accede a la universidad pública a través de aulas híbridas equipadas bajo Res. CD-CURZA N° 196/2022."
      },
      {
        sede: "Nodos Territoriales: Los Menucos y Ramos Mexía",
        detalle: "Territorio de la estepa patagónica profunda. Los docentes requieren competencias didácticas específicas para la mediación tecnológica y la tutoría a distancia sincrónica/asincrónica."
      }
    ],

    faq: [
      {
        pregunta: "¿Por qué un modelo 360° y no la tradicional encuesta estudiantil?",
        respuesta: "La encuesta estudiantil unilateral genera sesgos de popularidad o complacencia y evalúa solo un fragmento del hecho educativo. El modelo 360° triangula 4 perspectivas (autoevaluación reflexiva, pares de cátedra, estudiantes y gestión departamental), logrando una visión holística y formativa."
      },
      {
        pregunta: "¿Cómo se previene el riesgo de que el modelo sea percibido como persecutorio?",
        respuesta: "Mediante dos blindajes: 1) Blindaje Normativo: desacoplamiento absoluto del Art. 75 del Estatuto (permanencia) y vinculación exclusiva con el Art. 76 (formación continua); 2) Blindaje Técnico: anonimato estadístico absoluto auditado por comisiones paritarias."
      },
      {
        pregunta: "¿Qué rol juega el Convenio Colectivo de Trabajo (Dec. 1246/15)?",
        respuesta: "Es el marco protector rector. El CCT prohíbe modificaciones unilaterales en las condiciones de trabajo docente. Por tanto, el modelo 360° no puede imponerse de arriba hacia abajo; debe construirse como acuerdo paritario negociado (Matus: poder compartido)."
      },
      {
        pregunta: "¿Cómo incide la Red de Nodos Territoriales en la evaluación?",
        respuesta: "Bajo la Res. 196/2022, la labor del docente del CURZAS no se limita al pizarrón tradicional; incluye diseñar aulas virtuales en Moodle, sostener videoconferencias y tutorizar estudiantes en parajes alejados. Los instrumentos antiguos en papel son obsoletos para evaluar esta docencia híbrida."
      },
      {
        pregunta: "¿Cuál es el valor público concreto que este TFG aporta al CURZAS?",
        respuesta: "Brinda por primera vez evidencia empírica rigurosa y un diagnóstico de factibilidad situado en la Patagonia, permitiendo a las autoridades universitarias tomar decisiones informadas sobre políticas de desarrollo docente sin importar recetas enlatadas."
      }
    ]
  },

  // Las 20 Filminas de la Presentación Oral (30 minutos cronometrados)
  slides: [
    // ─── BLOQUE I: APERTURA Y ENCUADRE INSTITUCIONAL (Filminas 1 a 3) ────────
    {
      id: "slide_1",
      numero: 1,
      bloque: "BLOQUE I: APERTURA",
      esquema: "Carátula Oficial y Presentación",
      badge: "UNCo — CURZAS | SIA 2026",
      titulo: "Evaluación del Desempeño Docente y Factibilidad de un Modelo 360°",
      subtitulo: "Enfoque Formativo Situado en el Departamento de Administración Pública del CURZAS-UNCo",
      puntosClave: [
        "Tesina de Graduación: Licenciatura en Gestión de Recursos Humanos (Ciclo de Complementación Curricular).",
        "Autor: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes (Legajo N° 8252 — DNI N° 35.492.138).",
        "Tribunal Docente: Dra. Deborah Noguera, Esp. Federico Abeiro y Esp. María Cecilia Aguirre.",
        "Sede Académica: Viedma, Río Negro — República Argentina."
      ],
      metadatosFooter: "Exposición Oral de Proyecto de Tesina • Tiempo total: 30 minutos",
      escena3D: "anim_01",
      guionOrador: "Estimados miembros del tribunal evaluador, Dra. Deborah Noguera, Esp. Federico Abeiro y Esp. María Cecilia Aguirre. Inicio formalmente la defensa de mi Proyecto de Trabajo Final de Graduación titulado 'Evaluación del Desempeño Docente y Factibilidad de Implementación de un Modelo de Retroalimentación 360° en el Departamento de Administración Pública del CURZAS-UNCo'. Esta investigación se sitúa en la intersección estratégica entre la Administración Pública y la Gestión de Recursos Humanos en la universidad nacional cogobernada."
    },

    {
      id: "slide_2",
      numero: 2,
      bloque: "BLOQUE I: ENCUADRE",
      esquema: "Línea de Investigación y Relevancia",
      badge: "Pertinencia Disciplinar",
      titulo: "Gestión Estratégica de Personas y Valor Público",
      subtitulo: "Superación del Paradigma Burocrático Tradicional en la Universidad Pública",
      puntosClave: [
        "Línea Temática: Modelos de evaluación formativa de recursos humanos en organizaciones públicas complejas.",
        "Generación de Valor Público: La docencia universitaria como servicio esencial que requiere aprendizaje y mejora continua.",
        "Desafío de RRHH: Superar el ritualismo formalista que concibe a la evaluación como un mero trámite administrativo o punitivo.",
        "Propósito Central: Sentar bases empíricas para fortalecer las capacidades institucionales de la universidad pública patagónica."
      ],
      metadatosFooter: "Valor Público • Capacidades Estatales • Gestión de Personas",
      escena3D: "anim_02",
      guionOrador: "La relevancia de esta línea temática radica en que, históricamente, la administración pública ha gestionado a las personas bajo una mirada de control administrativo formal. Nuestro posicionamiento teórico postula que la evaluación debe ser una herramienta de desarrollo y aprendizaje reflexivo. Evaluar el desempeño docente no es auditar para sancionar; es generar las condiciones institucionales para que las cátedras mejoren continuamente la calidad pedagógica que brindan a la comunidad."
    },

    {
      id: "slide_3",
      numero: 3,
      bloque: "BLOQUE I: NORMATIVA",
      esquema: "Estructura Formal del TFG",
      badge: "Res. CD-CURZAS N° 266/23",
      titulo: "Marco Normativo Oficial y Arquitectura Docs-as-Code",
      subtitulo: "Alineación Rigurosa con los Estándares de la Cátedra SIA y Normas APA 7",
      puntosClave: [
        "Resolución CD-CURZAS N° 266/23: Cumplimiento de la estructura obligatoria de 10 apartados del Proyecto de Tesina.",
        "Metodología Docs-as-Code: Autoría académica unificada en Quarto (.qmd) y renderizado dual de alta fidelidad (Word y PDF).",
        "Normas APA 7ma Edición: Estricto apego a pautas de citación, carátula institucional sin paginado y sangría francesa.",
        "Progresión Académica: Integración acumulativa y validada de las entregas TP1, TP2 y TP3 aprobadas."
      ],
      metadatosFooter: "Res. 266/23 • APA 7ma Edición • Pipeline Automatizado",
      escena3D: "anim_03",
      guionOrador: "El proyecto se ajusta estrictamente al reglamento de Trabajos Finales de Graduación aprobado por la Resolución CD-CURZAS N° 266/23, articulando los 10 apartados canónicos. Desde el punto de vista metodológico, adoptamos el paradigma Docs-as-Code con Quarto y Typst, lo que garantiza trazabilidad de versiones, rigor tipográfico bajo APA 7ma Edición e integridad absoluta entre el planteo del problema, el marco teórico y la estrategia empírica."
    },

    // ─── BLOQUE II: ESQUEMA 1 — EL PROBLEMA Y EL TERRITORIO (Filminas 4 a 7) ─
    {
      id: "slide_4",
      numero: 4,
      bloque: "BLOQUE II: TERRITORIO",
      esquema: "Esquema 1: Contexto Situado",
      badge: "Esquema 1: Territorialidad",
      titulo: "El CURZAS en el Territorio: Sede Viedma y Nodos",
      subtitulo: "Inserción Regional en la Costa Atlántica y la Línea Sur Rionegrina",
      puntosClave: [
        "Sede Cabecera Viedma: Polo administrativo y académico conurbado con Carmen de Patagones.",
        "Ecosistema Territorial Descentralizado: Presencia en la estepa y costa mediante aulas equipadas.",
        "Diversidad Socioeconómica del Claustro Estudiantil: Estudiantes que son trabajadores y primeras generaciones universitarias.",
        "Desafío de Gestión de RRHH: Acompañar a un cuerpo docente disperso geográficamente con diversas realidades de conectividad."
      ],
      metadatosFooter: "Territorialidad • Patagonia Norte • Democratización del Acceso",
      escena3D: "anim_04",
      guionOrador: "Pasando al Esquema 1, nuestro objeto de estudio no se sitúa en un campus universitario tradicional ni en una metrópoli central. El CURZAS tiene un despliegue territorial extenso y singular en la Patagonia Norte. Desde su sede cabecera en Viedma, articula una comunidad académica diversa que abarca desde la capital provincial hasta localidades del interior provincial. Comprender este contexto es vital: no se puede diseñar un sistema de evaluación de personal docente ignorando el territorio donde enseñan."
    },

    {
      id: "slide_5",
      numero: 5,
      bloque: "BLOQUE II: DOCENCIA HÍBRIDA",
      esquema: "Esquema 1: Mediaciones Tecnológicas",
      badge: "Res. CD-CURZA N° 196/2022",
      titulo: "Mapeo Territorial y Mediaciones Tecnológicas",
      subtitulo: "La Docencia Híbrida como Nueva Realidad Laboral Docente",
      puntosClave: [
        "Red de Nodos Territoriales: Sierra Grande, Valcheta, Los Menucos y Ramos Mexía.",
        "Institucionalización: La Res. CD-CURZA N° 196/2022 formalizó la presencialidad remota sincrónica y asincrónica.",
        "Transformación del Trabajo Docente: El profesor ya no solo dicta clases frente a un aula física; gestiona entornos Moodle y tutorías a distancia.",
        "Obsolescencia Instrumental: Los cuestionarios tradicionales en papel son ciegos ante las competencias didáctico-digitales que demanda el territorio."
      ],
      metadatosFooter: "Red de Nodos • Aulas Híbridas • Competencias Digitales",
      escena3D: "anim_05",
      diagramaSVG: "assets/red_territorial.svg",
      guionOrador: "Como podemos observar en el diagrama de la Red Territorial que tienen en pantalla, la Resolución CD-CURZA 196/2022 institucionalizó las mediaciones tecnológicas en los nodos de Sierra Grande, Valcheta, Los Menucos y Ramos Mexía. Esto reconfiguró por completo la jornada laboral del docente: preparar contenidos interactivos, coordinar videoconferencias y tutorizar estudiantes remotos. Los instrumentos evaluativos tradicionales en papel quedan obsoletos porque no ponderan estas competencias complejas."
    },

    {
      id: "slide_6",
      numero: 6,
      bloque: "BLOQUE II: PROBLEMATIZACIÓN",
      esquema: "Esquema 1: Desnaturalización",
      badge: "Vigilancia Epistemológica",
      titulo: "Desnaturalización del Problema de Investigación",
      subtitulo: "De la Rutina Institucional al Objeto Científico (Wainerman & Sautu, 2011)",
      puntosClave: [
        "Desnaturalizar lo Cotidiano: Cuestionar la creencia de que 'evaluar' consiste en repartir una planilla de preguntas al finalizar el cuatrimestre.",
        "Distinción Fundamental: El problema de gestión (falta de información) se convierte en objeto teórico al indagar las condiciones de factibilidad de una innovación.",
        "Superación del Ritualismo: Evitar que la evaluación sea una pantomima burocrática archivada en cajones sin impacto formativo.",
        "Construcción Epistemológica: Articulación entre sociología del trabajo público, teoría organizacional y derecho universitario."
      ],
      metadatosFooter: "Wainerman & Sautu (2011) • Epistemología • Ciencias Sociales",
      escena3D: "anim_06",
      guionOrador: "Construir este problema exigió aplicar lo que Catalina Wainerman y Ruth Sautu denominan la desnaturalización de lo cotidiano. En la vida universitaria se asume con naturalidad que la evaluación docente es una encuesta en papel tomada a las apuradas en la última clase. Desnaturalizar esa rutina implicó preguntarnos: ¿qué evalúa realmente esa encuesta? ¿Sirve para mejorar la enseñanza o es un mero cumplimiento burocrático? Así transformamos un reclamo administrativo en un genuino problema de investigación científica."
    },

    {
      id: "slide_7",
      numero: 7,
      bloque: "BLOQUE II: TENSIÓN NORMATIVA",
      esquema: "Esquema 1: Tensión de Fondo",
      badge: "Estatuto UNCo (Ord. 0988/2025)",
      titulo: "La Tensión Estructural: Art. 75 vs. Art. 76",
      subtitulo: "El Dilema entre la Amenaza de Cesantía y la Formación Docente Continua",
      puntosClave: [
        "Art. 75 Estatuto UNCo (Carrera Docente Sumativa): Dispone que dos evaluaciones negativas consecutivas causan la vacancia del cargo.",
        "Efecto Colateral: Genera justificado temor, sospecha gremial y conductas defensivas ante cualquier intento de evaluación.",
        "Art. 76 Estatuto UNCo (Programa Anual de Capacitación): Mandato estatutario para el perfeccionamiento pedagógico continuo.",
        "La Solución Propuesta: Desacoplar el modelo 360° del Art. 75 y anclarlo de forma 100% confidencial y formativa en el Art. 76."
      ],
      metadatosFooter: "Art. 75 (Control) • Art. 76 (Capacitación) • Desacoplamiento Ético",
      escena3D: "anim_07",
      guionOrador: "Aquí llegamos al nudo crítico de la investigación. El Estatuto de la UNCo establece en su Artículo 75 que dos evaluaciones desfavorables consecutivas provocan la pérdida del cargo docente. Por lo tanto, cualquier dispositivo evaluativo genera inmediatamente recelo gremial si se sospecha que se usará para perseguir o despedir. Nuestra propuesta de tesis consiste en desacoplar radicalmente la retroalimentación 360° del Artículo 75 y anclarla de manera exclusiva y protegida en el Artículo 76, que regula la capacitación docente continua."
    },

    // ─── BLOQUE III: PREGUNTAS Y OBJETIVOS (Filminas 8 y 9) ──────────────────
    {
      id: "slide_8",
      numero: 8,
      bloque: "BLOQUE III: PREGUNTAS",
      esquema: "Problematización",
      badge: "Interrogantes de Investigación",
      titulo: "Pregunta Central y Preguntas Secundarias",
      subtitulo: "Ejes Analíticos que Guiaron la Delimitación del Objeto de Estudio",
      puntosClave: [
        "Pregunta Central: ¿Cuáles son las condiciones de factibilidad organizacional, técnica, normativa y de gobernanza multinivel para implementar un modelo 360° formativo en el Departamento (2025–2026)?",
        "Eje 1 (Normativo-Empírico): ¿Cómo conviven los reglamentos formales con las prácticas reales de evaluación?",
        "Eje 2 (Percepciones de Actores): ¿Qué grado de confianza y disposición manifiestan docentes y estudiantes?",
        "Eje 3 (Gobernanza y Anonimato): ¿Qué garantías criptográficas y paritarias son indispensables para evitar usos punitivos?"
      ],
      metadatosFooter: "Pregunta Central • Ejes Analíticos • Res. 266/23",
      escena3D: "anim_08",
      guionOrador: "En función de esta tensión, formulamos nuestra pregunta rectora: ¿Cuáles son las condiciones de factibilidad organizacional, técnica, normativa y de gobernanza multinivel para la implementación de un modelo de retroalimentación multiactoral 360 grados en el Departamento de Administración Pública del CURZAS-UNCo durante el período 2025-2026? De ella se desprenden los interrogantes sobre las normas vigentes, la disposición subjetiva de los actores y los mecanismos informáticos de resguardo."
    },

    {
      id: "slide_9",
      numero: 9,
      bloque: "BLOQUE III: OBJETIVOS",
      esquema: "Matriz de Objetivos",
      badge: "Coherencia Metodológica",
      titulo: "Matriz de Objetivos del Proyecto de Tesina",
      subtitulo: "Articulación entre el Objetivo General y los Cuatro Objetivos Específicos",
      puntosClave: [
        "Objetivo General: Determinar las condiciones de factibilidad organizacional, técnica, normativa y de gobernanza para el modelo 360° formativo.",
        "Obj. Específico 1: Relevar y caracterizar instrumentos, procedimientos y prácticas vigentes distinguiendo prescripciones estatutarias de su aplicación real.",
        "Obj. Específico 2: Explorar percepciones, disposiciones y representaciones de docentes, estudiantes y autoridades.",
        "Obj. Específico 3: Identificar condicionantes técnicos (anonimato), normativos (CCT) y de cogobierno paritario.",
        "Obj. Específico 4: Proponer lineamientos orientativos para una eventual implementación formativa y situada."
      ],
      metadatosFooter: "Objetivo General • 4 Objetivos Específicos • Res. CD-CURZAS N° 266/23",
      escena3D: "anim_09",
      guionOrador: "Esta matriz de objetivos plasma la directriz de la Resolución 266/23. Nuestro Objetivo General determina la factibilidad integral del modelo. Los cuatro objetivos específicos desagregan la tarea con precisión quirúrgica: primero, el diagnóstico normativo-operativo; segundo, el relevamiento de percepciones y clima de confianza; tercero, la identificación de los cuellos de botella técnicos y gremiales; y cuarto, la formulación de lineamientos orientativos adaptados a la realidad del CURZAS."
    },

    // ─── BLOQUE IV: ESQUEMA 2 — MARCO TEÓRICO Y MODELOS (Filminas 10 a 14) ───
    {
      id: "slide_10",
      numero: 10,
      bloque: "BLOQUE IV: MARCO TEÓRICO",
      esquema: "Esquema 2: Francisco Longo (2006)",
      badge: "Marco Teórico Sustantivo",
      titulo: "El Enfoque Sistémico de Francisco Longo (2006)",
      subtitulo: "Marco Analítico de Gestión del Empleo Público en Organizaciones Complejas",
      puntosClave: [
        "Superación del Enfoque Mecanicista: La gestión de personas no es una suma de trámites burocráticos aislados, sino un sistema integrado.",
        "Los Siete Subsistemas de Longo: Planificación, Organización del Trabajo, Gestión del Empleo, Rendimiento, Compensación, Desarrollo y Relaciones Humanas.",
        "Postulado Central de Longo: 'Evaluar el rendimiento sin conectarlo con el desarrollo y la formación constituye un ejercicio burocrático estéril'.",
        "Alineación Estratégica: El modelo 360° opera como bisagra entre la evaluación reflexiva y el plan anual de capacitación docente."
      ],
      metadatosFooter: "Francisco Longo (2006) • Empleo Público • Gestión Sistémica",
      escena3D: "anim_10",
      guionOrador: "Ingresando al Esquema 2 de Marco Teórico, la piedra angular de esta tesis es el modelo de gestión del empleo público de Francisco Longo (2006). Longo advierte con crudeza que evaluar el rendimiento de los trabajadores públicos sin vincularlo orgánicamente con el desarrollo y la capacitación es un trámite estéril que solo genera cinismo y desinterés. Por eso, adoptamos su enfoque sistémico para diseñar una herramienta que conecte el diagnóstico con la formación continua."
    },

    {
      id: "slide_11",
      numero: 11,
      bloque: "BLOQUE IV: DIAGRAMA LONGO",
      esquema: "Esquema 2: Diagrama Arquitectónico SVG",
      badge: "Visualización Conceptual SVG",
      titulo: "Arquitectura de Subsistemas de Recursos Humanos",
      subtitulo: "Diagrama Oficial del Modelo de Francisco Longo (2006)",
      puntosClave: [
        "Eje Vertical Superior: La Estrategia Institucional orienta la Planificación global de recursos humanos.",
        "Núcleo Operativo: Organización del Trabajo y Gestión del Empleo fijan perfiles y condiciones de ingreso y permanencia.",
        "Eje de Retroalimentación: Gestión del Rendimiento alimenta a la Gestión del Desarrollo.",
        "Marco Protector Transversal: La Gestión de las Relaciones Humanas y Sociales asegura la tutela paritaria y el diálogo colectivo."
      ],
      metadatosFooter: "Diagrama SVG Oficial • Longo (2006) • Modelo Sistémico",
      escena3D: "anim_11",
      diagramaSVG: "assets/Sistemas-longo.svg",
      guionOrador: "En la pantalla podemos observar el diagrama SVG oficial que modela la arquitectura de Longo. Observen cómo la Estrategia Institucional de la Universidad orienta la Planificación de cátedras, descendiendo hacia la Organización del Trabajo y la Gestión del Empleo. Pero el corazón de nuestro TFG reside en la interconexión horizontal: la Gestión del Rendimiento dialoga directamente con la Gestión del Desarrollo, resguardada por las Relaciones Humanas y Sociales paritarias."
    },

    {
      id: "slide_12",
      numero: 12,
      bloque: "BLOQUE IV: CUATRO SUBSISTEMAS",
      esquema: "Esquema 2: Articulación Situada",
      badge: "Operacionalización en CURZAS",
      titulo: "Articulación de los Cuatro Subsistemas Clave",
      subtitulo: "Traducción Situada de la Teoría de Longo a la Universidad Pública",
      puntosClave: [
        "1. Gestión del Rendimiento: La retroalimentación 360° aporta datos cualitativos integrales sobre la labor didáctica e investigativa.",
        "2. Organización del Trabajo: Pondera los roles específicos de cátedras presenciales, semipresenciales y tutorías en Nodos Territoriales.",
        "3. Gestión del Desarrollo: Los resultados 360° alimentan las convocatorias a talleres pedagógicos del Art. 76 del Estatuto.",
        "4. Relaciones Humanas y Sociales: El Convenio Colectivo (Dec. 1246/15) y los gremios garantizan que la información sea estrictamente formativa."
      ],
      metadatosFooter: "Rendimiento • Organización • Desarrollo • Relaciones Humanas",
      escena3D: "anim_12",
      guionOrador: "Operacionalizamos la teoría de Longo seleccionando cuatro subsistemas interconectados: Rendimiento, que aporta la información evaluativa circular; Organización del Trabajo, que reconoce las exigencias de la docencia híbrida en el territorio; Desarrollo, que transforma los resultados en cursos y trayectorias formativas; y Relaciones Humanas, que convoca al sindicato docente y a la comisión paritaria para garantizar que no haya desviaciones punitivas."
    },

    {
      id: "slide_13",
      numero: 13,
      bloque: "BLOQUE IV: MODELO 360",
      esquema: "Esquema 2: Dispositivo Metodológico",
      badge: "Triangulación Multiactoral",
      titulo: "El Dispositivo de Retroalimentación 360 Grados",
      subtitulo: "Triangulación de Perspectivas y Mitigación de Sesgos Unilaterales",
      puntosClave: [
        "Definición: Proceso circular en el que el desempeño de una persona es apreciado por múltiples actores de su entorno de trabajo.",
        "Superación del Sesgo Unilateral: La encuesta estudiantil clásica suele castigar la exigencia pedagógica o premiar la simpatía; el 360° equilibra visiones.",
        "Evidencia Empírica Universitaria: Investigaciones de Obando Freire (2014) y Sifuentes (2016) demuestran su alta validez formativa.",
        "Condición Sine Qua Non: Resguardo absoluto del anonimato y compromiso explícito de no utilizar los informes en sumarios o despidos."
      ],
      metadatosFooter: "Evaluación Circular • Triangulación • Obando Freire & Sifuentes",
      escena3D: "anim_13",
      guionOrador: "El modelo de retroalimentación 360 grados, originado en la psicología organizacional y adaptado con éxito en universidades de América Latina, triangula cuatro miradas convergentes: la autoevaluación del propio docente, el juicio fundado de sus colegas de cátedra, la mirada de los estudiantes y la perspectiva estratégica de la Dirección Departamental. Esto neutraliza los sesgos de popularidad de las encuestas tradicionales."
    },

    {
      id: "slide_14",
      numero: 14,
      bloque: "BLOQUE IV: DIAGRAMA 360",
      esquema: "Esquema 2: Arquitectura Visual 360°",
      badge: "Diagrama Vectorial SVG",
      titulo: "Arquitectura Circular del Modelo 360° en CURZAS",
      subtitulo: "Triangulación Multiactoral Formativa y Protección Criptográfica del Anonimato",
      puntosClave: [
        "Cuadrante 1 (Norte): Autoevaluación reflexiva sobre prácticas didácticas y tutorías virtuales.",
        "Cuadrante 2 (Este): Coevaluación entre pares de cátedra y articulación de programas analíticos.",
        "Cuadrante 3 (Sur): Apreciación estudiantil situada sobre acompañamiento y claridad pedagógica.",
        "Cuadrante 4 (Oeste): Dirección Departamental: planificación estratégica y cumplimiento de metas de carrera.",
        "Núcleo y Blindajes: Flujo directo hacia el Desarrollo Docente (Art. 76) con anonimato auditado por comisiones paritarias."
      ],
      metadatosFooter: "Diagrama SVG Modelo 360° • 4 Cuadrantes • Núcleo Formativo",
      escena3D: "anim_14",
      diagramaSVG: "assets/modelo_360.svg",
      guionOrador: "En el diagrama vectorial que estamos proyectando se observa con nitidez la arquitectura circular: los cuatro nodos confluyen hacia el núcleo central, que es el Desarrollo Docente bajo el Artículo 76 del Estatuto. En las esquinas inferiores se aprecian los dos blindajes esenciales: la protección criptográfica del anonimato en Moodle y el desacoplamiento formal respecto a los expedientes de cesantía."
    },

    // ─── BLOQUE V: GOBERNANZA, PODER Y TECNOLOGÍA (Filminas 15 y 16) ─────────
    {
      id: "slide_15",
      numero: 15,
      bloque: "BLOQUE V: MATUS PES",
      esquema: "Esquema 2: Planificación Estratégica Situacional",
      badge: "Carlos Matus (1993)",
      titulo: "Carlos Matus: La Universidad como Arena de Poder Compartido",
      subtitulo: "La Viabilidad Política como Construcción en el Cogobierno Universitario",
      puntosClave: [
        "Planificación Estratégica Situacional (PES): En las organizaciones públicas coexisten múltiples actores con intereses legítimos diferenciados.",
        "Arenas de Poder Compartido: En el CURZAS, ninguna autoridad puede imponer un sistema de evaluación por decreto; debe concertarse en cogobierno.",
        "Variables de Control Compartido: La factibilidad política requiere acordar con el gremio docente (ADUNC/FADUNC), los centros de estudiantes y autoridades.",
        "Gestión del Conflicto: Transformar la prevención y el rechazo inicial en un acuerdo constructivo de mejora laboral docente."
      ],
      metadatosFooter: "Carlos Matus (1993) • Poder Compartido • Cogobierno Universitario",
      escena3D: "anim_15",
      guionOrador: "Para evitar la ingenuidad tecnocrática de creer que basta con proponer un formulario para que se aplique, recurrimos a Carlos Matus y su Planificación Estratégica Situacional. La universidad nacional es una arena de poder compartido y conflicto legítimo. El Consejo Directivo del CURZAS es cogobernado por docentes, estudiantes, nodocentes y graduados. La viabilidad de este modelo no se decreta administrativamente; se construye mediante la concertación política paritaria."
    },

    {
      id: "slide_16",
      numero: 16,
      bloque: "BLOQUE V: ESTADO PLATAFORMA",
      esquema: "Esquema 2: Tecnología y Gobernanza",
      badge: "Oszlak (2020) & Cao/Blutman (2023)",
      titulo: "Estado Plataforma, Poligobernanza y Anonimato Algorítmico",
      subtitulo: "Capacidades Estatales Inteligentes sin Caer en el Tecno-Autoritarismo",
      puntosClave: [
        "Oscar Oszlak (2020) - El Estado Exponencial: Incorporar plataformas digitales (SIU-Guaraní y Moodle) para expandir capacidades institucionales.",
        "Anonimato Algorítmico: Criterio técnico estricto de n-mínimo de respuestas para impedir la inferencia individual en comisiones pequeñas.",
        "Horacio Cao & Gustavo Blutman (2023) - Poligobernanza: Superación del centralismo burocrático mediante redes colaborativas de gestión pública.",
        "Articulación Multinivel: Diálogo institucional entre Rectorado (Neuquén), Sede Central CURZAS (Viedma), Nodos y Claustros."
      ],
      metadatosFooter: "Oszlak (2020) • Cao & Blutman (2023) • Poligobernanza",
      escena3D: "anim_16",
      guionOrador: "Oscar Oszlak nos brinda la clave técnica: el Estado en la era exponencial debe valerse de plataformas digitales para construir capacidades estatales, pero cuidando con celo no caer en el tecno-autoritarismo. El sistema Moodle debe contar con algoritmos que impidan deducir quién respondió qué en cátedras con matrícula reducida. Y con Cao y Blutman comprendemos que la gobernanza en la Patagonia es multinivel y poligobernada, articulando a Rectorado con el CURZAS."
    },

    // ─── BLOQUE VI: METODOLOGÍA, FACTIBILIDAD Y CIERRE (Filminas 17 a 20) ────
    {
      id: "slide_17",
      numero: 17,
      bloque: "BLOQUE VI: METODOLOGÍA",
      esquema: "Esquema 3: Estrategia Metodológica",
      badge: "Diseño de Investigación",
      titulo: "Estrategia Metodológica y Triangulación Empírica",
      subtitulo: "Enfoque Cualitativo Exploratorio-Descriptivo Situado en el Departamento",
      puntosClave: [
        "Enfoque Metodológico: Predominantemente cualitativo, de corte exploratorio-descriptivo y transversal (2025–2026).",
        "Muestra y Actores Clave: Docentes regulares e interinos del Dpto. de Administración Pública, estudiantes de la Licenciatura, autoridades y tutores de Nodos.",
        "Técnicas de Recolección: Entrevistas en profundidad semiestructuradas, grupos focales temáticos y análisis documental normativo.",
        "Triangulación de Fuentes: Cruce de discursos de autoridades, percepciones docentes y reclamos estudiantiles para garantizar validez científica."
      ],
      metadatosFooter: "Diseño Cualitativo • Muestra Situada • Entrevistas y Grupos Focales",
      escena3D: "anim_17",
      guionOrador: "En el Esquema 3 metodológico, la investigación adopta un diseño predominantemente cualitativo, exploratorio y descriptivo. No buscamos una generalización estadística abstracta, sino comprender en profundidad los sentidos, temores y expectativas de los actores del Departamento de Administración Pública. La muestra incluye profesores regulares e interinos, representantes estudiantiles, autoridades y tutores de los nodos de la Línea Sur."
    },

    {
      id: "slide_18",
      numero: 18,
      bloque: "BLOQUE VI: FACTIBILIDAD",
      esquema: "Esquema 3: Cinco Dimensiones",
      badge: "Operacionalización Analítica",
      titulo: "Las Cinco Dimensiones Analíticas de Factibilidad",
      subtitulo: "Matriz Integral para la Evaluación de Viabilidad Institucional",
      puntosClave: [
        "1. Factibilidad Normativa: Resguardo irrestricto del CCT Docente (Dec. 1246/15) y desacoplamiento estatutario del Art. 75.",
        "2. Factibilidad Técnica: Compatibilidad con plataformas SIU/Moodle, protección criptográfica y usabilidad accesible.",
        "3. Factibilidad Organizacional: Capacidad departamental y de Secretaría Académica para procesar datos y articular talleres formativos.",
        "4. Factibilidad Cultural: Clima institucional de confianza, superación del miedo a la sanción y cultura de autoevaluación reflexiva.",
        "5. Factibilidad de Gobernanza: Aprobación por consenso en Consejo Directivo paritario multiactoral (Matus: poder compartido)."
      ],
      metadatosFooter: "5 Dimensiones • Criterios de Evaluación • Viabilidad Institucional",
      escena3D: "anim_18",
      guionOrador: "La factibilidad de la propuesta se operacionaliza en cinco dimensiones interdependientes: la normativa, que garantiza la legalidad laboral; la técnica, que asegura el software y el anonimato; la organizacional, que valida la capacidad de respuesta administrativa; la cultural, que mide el clima de confianza en las cátedras; y la gobernanza, que asegura el consenso político en el Consejo Directivo."
    },

    {
      id: "slide_19",
      numero: 19,
      bloque: "BLOQUE VI: VACANCIA",
      esquema: "Esquema 3: Vacancia Disciplinar",
      badge: "Aporte al Conocimiento Científico",
      titulo: "Vacancia Disciplinar y Aportes a la Gestión Pública",
      subtitulo: "Contribución Original a los Recursos Humanos en la Universidad Pública Patagónica",
      puntosClave: [
        "Vacancia Científica Comprobada: No existen en la literatura nacional estudios empíricos de factibilidad 360° en universidades públicas cogobernadas con redes territoriales híbridas.",
        "Aporte Teórico-Disciplinar: Enriquecer el campo de la Gestión de Recursos Humanos públicos con evidencia empírica situada en la Patagonia.",
        "Aporte a la Gestión Institucional: Proporcionar a las autoridades del CURZAS y la UNCo un insumo riguroso para la toma de decisiones informadas.",
        "Autonomía Universitaria: Resolver problemáticas pedagógicas con herramientas propias sin importar recetas estandarizadas del sector privado."
      ],
      metadatosFooter: "Vacancia Científica • Patagonia • Autonomía y Valor Público",
      escena3D: "anim_19",
      guionOrador: "La revisión del estado de la cuestión confirmó una notable vacancia disciplinar: no se registran en el país estudios de factibilidad 360 grados situados en universidades públicas patagónicas con dispersión geográfica y docencia híbrida. Por tanto, este TFG no solo cumple con un requisito de graduación, sino que llena un vacío de conocimiento, brindando al CURZAS evidencia empírica rigurosa para innovar en su carrera docente con plena autonomía."
    },

    {
      id: "slide_20",
      numero: 20,
      bloque: "BLOQUE VI: CONCLUSIONES",
      esquema: "Esquema 3: Cierre y Preguntas",
      badge: "Cierre de Exposición Oral",
      titulo: "Conclusiones, Síntesis y Apertura de Preguntas",
      subtitulo: "Hacia una Evaluación Docente Formativa, Situada y Democrática en el CURZAS",
      puntosClave: [
        "Síntesis de Factibilidad: La viabilidad es alta siempre que se garantice el desacoplamiento del Art. 75 y la confidencialidad técnica.",
        "Compromiso con la Universidad Pública: Fortalecer la docencia y el acompañamiento a estudiantes en parajes patagónicos.",
        "Agradecimiento Institucional: A la cátedra del Seminario de Integración y Aplicación y al Departamento de Administración Pública.",
        "Apertura al Tribunal: Quedo a entera disposición de la Dra. Noguera, el Esp. Abeiro y la Esp. Aguirre para sus preguntas y devoluciones."
      ],
      metadatosFooter: "Fin de Exposición • Tiempo: 30 minutos • Espacio para el Tribunal",
      escena3D: "anim_20",
      guionOrador: "Concluyo esta exposición oral reafirmando que evaluar el desempeño docente en la universidad pública no es una técnica de vigilancia burocrática, sino un compromiso ético con la calidad de la enseñanza y con el futuro de nuestros estudiantes en toda la geografía rionegrina. Agradezco profundamente las devoluciones y el acompañamiento formativo del equipo docente de cátedra a lo largo de este trayecto. Quedo a entera disposición del tribunal para responder sus preguntas."
    }
  ]
};

// Exportación compatible tanto con entorno navegador (window) como con módulos ES
if (typeof window !== "undefined") {
  window.PRESENTACION_DATA = PRESENTACION_DATA;
}
if (typeof module !== "undefined" && module.exports) {
  module.exports = PRESENTACION_DATA;
}
