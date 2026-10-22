/**
 * =============================================================================
 * MOTOR GRÁFICO 3D (THREE.JS) — PRESENTACIÓN DE TESINA
 * Universidad Nacional del Comahue — CURZAS
 * Autor: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes
 * =============================================================================
 * Renderiza los 6 objetos 3D conceptuales situados en el SEGUNDO PLANO
 * (desplazados a la derecha del lienzo para no interferir jamás con la lectura
 * del texto principal).
 */

class Presentation3D {
  constructor(canvasElement) {
    this.canvas = canvasElement;
    this.currentSceneId = "hero_orbit";
    this.scenes = {};
    this.dataPackets = []; // Paquetes de datos que viajan por las curvas
    this.nodeBeacons = [];  // Balizas territoriales pulsantes
    
    // Encuadre de Cámara: Desplazamiento calculado para que el objeto quede
    // exactamente en el tercio derecho (segundo plano ambiental)
    this.cameraTargets = {
      hero_orbit:      { pos: [1.8, 1.2, 7.0], lookAt: [1.2, 0, 0] },
      mapa_rio_negro:  { pos: [2.2, 4.2, 5.8], lookAt: [1.3, 0, 0] },
      balanza_tension: { pos: [2.0, 1.5, 6.2], lookAt: [1.2, 0.2, 0] },
      prisma_longo:    { pos: [2.0, 1.8, 6.0], lookAt: [1.2, 0, 0] },
      orbita_360:      { pos: [2.0, 2.2, 6.5], lookAt: [1.2, 0, 0] },
      matriz_sintesis: { pos: [1.8, 1.8, 6.2], lookAt: [1.1, 0, 0] }
    };

    this.currentCamPos = new THREE.Vector3(1.8, 1.2, 7.0);
    this.targetCamPos = new THREE.Vector3(1.8, 1.2, 7.0);
    this.currentLookAt = new THREE.Vector3(1.2, 0, 0);
    this.targetLookAt = new THREE.Vector3(1.2, 0, 0);

    this.init();
  }

