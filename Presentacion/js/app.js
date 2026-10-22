/**
 * =============================================================================
 * CONTROLADOR PRINCIPAL — APLICACIÓN DE PRESENTACIÓN DE TESINA (20 FILMINAS)
 * Universidad Nacional del Comahue — CURZAS
 * Autor: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes
 * =============================================================================
 * Administra la navegación a través de las 20 filminas, el visor de diagramas
 * vectoriales SVG, el cronómetro de 30 minutos, el modo enfoque de texto
 * y el panel de respaldo metodológico de 7 pestañas para el jurado.
 */

class PresentationApp {
  constructor(data) {
    this.data = data;
    this.currentSlideIndex = 0;
    this.totalSlides = data.slides.length;

    // Cronómetro de 30 minutos
    this.totalSeconds = data.timing.totalMinutos * 60;
    this.elapsedSeconds = 0;
    this.timerRunning = false;
    this.timerInterval = null;

    // Estado del modo enfoque de texto (atenuación del fondo 3D)
    this.is3dDimmed = false;

    // Catálogo de Diagramas Vectoriales SVG Oficiales del TFG
    this.catalogoSVGs = [
      {
        id: "longo_oficial",
        titulo: "Subsistemas de la Gestión de Recursos Humanos",
        autor: "Francisco Longo (2006)",
        archivo: "assets/Sistemas-longo.svg",
        descripcion: "Diagrama arquitectónico central que modela la alineación estratégica, la planificación y la retroalimentación continua entre el Rendimiento y el Desarrollo Docente."
      },
      {
        id: "modelo_360_curzas",
        titulo: "Arquitectura Circular del Modelo de Retroalimentación 360°",
        autor: "Héctor Daniel Ayarachi Fuentes (2026)",
        archivo: "assets/modelo_360.svg",
        descripcion: "Triangulación formativa de 4 cuadrantes (Autoevaluación, Pares, Estudiantes, Dirección) con blindaje de anonimato y desacoplamiento estatutario del Art. 75."
      },
      {
        id: "red_nodos_territorio",
        titulo: "Mapeo Territorial y Red de Nodos de Docencia Híbrida",
        autor: "CURZAS-UNCo (Res. CD-CURZA N° 196/2022)",
        archivo: "assets/red_territorial.svg",
        descripcion: "Distribución geográfica de la Sede Cabecera Viedma y los Nodos Territoriales de Sierra Grande, Valcheta, Los Menucos y Ramos Mexía con mediaciones tecnológicas."
      },
      {
        id: "subsistemas_operativos",
        titulo: "Estrategia y Subsistemas de RRHH (Detalle Operativo)",
        autor: "Francisco Longo (2006)",
        archivo: "assets/subsistemas_longo.svg",
        descripcion: "Desglose técnico ampliado de las relaciones laborales, condiciones de compensación y organización del trabajo en el sector público."
      }
    ];

    // Elementos del DOM
    this.initDOMElements();

    // Inicializar Motor 3D
    const canvas = document.getElementById("webgl-canvas");
    this.engine3D = new window.Presentation3D(canvas);

    // Configurar Eventos e Inicializar
    this.bindEvents();
    this.renderStationsIndicator();
    this.renderSlide(0);
    this.populateDrawerContent();
  }

  initDOMElements() {
    this.cardElement = document.getElementById("slide-card");
    this.badgeElement = document.getElementById("slide-badge");
    this.bloqueBadgeElement = document.getElementById("slide-bloque-badge");
    this.titleElement = document.getElementById("slide-title");
    this.subtitleElement = document.getElementById("slide-subtitle");
    this.bulletsElement = document.getElementById("slide-bullets");
    this.footerMetaElement = document.getElementById("slide-footer-meta");

    this.slideCounter = document.getElementById("slide-counter");

    this.timerDisplay = document.getElementById("timer-display");
    this.btnTimerToggle = document.getElementById("btn-timer-toggle");
    this.btnTimerReset = document.getElementById("btn-timer-reset");

    this.btnPrev = document.getElementById("btn-prev");
    this.btnNext = document.getElementById("btn-next");
    this.stationsContainer = document.getElementById("stations-indicator");

    this.notesModal = document.getElementById("notes-modal");
    this.notesBody = document.getElementById("notes-body");
    this.btnToggleNotes = document.getElementById("btn-toggle-notes");
    this.btnCloseNotes = document.getElementById("btn-close-notes");

    this.drawerBackdrop = document.getElementById("drawer-backdrop");
    this.drawerPanel = document.getElementById("drawer-panel");
    this.btnToggleDrawer = document.getElementById("btn-toggle-drawer");
    this.btnCloseDrawer = document.getElementById("btn-close-drawer");
    this.drawerContent = document.getElementById("drawer-content");

    this.btnDim3d = document.getElementById("btn-dim-3d");
    this.canvas = document.getElementById("webgl-canvas");

    // Modal Visor SVG
    this.svgModal = document.getElementById("svg-modal");
    this.svgModalBackdrop = document.getElementById("svg-modal-backdrop");
    this.svgModalTitle = document.getElementById("svg-modal-title");
    this.svgModalImg = document.getElementById("svg-modal-img");
    this.btnCloseSvg = document.getElementById("btn-close-svg");
  }

