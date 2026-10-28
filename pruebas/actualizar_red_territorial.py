# -*- coding: utf-8 -*-
"""
Actualiza red_territorial.svg con los 10 Nodos Universitarios del CURZAS y la Sede Central Viedma
"""
import re

svg_path = 'Entregas/Actividad 4/quarto/assets/red_territorial.svg'
with open(svg_path, 'r', encoding='utf-8') as f:
    svg = f.read()

# Reemplazar la tarjeta vieja por la capa completa institucional con los 10 nodos y referencias
old_header_pat = r'<g id="clean_header".*?</g>\s*<!-- Rótulo Cartográfico'

new_header_and_nodes = '''<!-- ====================================================================== -->
<!-- CAPA INSTITUCIONAL: RED TERRITORIAL DE NODOS UNIVERSITARIOS (CURZAS-UNCo) -->
<!-- ====================================================================== -->
<g id="red_nodos_curzas">

  <!-- 1. Placa de Encabezado Institucional y Referencias -->
  <g id="header_institucional" transform="translate(35, 45)">
    <rect x="-15" y="-12" width="460" height="340" rx="10" fill="#ffffff" fill-opacity="0.96" stroke="#0f3b7d" stroke-width="2" />
    
    <!-- Título Institucional -->
    <text x="0" y="26" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:900;fill:#0f3b7d;letter-spacing:1px;">UNIVERSIDAD NACIONAL DEL COMAHUE</text>
    <text x="0" y="50" style="font-family:'Segoe UI',Arial,sans-serif;font-size:17px;font-weight:700;fill:#0369a1;letter-spacing:0.5px;">CURZAS — Sede Central Viedma</text>
    <line x1="0" y1="62" x2="430" y2="62" style="stroke:#c89632;stroke-width:2.5px;stroke-linecap:round;" />
    
    <!-- Subtítulo de la Red -->
    <text x="0" y="86" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:800;fill:#1e293b;">Red Territorial de Nodos Universitarios</text>
    <text x="0" y="106" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:600;font-style:italic;fill:#475569;">Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)</text>
    
    <line x1="0" y1="120" x2="430" y2="120" style="stroke:#cbd5e1;stroke-width:1px;" />
    
    <!-- Ref 1: Sede Central Viedma -->
    <g transform="translate(0, 132)">
      <circle cx="14" cy="10" r="12" fill="#c89632" stroke="#0f2d59" stroke-width="2.5" />
      <text x="14" y="16" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:900;fill:#ffffff;">★</text>
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    </g>
    
    <!-- Ref 2: Nodos Universitarios -->
    <g transform="translate(0, 168)">
      <circle cx="14" cy="10" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
      <circle cx="14" cy="10" r="4.5" fill="#ffffff" />
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#0369a1;">Nodos Universitarios (10 Localidades):</text>
    </g>
    
    <!-- Detalle de los 10 Nodos agrupados por región -->
    <g transform="translate(15, 198)">
      <text x="0" y="14" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Región Sur (Línea Sur):</text>
      <text x="16" y="32" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Los Menucos, Sierra Colorada, Valcheta,</text>
      <text x="16" y="48" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Ramos Mexía, Maquinchao y Comallo</text>
      
      <text x="0" y="74" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Valle Medio y Costa Atlántica:</text>
      <text x="16" y="92" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">San Antonio Oeste, General Conesa, Lamarque</text>
      <text x="16" y="108" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">y Sierra Grande</text>
    </g>
  </g>

  <!-- 2. Líneas de Conectividad Territorial Institucional (Traza de Red) -->
  <g id="red_conectividad" stroke="#0284c7" stroke-width="3" stroke-dasharray="8,6" stroke-opacity="0.75" fill="none">
    <!-- Corredor Este-Oeste RN 23: Viedma -> Conesa -> SAO -> Valcheta -> Ramos Mexia -> Sierra Colorada -> Los Menucos -> Maquinchao -> Comallo -->
    <path d="M 1535,832 L 1238,632 L 1090,766 L 946,766 L 795,755 L 652,750 L 545,845 L 435,948 L 235,940" />
    <!-- Conexión Valle Medio: Conesa -> Lamarque -->
    <path d="M 1238,632 L 975,475" />
    <!-- Conexión Costa Atlántica Sur RN 3: SAO -> Sierra Grande -->
    <path d="M 1090,766 L 1080,1040" />
  </g>

  <!-- 3. Marcadores y Cápsulas de los 10 Nodos Universitarios -->

  <!-- NODO 1: Los Menucos -->
  <g id="nodo_los_menucos" transform="translate(545, 845)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Los Menucos</text>
  </g>

  <!-- NODO 2: Sierra Colorada -->
  <g id="nodo_sierra_colorada" transform="translate(652, 750)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-80" y="-36" width="160" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Colorada</text>
  </g>

  <!-- NODO 3: Valcheta -->
  <g id="nodo_valcheta" transform="translate(946, 766)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="18" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Valcheta</text>
  </g>

  <!-- NODO 4: Ramos Mexía -->
  <g id="nodo_ramos_mexia" transform="translate(795, 755)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Ramos Mexía</text>
  </g>

  <!-- NODO 5: San Antonio Oeste -->
  <g id="nodo_san_antonio" transform="translate(1090, 766)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-95" y="18" width="190" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● San Antonio Oeste</text>
  </g>

  <!-- NODO 6: General Conesa -->
  <g id="nodo_conesa" transform="translate(1238, 632)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="-36" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● General Conesa</text>
  </g>

  <!-- NODO 7: Lamarque -->
  <g id="nodo_lamarque" transform="translate(975, 475)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="18" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Lamarque</text>
  </g>

  <!-- NODO 8: Maquinchao -->
  <g id="nodo_maquinchao" transform="translate(435, 948)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-65" y="18" width="130" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Maquinchao</text>
  </g>

  <!-- NODO 9: Comallo -->
  <g id="nodo_comallo" transform="translate(235, 940)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-55" y="-36" width="110" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="-19" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Comallo</text>
  </g>

  <!-- NODO 10: Sierra Grande -->
  <g id="nodo_sierra_grande" transform="translate(1080, 1040)">
    <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="0" cy="0" r="5" fill="#ffffff" />
    <rect x="-75" y="18" width="150" height="26" rx="5" fill="#ffffff" fill-opacity="0.95" stroke="#0284c7" stroke-width="1.8" />
    <text x="0" y="35" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f3b7d;">● Sierra Grande</text>
  </g>

  <!-- SEDE CENTRAL: Viedma -->
  <g id="sede_viedma" transform="translate(1535, 832)">
    <circle cx="0" cy="0" r="19" fill="#c89632" stroke="#0f2d59" stroke-width="3.5" />
    <text x="0" y="7" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:900;fill:#ffffff;">★</text>
    <rect x="-135" y="-46" width="270" height="34" rx="6" fill="#0f2d59" stroke="#c89632" stroke-width="2" />
    <text x="0" y="-23" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:900;fill:#ffffff;">★ VIEDMA (Sede CURZAS)</text>
  </g>

</g>
<!-- Rótulo Cartográfico'''

svg_updated = re.sub(old_header_pat, new_header_and_nodes, svg, flags=re.DOTALL)

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_updated)

print('[OK] red_territorial.svg actualizado exitosamente.')

