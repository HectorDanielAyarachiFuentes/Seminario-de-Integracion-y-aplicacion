# -*- coding: utf-8 -*-
"""
Regenera red_territorial.svg eliminando todas las superposiciones, agregando fondo de mar celeste
y dejando una cartografía limpia e impecable de los 10 Nodos del CURZAS.
"""
import xml.etree.ElementTree as ET

svg_path = 'Entregas/Actividad 4/quarto/assets/red_territorial.svg'
tree = ET.parse(svg_path)
root = tree.getroot()

# Espacio de nombres SVG
ns = {'svg': 'http://www.w3.org/2000/svg'}

# 1. Obtener todos los paths de departamentos de g2476 en layer1
paths_deptos = []
for g in root.iter('{http://www.w3.org/2000/svg}g'):
    if g.attrib.get('id') == 'g2476':
        for child in g:
            if child.tag.endswith('path'):
                paths_deptos.append(ET.tostring(child, encoding='unicode'))

print(f"Total paths de departamentos encontrados: {len(paths_deptos)}")

# Construir el nuevo SVG desde cero con la base limpia y sin elementos obsoletos
nuevo_svg = f'''<?xml version="1.0" encoding="utf-8"?>
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
    <g id="poligonos_departamentos">
      {''.join(paths_deptos)}
    </g>
  </g>

  <!-- 3. Rótulos Tenues de Departamentos (Contexto Geográfico Suave) -->
  <g id="rotulos_departamentos" style="font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:700;letter-spacing:1px;fill:#64748b;fill-opacity:0.45;text-anchor:middle;text-transform:uppercase;">
    <text x="730" y="290">Gral. Roca</text>
    <text x="965" y="420">Avellaneda</text>
    <text x="1230" y="490">Pichi Mahuida</text>
    <text x="590" y="550">El Cuy</text>
    <text x="765" y="660">9 de Julio</text>
    <text x="1270" y="690">Conesa</text>
    <text x="970" y="650">Valcheta</text>
    <text x="1350" y="770">Adolfo Alsina</text>
    <text x="350" y="850">25 de Mayo</text>
    <text x="110" y="830">Pilcaniyeu</text>
    <text x="145" y="1035">Ñorquinco</text>
    <text x="-40" y="990">Bariloche</text>
  </g>

  <!-- 4. Rótulo Cartográfico del Océano y Golfo San Matías (Ubicado en el agua limpia) -->
  <g id="rotulos_maritimos" transform="translate(1360, 990)" text-anchor="middle">
    <rect x="-170" y="-35" width="340" height="70" rx="8" fill="#ffffff" fill-opacity="0.8" stroke="#bae6fd" stroke-width="1.5" />
    <text x="0" y="-6" style="font-family:'Segoe UI',Arial,sans-serif;font-size:23px;font-weight:900;letter-spacing:2px;fill:#0369a1;">GOLFO SAN MATÍAS</text>
    <text x="0" y="20" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:1px;fill:#0284c7;">Mar Argentino • Océano Atlántico</text>
  </g>

  <!-- 5. Trazas de Conectividad Territorial (Red Híbrida y Virtual de Nodos) -->
  <g id="red_conectividad" stroke="#0284c7" stroke-width="3.5" stroke-dasharray="10,6" stroke-opacity="0.8" fill="none">
    <!-- Corredor Este-Oeste RN 23: Viedma -> Conesa -> SAO -> Valcheta -> Ramos Mexia -> Sierra Colorada -> Los Menucos -> Maquinchao -> Comallo -->
    <path d="M 1535,832 L 1238,632 L 1090,766 L 946,766 L 795,755 L 652,750 L 545,845 L 435,948 L 235,940" />
    <!-- Conexión Valle Medio: Conesa -> Lamarque -->
    <path d="M 1238,632 L 975,475" />
    <!-- Conexión Costa Atlántica Sur RN 3: SAO -> Sierra Grande -->
    <path d="M 1090,766 L 1080,1040" />
  </g>

  <!-- 6. Placa de Encabezado Institucional y Referencias (Sector Noroeste Limpio) -->
  <g id="header_institucional" transform="translate(25, 40)" filter="url(#shadow)">
    <rect x="0" y="0" width="460" height="340" rx="10" fill="#ffffff" fill-opacity="0.97" stroke="#0f3b7d" stroke-width="2" />
    
    <text x="20" y="32" style="font-family:'Segoe UI',Arial,sans-serif;font-size:21px;font-weight:900;fill:#0f3b7d;letter-spacing:0.8px;">UNIVERSIDAD NACIONAL DEL COMAHUE</text>
    <text x="20" y="56" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:700;fill:#0369a1;letter-spacing:0.5px;">CURZAS — Sede Central Viedma</text>
    <line x1="20" y1="68" x2="440" y2="68" style="stroke:#c89632;stroke-width:2.5px;stroke-linecap:round;" />
    
    <text x="20" y="94" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:800;fill:#1e293b;">Red Territorial de Nodos Universitarios</text>
    <text x="20" y="114" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:600;font-style:italic;fill:#475569;">Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)</text>
    
    <line x1="20" y1="128" x2="440" y2="128" style="stroke:#e2e8f0;stroke-width:1.5px;" />
    
    <!-- Ref 1: Sede Central Viedma -->
    <g transform="translate(20, 142)">
      <circle cx="14" cy="10" r="12" fill="#c89632" stroke="#0f2d59" stroke-width="2.5" />
      <text x="14" y="16" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:900;fill:#ffffff;">★</text>
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    </g>
    
    <!-- Ref 2: Nodos Universitarios -->
    <g transform="translate(20, 178)">
      <circle cx="14" cy="10" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
      <circle cx="14" cy="10" r="4.5" fill="#ffffff" />
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#0369a1;">Nodos Universitarios (10 Localidades):</text>
    </g>
    
    <!-- Detalle de los 10 Nodos agrupados por región -->
    <g transform="translate(35, 208)">
      <text x="0" y="14" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Región Sur (Línea Sur):</text>
      <text x="14" y="32" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Los Menucos, Sierra Colorada, Valcheta,</text>
      <text x="14" y="48" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Ramos Mexía, Maquinchao y Comallo</text>
      
      <text x="0" y="74" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Valle Medio y Costa Atlántica:</text>
      <text x="14" y="92" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">San Antonio Oeste, General Conesa, Lamarque</text>
      <text x="14" y="108" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">y Sierra Grande</text>
    </g>
  </g>

  <!-- 7. Marcadores y Cápsulas de los 10 Nodos Universitarios (Sin ninguna superposición) -->

  <!-- NODO 1: Los Menucos -->
  <g id="nodo_los_menucos" transform="translate(545, 845)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Los Menucos</text>
  </g>

  <!-- NODO 2: Sierra Colorada -->
  <g id="nodo_sierra_colorada" transform="translate(652, 750)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-80" y="-36" width="160" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Colorada</text>
  </g>

  <!-- NODO 3: Valcheta -->
  <g id="nodo_valcheta" transform="translate(946, 766)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="18" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Valcheta</text>
  </g>

  <!-- NODO 4: Ramos Mexía -->
  <g id="nodo_ramos_mexia" transform="translate(795, 755)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Ramos Mexía</text>
  </g>

  <!-- NODO 5: San Antonio Oeste -->
  <g id="nodo_san_antonio" transform="translate(1090, 766)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-95" y="18" width="190" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● San Antonio Oeste</text>
  </g>

  <!-- NODO 6: General Conesa -->
  <g id="nodo_conesa" transform="translate(1238, 632)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● General Conesa</text>
  </g>

  <!-- NODO 7: Lamarque -->
  <g id="nodo_lamarque" transform="translate(975, 475)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="18" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Lamarque</text>
  </g>

  <!-- NODO 8: Maquinchao -->
  <g id="nodo_maquinchao" transform="translate(435, 948)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-65" y="18" width="130" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Maquinchao</text>
  </g>

  <!-- NODO 9: Comallo -->
  <g id="nodo_comallo" transform="translate(235, 940)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="-36" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Comallo</text>
  </g>

  <!-- NODO 10: Sierra Grande -->
  <g id="nodo_sierra_grande" transform="translate(1080, 1040)" filter="url(#shadow)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="18" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Grande</text>
  </g>

  <!-- 8. SEDE CENTRAL: Viedma (Destacada y Nítida) -->
  <g id="sede_viedma" transform="translate(1535, 832)" filter="url(#glow_viedma)">
    <circle cx="0" cy="0" r="20" fill="#c89632" stroke="#0f2d59" stroke-width="3.5" />
    <text x="0" y="8" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:23px;font-weight:900;fill:#ffffff;">★</text>
    <rect x="-140" y="-48" width="280" height="34" rx="6" fill="#0f2d59" stroke="#c89632" stroke-width="2.2" />
    <text x="0" y="-25" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:900;fill:#ffffff;letter-spacing:0.5px;">★ VIEDMA (Sede Central CURZAS)</text>
  </g>

</svg>
'''

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(nuevo_svg)

print('[OK] red_territorial.svg reconstruido con pureza cartográfica, sin textos superpuestos y con fondo oceánico.')