  bindEvents() {
    // Botones de Navegación
    this.btnPrev.addEventListener("click", () => this.prevSlide());
    this.btnNext.addEventListener("click", () => this.nextSlide());

    // Cronómetro
    this.btnTimerToggle.addEventListener("click", () => this.toggleTimer());
    this.btnTimerReset.addEventListener("click", () => this.resetTimer());

    // Modal de Notas de Orador
    this.btnToggleNotes.addEventListener("click", () => this.toggleNotes());
    this.btnCloseNotes.addEventListener("click", () => this.toggleNotes(false));

    // Drawer de Respaldo Metodológico
    this.btnToggleDrawer.addEventListener("click", () => this.toggleDrawer());
    this.btnCloseDrawer.addEventListener("click", () => this.toggleDrawer(false));
    this.drawerBackdrop.addEventListener("click", () => this.toggleDrawer(false));

    // Modal Visor SVG
    if (this.btnCloseSvg) {
      this.btnCloseSvg.addEventListener("click", () => this.closeSvgModal());
    }
    if (this.svgModalBackdrop) {
      this.svgModalBackdrop.addEventListener("click", () => this.closeSvgModal());
    }

    // Modo Enfoque de Texto (Atenuar 3D)
    if (this.btnDim3d) {
      this.btnDim3d.addEventListener("click", () => this.toggle3dDim());
    }

    // Pestañas del Drawer (7 categorías)
    document.querySelectorAll(".drawer-tab").forEach((tab) => {
      tab.addEventListener("click", (e) => {
        document.querySelectorAll(".drawer-tab").forEach((t) => t.classList.remove("active"));
        e.currentTarget.classList.add("active");
        this.renderDrawerTab(e.currentTarget.dataset.tab);
      });
    });

    // Atajos de Teclado Profesionales
    window.addEventListener("keydown", (e) => {
      if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
        this.nextSlide();
      } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
        this.prevSlide();
      } else if (e.key.toLowerCase() === "n") {
        this.toggleNotes();
      } else if (e.key.toLowerCase() === "m") {
        this.toggleDrawer();
      } else if (e.key.toLowerCase() === "v") {
        // Atajo V: Ver diagrama SVG de la filmina actual si existe
        const slide = this.data.slides[this.currentSlideIndex];
        if (slide.diagramaSVG) {
          this.openSvgModal(slide.diagramaSVG, slide.titulo);
        } else {
          this.toggleDrawer(true);
          document.querySelector('[data-tab="svgs"]')?.click();
        }
      } else if (e.key.toLowerCase() === "d") {
        this.toggle3dDim();
      } else if (e.key.toLowerCase() === "t") {
        this.toggleTimer();
      } else if (e.key.toLowerCase() === "f") {
        this.toggleFullscreen();
      } else if (e.key === "Escape") {
        this.closeSvgModal();
        this.toggleNotes(false);
        this.toggleDrawer(false);
      }
    });
  }

  renderStationsIndicator() {
    this.stationsContainer.innerHTML = "";
    for (let i = 0; i < this.totalSlides; i++) {
      const dot = document.createElement("div");
      dot.className = `station-dot ${i === 0 ? "active" : ""}`;
      dot.title = `Filmina ${i + 1}: ${this.data.slides[i].esquema}`;
      dot.addEventListener("click", () => this.goToSlide(i));
      this.stationsContainer.appendChild(dot);
    }
  }

  renderSlide(index) {
    const slide = this.data.slides[index];

    // Animación suave de transición de tarjeta de texto
    this.cardElement.classList.add("entering");

    setTimeout(() => {
      this.badgeElement.textContent = `FILMINA ${index + 1} / ${this.totalSlides} • ${slide.badge}`;
      if (this.bloqueBadgeElement) {
        this.bloqueBadgeElement.textContent = slide.bloque || "SIA 2026";
      }
      this.titleElement.textContent = slide.titulo;
      this.subtitleElement.textContent = slide.subtitulo;

      this.bulletsElement.innerHTML = "";
      slide.puntosClave.forEach((punto) => {
        const li = document.createElement("li");
        li.textContent = punto;
        this.bulletsElement.appendChild(li);
      });

      // Si la filmina tiene un diagrama SVG oficial vinculado, agregamos el botón de apertura interactiva
      if (slide.diagramaSVG) {
        const svgActionBox = document.createElement("div");
        svgActionBox.className = "slide-svg-action";
        svgActionBox.innerHTML = `
          <button class="btn-open-svg" title="Observar Diagrama Vectorial SVG (Atajo: V)">
            <span>📐 Observar Diagrama SVG de Esta Sección</span>
            <span class="shortcut-pill">V</span>
          </button>
        `;
        svgActionBox.querySelector("button").addEventListener("click", () => {
          this.openSvgModal(slide.diagramaSVG, slide.titulo);
        });
        this.bulletsElement.appendChild(svgActionBox);
      }

      this.footerMetaElement.innerHTML = `
        <span>📌 ${slide.metadatosFooter}</span>
        <span>⏱️ Ritmo sugerido: ~1.5 min</span>
      `;

      // Actualizar contador en la cabecera
      if (this.slideCounter) {
        this.slideCounter.textContent = `${index + 1} / ${this.totalSlides}`;
      }

      // Actualizar teleprompter de notas del orador
      this.notesBody.innerHTML = `
        <p><strong>🎯 Objetivo de la Filmina ${index + 1}:</strong> ${slide.esquema}</p>
        <p style="margin-top: 0.6rem;">${slide.guionOrador}</p>
      `;

      // Sincronizar indicador visual de estaciones (dots)
      const dots = this.stationsContainer.querySelectorAll(".station-dot");
      dots.forEach((dot, idx) => {
        dot.classList.toggle("active", idx === index);
      });

      // Habilitar/Deshabilitar botones
      this.btnPrev.disabled = index === 0;
      this.btnNext.disabled = index === this.totalSlides - 1;

      // Notificar al motor 3D para posicionar el objeto de segundo plano correspondiente
      this.engine3D.switchScene(slide.escena3D);

      this.cardElement.classList.remove("entering");
    }, 180);
  }

  nextSlide() {
    if (this.currentSlideIndex < this.totalSlides - 1) {
      this.goToSlide(this.currentSlideIndex + 1);
    }
  }

  prevSlide() {
    if (this.currentSlideIndex > 0) {
      this.goToSlide(this.currentSlideIndex - 1);
    }
  }

  goToSlide(index) {
    if (index >= 0 && index < this.totalSlides) {
      this.currentSlideIndex = index;
      this.renderSlide(index);
    }
  }

  // ─── VISOR MODAL DE DIAGRAMAS SVG EN ALTA DEFINICIÓN ─────────────────────
  openSvgModal(src, title) {
    if (!this.svgModal) return;
    this.svgModalImg.src = src;
    this.svgModalTitle.textContent = `📐 ${title || "Diagrama Conceptual SVG"}`;
    this.svgModal.classList.add("open");
    this.svgModalBackdrop.classList.add("open");
  }

  closeSvgModal() {
    if (!this.svgModal) return;
    this.svgModal.classList.remove("open");
    this.svgModalBackdrop.classList.remove("open");
    setTimeout(() => {
      this.svgModalImg.src = "";
    }, 300);
  }

  // ─── CRONÓMETRO REGRESIVO DE 30 MINUTOS ──────────────────────────────────
  toggleTimer() {
    if (this.timerRunning) {
      this.pauseTimer();
    } else {
      this.startTimer();
    }
  }

  startTimer() {
    if (!this.timerRunning) {
      this.timerRunning = true;
      this.btnTimerToggle.textContent = "⏸";
      this.btnTimerToggle.title = "Pausar cronómetro (T)";

      this.timerInterval = setInterval(() => {
        this.elapsedSeconds++;
        this.updateTimerDisplay();

        if (this.elapsedSeconds >= this.totalSeconds) {
          this.pauseTimer();
          alert("⏱️ Los 30 minutos estipulados para la exposición han concluido.");
        }
      }, 1000);
    }
  }

  pauseTimer() {
    this.timerRunning = false;
    this.btnTimerToggle.textContent = "▶";
    this.btnTimerToggle.title = "Iniciar cronómetro (T)";
    clearInterval(this.timerInterval);
  }

  resetTimer() {
    this.pauseTimer();
    this.elapsedSeconds = 0;
    this.updateTimerDisplay();
  }

  updateTimerDisplay() {
    const remainingSeconds = Math.max(0, this.totalSeconds - this.elapsedSeconds);
    const m = Math.floor(remainingSeconds / 60);
    const s = remainingSeconds % 60;
    this.timerDisplay.textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;

    const minutosTranscurridos = Math.floor(this.elapsedSeconds / 60);

    this.timerDisplay.classList.remove("warning", "critical");
    if (minutosTranscurridos >= this.data.timing.alertaRojaMinutos) {
      this.timerDisplay.classList.add("critical");
    } else if (minutosTranscurridos >= this.data.timing.alertaAmarillaMinutos) {
      this.timerDisplay.classList.add("warning");
    }
  }

  // ─── HERRAMIENTAS LATERALES Y DRAWERS ───────────────────────────────────
  toggleNotes(forceState) {
    const isOpen = this.notesModal.classList.contains("open");
    const newState = forceState !== undefined ? forceState : !isOpen;
    this.notesModal.classList.toggle("open", newState);
    this.btnToggleNotes.classList.toggle("active", newState);
  }

  toggleDrawer(forceState) {
    const isOpen = this.drawerPanel.classList.contains("open");
    const newState = forceState !== undefined ? forceState : !isOpen;
    this.drawerPanel.classList.toggle("open", newState);
    this.drawerBackdrop.classList.toggle("open", newState);
    this.btnToggleDrawer.classList.toggle("active", newState);
  }

  toggle3dDim() {
    this.is3dDimmed = !this.is3dDimmed;
    this.canvas.classList.toggle("dimmed", this.is3dDimmed);
    if (this.btnDim3d) {
      this.btnDim3d.classList.toggle("active", this.is3dDimmed);
      this.btnDim3d.title = this.is3dDimmed
        ? "Modo Enfoque Texto Activo (D)"
        : "Atenuar Fondo 3D / Enfoque Texto (D)";
    }
  }

  populateDrawerContent() {
    this.renderDrawerTab("autores");
  }

  renderDrawerTab(tabType) {
    this.drawerContent.innerHTML = "";
    const f = this.data.fichasRespaldo;

    if (tabType === "autores" && f.autores) {
      f.autores.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card";
        card.innerHTML = `
          <h4>🧠 ${item.autor}</h4>
          <p>${item.concepto}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "normativa" && f.normativa) {
      f.normativa.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card";
        card.innerHTML = `
          <h4>📜 ${item.norma}</h4>
          <p>${item.descripcion}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "objetivos" && (f.objetivos || f.matrizObjetivos)) {
      const lista = f.objetivos || f.matrizObjetivos;
      lista.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card";
        card.innerHTML = `
          <h4>🎯 ${item.nivel}</h4>
          <p>${item.texto}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "dimensiones" && f.dimensiones) {
      f.dimensiones.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card";
        card.innerHTML = `
          <h4>⚙️ ${item.dim}</h4>
          <p>${item.detalle}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "territorio" && f.territorio) {
      f.territorio.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card";
        card.innerHTML = `
          <h4>📍 ${item.sede}</h4>
          <p>${item.detalle}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "faq" && f.faq) {
      f.faq.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card faq-card";
        card.innerHTML = `
          <h4>❓ ${item.pregunta}</h4>
          <p><strong>R:</strong> ${item.respuesta}</p>
        `;
        this.drawerContent.appendChild(card);
      });
    } else if (tabType === "svgs") {
      this.catalogoSVGs.forEach((item) => {
        const card = document.createElement("div");
        card.className = "ref-card svg-ref-card";
        card.innerHTML = `
          <h4>📐 ${item.titulo}</h4>
          <p><strong>Fuente:</strong> ${item.autor}</p>
          <p style="margin-top: 0.4rem;">${item.descripcion}</p>
          <button class="btn-inspect-svg" style="margin-top: 0.8rem; width: 100%; padding: 0.5rem; background: rgba(56, 189, 248, 0.2); border: 1px solid #38bdf8; color: #fff; border-radius: 6px; cursor: pointer; font-weight: 600;">
            🔍 Abrir Diagrama en Pantalla Completa
          </button>
        `;
        card.querySelector(".btn-inspect-svg").addEventListener("click", () => {
          this.openSvgModal(item.archivo, item.titulo);
        });
        this.drawerContent.appendChild(card);
      });
    }
  }

  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(() => {});
      }
    }
  }
}

// Inicializar la aplicación al cargar el DOM
window.addEventListener("DOMContentLoaded", () => {
  if (window.PRESENTACION_DATA) {
    window.app = new PresentationApp(window.PRESENTACION_DATA);
  } else {
    console.error("No se encontraron los metadatos de PRESENTACION_DATA.");
  }
});
