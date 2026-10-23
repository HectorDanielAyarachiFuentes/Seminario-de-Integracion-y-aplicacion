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

    // Estado interactivo de usuario (Rotación 360°, Pan y Zoom con mouse o rueda)
    this.userRotation = { x: 0, y: 0 };
    this.targetUserRotation = { x: 0, y: 0 };
    this.userZoom = 0; // offset de distancia con la rueda del mouse
    this.targetUserZoom = 0;
    this.userPan = { x: 0, y: 0 };
    this.targetUserPan = { x: 0, y: 0 };

    this.isDragging = false;
    this.previousPointerPos = { x: 0, y: 0 };
    this.dragButton = 0; // 0 = rotar en 3D, 2 = pan/desplazar

    // Posiciones de cámara cinematográficas y sobrias orientadas hacia la derecha
    // para dejar espacio prioritario a la tarjeta de texto institucional a la izquierda
    this.cameraTargets = {
      anim_01: { pos: [2.3, 1.4, 6.8], lookAt: [1.4, 0.2, 0] },
      anim_02: { pos: [2.2, 1.6, 6.5], lookAt: [1.3, 0.1, 0] },
      anim_03: { pos: [2.4, 1.2, 6.8], lookAt: [1.4, 0.0, 0] },
      anim_04: { pos: [1.8, 3.2, 5.4], lookAt: [1.5, -0.4, 0.1] },
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

    // Controles interactivos de rotación 360°, pan y zoom con mouse o rueda
    this.setupInteractiveControls();

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

  /** Etiqueta 3D tipo Sprite vectorial nítida sobre cualquier perspectiva */
  createLabelSprite(title, subtitle = "", color = "#0f2d59", isMain = false, customScale = null) {
    const canvas = document.createElement("canvas");
    canvas.width = 440;
    canvas.height = 130;
    const ctx = canvas.getContext("2d");

    // Fondo pill académico nítido con marco fino de latón
    const x = 10, y = 10, w = 420, h = 110, r = 20;
    ctx.fillStyle = isMain ? "rgba(255, 255, 255, 0.98)" : "rgba(255, 255, 255, 0.94)";
    ctx.strokeStyle = isMain ? "#b8860b" : "rgba(15, 45, 89, 0.45)";
    ctx.lineWidth = isMain ? 4 : 2.5;

    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r);
    ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h);
    ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r);
    ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    // Texto principal
    ctx.font = isMain ? "bold 26px 'Cinzel', Georgia, serif" : "bold 23px 'Inter', Arial, sans-serif";
    ctx.fillStyle = color;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(title, 220, subtitle ? 48 : 65);

    // Subtítulo
    if (subtitle) {
      ctx.font = "600 16px 'Inter', Arial, sans-serif";
      ctx.fillStyle = isMain ? "#b8860b" : "#475569";
      ctx.fillText(subtitle, 220, 82);
    }

    const texture = new THREE.CanvasTexture(canvas);
    texture.minFilter = THREE.LinearFilter;
    const spriteMat = new THREE.SpriteMaterial({
      map: texture,
      transparent: true,
      depthTest: true,
      depthWrite: false
    });
    const sprite = new THREE.Sprite(spriteMat);
    if (customScale) {
      sprite.scale.set(customScale.x, customScale.y, 1);
    } else {
      sprite.scale.set(isMain ? 0.72 : 0.52, isMain ? 0.22 : 0.16, 1);
    }
    return sprite;
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
  // 4. TERRITORIO: Maqueta Geodésica de la República Argentina y Río Negro
  //    Relieve escultórico nacional en mármol con Río Negro en alto relieve
  //    de latón dorado, las 5 sedes georreferenciadas y arcos de docencia híbrida
  // ──────────────────────────────────────────────────────────────────────────
  buildScene_anim_04(g) {
    this.createMuseumPlinth(g, 1.95, 0.16);

    // Placa oceánica base (Mar Argentino / Cuenca Atlántica)
    const oceanBase = new THREE.Mesh(
      new THREE.CylinderGeometry(1.88, 1.92, 0.04, 64),
      this.graniteMat(0x1e293b)
    );
    oceanBase.position.y = -1.10;
    g.add(oceanBase);

    // ── 1. SILUETA GEOGRÁFICA DE LA REPÚBLICA ARGENTINA (Base Escultórica) ──
    const argShape = new THREE.Shape();
    // Punto de partida: La Quiaca / Jujuy (Norte extremo)
    argShape.moveTo(-0.25, 1.35);
    argShape.lineTo(0.12, 1.15);   // Formosa / Chaco
    argShape.lineTo(0.58, 1.05);   // Misiones (Cataratas del Iguazú)
    argShape.lineTo(0.42, 0.75);   // Corrientes
    argShape.lineTo(0.36, 0.50);   // Entre Ríos
    argShape.lineTo(0.38, 0.35);   // Buenos Aires (Río de la Plata)
    argShape.lineTo(0.60, 0.20);   // Cabo San Antonio
    argShape.lineTo(0.50, 0.05);   // Mar del Plata
    argShape.lineTo(0.30, -0.10);  // Bahía Blanca
    argShape.lineTo(0.36, -0.25);  // Viedma (Desembocadura Río Negro)
    argShape.lineTo(0.24, -0.38);  // Golfo San Matías (Sierra Grande)
    argShape.lineTo(0.34, -0.52);  // Península Valdés (Chubut)
    argShape.lineTo(0.18, -0.78);  // Golfo San Jorge (Comodoro Rivadavia)
    argShape.lineTo(0.14, -1.05);  // Costa de Santa Cruz (Puerto Deseado)
    argShape.lineTo(0.08, -1.30);  // Cabo Vírgenes / Estrecho de Magallanes
    argShape.lineTo(0.05, -1.52);  // Tierra del Fuego (Ushuaia)
    argShape.lineTo(-0.02, -1.62); // Cabo de Hornos
    argShape.lineTo(-0.08, -1.48); // Cordillera Fueguina
    argShape.lineTo(-0.14, -1.15); // Hielos Continentales (Santa Cruz)
    argShape.lineTo(-0.28, -0.68); // Andes de Chubut (Esquel)
    argShape.lineTo(-0.38, -0.36); // Andes de Río Negro (Bariloche / El Bolsón)
    argShape.lineTo(-0.40, -0.12); // Andes de Neuquén
    argShape.lineTo(-0.42, 0.32);  // Andes de Mendoza (Aconcagua)
    argShape.lineTo(-0.38, 0.65);  // Andes de San Juan y La Rioja
    argShape.lineTo(-0.34, 1.00);  // Puna de Catamarca y Salta
    argShape.lineTo(-0.30, 1.28);  // Puna de Jujuy (Paso de Jama)
    argShape.closePath();

    const argExtrudeOpts = {
      depth: 0.08,
      bevelEnabled: true,
      bevelThickness: 0.018,
      bevelSize: 0.016,
      bevelSegments: 3
    };
    const argGeo = new THREE.ExtrudeGeometry(argShape, argExtrudeOpts);
    const argMesh = new THREE.Mesh(argGeo, this.marbleMat(0xf1efe8));
    argMesh.rotation.x = -Math.PI / 2;
    argMesh.position.set(0, -1.08, 0);
    g.add(argMesh);

    // Contorno sutil de latón en la costa argentina
    const argEdges = new THREE.LineSegments(
      new THREE.EdgesGeometry(argGeo, 28),
      new THREE.LineBasicMaterial({ color: 0xb8860b, transparent: true, opacity: 0.45 })
    );
    argMesh.add(argEdges);

    // ── 1.B. PLATAFORMA CONTINENTAL ARGENTINA (Soberanía Submarina y Talud del Mar Argentino) ──
    const shelfShape = new THREE.Shape();
    shelfShape.moveTo(0.38, 0.35);  // Frente al Río de la Plata
    shelfShape.lineTo(0.72, 0.18);  // Talud frente a Provincia de Buenos Aires
    shelfShape.lineTo(0.68, -0.15); // Talud exterior del Mar Argentino
    shelfShape.lineTo(0.62, -0.45); // Frente al Golfo San Matías y Península Valdés
    shelfShape.lineTo(0.66, -0.85); // Cuenca Marina Austral
    shelfShape.lineTo(0.70, -1.12); // Meseta submarina de Malvinas (Este)
    shelfShape.lineTo(0.64, -1.34); // Banco Burdwood / Namuncurá (Sur)
    shelfShape.lineTo(0.25, -1.45); // Litoral del Pasaje de Drake
    shelfShape.lineTo(0.05, -1.52); // Tierra del Fuego
    shelfShape.lineTo(0.08, -1.30); // Costa de Santa Cruz
    shelfShape.lineTo(0.14, -1.05);
    shelfShape.lineTo(0.18, -0.78); // Golfo San Jorge
    shelfShape.lineTo(0.34, -0.52); // Península Valdés
    shelfShape.lineTo(0.24, -0.38); // Golfo San Matías
    shelfShape.lineTo(0.36, -0.25); // Desembocadura del Río Negro
    shelfShape.lineTo(0.30, -0.10);
    shelfShape.lineTo(0.50, 0.05);  // Mar del Plata
    shelfShape.lineTo(0.60, 0.20);
    shelfShape.closePath();

    const shelfGeo = new THREE.ExtrudeGeometry(shelfShape, {
      depth: 0.025,
      bevelEnabled: true,
      bevelThickness: 0.008,
      bevelSize: 0.008,
      bevelSegments: 2
    });
    const shelfMat = new THREE.MeshStandardMaterial({
      color: 0x0284c7,
      roughness: 0.32,
      metalness: 0.15,
      transparent: true,
      opacity: 0.35
    });
    const shelfMesh = new THREE.Mesh(shelfGeo, shelfMat);
    shelfMesh.rotation.x = -Math.PI / 2;
    shelfMesh.position.set(0, -1.096, 0);
    g.add(shelfMesh);

    // Límite exterior de la Plataforma Continental (Borde celeste náutico de soberanía marítima)
    const shelfEdges = new THREE.LineSegments(
      new THREE.EdgesGeometry(shelfGeo, 24),
      new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.65 })
    );
    shelfMesh.add(shelfEdges);

    // ── 1.C. ISLAS MALVINAS (Soberanía Argentina • Isla Gran Malvina e Isla Soledad) ──
    // 1. Isla Gran Malvina (Oeste)
    const gmShape = new THREE.Shape();
    gmShape.moveTo(0.39, -1.15);
    gmShape.lineTo(0.43, -1.13);
    gmShape.lineTo(0.46, -1.16);
    gmShape.lineTo(0.47, -1.21);
    gmShape.lineTo(0.44, -1.26);
    gmShape.lineTo(0.40, -1.25);
    gmShape.lineTo(0.38, -1.20);
    gmShape.closePath();

    // 2. Isla Soledad (Este, con Istmo de Darwin y Lafonia)
    const isShape = new THREE.Shape();
    isShape.moveTo(0.49, -1.13);
    isShape.lineTo(0.56, -1.12);
    isShape.lineTo(0.59, -1.16); // Puerto Argentino
    isShape.lineTo(0.54, -1.20); // Istmo de Darwin
    isShape.lineTo(0.57, -1.25); // Lafonia
    isShape.lineTo(0.53, -1.28);
    isShape.lineTo(0.49, -1.24);
    isShape.lineTo(0.51, -1.18);
    isShape.closePath();

    // 3. Isla de los Estados (al este de Tierra del Fuego)
    const ieShape = new THREE.Shape();
    ieShape.moveTo(0.12, -1.53);
    ieShape.lineTo(0.19, -1.51);
    ieShape.lineTo(0.22, -1.54);
    ieShape.lineTo(0.14, -1.56);
    ieShape.closePath();

    const malvinasExtrudeOpts = {
      depth: 0.075,
      bevelEnabled: true,
      bevelThickness: 0.016,
      bevelSize: 0.014,
      bevelSegments: 3
    };

    const gmGeo = new THREE.ExtrudeGeometry(gmShape, malvinasExtrudeOpts);
    const isGeo = new THREE.ExtrudeGeometry(isShape, malvinasExtrudeOpts);
    const ieGeo = new THREE.ExtrudeGeometry(ieShape, { depth: 0.06, bevelEnabled: true, bevelThickness: 0.01, bevelSize: 0.01 });

    const gmMesh = new THREE.Mesh(gmGeo, this.marbleMat(0xfdfbf7));
    const isMesh = new THREE.Mesh(isGeo, this.marbleMat(0xfdfbf7));
    const ieMesh = new THREE.Mesh(ieGeo, this.marbleMat(0xfdfbf7));

    gmMesh.rotation.x = -Math.PI / 2;
    gmMesh.position.set(0, -1.08, 0);
    isMesh.rotation.x = -Math.PI / 2;
    isMesh.position.set(0, -1.08, 0);
    ieMesh.rotation.x = -Math.PI / 2;
    ieMesh.position.set(0, -1.08, 0);

    // Contorno de latón bruñido de soberanía nacional
    const gmEdges = new THREE.LineSegments(
      new THREE.EdgesGeometry(gmGeo, 20),
      new THREE.LineBasicMaterial({ color: 0xd4af37, linewidth: 2 })
    );
    gmMesh.add(gmEdges);

    const isEdges = new THREE.LineSegments(
      new THREE.EdgesGeometry(isGeo, 20),
      new THREE.LineBasicMaterial({ color: 0xd4af37, linewidth: 2 })
    );
    isMesh.add(isEdges);

    g.add(gmMesh);
    g.add(isMesh);
    g.add(ieMesh);

    // Faro / Baliza de Soberanía en Puerto Argentino (Isla Soledad)
    const paBeacon = new THREE.Group();
    const paPin = new THREE.Mesh(
      new THREE.CylinderGeometry(0.007, 0.010, 0.05, 12),
      this.brassMat(0xd4af37)
    );
    paPin.position.set(0.575, -0.98, 1.15);
    paBeacon.add(paPin);

    const paGem = new THREE.Mesh(
      new THREE.SphereGeometry(0.018, 16, 16),
      this.glassMat(0x38bdf8, { roughness: 0.1, transmission: 0.9 })
    );
    paGem.position.set(0.575, -0.945, 1.15);
    paBeacon.add(paGem);

    const paHalo = new THREE.Mesh(
      new THREE.TorusGeometry(0.024, 0.0025, 8, 16),
      this.brassMat()
    );
    paHalo.rotation.x = Math.PI / 2;
    paHalo.position.set(0.575, -0.945, 1.15);
    paBeacon.add(paHalo);

    const paLight = new THREE.PointLight(0x38bdf8, 0.8, 0.9);
    paLight.position.set(0.575, -0.94, 1.15);
    paBeacon.add(paLight);
    g.add(paBeacon);

    // Etiqueta Cartográfica de las Islas Malvinas
    const malvinasLabel = this.createLabelSprite(
      "ISLAS MALVINAS",
      "Soberanía Argentina • Atlántico Sur",
      "#0f2d59",
      true,
      { x: 0.65, y: 0.18 }
    );
    malvinasLabel.position.set(0.68, -0.72, 1.22);
    g.add(malvinasLabel);

    // Hilo conductor de latón hacia Puerto Argentino
    const malvinasLeaderGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(0.575, -0.94, 1.15),
      new THREE.Vector3(0.68, -0.78, 1.22)
    ]);
    const malvinasLeaderLine = new THREE.Line(
      malvinasLeaderGeo,
      new THREE.LineBasicMaterial({ color: 0xb8860b, transparent: true, opacity: 0.65 })
    );
    g.add(malvinasLeaderLine);

    // ── 1.D. MAR ARGENTINO Y OCÉANO ATLÁNTICO SUR (Rótulo Náutico y Ondas de Relieve) ──
    const marArgLabel = this.createLabelSprite(
      "MAR ARGENTINO",
      "Océano Atlántico Sur • Plataforma Continental",
      "#0284c7",
      false,
      { x: 0.70, y: 0.17 }
    );
    marArgLabel.position.set(0.72, -0.90, 0.68);
    g.add(marArgLabel);

    // Aro exterior náutico de latón pulido sobre la placa oceánica
    const oceanRim = new THREE.Mesh(
      new THREE.TorusGeometry(1.90, 0.012, 16, 64),
      this.brassMat(0xd4af37)
    );
    oceanRim.rotation.x = Math.PI / 2;
    oceanRim.position.y = -1.09;
    g.add(oceanRim);

    // ── 2. PROVINCIA DE RÍO NEGRO (Protagonista en Alto Relieve de Latón Dorado) ──
    const rnShape = new THREE.Shape();
    rnShape.moveTo(-0.26, -0.12);  // Noroeste: Catriel / Río Colorado
    rnShape.lineTo(0.08, -0.14);   // Norte: Curso Río Colorado / Valle Medio
    rnShape.lineTo(0.28, -0.18);   // Noreste: Guardia Mitre
    rnShape.lineTo(0.36, -0.25);   // Este: Viedma / El Cóndor (Desembocadura)
    rnShape.lineTo(0.25, -0.33);   // Sudeste: San Antonio Oeste / Las Grutas
    rnShape.lineTo(0.23, -0.42);   // Sudeste: Sierra Grande / Paralelo 42° costa
    rnShape.lineTo(-0.36, -0.42);  // Sur: Paralelo 42° S (Límite recto con Chubut)
    rnShape.lineTo(-0.38, -0.38);  // Sudoeste: El Bolsón / Cordillera
    rnShape.lineTo(-0.34, -0.28);  // Oeste: Bariloche / Lago Nahuel Huapi
    rnShape.lineTo(-0.24, -0.19);  // Noroeste: Río Limay / Confluencia Cipolletti
    rnShape.closePath();

    const rnExtrudeOpts = {
      depth: 0.12,
      bevelEnabled: true,
      bevelThickness: 0.02,
      bevelSize: 0.015,
      bevelSegments: 3
    };
    const rnGeo = new THREE.ExtrudeGeometry(rnShape, rnExtrudeOpts);
    const rnMesh = new THREE.Mesh(rnGeo, this.brassMat(0xd4af37));
    rnMesh.rotation.x = -Math.PI / 2;
    rnMesh.position.set(0, -1.00, 0);
    g.add(rnMesh);

    // Contorno biselado de oro brillante para Río Negro
    const rnEdges = new THREE.LineSegments(
      new THREE.EdgesGeometry(rnGeo, 20),
      new THREE.LineBasicMaterial({ color: 0xffe082, linewidth: 2 })
    );
    rnMesh.add(rnEdges);

    // Curso fluvial estilizado del Río Negro (cristal azul cerúleo)
    const riverCurve = new THREE.CatmullRomCurve3([
      new THREE.Vector3(-0.24, -0.87, 0.19),
      new THREE.Vector3(-0.06, -0.87, 0.20),
      new THREE.Vector3(0.12, -0.87, 0.22),
      new THREE.Vector3(0.26, -0.87, 0.24),
      new THREE.Vector3(0.36, -0.87, 0.25)
    ]);
    const riverGeo = new THREE.TubeGeometry(riverCurve, 24, 0.01, 6, false);
    const riverMesh = new THREE.Mesh(riverGeo, this.glassMat(0x0284c7));
    g.add(riverMesh);

    // Traza de la Ruta Nacional 23 (Eje de la Línea Sur en latón bruñido)
    const routeCurve = new THREE.CatmullRomCurve3([
      new THREE.Vector3(0.36, -0.872, 0.25),   // Viedma
      new THREE.Vector3(0.14, -0.872, 0.31),   // Valcheta
      new THREE.Vector3(0.00, -0.872, 0.32),   // Ramos Mexía
      new THREE.Vector3(-0.14, -0.872, 0.33),  // Los Menucos
      new THREE.Vector3(-0.34, -0.872, 0.28)   // Bariloche
    ]);
    const routeGeo = new THREE.TubeGeometry(routeCurve, 32, 0.007, 6, false);
    const routeMesh = new THREE.Mesh(routeGeo, this.brassMat(0xb8860b));
    g.add(routeMesh);

    // ── 3. LAS SEDES Y NODOS DEL CURZAS (Georreferenciadas con Balizas Geodésicas) ──
    const sedesData = [
      {
        nombre: "VIEDMA",
        tipo: "★ SEDE CENTRAL",
        subtitulo: "CURZAS-UNCo • Rectorado",
        x: 0.36, z: 0.25,
        isCabecera: true,
        colorGem: 0xffd700,
        labelPos: { x: 0.44, y: -0.36, z: 0.14 } // Al Este sobre el Océano Atlántico
      },
      {
        nombre: "Nodo Valcheta",
        tipo: "Portal Línea Sur",
        subtitulo: "Aula Híbrida",
        x: 0.14, z: 0.31,
        isCabecera: false,
        colorGem: 0x0284c7,
        labelPos: { x: 0.14, y: -0.46, z: 0.15 } // Al Norte de la Ruta Nacional 23
      },
      {
        nombre: "Nodo Ramos Mexía",
        tipo: "Línea Sur Alta",
        subtitulo: "Sincronía Digital",
        x: 0.00, z: 0.32,
        isCabecera: false,
        colorGem: 0x38bdf8,
        labelPos: { x: -0.02, y: -0.62, z: 0.48 } // Al Sur de la Ruta Nacional 23
      },
      {
        nombre: "Nodo Los Menucos",
        tipo: "Sur Central",
        subtitulo: "Entornos Moodle",
        x: -0.14, z: 0.33,
        isCabecera: false,
        colorGem: 0x10b981,
        labelPos: { x: -0.28, y: -0.44, z: 0.20 } // Al Oeste hacia Bariloche
      },
      {
        nombre: "Nodo Sierra Grande",
        tipo: "Costa Atlántica",
        subtitulo: "Tutorías Remotas",
        x: 0.23, z: 0.41,
        isCabecera: false,
        colorGem: 0xf59e0b,
        labelPos: { x: 0.35, y: -0.58, z: 0.52 } // Al Sudeste sobre el Golfo San Matías
      }
    ];

    const viedmaBeaconPos = new THREE.Vector3(0.36, -0.58, 0.25);
    this.nodeCurves04 = [];
    this.nodePulses04 = [];

    sedesData.forEach((sede) => {
      const pinGroup = new THREE.Group();

      if (sede.isCabecera) {
        // ── Sede Central Viedma (Monumento Clásico de Latón y Mármol) ──
        const step1 = new THREE.Mesh(
          new THREE.CylinderGeometry(0.07, 0.09, 0.022, 24),
          this.brassMat()
        );
        step1.position.y = -0.865;
        pinGroup.add(step1);

        const step2 = new THREE.Mesh(
          new THREE.CylinderGeometry(0.05, 0.055, 0.016, 24),
          this.marbleMat()
        );
        step2.position.y = -0.846;
        pinGroup.add(step2);

        // Estela esbelta arquitectónica
        const stela = new THREE.Mesh(
          new THREE.CylinderGeometry(0.022, 0.026, 0.24, 20),
          this.marbleMat(0xfdfbf7)
        );
        stela.position.y = -0.72;
        pinGroup.add(stela);

        // Aros de collar de latón
        const collar = new THREE.Mesh(
          new THREE.TorusGeometry(0.029, 0.0035, 12, 24),
          this.brassMat()
        );
        collar.rotation.x = Math.PI / 2;
        collar.position.y = -0.61;
        pinGroup.add(collar);

        // Orbe y Esfera Armilar Giratoria de Viedma
        const orb = new THREE.Mesh(
          new THREE.SphereGeometry(0.042, 24, 24),
          this.brassMat(0xffd700)
        );
        orb.position.y = -0.58;
        pinGroup.add(orb);

        const armRing = new THREE.Group();
        const r1 = new THREE.Mesh(
          new THREE.TorusGeometry(0.075, 0.005, 16, 36),
          this.brassMat()
        );
        const r2 = new THREE.Mesh(
          new THREE.TorusGeometry(0.075, 0.005, 16, 36),
          this.brassMat()
        );
        r2.rotation.x = Math.PI / 2;
        armRing.add(r1);
        armRing.add(r2);
        armRing.position.y = -0.58;
        pinGroup.add(armRing);
        this.viedmaRing04 = armRing;

        const beaconLight = new THREE.PointLight(0xffd700, 1.4, 2.2);
        beaconLight.position.y = -0.56;
        pinGroup.add(beaconLight);

      } else {
        // ── Nodos Territoriales (Monolitos Geodésicos de Precisión - Sin aspecto de velas) ──
        const base = new THREE.Mesh(
          new THREE.CylinderGeometry(0.038, 0.046, 0.016, 20),
          this.brassMat(0xd4af37)
        );
        base.position.y = -0.87;
        pinGroup.add(base);

        // Aguja vertical de latón
        const mast = new THREE.Mesh(
          new THREE.CylinderGeometry(0.006, 0.006, 0.14, 12),
          this.brassMat()
        );
        mast.position.y = -0.79;
        pinGroup.add(mast);

        // Gema óptica cristalina iluminada
        const gem = new THREE.Mesh(
          new THREE.SphereGeometry(0.026, 20, 20),
          this.glassMat(sede.colorGem, { roughness: 0.08, transmission: 0.85 })
        );
        gem.position.y = -0.71;
        pinGroup.add(gem);

        // Halo horizontal de latón
        const ring = new THREE.Mesh(
          new THREE.TorusGeometry(0.036, 0.0035, 12, 24),
          this.brassMat()
        );
        ring.rotation.x = Math.PI / 2;
        ring.position.y = -0.71;
        pinGroup.add(ring);

        const nodeLight = new THREE.PointLight(sede.colorGem, 0.7, 1.2);
        nodeLight.position.y = -0.70;
        pinGroup.add(nodeLight);

        // ── 4. ARCOS PARABÓLICOS DE TRANSMISIÓN DE DOCENCIA HÍBRIDA (Res. 196/2022) ──
        const nodeTarget = new THREE.Vector3(sede.x, -0.71, sede.z);
        const dist = viedmaBeaconPos.distanceTo(nodeTarget);
        const midPoint = new THREE.Vector3().addVectors(viedmaBeaconPos, nodeTarget).multiplyScalar(0.5);
        // Altura parabólica estratificada y armoniosa proporcional a la distancia
        midPoint.y = -0.58 + dist * 0.72;

        const arcCurve = new THREE.QuadraticBezierCurve3(
          viedmaBeaconPos,
          midPoint,
          nodeTarget
        );
        const arcGeo = new THREE.TubeGeometry(arcCurve, 36, 0.0042, 8, false);
        const arcMesh = new THREE.Mesh(
          arcGeo,
          new THREE.MeshStandardMaterial({
            color: 0xe6b800,
            roughness: 0.15,
            metalness: 0.85,
            emissive: 0x996515,
            emissiveIntensity: 0.25
          })
        );
        g.add(arcMesh);

        // Pulso fotónico de datos / clase sincrónica
        const pulse = new THREE.Mesh(
          new THREE.SphereGeometry(0.014, 16, 16),
          new THREE.MeshBasicMaterial({ color: 0xfffad0 })
        );
        pulse.position.copy(nodeTarget);
        g.add(pulse);

        this.nodeCurves04.push(arcCurve);
        this.nodePulses04.push(pulse);
      }

      pinGroup.position.set(sede.x, 0, sede.z);
      g.add(pinGroup);

      // ── ETIQUETA ESCALONADA CON HILO GUÍA DE LATÓN (CERO SUPERPOSICIONES) ──
      const label = this.createLabelSprite(
        sede.nombre,
        sede.tipo,
        sede.isCabecera ? "#996515" : "#0f2d59",
        sede.isCabecera,
        sede.isCabecera ? { x: 0.65, y: 0.20 } : { x: 0.48, y: 0.15 }
      );
      label.position.set(sede.labelPos.x, sede.labelPos.y, sede.labelPos.z);
      g.add(label);

      // Trazador geodésico de latón (línea sutil que une la etiqueta flotante con la base del nodo)
      const pinTop = new THREE.Vector3(sede.x, sede.isCabecera ? -0.54 : -0.68, sede.z);
      const labelAnchor = new THREE.Vector3(sede.labelPos.x, sede.labelPos.y - 0.06, sede.labelPos.z);
      const leaderGeo = new THREE.BufferGeometry().setFromPoints([pinTop, labelAnchor]);
      const leaderLine = new THREE.Line(
        leaderGeo,
        new THREE.LineBasicMaterial({ color: 0xb8860b, transparent: true, opacity: 0.55 })
      );
      g.add(leaderLine);
    });

    // ── 5. ROSA DE LOS VIENTOS Y CARTELA CARTOGRÁFICA EN EL BORDE OCEÁNICO ──
    const compassGroup = new THREE.Group();
    compassGroup.position.set(0.78, -1.07, 0.28);

    const compRing = new THREE.Mesh(
      new THREE.RingGeometry(0.16, 0.19, 32),
      this.brassMat()
    );
    compRing.rotation.x = -Math.PI / 2;
    compassGroup.add(compRing);

    const starGeom = new THREE.ConeGeometry(0.05, 0.22, 4);
    const needleN = new THREE.Mesh(starGeom, this.brassMat(0xd4af37));
    needleN.rotation.x = Math.PI / 2;
    compassGroup.add(needleN);
    this.compassNeedle04 = needleN;

    const needleS = new THREE.Mesh(starGeom, this.graniteMat());
    needleS.rotation.x = -Math.PI / 2;
    compassGroup.add(needleS);

    g.add(compassGroup);

    // Cartela institucional integrada en el pedestal granítico (zócalo sur bajo Tierra del Fuego)
    const cartela = this.createLabelSprite(
      "RED DE NODOS CURZAS",
      "Res. CD-CURZA N° 196/2022 • Docencia Híbrida",
      "#0f2d59",
      false,
      { x: 0.62, y: 0.18 }
    );
    cartela.position.set(0.10, -1.02, 1.68);
    g.add(cartela);
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
     SISTEMA DE INTERACCIÓN 3D: ROTACIÓN 360°, PAN Y ZOOM CON MOUSE / RUEDA
     ═══════════════════════════════════════════════════════════════════════════ */
  setupInteractiveControls() {
    this.canvas.style.cursor = "grab";

    // 1. Zoom Progresivo con la Rueda del Mouse sobre el lienzo 3D
    this.canvas.addEventListener("wheel", (e) => {
      e.preventDefault();
      // Scroll hacia abajo aleja la cámara, scroll hacia arriba acerca la cámara al objeto
      const zoomSpeed = 0.0035;
      this.targetUserZoom = Math.max(-4.2, Math.min(6.5, this.targetUserZoom + e.deltaY * zoomSpeed));
    }, { passive: false });

    // 2. Clic y Arrastre con Mouse o Toque (Rotación libre 360° y Desplazamiento Pan)
    this.canvas.addEventListener("pointerdown", (e) => {
      this.isDragging = true;
      this.dragButton = e.button;
      this.previousPointerPos = { x: e.clientX, y: e.clientY };
      this.canvas.style.cursor = "grabbing";
      try {
        this.canvas.setPointerCapture(e.pointerId);
      } catch (_) {}
    });

    window.addEventListener("pointermove", (e) => {
      if (!this.isDragging) return;

      const deltaX = e.clientX - this.previousPointerPos.x;
      const deltaY = e.clientY - this.previousPointerPos.y;
      this.previousPointerPos = { x: e.clientX, y: e.clientY };

      if (this.dragButton === 0 && !e.shiftKey) {
        // Clic izquierdo: Rotación orbital del objeto 3D en 360°
        this.targetUserRotation.y += deltaX * 0.009;
        // Inclinación vertical (pitch) suave
        this.targetUserRotation.x = Math.max(-0.85, Math.min(0.85, this.targetUserRotation.x + deltaY * 0.007));
      } else {
        // Clic secundario (derecho) o Shift + Clic: Desplazamiento (Pan)
        this.targetUserPan.x += deltaX * 0.0045;
        this.targetUserPan.y -= deltaY * 0.0045;
      }
    });

    const stopDragging = (e) => {
      if (this.isDragging) {
        this.isDragging = false;
        this.canvas.style.cursor = "grab";
        try {
          this.canvas.releasePointerCapture(e.pointerId);
        } catch (_) {}
      }
    };

    window.addEventListener("pointerup", stopDragging);
    window.addEventListener("pointercancel", stopDragging);

    // 3. Doble clic en el fondo: recentrar suavemente al ángulo inicial de la filmina
    this.canvas.addEventListener("dblclick", () => {
      this.resetUserControls();
    });

    // Desactivar menú contextual para permitir pan libre con clic secundario
    this.canvas.addEventListener("contextmenu", (e) => e.preventDefault());
  }

  resetUserControls() {
    this.targetUserRotation.x = 0;
    this.targetUserRotation.y = 0;
    this.targetUserZoom = 0;
    this.targetUserPan.x = 0;
    this.targetUserPan.y = 0;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     TRANSICIÓN CINEMATOGRÁFICA Y CONTROL DE CÁMARA
     ═══════════════════════════════════════════════════════════════════════════ */
  switchScene(newSceneId) {
    if (this.currentSceneId === newSceneId) return;

    const oldG = this.scenes[this.currentSceneId];
    const newG = this.scenes[newSceneId];

    if (oldG) {
      oldG.visible = false;
      oldG.rotation.set(0, 0, 0);
      oldG.position.set(1.6, 0, 0);
    }
    if (newG) {
      newG.visible = true;
      newG.rotation.set(0, 0, 0);
      newG.position.set(1.6, 0, 0);
    }

    this.currentSceneId = newSceneId;
    this.resetUserControls();

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

    // 1. Amortiguación e interpolación suave (Lerp) de las órdenes del usuario
    this.userRotation.x += (this.targetUserRotation.x - this.userRotation.x) * 0.08;
    this.userRotation.y += (this.targetUserRotation.y - this.userRotation.y) * 0.08;
    this.userZoom += (this.targetUserZoom - this.userZoom) * 0.08;
    this.userPan.x += (this.targetUserPan.x - this.userPan.x) * 0.08;
    this.userPan.y += (this.targetUserPan.y - this.userPan.y) * 0.08;

    // 2. Zoom Progresivo con Rueda: Dolly de la cámara respecto al objeto
    const camDir = new THREE.Vector3().subVectors(this.targetCamPos, this.targetLookAt).normalize();
    const baseDist = this.targetCamPos.distanceTo(this.targetLookAt);
    const effectiveDist = Math.max(2.2, Math.min(12.5, baseDist + this.userZoom));

    const desiredCamPos = new THREE.Vector3()
      .copy(this.targetLookAt)
      .addScaledVector(camDir, effectiveDist);

    desiredCamPos.x += this.userPan.x;
    desiredCamPos.y += this.userPan.y;

    const desiredLookAt = new THREE.Vector3()
      .copy(this.targetLookAt)
      .add(new THREE.Vector3(this.userPan.x, this.userPan.y, 0));

    this.currentCamPos.lerp(desiredCamPos, 0.045);
    this.currentLookAt.lerp(desiredLookAt, 0.045);
    this.camera.position.copy(this.currentCamPos);
    this.camera.lookAt(this.currentLookAt);

    // 3. Motes dorados de polvo en lenta deriva atmosférica
    if (this.dustParticles) {
      this.dustParticles.rotation.y = t * 0.006;
    }

    // 4. Aplicar rotación orbital y desplazamiento interactivo a la escultura 3D activa
    const activeGroup = this.scenes[this.currentSceneId];
    if (activeGroup) {
      activeGroup.position.x = 1.6 + this.userPan.x;
      activeGroup.position.y = this.userPan.y;
      activeGroup.rotation.y = this.userRotation.y;
      activeGroup.rotation.x = this.userRotation.x;
    }

    // 5. Micro-rotación lenta y solemne de cada escultura según la escena activa
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
      if (this.viedmaRing04) {
        this.viedmaRing04.rotation.y = t * 0.45;
        this.viedmaRing04.rotation.x = Math.sin(t * 0.3) * 0.2;
      }
      if (this.nodePulses04 && this.nodeCurves04) {
        this.nodePulses04.forEach((pulse, idx) => {
          const curve = this.nodeCurves04[idx];
          if (curve) {
            const prog = (t * 0.35 + idx * 0.25) % 1.0;
            pulse.position.copy(curve.getPoint(prog));
          }
        });
      }
      if (this.compassNeedle04) {
        this.compassNeedle04.rotation.z = Math.sin(t * 0.5) * 0.04;
      }
      const g4 = this.scenes["anim_04"];
      if (g4) {
        g4.rotation.y = this.userRotation.y + Math.sin(t * 0.12) * 0.04;
        g4.rotation.x = this.userRotation.x;
      }
    }
    else if (id === "anim_05") {
      const g5 = this.scenes["anim_05"];
      if (g5) {
        g5.rotation.y = this.userRotation.y + Math.sin(t * 0.2) * 0.08;
        g5.rotation.x = this.userRotation.x;
      }
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
      if (g12) {
        g12.rotation.y = this.userRotation.y + Math.sin(t * 0.3) * 0.06;
        g12.rotation.x = this.userRotation.x;
      }
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
      if (g15) {
        g15.rotation.y = this.userRotation.y + t * 0.06;
        g15.rotation.x = this.userRotation.x;
      }
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
