/**
 * =============================================================================
 * MOTOR GRÁFICO 3D ACADÉMICO — PRESENTACIÓN DE TESINA (20 ESCULTURAS SOLEMNES)
 * Universidad Nacional del Comahue — CURZAS
 * Autor: Tec. Sup. en RRHH Héctor Daniel Ayarachi Fuentes
 * =============================================================================
 *
 * Estética: Galería de museo universitario, piezas escultóricas de mármol de
 * Carrara, latón dorado envejecido, bronce escultórico, cristal ahumado e
 * iluminación de exhibición sobria. Sin estética gamer, sin luces de neón ni
 * lásers: diseño de arte académico clásico y riguroso.
 */

class Presentation3D {
  constructor(canvasElement) {
    this.canvas = canvasElement;
    this.currentSceneId = "anim_01";
    this.scenes = {};
    this.animTime = 0;

    // Posiciones de cámara cinematográficas y sobrias orientadas hacia la derecha
    // para dejar espacio prioritario a la tarjeta de texto institucional a la izquierda
    this.cameraTargets = {
      anim_01: { pos: [2.3, 1.4, 6.8], lookAt: [1.4, 0.2, 0] },
      anim_02: { pos: [2.2, 1.6, 6.5], lookAt: [1.3, 0.1, 0] },
      anim_03: { pos: [2.4, 1.2, 6.8], lookAt: [1.4, 0.0, 0] },
      anim_04: { pos: [2.3, 2.8, 5.8], lookAt: [1.3, -0.2, 0] },
      anim_05: { pos: [2.1, 2.2, 5.6], lookAt: [1.2, 0.0, 0] },
      anim_06: { pos: [2.0, 1.4, 6.5], lookAt: [1.2, 0.1, 0] },
      anim_07: { pos: [2.2, 1.5, 6.2], lookAt: [1.3, 0.1, 0] },
      anim_08: { pos: [2.3, 1.8, 6.4], lookAt: [1.3, 0.1, 0] },
      anim_09: { pos: [2.1, 1.4, 6.2], lookAt: [1.2, 0.0, 0] },
      anim_10: { pos: [2.2, 1.6, 6.0], lookAt: [1.3, 0.1, 0] },
      anim_11: { pos: [2.6, 1.3, 7.2], lookAt: [1.6, 0.0, 0] },
      anim_12: { pos: [2.3, 1.7, 6.0], lookAt: [1.3, 0.1, 0] },
      anim_13: { pos: [2.2, 1.8, 6.4], lookAt: [1.3, 0.1, 0] },
      anim_14: { pos: [2.4, 1.5, 6.8], lookAt: [1.4, 0.0, 0] },
      anim_15: { pos: [2.1, 1.6, 6.2], lookAt: [1.2, 0.1, 0] },
      anim_16: { pos: [2.3, 1.8, 6.4], lookAt: [1.3, 0.1, 0] },
      anim_17: { pos: [2.2, 1.6, 6.0], lookAt: [1.2, 0.1, 0] },
      anim_18: { pos: [2.1, 1.8, 6.2], lookAt: [1.2, 0.1, 0] },
      anim_19: { pos: [2.3, 2.2, 6.5], lookAt: [1.3, 0.2, 0] },
      anim_20: { pos: [2.0, 1.4, 6.8], lookAt: [1.2, 0.1, 0] }
    };

    this.currentCamPos  = new THREE.Vector3(2.3, 1.4, 6.8);
    this.targetCamPos   = new THREE.Vector3(2.3, 1.4, 6.8);
    this.currentLookAt  = new THREE.Vector3(1.4, 0.2, 0);
    this.targetLookAt   = new THREE.Vector3(1.4, 0.2, 0);

    this.init();
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     INICIALIZACIÓN DEL RENDERER Y ESCENA ACADÉMICA (GALERÍA BLANCA CLÁSICA)
     ═══════════════════════════════════════════════════════════════════════════ */
  init() {
    this.scene = new THREE.Scene();
    // Atmósfera de galería clásica en blanco marfil / luz de día
    this.scene.fog = new THREE.FogExp2(0xf4f6f9, 0.038);

    this.camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 0.1, 100);
    this.camera.position.copy(this.currentCamPos);

    this.renderer = new THREE.WebGLRenderer({
      canvas: this.canvas,
      antialias: true,
      alpha: true,
      powerPreference: "high-performance"
    });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.setClearColor(0xf4f6f9, 1);
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.05;
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // Iluminación de museo / galería de esculturas clásicas con luz natural
    this.setupMuseumLighting();

    // Motes sutiles de polvo dorado de biblioteca bajo la luz del sol
    this.createAtmosphericMotes();

    // Construcción de las 20 esculturas académicas
    this.buildAll20Scenes();

    window.addEventListener("resize", () => this.onWindowResize());
    this.clock = new THREE.Clock();
    this.animate();
  }

