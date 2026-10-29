# -*- coding: utf-8 -*-

# Read the current SVG to get defs and polygons
with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'r', encoding='utf-8') as f:
    text = f.read()

p_start = text.find('<g id="poligonos_departamentos">')
p_end = text.find('</g>\n  </g>', p_start)
poligonos = text[p_start:p_end+4]

svg_content = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-90 0 1853 1260" width="100%" height="100%">
  <defs>
    <!-- Filtro de sombra suave para cápsulas y rótulos -->
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.18" />
    </filter>
    <filter id="glow_viedma" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#c89632" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- 1. Fondo de Agua Oceánica (Golfo San Matías y Mar Argentino) -->
  <rect x="-90" y="0" width="1853" height="1260" fill="#e0f2fe" />

  <!-- 2. Capa de Departamentos de la Provincia de Río Negro -->
  <g id="capa_departamentos" transform="translate(112.92857, 24.923532)">
{poligonos}
  </g>

  <!-- 3. Rótulos de Departamentos en COLOR NEGRO (Solicitud de Usuario) -->
  <g id="rotulos_departamentos" style="font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:900;letter-spacing:1.5px;fill:#000000;fill-opacity:0.88;text-anchor:middle;text-transform:uppercase;">
    <text x="730" y="270">Gral. Roca</text>
    <text x="965" y="530">Avellaneda</text>
    <text x="1360" y="520">Pichi Mahuida</text>
    <text x="590" y="530">El Cuy</text>
    <text x="840" y="670">9 de Julio</text>
    <text x="1450" y="710">Conesa</text>
    <text x="1060" y="660">Valcheta</text>
    <text x="1190" y="940">San Antonio</text>
    <text x="1500" y="760">Adolfo Alsina</text>
    <text x="550" y="720">25 de Mayo</text>
    <text x="250" y="800">Pilcaniyeu</text>
    <text x="70" y="1030">Bariloche</text>
    <text x="220" y="1070">Ñorquinco</text>
  </g>

  <!-- 4. Cabeceras Departamentales que no son Nodos (Rojo Bordó Institucional con etiqueta) -->
  <g id="cabeceras_departamentales">
    <!-- General Roca (Cabecera de Gral. Roca) -->
    <g transform="translate(741, 355)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">General Roca</text>
    </g>

    <!-- Choele Choel (Cabecera de Avellaneda) -->
    <g transform="translate(965, 430)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">Choele Choel</text>
    </g>

    <!-- El Cuy (Cabecera de El Cuy) -->
    <g transform="translate(490, 610)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">El Cuy</text>
    </g>

    <!-- San Carlos de Bariloche (Cabecera de Bariloche) -->
    <g transform="translate(60, 930)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">S. C. de Bariloche</text>
    </g>

    <!-- Pilcaniyeu (Cabecera de Pilcaniyeu) -->
    <g transform="translate(195, 920)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">Pilcaniyeu</text>
    </g>

    <!-- Ñorquinco (Cabecera de Ñorquinco) -->
    <g transform="translate(145, 1070)">
      <circle cx="0" cy="0" r="6" fill="#b91c1c" stroke="#ffffff" stroke-width="1.8" />
      <text x="10" y="5" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#7f1d1d;">Ñorquinco</text>
    </g>
  </g>

  <!-- 5. Rótulo Cartográfico del Océano y Golfo San Matías (Ubicado en el agua limpia) -->
  <g id="rotulos_maritimos" transform="translate(1500, 1030)" text-anchor="middle">
    <rect x="-170" y="-35" width="340" height="70" rx="8" fill="#ffffff" fill-opacity="0.82" stroke="#bae6fd" stroke-width="1.5" />
    <text x="0" y="-6" style="font-family:'Segoe UI',Arial,sans-serif;font-size:23px;font-weight:900;letter-spacing:2px;fill:#0369a1;">GOLFO SAN MATÍAS</text>
    <text x="0" y="20" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:1px;fill:#0284c7;">Mar Argentino • Océano Atlántico</text>
  </g>

  <!-- 6. Trazas de Conectividad Territorial (Red Híbrida y Virtual de Nodos) -->
  <g id="red_conectividad" stroke="#0284c7" stroke-width="3.5" stroke-dasharray="10,6" stroke-opacity="0.85" fill="none">
    <!-- Corredor Este-Oeste RN 23: SAO/Las Grutas -> Valcheta -> Ramos Mexia -> Sierra Colorada -> Los Menucos -> Maquinchao -> Ing. Jacobacci -->
    <path d="M 1315,830 L 1080,780 L 910,770 L 770,760 L 610,830 L 495,915 L 395,945" />
    
    <!-- Corredor Costa / Valle RN 3 y RN 250: Viedma -> General Conesa -> San Antonio Oeste / Las Grutas -->
    <path d="M 1560,825 L 1350,670 L 1315,830" />
    
    <!-- Corredor Noreste RN 251 / RN 22: General Conesa -> Río Colorado -->
    <path d="M 1350,670 L 1520,390" />
    
    <!-- Corredor Costa Atlántica Sur RN 3: San Antonio Oeste / Las Grutas -> Sierra Grande -->
    <path d="M 1315,830 L 1240,1040" />
  </g>

  <!-- 7. Placa de Encabezado Institucional y Referencias (Sector Noroeste Limpio) -->
  <g id="header_institucional" transform="translate(25, 30)" filter="url(#shadow)">
    <rect x="0" y="0" width="515" height="360" rx="12" fill="#ffffff" fill-opacity="0.97" stroke="#0f3b7d" stroke-width="2.2" />
    
    <text x="24" y="32" style="font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:900;fill:#0f3b7d;letter-spacing:0.2px;">UNIVERSIDAD NACIONAL DEL COMAHUE</text>
    <text x="24" y="54" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:700;fill:#0369a1;letter-spacing:0.2px;">CURZAS — Sede Central Viedma</text>
    <line x1="24" y1="65" x2="491" y2="65" style="stroke:#c89632;stroke-width:2.5px;stroke-linecap:round;" />
    
    <text x="24" y="88" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#1e293b;">Red Territorial de Nodos Universitarios</text>
    <text x="24" y="106" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;font-style:italic;fill:#475569;">Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)</text>
    
    <line x1="24" y1="118" x2="491" y2="118" style="stroke:#e2e8f0;stroke-width:1.5px;" />
    
    <!-- Ref 1: Sede Central Viedma -->
    <g transform="translate(24, 132)">
      <circle cx="14" cy="10" r="12" fill="#c89632" stroke="#0f2d59" stroke-width="2.5" />
      <text x="14" y="16" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:900;fill:#ffffff;">★</text>
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    </g>
    
    <!-- Ref 2: Nodos Universitarios -->
    <g transform="translate(24, 164)">
      <circle cx="14" cy="10" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
      <circle cx="14" cy="10" r="4.5" fill="#ffffff" />
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0369a1;">Nodos Universitarios (10 Localidades):</text>
    </g>
    
    <!-- Detalle de los 10 Nodos agrupados por región -->
    <g transform="translate(42, 194)">
      <text x="0" y="13" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:700;fill:#1e293b;">• Región Sur (Línea Sur - RN 23):</text>
      <text x="14" y="29" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">Valcheta, Ramos Mexía, Sierra Colorada,</text>
      <text x="14" y="44" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">Los Menucos, Maquinchao e Ing. Jacobacci</text>
      
      <text x="0" y="66" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:700;fill:#1e293b;">• Zona Atlántica y Noreste (RN 3, 250, 251 y 22):</text>
      <text x="14" y="82" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">San Antonio Oeste / Las Grutas, Sierra Grande,</text>
      <text x="14" y="97" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">General Conesa y Río Colorado</text>
    </g>

    <!-- Ref 3: Cabeceras Departamentales y Fuente -->
    <line x1="24" y1="316" x2="491" y2="316" style="stroke:#e2e8f0;stroke-width:1.2px;" />
    
    <g transform="translate(24, 324)">
      <circle cx="8" cy="8" r="5" fill="#b91c1c" stroke="#ffffff" stroke-width="1.5" />
      <text x="22" y="12" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:700;fill:#7f1d1d;">Cabecera Departamental</text>
      <text x="220" y="12" style="font-family:'Segoe UI',Arial,sans-serif;font-size:11.5px;font-style:italic;font-weight:700;fill:#0284c7;">Fuente: Elaboración propia.</text>
    </g>
  </g>

  <!-- 8. Marcadores y Cápsulas de los 10 Nodos Universitarios -->

  <!-- NODO 1: Valcheta (Dpto. Valcheta) -->
  <g id="nodo_valcheta" transform="translate(1080, 780)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="18" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Valcheta</text>
  </g>

  <!-- NODO 2: Ramos Mexía (Dpto. 9 de Julio) -->
  <g id="nodo_ramos_mexia" transform="translate(910, 770)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-70" y="-36" width="140" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Ramos Mexía</text>
  </g>

  <!-- NODO 3: Sierra Colorada (Dpto. 9 de Julio) -->
  <g id="nodo_sierra_colorada" transform="translate(770, 760)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="18" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Colorada</text>
  </g>

  <!-- NODO 4: Los Menucos (Dpto. 25 de Mayo) -->
  <g id="nodo_los_menucos" transform="translate(610, 830)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-70" y="-36" width="140" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Los Menucos</text>
  </g>

  <!-- NODO 5: Maquinchao (Dpto. 25 de Mayo) -->
  <g id="nodo_maquinchao" transform="translate(495, 915)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-65" y="18" width="130" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Maquinchao</text>
  </g>

  <!-- NODO 6: Ingeniero Jacobacci (Dpto. 25 de Mayo) -->
  <g id="nodo_jacobacci" transform="translate(395, 945)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Ing. Jacobacci</text>
  </g>

  <!-- NODO 7: San Antonio Oeste / Las Grutas (Dpto. San Antonio - Costa del Golfo) -->
  <g id="nodo_sao_las_grutas" transform="translate(1315, 830)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2.8" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-140" y="-42" width="250" height="30" rx="6" fill="#ffffff" fill-opacity="0.96" stroke="#0284c7" stroke-width="2" />
    <text x="-15" y="-22" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13.5px;font-weight:800;fill:#0f3b7d;">● San Antonio Oeste / Las Grutas</text>
  </g>

  <!-- NODO 8: Sierra Grande (Dpto. San Antonio - Costa Sur RN 3) -->
  <g id="nodo_sierra_grande" transform="translate(1240, 1040)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-70" y="18" width="140" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Grande</text>
  </g>

  <!-- NODO 9: General Conesa (Dpto. Conesa) -->
  <g id="nodo_conesa" transform="translate(1350, 670)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● General Conesa</text>
  </g>

  <!-- NODO 10: Río Colorado (Dpto. Pichi Mahuida - RN 22) -->
  <g id="nodo_rio_colorado" transform="translate(1520, 390)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-70" y="-36" width="140" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Río Colorado</text>
  </g>

  <!-- 9. SEDE CENTRAL: Viedma (Dpto. Adolfo Alsina) -->
  <g id="sede_viedma" transform="translate(1560, 825)" filter="url(#glow_viedma)">
    <circle cx="0" cy="0" r="20" fill="#c89632" stroke="#0f2d59" stroke-width="3.5" />
    <text x="0" y="8" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:23px;font-weight:900;fill:#ffffff;">★</text>
    <rect x="-140" y="-48" width="280" height="34" rx="6" fill="#0f2d59" stroke="#c89632" stroke-width="2.2" />
    <text x="0" y="-25" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:900;fill:#ffffff;letter-spacing:0.5px;">★ VIEDMA (Sede Central CURZAS)</text>
  </g>

</svg>'''

with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print("MAPA SVG ACTUALIZADO CON DEPARTAMENTOS EN NEGRO, CABECERAS Y ELABORACIÓN PROPIA!")