  init() {
    // 1. Escena, Niebla Atmosférica y Cámara
    this.scene = new THREE.Scene();
    this.scene.fog = new THREE.FogExp2(0x070d18, 0.05);

    this.camera = new THREE.PerspectiveCamera(
      45,
      window.innerWidth / window.innerHeight,
      0.1,
      100
    );
    this.camera.position.copy(this.currentCamPos);

    // 2. Renderer WebGL de Alta Definición
    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      alpha: true,
      powerPreference: "high-performance"
    });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.15;

    // 3. Sistema de Iluminación Cinematográfica Sutil (Segundo Plano)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.65);
    this.scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0x38bdf8, 1.2);
    dirLight1.position.set(5, 8, 5);
    this.scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0x10b981, 0.8);
    dirLight2.position.set(-5, -3, 3);
    this.scene.add(dirLight2);

    const goldRim = new THREE.PointLight(0xf59e0b, 1.2, 15);
    goldRim.position.set(3, 2, -2);
    this.scene.add(goldRim);

    // 4. Polvo Atmosférico / Partículas en Suspensión (Ambiente Académico)
    this.createAtmosphericDust();

    // 5. Construcción de los 6 Objetos Tridimensionales Pertinentes
    this.buildSceneHeroOrbit();
    this.buildSceneMapaRioNegro();
    this.buildSceneBalanzaTension();
    this.buildScenePrismaLongo();
    this.buildSceneOrbita360();
    this.buildSceneMatrizSintesis();

    // Evento de Redimensionamiento
    window.addEventListener("resize", () => this.onWindowResize());

    // Iniciar Bucle de Animación
    this.clock = new THREE.Clock();
    this.animate();
  }

  // ─── AMBIENTE: POLVO CÓSMICO / PARTÍCULAS SUTILES ────────────────────────
  createAtmosphericDust() {
    const count = 400;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);

    for (let i = 0; i < count * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 22;
      positions[i + 1] = (Math.random() - 0.5) * 16;
      positions[i + 2] = (Math.random() - 0.5) * 16;

      const isCyan = Math.random() > 0.4;
      colors[i] = isCyan ? 0.22 : 0.96;
      colors[i + 1] = isCyan ? 0.74 : 0.62;
      colors[i + 2] = isCyan ? 0.97 : 0.04;
    }

    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));

    const material = new THREE.PointsMaterial({
      size: 0.045,
      vertexColors: true,
      transparent: true,
      opacity: 0.4,
      blending: THREE.AdditiveBlending
    });

    this.dustParticles = new THREE.Points(geometry, material);
    this.scene.add(this.dustParticles);
  }

  // ─── OBJETO 1: MONUMENTO AL SABER UNIVERSITARIO Y COGOBIERNO ─────────────
  buildSceneHeroOrbit() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // Pedestal cilíndrico de base en alambre y metal oscuro
    const baseGeo = new THREE.CylinderGeometry(1.6, 1.9, 0.2, 32);
    const baseMat = new THREE.MeshStandardMaterial({
      color: 0x0d1b2a,
      roughness: 0.5,
      metalness: 0.8
    });
    const baseMesh = new THREE.Mesh(baseGeo, baseMat);
    baseMesh.position.y = -1.6;
    group.add(baseMesh);

    // Núcleo facetado (Icosaedro de Zafiro reflectante con luz interna)
    const coreGeo = new THREE.IcosahedronGeometry(0.85, 1);
    const coreMat = new THREE.MeshPhysicalMaterial({
      color: 0x38bdf8,
      emissive: 0x0284c7,
      emissiveIntensity: 0.35,
      roughness: 0.1,
      metalness: 0.3,
      transmission: 0.65,
      transparent: true,
      opacity: 0.9
    });
    this.heroCore = new THREE.Mesh(coreGeo, coreMat);
    group.add(this.heroCore);

    // Núcleo interno pulsante
    const innerGeo = new THREE.SphereGeometry(0.4, 24, 24);
    const innerMat = new THREE.MeshBasicMaterial({
      color: 0xffffff,
      wireframe: true
    });
    this.heroInner = new THREE.Mesh(innerGeo, innerMat);
    this.heroCore.add(this.heroInner);

    // 3 Anillos Giroscópicos Académicos Concêntricos
    this.heroRings = [];
    const ringRadii = [1.35, 1.7, 2.05];
    const ringColors = [0x38bdf8, 0x10b981, 0xf59e0b];

    ringRadii.forEach((r, idx) => {
      const ringGeo = new THREE.TorusGeometry(r, 0.022, 16, 100);
      const ringMat = new THREE.MeshStandardMaterial({
        color: ringColors[idx],
        emissive: ringColors[idx],
        emissiveIntensity: 0.45,
        metalness: 0.9,
        roughness: 0.1
      });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = (idx + 1) * 0.5;
      ring.rotation.y = (idx + 1) * 0.4;
      group.add(ring);
      this.heroRings.push(ring);
    });

    group.visible = true;
    this.scenes["hero_orbit"] = group;
    this.scene.add(group);
  }

  // ─── OBJETO 2: CARTOGRAFÍA DE RÍO NEGRO Y RED DE NODOS TERRITORIALES ──────
  buildSceneMapaRioNegro() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // Plano del relieve provincial (malla cuadriculada estilizada de Río Negro)
    const gridGeo = new THREE.PlaneGeometry(5.5, 4.0, 24, 20);
    const gridMat = new THREE.MeshBasicMaterial({
      color: 0x1e293b,
      wireframe: true,
      transparent: true,
      opacity: 0.45
    });
    const grid = new THREE.Mesh(gridGeo, gridMat);
    grid.rotation.x = -Math.PI / 2.3;
    grid.position.y = -0.8;
    group.add(grid);

    // Definición de Nodos Reales del CURZAS (Coordenadas escaladas en el plano)
    // Sede Cabecera: Viedma (Este / Costa Atlántica)
    // Nodos Línea Sur y Costa: Sierra Grande, Valcheta, Los Menucos, Ramos Mexía
    const nodos = [
      { id: "viedma", nombre: "Viedma (Sede)", pos: [1.6, -0.6, 0.4], color: 0xf59e0b, main: true },
      { id: "sierra", nombre: "Sierra Grande", pos: [1.2, -0.7, 1.2], color: 0x38bdf8, main: false },
      { id: "valcheta", nombre: "Valcheta", pos: [0.3, -0.65, 0.2], color: 0x10b981, main: false },
      { id: "menucos", nombre: "Los Menucos", pos: [-0.8, -0.6, -0.2], color: 0x10b981, main: false },
      { id: "ramos", nombre: "Ramos Mexía", pos: [-0.3, -0.62, -0.1], color: 0x38bdf8, main: false }
    ];

    const viedmaPos = new THREE.Vector3(1.6, -0.6, 0.4);

    nodos.forEach((nodo) => {
      // Baliza / Torre del nodo
      const beaconHeight = nodo.main ? 0.7 : 0.4;
      const beaconGeo = new THREE.CylinderGeometry(0.04, 0.08, beaconHeight, 16);
      const beaconMat = new THREE.MeshStandardMaterial({
        color: nodo.color,
        emissive: nodo.color,
        emissiveIntensity: 0.6,
        metalness: 0.8
      });
      const beacon = new THREE.Mesh(beaconGeo, beaconMat);
      beacon.position.set(nodo.pos[0], nodo.pos[1] + beaconHeight / 2, nodo.pos[2]);
      group.add(beacon);

      // Anillo concéntrico de señal pulsante
      const ringGeo = new THREE.RingGeometry(0.12, 0.18, 24);
      const ringMat = new THREE.MeshBasicMaterial({
        color: nodo.color,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.8
      });
      const pulseRing = new THREE.Mesh(ringGeo, ringMat);
      pulseRing.rotation.x = Math.PI / 2;
      pulseRing.position.set(nodo.pos[0], nodo.pos[1] + 0.02, nodo.pos[2]);
      group.add(pulseRing);

      this.nodeBeacons.push({ mesh: beacon, ring: pulseRing, baseScale: 1 });

      // Arcos Bézier luminosos que conectan Viedma con los nodos (Docencia Híbrida / Res. 196/2022)
      if (!nodo.main) {
        const destPos = new THREE.Vector3(...nodo.pos);
        const midPoint = new THREE.Vector3()
          .addVectors(viedmaPos, destPos)
          .multiplyScalar(0.5);
        midPoint.y += 0.65; // Arco aéreo representativo de mediación tecnológica satelital

        const curve = new THREE.QuadraticBezierCurve3(viedmaPos, midPoint, destPos);
        const points = curve.getPoints(36);
        const curveGeo = new THREE.BufferGeometry().setFromPoints(points);
        const curveMat = new THREE.LineBasicMaterial({
          color: 0x38bdf8,
          transparent: true,
          opacity: 0.6
        });
        const line = new THREE.Line(curveGeo, curveMat);
        group.add(line);

        // Fotón de datos viajero que recorre el cable virtual
        const packetGeo = new THREE.SphereGeometry(0.045, 12, 12);
        const packetMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        const packet = new THREE.Mesh(packetGeo, packetMat);
        group.add(packet);

        this.dataPackets.push({ mesh: packet, curve: curve, progress: Math.random() });
      }
    });

    group.visible = false;
    this.scenes["mapa_rio_negro"] = group;
    this.scene.add(group);
  }

  // ─── OBJETO 3: PUENTE DE TENSIÓN PARADIGMÁTICA (ART. 75 vs. ART. 76) ──────
  buildSceneBalanzaTension() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // Plataforma de diálogo normativo
    const floorGeo = new THREE.CylinderGeometry(1.9, 2.1, 0.15, 36);
    const floorMat = new THREE.MeshStandardMaterial({
      color: 0x0f172a,
      roughness: 0.6,
      metalness: 0.8
    });
    const floor = new THREE.Mesh(floorGeo, floorMat);
    floor.position.y = -1.2;
    group.add(floor);

    // PILAR IZQUIERDO: "Control Estatutario y Sumatividad" (Art. 75 - Ámbar)
    const pilar1Geo = new THREE.BoxGeometry(0.45, 2.0, 0.45);
    const pilar1Mat = new THREE.MeshPhysicalMaterial({
      color: 0xf59e0b,
      emissive: 0xb45309,
      emissiveIntensity: 0.3,
      roughness: 0.2,
      metalness: 0.5,
      transparent: true,
      opacity: 0.85
    });
    const pilar1 = new THREE.Mesh(pilar1Geo, pilar1Mat);
    pilar1.position.set(-1.0, 0, 0);
    group.add(pilar1);

    // PILAR DERECHO: "Formación Docente y Desarrollo Continuo" (Art. 76 - Esmeralda)
    const pilar2Geo = new THREE.BoxGeometry(0.45, 2.0, 0.45);
    const pilar2Mat = new THREE.MeshPhysicalMaterial({
      color: 0x10b981,
      emissive: 0x047857,
      emissiveIntensity: 0.3,
      roughness: 0.2,
      metalness: 0.5,
      transparent: true,
      opacity: 0.85
    });
    const pilar2 = new THREE.Mesh(pilar2Geo, pilar2Mat);
    pilar2.position.set(1.0, 0, 0);
    group.add(pilar2);

    // PUENTE DE TENSIÓN: Arco de energía que une ambos pilares
    const bridgeCurve = new THREE.QuadraticBezierCurve3(
      new THREE.Vector3(-1.0, 0.9, 0),
      new THREE.Vector3(0, 1.45, 0),
      new THREE.Vector3(1.0, 0.9, 0)
    );
    const bridgeGeo = new THREE.TubeGeometry(bridgeCurve, 32, 0.04, 12, false);
    const bridgeMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const bridgeMesh = new THREE.Mesh(bridgeGeo, bridgeMat);
    group.add(bridgeMesh);

    // NÚCLEO LEVITANTE DE EQUILIBRIO ÉTICO Y GOBERNANZA (Oscila suavemente)
    const orbGeo = new THREE.OctahedronGeometry(0.38, 1);
    const orbMat = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      emissive: 0x38bdf8,
      emissiveIntensity: 0.6,
      roughness: 0.1,
      metalness: 0.2
    });
    this.tensionOrb = new THREE.Mesh(orbGeo, orbMat);
    this.tensionOrb.position.set(0, 1.45, 0);
    group.add(this.tensionOrb);

    group.visible = false;
    this.scenes["balanza_tension"] = group;
    this.scene.add(group);
  }

  // ─── OBJETO 4: ESTRUCTURA SISTÉMICA DE 4 SUBSISTEMAS (LONGO 2006) ────────
  buildScenePrismaLongo() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // Base del Sistema Público
    const baseGeo = new THREE.CylinderGeometry(1.8, 2.0, 0.2, 4); // Base cuadrangular
    const baseMat = new THREE.MeshStandardMaterial({
      color: 0x070d18,
      roughness: 0.4,
      metalness: 0.9
    });
    const base = new THREE.Mesh(baseGeo, baseMat);
    base.rotation.y = Math.PI / 4;
    base.position.y = -1.2;
    group.add(base);

    // 4 Columnas que representan los 4 Subsistemas de Longo:
    // 1. Gestión del Rendimiento (Azul)
    // 2. Organización del Trabajo (Cian)
    // 3. Gestión del Desarrollo (Verde Esmeralda)
    // 4. Relaciones Humanas y Sociales (Oro)
    this.longoPillars = [];
    const pillarData = [
      { col: 0x2563eb, pos: [-0.85, 0, -0.85] },
      { col: 0x06b6d4, pos: [0.85, 0, -0.85] },
      { col: 0x10b981, pos: [0.85, 0, 0.85] },
      { col: 0xf59e0b, pos: [-0.85, 0, 0.85] }
    ];

    pillarData.forEach((p) => {
      const geo = new THREE.BoxGeometry(0.32, 1.7, 0.32);
      const mat = new THREE.MeshStandardMaterial({
        color: p.col,
        emissive: p.col,
        emissiveIntensity: 0.35,
        roughness: 0.3,
        metalness: 0.7
      });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(...p.pos);
      group.add(mesh);
      this.longoPillars.push(mesh);
    });

    // Prisma Central Flotante: "VALOR PÚBLICO ESTRATÉGICO"
    const prismGeo = new THREE.OctahedronGeometry(0.55, 0);
    const prismMat = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      emissive: 0x38bdf8,
      emissiveIntensity: 0.5,
      roughness: 0.1,
      metalness: 0.4,
      transmission: 0.7,
      transparent: true,
      opacity: 0.95
    });
    this.longoCore = new THREE.Mesh(prismGeo, prismMat);
    this.longoCore.position.set(0, 0.3, 0);
    group.add(this.longoCore);

    // Vínculos reticulares de luz entre columnas
    const wireGeo = new THREE.BufferGeometry();
    const wirePos = new Float32Array([
      -0.85, 0.85, -0.85,  0.85, 0.85, -0.85,
       0.85, 0.85, -0.85,  0.85, 0.85,  0.85,
       0.85, 0.85,  0.85, -0.85, 0.85,  0.85,
      -0.85, 0.85,  0.85, -0.85, 0.85, -0.85
    ]);
    wireGeo.setAttribute("position", new THREE.BufferAttribute(wirePos, 3));
    const wireMat = new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.5 });
    const wire = new THREE.LineSegments(wireGeo, wireMat);
    group.add(wire);

    group.visible = false;
    this.scenes["prisma_longo"] = group;
    this.scene.add(group);
  }

  // ─── OBJETO 5: GIROSCOPIO 360° Y ESCUDO DE ANONIMATO (OSZLAK / MATUS) ─────
  buildSceneOrbita360() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // 4 Nodos de la Triangulación 360°:
    // 1. Autoevaluación Docente
    // 2. Coevaluación entre Pares
    // 3. Heteroevaluación Estudiantil
    // 4. Dirección Departamental
    this.actores360 = [];
    const actores = [
      { color: 0x38bdf8, angle: 0, radius: 1.45 },
      { color: 0x10b981, angle: Math.PI / 2, radius: 1.45 },
      { color: 0xf59e0b, angle: Math.PI, radius: 1.45 },
      { color: 0xa855f7, angle: (Math.PI * 3) / 2, radius: 1.45 }
    ];

    // Anillo orbital central de retroalimentación
    const orbitRingGeo = new THREE.TorusGeometry(1.45, 0.025, 16, 80);
    const orbitRingMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.55
    });
    this.orbit360Ring = new THREE.Mesh(orbitRingGeo, orbitRingMat);
    this.orbit360Ring.rotation.x = Math.PI / 2.5;
    group.add(this.orbit360Ring);

    actores.forEach((act) => {
      const nodeGeo = new THREE.SphereGeometry(0.18, 20, 20);
      const nodeMat = new THREE.MeshStandardMaterial({
        color: act.color,
        emissive: act.color,
        emissiveIntensity: 0.6,
        roughness: 0.2,
        metalness: 0.7
      });
      const node = new THREE.Mesh(nodeGeo, nodeMat);
      node.userData = { angle: act.angle, radius: act.radius };
      group.add(node);
      this.actores360.push(node);
    });

    // ESCUDO GEODÉSICO DE ANONIMATO Y PROTECCIÓN DE DATOS (Oszlak / CCT)
    const shieldGeo = new THREE.IcosahedronGeometry(1.05, 1);
    const shieldMat = new THREE.MeshBasicMaterial({
      color: 0x10b981,
      wireframe: true,
      transparent: true,
      opacity: 0.35
    });
    this.shield360 = new THREE.Mesh(shieldGeo, shieldMat);
    group.add(this.shield360);

    group.visible = false;
    this.scenes["orbita_360"] = group;
    this.scene.add(group);
  }

  // ─── OBJETO 6: RADAR 3D DE LAS 5 DIMENSIONES DE FACTIBILIDAD ─────────────
  buildSceneMatrizSintesis() {
    const group = new THREE.Group();
    group.position.set(1.5, 0, 0);

    // Pentágono de 5 radios (Normativa, Técnica, Organizacional, Cultural, Gobernanza)
    const numAxes = 5;
    const radius = 1.6;

    // Ejes radiales
    for (let i = 0; i < numAxes; i++) {
      const angle = (i * 2 * Math.PI) / numAxes - Math.PI / 2;
      const x = Math.cos(angle) * radius;
      const z = Math.sin(angle) * radius;

      const axisGeo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, -0.6, 0),
        new THREE.Vector3(x, 0.4, z)
      ]);
      const axisMat = new THREE.LineBasicMaterial({
        color: 0x475569,
        transparent: true,
        opacity: 0.6
      });
      const axisLine = new THREE.Line(axisGeo, axisMat);
      group.add(axisLine);

      // Baliza en cada vértice del pentágono
      const nodeGeo = new THREE.SphereGeometry(0.08, 16, 16);
      const nodeMat = new THREE.MeshStandardMaterial({
        color: 0x38bdf8,
        emissive: 0x38bdf8,
        emissiveIntensity: 0.5
      });
      const node = new THREE.Mesh(nodeGeo, nodeMat);
      node.position.set(x, 0.4, z);
      group.add(node);
    }

    // Polígono Tridimensional de Factibilidad Positiva (Extruido)
    const factorScores = [0.88, 0.82, 0.85, 0.78, 0.92]; // Ponderación de viabilidad
    const shape = new THREE.Shape();

    for (let i = 0; i < numAxes; i++) {
      const angle = (i * 2 * Math.PI) / numAxes - Math.PI / 2;
      const r = radius * factorScores[i];
      const x = Math.cos(angle) * r;
      const y = Math.sin(angle) * r;
      if (i === 0) shape.moveTo(x, y);
      else shape.lineTo(x, y);
    }
    shape.closePath();

    const extrudeSettings = { depth: 0.15, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 0.04, bevelThickness: 0.04 };
    const polyGeo = new THREE.ExtrudeGeometry(shape, extrudeSettings);
    const polyMat = new THREE.MeshPhysicalMaterial({
      color: 0x10b981,
      emissive: 0x059669,
      emissiveIntensity: 0.4,
      roughness: 0.2,
      metalness: 0.3,
      transmission: 0.6,
      transparent: true,
      opacity: 0.8
    });
    this.radarMesh = new THREE.Mesh(polyGeo, polyMat);
    this.radarMesh.rotation.x = -Math.PI / 2.4;
    this.radarMesh.position.y = -0.1;
    group.add(this.radarMesh);

    group.visible = false;
    this.scenes["matriz_sintesis"] = group;
    this.scene.add(group);
  }

  // ─── TRANSICIÓN SUAVE ENTRE ESCENAS TRIDIMENSIONALES ─────────────────────
  switchScene(newSceneId) {
    if (this.currentSceneId === newSceneId) return;

    const oldGroup = this.scenes[this.currentSceneId];
    const newGroup = this.scenes[newSceneId];

    if (oldGroup) oldGroup.visible = false;
    if (newGroup) newGroup.visible = true;

    this.currentSceneId = newSceneId;

    // Actualizar objetivos de cámara
    const target = this.cameraTargets[newSceneId];
    if (target) {
      this.targetCamPos.set(...target.pos);
      this.targetLookAt.set(...target.lookAt);
    }
  }

  // ─── AJUSTE DINÁMICO AL TAMAÑO DE PANTALLA ────────────────────────────────
  onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  // ─── BUCLE PRINCIPAL DE ANIMACIÓN Y FÍSICA (60 FPS) ───────────────────────
  animate() {
    requestAnimationFrame(() => this.animate());

    const delta = this.clock.getDelta();
    const time = this.clock.getElapsedTime();

    // 1. Interpolación Suave de Cámara (Lerp Cinematográfico)
    this.currentCamPos.lerp(this.targetCamPos, 0.05);
    this.currentLookAt.lerp(this.targetLookAt, 0.05);
    this.camera.position.copy(this.currentCamPos);
    this.camera.lookAt(this.currentLookAt);

    // 2. Rotación Lenta del Polvo Atmosférico
    if (this.dustParticles) {
      this.dustParticles.rotation.y = time * 0.015;
    }

    // 3. Animaciones Específicas del Objeto en Escena
    if (this.currentSceneId === "hero_orbit") {
      if (this.heroCore) {
        this.heroCore.rotation.y = time * 0.4;
        this.heroCore.rotation.x = Math.sin(time * 0.5) * 0.15;
      }
      if (this.heroRings) {
        this.heroRings[0].rotation.z = time * 0.3;
        this.heroRings[1].rotation.x = time * 0.45;
        this.heroRings[2].rotation.y = time * 0.25;
      }
    } else if (this.currentSceneId === "mapa_rio_negro") {
      // Pulso de balizas territoriales
      this.nodeBeacons.forEach((b, idx) => {
        const s = 1 + Math.sin(time * 3 + idx) * 0.25;
        b.ring.scale.set(s, s, s);
      });
      // Flujo de paquetes de datos de docencia híbrida por los arcos
      this.dataPackets.forEach((dp) => {
        dp.progress += delta * 0.45;
        if (dp.progress > 1) dp.progress = 0;
        const pt = dp.curve.getPoint(dp.progress);
        dp.mesh.position.copy(pt);
      });
    } else if (this.currentSceneId === "balanza_tension") {
      if (this.tensionOrb) {
        this.tensionOrb.position.y = 1.45 + Math.sin(time * 2.5) * 0.08;
        this.tensionOrb.rotation.y = time * 0.6;
      }
    } else if (this.currentSceneId === "prisma_longo") {
      if (this.longoCore) {
        this.longoCore.rotation.y = time * 0.5;
        this.longoCore.position.y = 0.3 + Math.sin(time * 2) * 0.06;
      }
      if (this.scenes["prisma_longo"]) {
        this.scenes["prisma_longo"].rotation.y = Math.sin(time * 0.3) * 0.15;
      }
    } else if (this.currentSceneId === "orbita_360") {
      if (this.shield360) {
        this.shield360.rotation.y = time * 0.25;
        this.shield360.rotation.x = time * 0.15;
      }
      if (this.actores360) {
        this.actores360.forEach((actor) => {
          const curA = actor.userData.angle + time * 0.5;
          actor.position.x = Math.cos(curA) * actor.userData.radius;
          actor.position.z = Math.sin(curA) * actor.userData.radius;
          actor.position.y = Math.sin(curA * 2) * 0.15;
        });
      }
    } else if (this.currentSceneId === "matriz_sintesis") {
      if (this.scenes["matriz_sintesis"]) {
        this.scenes["matriz_sintesis"].rotation.y = time * 0.2;
      }
    }

    this.renderer.render(this.scene, this.camera);
  }
}

// Exportación global
window.Presentation3D = Presentation3D;