  setupMuseumLighting() {
    // 1. Luz Ambiental clara y envolvente de galería
    const amb = new THREE.AmbientLight(0xffffff, 0.95);
    this.scene.add(amb);

    // 2. Spotlight Principal de Galería (luz cálida cenital sobre la escultura)
    this.keyLight = new THREE.DirectionalLight(0xfff5e6, 1.35);
    this.keyLight.position.set(5, 9, 6);
    this.keyLight.castShadow = true;
    this.keyLight.shadow.mapSize.set(1024, 1024);
    this.scene.add(this.keyLight);

    // 3. Luz de Relleno Suave (cielo diáfano azul pálido)
    const fill = new THREE.DirectionalLight(0xdbeafe, 0.55);
    fill.position.set(-6, 2, 4);
    this.scene.add(fill);

    // 4. Luz de Contorno de Latón (bronce y oro desde atrás)
    this.rimLight = new THREE.PointLight(0xb8860b, 0.9, 18);
    this.rimLight.position.set(3, 4, -4);
    this.scene.add(this.rimLight);

    // 5. Rebote de suelo de mármol claro
    const bounce = new THREE.HemisphereLight(0xffffff, 0xe2e8f0, 0.7);
    this.scene.add(bounce);
  }

  createAtmosphericMotes() {
    // Puntos sutiles de polvo dorado flotando como partículas de luz solar en una biblioteca clásica
    const count = 180;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);

    for (let i = 0; i < count; i++) {
      pos[i * 3]     = (Math.random() - 0.5) * 24;
      pos[i * 3 + 1] = (Math.random() - 0.5) * 16;
      pos[i * 3 + 2] = (Math.random() - 0.5) * 16;
    }

    geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));

    const mat = new THREE.PointsMaterial({
      color: 0xb8860b,
      size: 0.022,
      transparent: true,
      opacity: 0.22,
      sizeAttenuation: true
    });

    this.dustParticles = new THREE.Points(geo, mat);
    this.scene.add(this.dustParticles);
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     MATERIALES NOBLES: Mármol, Latón, Bronce, Granito y Cristal Ahumado
     ═══════════════════════════════════════════════════════════════════════════ */

  /** Mármol blanco de Carrara / Alabastro marfil */
  marbleMat(color = 0xfcfbf9, opts = {}) {
    return new THREE.MeshStandardMaterial({
      color,
      roughness: 0.32,
      metalness: 0.02,
      ...opts
    });
  }

  /** Latón dorado cepillado / Oro antiguo (instrumental académico y astronómico) */
  brassMat(color = 0xb8860b, opts = {}) {
    return new THREE.MeshStandardMaterial({
      color,
      roughness: 0.22,
      metalness: 0.9,
      ...opts
    });
  }

  /** Bronce escultórico patinado */
  bronzeMat(color = 0x5a4329, opts = {}) {
    return new THREE.MeshStandardMaterial({
      color,
      roughness: 0.35,
      metalness: 0.85,
      ...opts
    });
  }

  /** Granito pulido pizarra (base de pedestales de museo para anclaje visual) */
  graniteMat(color = 0x242d3d, opts = {}) {
    return new THREE.MeshStandardMaterial({
      color,
      roughness: 0.38,
      metalness: 0.15,
      ...opts
    });
  }

  /** Cristal óptico esmerilado de museo */
  glassMat(color = 0xdde6ed, opts = {}) {
    return new THREE.MeshPhysicalMaterial({
      color,
      roughness: 0.1,
      metalness: 0.05,
      transmission: 0.82,
      transparent: true,
      opacity: 0.78,
      clearcoat: 1.0,
      clearcoatRoughness: 0.08,
      ...opts
    });
  }

  /** Pedestal clásico de museo para soportar cada escultura */
  createMuseumPlinth(parent, radius = 1.4, height = 0.18) {
    const plinth = new THREE.Group();

    // Base de granito
    const baseGeo = new THREE.CylinderGeometry(radius, radius * 1.06, height, 48);
    const baseMesh = new THREE.Mesh(baseGeo, this.graniteMat());
    baseMesh.position.y = -1.2;
    plinth.add(baseMesh);

    // Moldura o aro de latón superior
    const rimGeo = new THREE.TorusGeometry(radius * 0.98, 0.015, 16, 64);
    const rimMesh = new THREE.Mesh(rimGeo, this.brassMat());
    rimMesh.rotation.x = Math.PI / 2;
    rimMesh.position.y = -1.2 + height / 2;
    plinth.add(rimMesh);

    parent.add(plinth);
    return plinth;
  }

  /** Aro astronómico / armilar de latón */
  createBrassArmillaryRing(radius, tube = 0.018, parent) {
    const geo = new THREE.TorusGeometry(radius, tube, 24, 96);
    const mesh = new THREE.Mesh(geo, this.brassMat());
    parent.add(mesh);
    return mesh;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     CONSTRUCCIÓN DE LAS 20 ESCULTURAS ACADÉMICAS
     ═══════════════════════════════════════════════════════════════════════════ */
  buildAll20Scenes() {
    for (let i = 1; i <= 20; i++) {
      const id = `anim_${String(i).padStart(2, "0")}`;
      const group = new THREE.Group();
      group.position.set(1.6, 0, 0);
      group.visible = i === 1;
      this.scenes[id] = group;
      this.scene.add(group);
      this[`buildScene_${id}`](group);
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 1. APERTURA INSTITUCIONAL: Esfera Armilar Renacentista (CURZAS - UNCo)
  //    Pedestal de granito y latón + 3 aros meridiano concéntricos + orbe marfil
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_01(g) {
    this.createMuseumPlinth(g, 1.4);

    // Columna central de soporte
    const column = new THREE.Mesh(
      new THREE.CylinderGeometry(0.08, 0.14, 0.8, 32),
      this.marbleMat(0xf5f3ee)
    );
    column.position.y = -0.7;
    g.add(column);

    // Esfera central de alabastro marfil
    this.core01 = new THREE.Mesh(
      new THREE.SphereGeometry(0.55, 48, 48),
      this.marbleMat(0xfdfbf7)
    );
    g.add(this.core01);

    // Tres aros astronómicos de latón
    this.rings01 = [
      this.createBrassArmillaryRing(1.15, 0.016, g),
      this.createBrassArmillaryRing(1.45, 0.016, g),
      this.createBrassArmillaryRing(1.75, 0.018, g)
    ];

    // Eje polar con remate esférico
    const axis = new THREE.Mesh(
      new THREE.CylinderGeometry(0.02, 0.02, 2.3, 16),
      this.brassMat()
    );
    g.add(axis);
    this.axis01 = axis;
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 2. VALOR PÚBLICO: Monumento de Anillos Armónicos (Oszlak / Moore)
  //    Tres aros de bronce esculpido en levitación escalonada sobre mármol
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_02(g) {
    this.createMuseumPlinth(g, 1.35);

    // Gema central de cristal
    this.core02 = new THREE.Mesh(
      new THREE.DodecahedronGeometry(0.48, 2),
      this.glassMat(0xf8fafc)
    );
    g.add(this.core02);

    // Tres anillos de bronce en expansión vertical armónica
    this.rings02 = [];
    const radii = [0.85, 1.25, 1.65];
    radii.forEach((r, idx) => {
      const ring = this.createBrassArmillaryRing(r, 0.015, g);
      ring.rotation.x = Math.PI / 2;
      ring.position.y = -0.3 + idx * 0.35;
      this.rings02.push(ring);
    });
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 3. MARCO NORMATIVO: Frontispicio de Templo Clásico (Res. 266/23)
  //    Tres columnas jónicas de mármol con arquitrabe y frontón de latón
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_03(g) {
    this.createMuseumPlinth(g, 1.5);

    this.pillars03 = [];
    const colPositions = [-0.9, 0, 0.9];

    colPositions.forEach((posX) => {
      const col = new THREE.Group();

      // Base
      col.add(new THREE.Mesh(
        new THREE.CylinderGeometry(0.16, 0.18, 0.12, 24),
        this.brassMat()
      ));

      // Fuste estriado de mármol
      const fuste = new THREE.Mesh(
        new THREE.CylinderGeometry(0.1, 0.12, 1.8, 24),
        this.marbleMat()
      );
      fuste.position.y = 0.96;
      col.add(fuste);

      // Capitel de latón
      const cap = new THREE.Mesh(
        new THREE.CylinderGeometry(0.18, 0.1, 0.15, 24),
        this.brassMat()
      );
      cap.position.y = 1.92;
      col.add(cap);

      col.position.set(posX, -1.0, 0);
      g.add(col);
      this.pillars03.push(col);
    });

    // Arquitrabe horizontal de mármol
    const architrave = new THREE.Mesh(
      new THREE.BoxGeometry(2.3, 0.16, 0.35),
      this.marbleMat()
    );
    architrave.position.set(0, 1.05, 0);
    g.add(architrave);

    // Frontón superior con perfil triangular de latón
    const pediment = new THREE.Mesh(
      new THREE.ConeGeometry(1.2, 0.5, 4),
      this.brassMat()
    );
    pediment.rotation.y = Math.PI / 4;
    pediment.position.set(0, 1.38, 0);
    g.add(pediment);
    this.pediment03 = pediment;
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 4. TERRITORIO: Maqueta Geodésica de Río Negro con Hitos Escultóricos
  //    Placa de bronce topográfica con 5 obeliscos geodésicos en mármol y oro
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_04(g) {
    this.createMuseumPlinth(g, 1.6);

    // Placa territorial base en bronce oscuro
    const plate = new THREE.Mesh(
      new THREE.BoxGeometry(3.0, 0.1, 2.2),
      this.bronzeMat(0x423325)
    );
    plate.position.y = -0.9;
    g.add(plate);

    // 5 Obeliscos de hitos territoriales
    this.obelisks04 = [];
    const positions = [
      [1.1, 0.5],    // Viedma (Sede Cabecera)
      [0.4, 0.2],    // Valcheta
      [0.8, -0.4],   // Sierra Grande
      [-0.4, 0.3],   // Los Menucos
      [-0.1, -0.2]   // Ramos Mexía
    ];

    positions.forEach((pos, idx) => {
      const isCabecera = idx === 0;
      const obelisk = new THREE.Group();

      // Fuste de obelisco de mármol
      const height = isCabecera ? 1.5 : 0.85;
      const shaft = new THREE.Mesh(
        new THREE.CylinderGeometry(0.04, 0.08, height, 4),
        this.marbleMat()
      );
      shaft.position.y = height / 2;
      obelisk.add(shaft);

      // Piramidón superior de latón dorado
      const cap = new THREE.Mesh(
        new THREE.ConeGeometry(0.06, 0.15, 4),
        this.brassMat()
      );
      cap.position.y = height + 0.075;
      obelisk.add(cap);

      obelisk.position.set(pos[0], -0.85, pos[1]);
      g.add(obelisk);
      this.obelisks04.push(obelisk);
    });
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 5. DOCENCIA HÍBRIDA: Red Tensada de Nodos Territoriales
  //    Filamentos de latón conectando esferas perladas en equilibrio estático
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_05(g) {
    this.createMuseumPlinth(g, 1.5);

    const viedmaPos = new THREE.Vector3(1.0, 0.3, 0.2);
    const nodes = [
      new THREE.Vector3(0.3, 0.1, 0.8),
      new THREE.Vector3(-0.2, 0.2, -0.1),
      new THREE.Vector3(-0.9, -0.1, 0.4),
      new THREE.Vector3(-0.4, -0.2, -0.6)
    ];

    // Nodo central Viedma (perla mayor con anillo de latón)
    const vNode = new THREE.Mesh(
      new THREE.SphereGeometry(0.2, 32, 32),
      this.marbleMat(0xfdfbf7)
    );
    vNode.position.copy(viedmaPos);
    g.add(vNode);

    const vRing = this.createBrassArmillaryRing(0.32, 0.01, g);
    vRing.position.copy(viedmaPos);
    vRing.rotation.x = Math.PI / 3;

    // Nodos periféricos y filamentos de conexión
    this.filaments05 = [];
    nodes.forEach(pos => {
      const pNode = new THREE.Mesh(
        new THREE.SphereGeometry(0.12, 24, 24),
        this.brassMat()
      );
      pNode.position.copy(pos);
      g.add(pNode);

      // Filamento tensor de latón
      const lineCurve = new THREE.LineCurve3(viedmaPos, pos);
      const tubeGeo = new THREE.TubeGeometry(lineCurve, 20, 0.008, 8, false);
      const tube = new THREE.Mesh(tubeGeo, this.brassMat());
      g.add(tube);
      this.filaments05.push(tube);
    });
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 6. DESNATURALIZACIÓN: Escultura Cinética de Péndulos Armónicos
  //    Esferas de mármol suspendidas en alineación epistemológica (Wainerman & Sautu)
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_06(g) {
    this.createMuseumPlinth(g, 1.4);

    // Marco superior de bronce
    const topBar = new THREE.Mesh(
      new THREE.CylinderGeometry(0.03, 0.03, 2.2, 16),
      this.brassMat()
    );
    topBar.rotation.z = Math.PI / 2;
    topBar.position.y = 1.3;
    g.add(topBar);

    this.spheres06 = [];
    const count = 7;
    for (let i = 0; i < count; i++) {
      const posX = -0.8 + (i * 1.6) / (count - 1);
      const isOdd = i % 2 === 0;

      const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(0.11, 24, 24),
        isOdd ? this.marbleMat() : this.brassMat()
      );
      sphere.position.set(posX, 0.1, 0);
      g.add(sphere);

      // Hilo
      const stringGeo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(posX, 1.3, 0),
        new THREE.Vector3(posX, 0.1, 0)
      ]);
      const stringLine = new THREE.Line(
        stringGeo,
        new THREE.LineBasicMaterial({ color: 0x94a3b8 })
      );
      g.add(stringLine);

      this.spheres06.push({ mesh: sphere, line: stringLine, x: posX, freq: 1.2 + i * 0.1 });
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 7. TENSIÓN NORMATIVA: Balanza de la Justicia Universitaria (Art. 75 vs 76)
  //    Fuste de mármol con balancín de latón y platillos solemnes
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_07(g) {
    this.createMuseumPlinth(g, 1.4);

    // Pilar central de mármol
    const post = new THREE.Mesh(
      new THREE.CylinderGeometry(0.08, 0.12, 2.1, 24),
      this.marbleMat()
    );
    post.position.y = 0.05;
    g.add(post);

    // Balancín transversal de latón
    this.beam07 = new THREE.Group();
    const beamBar = new THREE.Mesh(
      new THREE.CylinderGeometry(0.025, 0.025, 2.2, 16),
      this.brassMat()
    );
    beamBar.rotation.z = Math.PI / 2;
    this.beam07.add(beamBar);

    // Dos platillos de bronce
    [-1.0, 1.0].forEach((posX, idx) => {
      const panGroup = new THREE.Group();
      const panMesh = new THREE.Mesh(
        new THREE.CylinderGeometry(0.35, 0.05, 0.08, 32),
        this.brassMat(idx === 0 ? 0xc5a059 : 0xd4af37)
      );
      panMesh.position.y = -0.65;
      panGroup.add(panMesh);

      // Cadenas
      const cord = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(0, -0.65, 0)
        ]),
        new THREE.LineBasicMaterial({ color: 0xc5a059 })
      );
      panGroup.add(cord);

      panGroup.position.set(posX, 0, 0);
      this.beam07.add(panGroup);
      if (idx === 0) this.panLeft07 = panGroup;
      else this.panRight07 = panGroup;
    });

    this.beam07.position.y = 1.05;
    g.add(this.beam07);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 8. PREGUNTAS DE INVESTIGACIÓN: Astrolabio Geodésico de Navegación
  //    Instrumento científico clásico con limbo graduado de latón y cristal
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_08(g) {
    this.createMuseumPlinth(g, 1.35);

    // Limbo graduado exterior de bronce
    this.astrolabeRing08 = this.createBrassArmillaryRing(1.2, 0.03, g);

    // Red interior en cruz de latón
    [-1, 1].forEach(d => {
      const bar = new THREE.Mesh(
        new THREE.BoxGeometry(d === -1 ? 2.3 : 0.02, 0.02, d === 1 ? 2.3 : 0.02),
        this.brassMat()
      );
      g.add(bar);
    });

    // Disco de cristal con grabados
    const disc = new THREE.Mesh(
      new THREE.CylinderGeometry(1.05, 1.05, 0.02, 32),
      this.glassMat()
    );
    disc.rotation.x = Math.PI / 2;
    g.add(disc);

    // Alidada / regla giratoria
    this.alidada08 = new THREE.Mesh(
      new THREE.BoxGeometry(0.08, 1.8, 0.04),
      this.brassMat(0xe8cf8d)
    );
    g.add(this.alidada08);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 9. MATRIZ DE OBJETIVOS: Tétrada Monumental de Placas de Bronce
  //    4 placas de bronce noble dispuestas en compás ordenado
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_09(g) {
    this.createMuseumPlinth(g, 1.4);

    this.tablets09 = [];
    for (let i = 0; i < 4; i++) {
      const tablet = new THREE.Group();

      // Placa de bronce
      const plate = new THREE.Mesh(
        new THREE.BoxGeometry(0.55, 0.95, 0.03),
        this.brassMat()
      );
      tablet.add(plate);

      // Marco fino de mármol
      const frame = new THREE.Mesh(
        new THREE.BoxGeometry(0.59, 0.99, 0.02),
        this.marbleMat()
      );
      frame.position.z = -0.01;
      tablet.add(frame);

      tablet.userData = { angle: (i * Math.PI) / 2 };
      g.add(tablet);
      this.tablets09.push(tablet);
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 10. FRANCISCO LONGO: Heptágono Escultórico de los 7 Subsistemas
  //     Prisma regular de 7 caras en mármol blanco y corona de latón
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_10(g) {
    this.createMuseumPlinth(g, 1.4);

    // Prisma heptagonal de mármol
    this.heptagon10 = new THREE.Mesh(
      new THREE.CylinderGeometry(0.7, 0.8, 1.4, 7),
      this.marbleMat(0xfaf8f5)
    );
    g.add(this.heptagon10);

    // Anillo exterior de latón
    this.ring10 = this.createBrassArmillaryRing(1.35, 0.02, g);
    this.ring10.rotation.x = Math.PI / 3;

    // Corona superior
    const crown = new THREE.Mesh(
      new THREE.ConeGeometry(0.5, 0.4, 7),
      this.brassMat()
    );
    crown.position.y = 0.9;
    g.add(crown);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 11. DIAGRAMA SVG LONGO: Atril de Honor Académico
  //     Marco sutil de latón sobre plinto para acompañar el diagrama SVG
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_11(g) {
    this.createMuseumPlinth(g, 1.5);

    // Atril de mármol
    const stand = new THREE.Mesh(
      new THREE.CylinderGeometry(0.08, 0.16, 1.3, 24),
      this.marbleMat()
    );
    stand.position.y = -0.45;
    g.add(stand);

    // Marco de honor
    this.frame11 = new THREE.Mesh(
      new THREE.TorusGeometry(1.2, 0.02, 16, 64),
      this.brassMat()
    );
    this.frame11.position.y = 0.35;
    g.add(this.frame11);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 12. CUATRO SUBSISTEMAS OPERATIVOS: Escalera Monumental de Mármol
  //     Cuatro pedestales escalonados ascendentes con molduras de latón
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_12(g) {
    this.createMuseumPlinth(g, 1.5);

    this.steps12 = [];
    for (let i = 0; i < 4; i++) {
      const step = new THREE.Group();
      const height = 0.6 + i * 0.35;

      const block = new THREE.Mesh(
        new THREE.BoxGeometry(0.3, height, 0.3),
        this.marbleMat()
      );
      block.position.y = -0.9 + height / 2;
      step.add(block);

      const rim = new THREE.Mesh(
        new THREE.BoxGeometry(0.32, 0.04, 0.32),
        this.brassMat()
      );
      rim.position.y = -0.9 + height + 0.02;
      step.add(rim);

      step.position.set(-0.75 + i * 0.5, 0, 0);
      g.add(step);
      this.steps12.push(step);
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 13. MODELO 360°: Giroscopio Cuádruple de Bronce y Alabastro
  //     4 aros cardinales girando solemnemente con 4 esferas de mármol
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_13(g) {
    this.createMuseumPlinth(g, 1.4);

    // Eje vertical
    const post = new THREE.Mesh(
      new THREE.CylinderGeometry(0.04, 0.08, 2.2, 16),
      this.marbleMat()
    );
    g.add(post);

    // Anillo exterior de latón
    this.gyroRing13 = this.createBrassArmillaryRing(1.3, 0.02, g);
    this.gyroRing13.rotation.x = Math.PI / 2.5;

    // 4 esferas de alabastro cardinales
    this.quadSpheres13 = [];
    for (let i = 0; i < 4; i++) {
      const sp = new THREE.Mesh(
        new THREE.SphereGeometry(0.14, 24, 24),
        i % 2 === 0 ? this.marbleMat(0xfdfbf7) : this.brassMat()
      );
      g.add(sp);
      this.quadSpheres13.push({ mesh: sp, angle: (i * Math.PI) / 2 });
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 14. BLINDAJE DE ANONIMATO: Cúpula Geodésica de Cristal y Tracería de Bronce
  //     Cúpula protectora arquitectónica de cristal esmerilado y nervaduras
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_14(g) {
    this.createMuseumPlinth(g, 1.5);

    // Cúpula esférica de cristal protector
    this.dome14 = new THREE.Mesh(
      new THREE.IcosahedronGeometry(1.25, 2),
      this.glassMat(0xf8fafc, { opacity: 0.82 })
    );
    g.add(this.dome14);

    // Nervaduras de bronce (wireframe sobrio de latón)
    const ribs = new THREE.Mesh(
      new THREE.IcosahedronGeometry(1.26, 2),
      new THREE.MeshStandardMaterial({
        color: 0xc5a059,
        wireframe: true,
        roughness: 0.3,
        metalness: 0.85
      })
    );
    g.add(ribs);
    this.ribs14 = ribs;

    // Núcleo de custodia dorado
    const innerGem = new THREE.Mesh(
      new THREE.OctahedronGeometry(0.28, 1),
      this.brassMat(0xe8cf8d)
    );
    g.add(innerGem);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 15. CARLOS MATUS (PES): Prisma Triangular de Triangulación Estratégica
  //     Prisma de mármol negro y barras tensoras de latón (Triángulo de Gobierno)
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_15(g) {
    this.createMuseumPlinth(g, 1.4);

    this.nodes15 = [];
    const colors = [0xc5a059, 0xf5f3ee, 0x6e5437];

    for (let i = 0; i < 3; i++) {
      const a = (i * 2 * Math.PI) / 3 - Math.PI / 2;
      const sphere = new THREE.Mesh(
        new THREE.DodecahedronGeometry(0.2, 1),
        i === 1 ? this.marbleMat() : this.brassMat()
      );
      sphere.position.set(Math.cos(a) * 1.15, 0, Math.sin(a) * 1.15);
      g.add(sphere);
      this.nodes15.push(sphere);
    }

    // Barras tensoras de latón conectando los 3 vértices
    for (let i = 0; i < 3; i++) {
      const next = (i + 1) % 3;
      const a1 = (i * 2 * Math.PI) / 3 - Math.PI / 2;
      const a2 = (next * 2 * Math.PI) / 3 - Math.PI / 2;
      const p1 = new THREE.Vector3(Math.cos(a1) * 1.15, 0, Math.sin(a1) * 1.15);
      const p2 = new THREE.Vector3(Math.cos(a2) * 1.15, 0, Math.sin(a2) * 1.15);

      const tube = new THREE.Mesh(
        new THREE.TubeGeometry(new THREE.LineCurve3(p1, p2), 10, 0.015, 8, false),
        this.brassMat()
      );
      g.add(tube);
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 16. POLIGOBERNANZA (Cao & Blutman): Estructura Arquitectónica de Tensegridad
  //     Barras de latón flotando en perfecto equilibrio tensado sin tocarse
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_16(g) {
    this.createMuseumPlinth(g, 1.4);

    this.tensegrity16 = new THREE.Group();
    for (let i = 0; i < 3; i++) {
      const bar = new THREE.Mesh(
        new THREE.CylinderGeometry(0.035, 0.035, 1.8, 16),
        this.brassMat()
      );
      bar.rotation.x = Math.PI / 3;
      bar.rotation.y = (i * 2 * Math.PI) / 3;
      bar.position.y = 0;
      this.tensegrity16.add(bar);
    }
    g.add(this.tensegrity16);

    // Aro unificador de mármol
    const ring = this.createBrassArmillaryRing(1.2, 0.012, g);
    ring.rotation.x = Math.PI / 2;
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 17. METODOLOGÍA: Teodolito y Prisma Óptico Geodésico
  //     Prisma de cristal puro tallado sobre montura clásica de latón
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_17(g) {
    this.createMuseumPlinth(g, 1.4);

    // Trípode clásico
    const tripod = new THREE.Mesh(
      new THREE.CylinderGeometry(0.04, 0.16, 1.2, 3),
      this.marbleMat()
    );
    tripod.position.y = -0.55;
    g.add(tripod);

    // Prisma triangular de cristal óptico puro
    this.prism17 = new THREE.Mesh(
      new THREE.CylinderGeometry(0.45, 0.45, 0.9, 3),
      this.glassMat(0xffffff)
    );
    this.prism17.position.y = 0.4;
    g.add(this.prism17);

    // Aro graduado de latón
    const ring = this.createBrassArmillaryRing(0.85, 0.015, g);
    ring.position.y = 0.4;
    ring.rotation.x = Math.PI / 2;
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 18. FACTIBILIDAD: Pentagrama Armónico de Vitral y Latón
  //     Escultura pentagonal con cinco ejes de bronce sosteniendo placas de cristal
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_18(g) {
    this.createMuseumPlinth(g, 1.4);

    const R = 1.2;
    this.pentGroup18 = new THREE.Group();

    // 5 radios de latón
    for (let i = 0; i < 5; i++) {
      const a = (i * 2 * Math.PI) / 5 - Math.PI / 2;
      const x = Math.cos(a) * R;
      const y = Math.sin(a) * R;

      const bar = new THREE.Mesh(
        new THREE.TubeGeometry(new THREE.LineCurve3(new THREE.Vector3(0, 0, 0), new THREE.Vector3(x, y, 0)), 8, 0.015, 8, false),
        this.brassMat()
      );
      this.pentGroup18.add(bar);

      // Nodo de mármol
      const dot = new THREE.Mesh(
        new THREE.SphereGeometry(0.09, 16, 16),
        this.marbleMat()
      );
      dot.position.set(x, y, 0);
      this.pentGroup18.add(dot);
    }

    this.pentGroup18.position.y = 0.2;
    g.add(this.pentGroup18);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 19. VACANCIA DISCIPLINAR: Torre Linterna de la Sabiduría Académica
  //     Faro clásico de mampostería y cúpula de bronce de biblioteca renacentista
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_19(g) {
    this.createMuseumPlinth(g, 1.4);

    // Torre cilíndrica de mármol
    this.tower19 = new THREE.Group();
    const shaft = new THREE.Mesh(
      new THREE.CylinderGeometry(0.3, 0.45, 1.8, 24),
      this.marbleMat()
    );
    shaft.position.y = -0.05;
    this.tower19.add(shaft);

    // Linterna de latón y cristal
    const lantern = new THREE.Mesh(
      new THREE.CylinderGeometry(0.25, 0.25, 0.45, 8),
      this.glassMat()
    );
    lantern.position.y = 1.0;
    this.tower19.add(lantern);

    // Cúpula superior de latón
    const dome = new THREE.Mesh(
      new THREE.SphereGeometry(0.28, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2),
      this.brassMat()
    );
    dome.position.y = 1.22;
    this.tower19.add(dome);

    g.add(this.tower19);
  }

  // ──────────────────────────────────────────────────────────────────────────
  // 20. CIERRE INSTITUCIONAL: Gran Medallón de Honor CURZAS - UNCo
  //     Medalla conmemorativa de bronce y oro sustentada sobre plinto clásico
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_20(g) {
    this.createMuseumPlinth(g, 1.5);

    this.medal20 = new THREE.Group();

    // Disco de medalla de bronce pulido
    const disc = new THREE.Mesh(
      new THREE.CylinderGeometry(1.05, 1.05, 0.12, 48),
      this.brassMat(0xd4af37)
    );
    disc.rotation.x = Math.PI / 2;
    this.medal20.add(disc);

    // Corona de laureles labrada (aro exterior de latón texturado)
    const laurel = new THREE.Mesh(
      new THREE.TorusGeometry(1.15, 0.03, 16, 64),
      this.brassMat(0xe8cf8d)
    );
    this.medal20.add(laurel);

    // Blasón central en bajorrelieve
    const innerEmblem = new THREE.Mesh(
      new THREE.CylinderGeometry(0.7, 0.7, 0.16, 32),
      this.marbleMat(0xfdfbf7)
    );
    innerEmblem.rotation.x = Math.PI / 2;
    this.medal20.add(innerEmblem);

    this.medal20.position.y = 0.2;
    g.add(this.medal20);
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     TRANSICIÓN CINEMATOGRÁFICA Y CONTROL DE CÁMARA
     ═══════════════════════════════════════════════════════════════════════════ */
  switchScene(newSceneId) {
    if (this.currentSceneId === newSceneId) return;

    const oldG = this.scenes[this.currentSceneId];
    const newG = this.scenes[newSceneId];

    if (oldG) oldG.visible = false;
    if (newG) newG.visible = true;

    this.currentSceneId = newSceneId;

    const target = this.cameraTargets[newSceneId];
    if (target) {
      this.targetCamPos.set(...target.pos);
      this.targetLookAt.set(...target.lookAt);
    }
  }

  onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     BUCLE DE ANIMACIÓN: MOVIMIENTO SOLEMNE Y DIGNO (MUSEO VIVO)
     ═══════════════════════════════════════════════════════════════════════════ */
  animate() {
    requestAnimationFrame(() => this.animate());

    const t = this.clock.getElapsedTime();

    // Interpolación suave y cinematográfica de la cámara
    this.currentCamPos.lerp(this.targetCamPos, 0.035);
    this.currentLookAt.lerp(this.targetLookAt, 0.035);
    this.camera.position.copy(this.currentCamPos);
    this.camera.lookAt(this.currentLookAt);

    // Motes dorados de polvo en lenta deriva atmosférica
    if (this.dustParticles) {
      this.dustParticles.rotation.y = t * 0.006;
    }

    // Micro-rotación lenta y solemne de cada escultura según la escena activa
    const id = this.currentSceneId;

    if (id === "anim_01") {
      if (this.core01) this.core01.rotation.y = t * 0.08;
      if (this.rings01) {
        this.rings01[0].rotation.x = t * 0.12;
        this.rings01[1].rotation.y = t * 0.10;
        this.rings01[2].rotation.z = t * 0.08;
      }
    }
    else if (id === "anim_02") {
      if (this.core02) this.core02.rotation.y = t * 0.1;
      if (this.rings02) {
        this.rings02.forEach((r, idx) => {
          r.rotation.z = t * (0.05 + idx * 0.03);
        });
      }
    }
    else if (id === "anim_03") {
      if (this.pediment03) {
        this.pediment03.rotation.y = Math.PI / 4 + Math.sin(t * 0.4) * 0.03;
      }
    }
    else if (id === "anim_04") {
      if (this.obelisks04) {
        this.obelisks04[0].rotation.y = t * 0.15;
      }
    }
    else if (id === "anim_05") {
      const g5 = this.scenes["anim_05"];
      if (g5) g5.rotation.y = Math.sin(t * 0.2) * 0.08;
    }
    else if (id === "anim_06") {
      if (this.spheres06) {
        this.spheres06.forEach(s => {
          const swing = Math.sin(t * s.freq) * 0.12;
          s.mesh.position.z = swing;
        });
      }
    }
    else if (id === "anim_07") {
      if (this.beam07) {
        this.beam07.rotation.z = Math.sin(t * 0.8) * 0.08;
      }
    }
    else if (id === "anim_08") {
      if (this.alidada08) {
        this.alidada08.rotation.z = t * 0.15;
      }
    }
    else if (id === "anim_09") {
      if (this.tablets09) {
        this.tablets09.forEach((tb, idx) => {
          const a = tb.userData.angle + t * 0.06;
          tb.position.set(Math.cos(a) * 0.9, 0, Math.sin(a) * 0.9);
          tb.rotation.y = -a + Math.PI / 2;
        });
      }
    }
    else if (id === "anim_10") {
      if (this.heptagon10) this.heptagon10.rotation.y = t * 0.08;
      if (this.ring10) this.ring10.rotation.z = t * 0.1;
    }
    else if (id === "anim_11") {
      if (this.frame11) this.frame11.rotation.z = t * 0.05;
    }
    else if (id === "anim_12") {
      const g12 = this.scenes["anim_12"];
      if (g12) g12.rotation.y = Math.sin(t * 0.3) * 0.06;
    }
    else if (id === "anim_13") {
      if (this.gyroRing13) this.gyroRing13.rotation.z = t * 0.12;
      if (this.quadSpheres13) {
        this.quadSpheres13.forEach((q, idx) => {
          const a = q.angle + t * 0.15;
          q.mesh.position.set(Math.cos(a) * 1.05, Math.sin(a) * 0.3, Math.sin(a) * 1.05);
        });
      }
    }
    else if (id === "anim_14") {
      if (this.dome14) this.dome14.rotation.y = t * 0.05;
      if (this.ribs14) this.ribs14.rotation.y = -t * 0.04;
    }
    else if (id === "anim_15") {
      const g15 = this.scenes["anim_15"];
      if (g15) g15.rotation.y = t * 0.06;
    }
    else if (id === "anim_16") {
      if (this.tensegrity16) this.tensegrity16.rotation.y = t * 0.08;
    }
    else if (id === "anim_17") {
      if (this.prism17) this.prism17.rotation.y = t * 0.1;
    }
    else if (id === "anim_18") {
      if (this.pentGroup18) this.pentGroup18.rotation.z = t * 0.05;
    }
    else if (id === "anim_19") {
      if (this.tower19) this.tower19.rotation.y = t * 0.08;
    }
    else if (id === "anim_20") {
      if (this.medal20) this.medal20.rotation.y = t * 0.12;
    }

    this.renderer.render(this.scene, this.camera);
  }
}

// Exportación global para app.js
window.Presentation3D = Presentation3D;
