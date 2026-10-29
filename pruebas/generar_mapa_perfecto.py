# -*- coding: utf-8 -*-
import re

with open('Presentacion/assets/RioNegro.svg', 'r', encoding='utf-8') as f:
    rio_svg = f.read()

# Extract layer1 and layer2
l1_match = re.search(r'(<g[^>]*id="layer1"[^>]*>.*?</g>\s*</g>)', rio_svg, re.DOTALL)
l2_match = re.search(r'(<g[^>]*id="layer2"[^>]*>.*?</g>\s*</g>)', rio_svg, re.DOTALL)

l1_str = l1_match.group(1)
l2_str = l2_match.group(1)

# In layer1, change department text color to black (#000000)
l1_str_black = l1_str.replace('fill:#0f2d59', 'fill:#000000')

# Remove duplicate cabecera text labels that are now represented by CURZAS blue capsules:
ids_to_remove = ['text2207', 'text2236', 'text2222', 'text2206', 'text2197', 'text2302', 'text2259']
for tid in ids_to_remove:
    l1_str_black = re.sub(rf'<text id="{tid}".*?</text>', '', l1_str_black, flags=re.DOTALL)

# Clean inkscape and sodipodi namespaces
def clean_svg_namespaces(text):
    text = re.sub(r'\s+inkscape:[a-zA-Z0-9_\-]+="[^"]*"', '', text)
    text = re.sub(r'\s+sodipodi:[a-zA-Z0-9_\-]+="[^"]*"', '', text)
    return text

l1_str_black = clean_svg_namespaces(l1_str_black)
l2_str = clean_svg_namespaces(l2_str)

# Helper function to generate modern CURZAS node badge matching reference infographic:
def make_node_badge(node_id, cx, cy, label, pop, pos='top', badge_w=120, badge_h=38):
    if pos == 'top':
        bx = cx - badge_w / 2
        by = cy - 14 - badge_h
    elif pos == 'bottom':
        bx = cx - badge_w / 2
        by = cy + 14
    elif pos == 'left':
        bx = cx - 14 - badge_w
        by = cy - badge_h / 2
    elif pos == 'right':
        bx = cx + 14
        by = cy - badge_h / 2
    elif pos == 'top-left':
        bx = cx - badge_w - 6
        by = cy - badge_h - 6
    
    tx = bx + badge_w / 2
    t1_y = by + 16
    t2_y = by + 30
    
    return f'''
  <!-- NODO: {label} -->
  <g id="{node_id}" filter="url(#shadow)">
    <!-- Conector / Círculo del Nodo estilo UNCo -->
    <circle cx="{cx}" cy="{cy}" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.5" />
    <circle cx="{cx}" cy="{cy}" r="5.5" fill="#ffffff" />
    <circle cx="{cx}" cy="{cy}" r="2.5" fill="#0f3b7d" />
    
    <!-- Tarjeta Compacta de 2 líneas (Nombre + Población) -->
    <rect x="{bx}" y="{by}" width="{badge_w}" height="{badge_h}" rx="6" fill="#ffffff" fill-opacity="0.96" stroke="#0284c7" stroke-width="1.6" />
    <text x="{tx}" y="{t1_y}" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:800;fill:#0f3b7d;">{label}</text>
    <text x="{tx}" y="{t2_y}" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:10.5px;font-weight:600;fill:#0284c7;">({pop} hab.)</text>
  </g>'''

# 10 Nodos CURZAS con COORDENADAS CARTOGRÁFICAS EXACTAS (sin offset erróneo):
# 1. Ing. Jacobacci (6.261 hab.) -> TOP
badge_jacobacci = make_node_badge('nodo_jacobacci', 450, 945, 'Ing. Jacobacci', '6.261', pos='top', badge_w=116, badge_h=38)

# 2. Maquinchao (2.494 hab.) -> BOTTOM (Exactamente sobre su cabecera 635.7, 940.3)
badge_maquinchao = make_node_badge('nodo_maquinchao', 635.7, 940.3, 'Maquinchao', '2.494', pos='bottom', badge_w=110, badge_h=38)

# 3. Los Menucos (5.187 hab.) -> TOP (En RN 23 en 25 de Mayo)
badge_los_menucos = make_node_badge('nodo_los_menucos', 720, 855, 'Los Menucos', '5.187', pos='top', badge_w=112, badge_h=38)

# 4. Sierra Colorada (1.542 hab.) -> TOP (Exactamente sobre su cabecera 814.3, 777.4)
badge_sierra_colorada = make_node_badge('nodo_sierra_colorada', 814.3, 777.4, 'Sierra Colorada', '1.542', pos='top', badge_w=120, badge_h=38)

# 5. Ramos Mexía (973 hab.) -> BOTTOM (En RN 23 en 9 de Julio)
badge_ramos_mexia = make_node_badge('nodo_ramos_mexia', 970, 795, 'Ramos Mexía', '973', pos='bottom', badge_w=110, badge_h=38)

# 6. Valcheta (4.493 hab.) -> TOP (Exactamente sobre su cabecera 1108.6, 806.7)
badge_valcheta = make_node_badge('nodo_valcheta', 1108.6, 806.7, 'Valcheta', '4.493', pos='top', badge_w=100, badge_h=38)

# 7. SAO (6.265 hab.) -> TOP (Exactamente sobre su cabecera 1330.7, 819.6 en Bahía San Antonio)
badge_sao = make_node_badge('nodo_sao', 1330.7, 819.6, 'SAO / Las Grutas', '6.265', pos='top', badge_w=132, badge_h=38)

# 8. Sierra Grande (7.404 hab.) -> LEFT (FIRMEMENTE EN TIERRA en Dpto. San Antonio 1260, 1060)
badge_sierra_grande = make_node_badge('nodo_sierra_grande', 1260, 1060, 'Sierra Grande', '7.404', pos='left', badge_w=114, badge_h=38)

# 9. Gral. Conesa (7.123 hab.) -> LEFT (Exactamente sobre su cabecera 1425.7, 672.4)
badge_conesa = make_node_badge('nodo_conesa', 1425.7, 672.4, 'Gral. Conesa', '7.123', pos='left', badge_w=110, badge_h=38)

# 10. Río Colorado (13.828 hab.) -> TOP (Exactamente sobre su cabecera 1507.1, 411.7 sobre el río)
badge_rio_colorado = make_node_badge('nodo_rio_colorado', 1507.1, 411.7, 'Río Colorado', '13.828', pos='top', badge_w=114, badge_h=38)

# Sede Central Viedma (Exactamente sobre su punto histórico 1683.6, 857.4)
badge_viedma = '''
  <!-- SEDE CENTRAL: Viedma (80.632 hab.) -->
  <g id="sede_viedma" filter="url(#glow_viedma)">
    <!-- Marcador Central con Estrella Dorada -->
    <circle cx="1683.6" cy="857.4" r="22" fill="#c89632" stroke="#0f2d59" stroke-width="3.5" />
    <circle cx="1683.6" cy="857.4" r="14" fill="#0f2d59" />
    <text x="1683.6" y="863" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:900;fill:#c89632;">★</text>
    
    <!-- Placa Viedma CURZA -->
    <rect x="1463.6" y="884" width="220" height="48" rx="8" fill="#0f2d59" stroke="#c89632" stroke-width="2.2" />
    <text x="1573.6" y="905" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:900;fill:#ffffff;letter-spacing:0.5px;">VIEDMA CURZA</text>
    <text x="1573.6" y="922" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:11.5px;font-weight:700;fill:#c89632;">Sede Central (80.632 hab.)</text>
  </g>
'''

curzas_overlay = f'''
  <!-- Filtros -->
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.18" />
    </filter>
    <filter id="glow_viedma" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#c89632" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Rótulo del Océano y Golfo San Matías (En agua abierta) -->
  <g id="rotulos_maritimos" text-anchor="middle">
    <rect x="1420" y="980" width="340" height="70" rx="8" fill="#ffffff" fill-opacity="0.82" stroke="#bae6fd" stroke-width="1.5" />
    <text x="1590" y="1009" style="font-family:'Segoe UI',Arial,sans-serif;font-size:23px;font-weight:900;letter-spacing:2px;fill:#0369a1;">GOLFO SAN MATÍAS</text>
    <text x="1590" y="1035" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;letter-spacing:1px;fill:#0284c7;">Mar Argentino • Océano Atlántico</text>
  </g>

  <!-- Trazas de Conectividad Territorial (Red Híbrida de Nodos CURZAS) -->
  <g id="red_conectividad" stroke="#0284c7" stroke-width="4" stroke-dasharray="10,6" stroke-opacity="0.9" fill="none">
    <!-- Corredor Este-Oeste RN 23: SAO -> Valcheta -> Ramos Mexia -> Sierra Colorada -> Los Menucos -> Maquinchao -> Ing. Jacobacci -->
    <path d="M 1330.7,819.6 L 1108.6,806.7 L 970,795 L 814.3,777.4 L 720,855 L 635.7,940.3 L 450,945" />
    
    <!-- Corredor Costa / Valle RN 3 y RN 250: Viedma -> General Conesa -> SAO -->
    <path d="M 1683.6,857.4 L 1425.7,672.4 L 1330.7,819.6" />
    
    <!-- Corredor Noreste RN 251 / RN 22: General Conesa -> Río Colorado -->
    <path d="M 1425.7,672.4 L 1507.1,411.7" />
    
    <!-- Corredor Costa Atlántica Sur RN 3: SAO -> Sierra Grande (FIRMEMENTE POR TIERRA) -->
    <path d="M 1330.7,819.6 L 1260,1060" />
  </g>

  <!-- Placa de Encabezado Institucional CURZAS (Sector Noroeste) -->
  <g id="header_institucional" filter="url(#shadow)">
    <rect x="25" y="30" width="515" height="360" rx="12" fill="#ffffff" fill-opacity="0.97" stroke="#0f3b7d" stroke-width="2.2" />
    
    <text x="49" y="62" style="font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:900;fill:#0f3b7d;letter-spacing:0.2px;">UNIVERSIDAD NACIONAL DEL COMAHUE</text>
    <text x="49" y="84" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:700;fill:#0369a1;letter-spacing:0.2px;">CURZAS — Sede Central Viedma</text>
    <line x1="49" y1="95" x2="516" y2="95" style="stroke:#c89632;stroke-width:2.5px;stroke-linecap:round;" />
    
    <text x="49" y="118" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:800;fill:#1e293b;">Red Territorial de Nodos Universitarios</text>
    <text x="49" y="136" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;font-style:italic;fill:#475569;">Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)</text>
    
    <line x1="49" y1="148" x2="516" y2="148" style="stroke:#e2e8f0;stroke-width:1.5px;" />
    
    <!-- Ref 1: Sede Central Viedma -->
    <circle cx="63" cy="172" r="12" fill="#c89632" stroke="#0f2d59" stroke-width="2.5" />
    <text x="63" y="178" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:900;fill:#ffffff;">★</text>
    <text x="85" y="177" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    
    <!-- Ref 2: Nodos Universitarios -->
    <circle cx="63" cy="204" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
    <circle cx="63" cy="204" r="4.5" fill="#ffffff" />
    <circle cx="63" cy="204" r="2" fill="#0f3b7d" />
    <text x="85" y="209" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:800;fill:#0369a1;">Nodos Universitarios (10 Localidades):</text>
    
    <!-- Detalle de los 10 Nodos agrupados por región -->
    <text x="67" y="237" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:700;fill:#1e293b;">• Región Sur (Línea Sur - RN 23):</text>
    <text x="81" y="253" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">Valcheta, Ramos Mexía, Sierra Colorada,</text>
    <text x="81" y="268" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">Los Menucos, Maquinchao e Ing. Jacobacci</text>
    
    <text x="67" y="290" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:700;fill:#1e293b;">• Zona Atlántica y Noreste (RN 3, 250, 251 y 22):</text>
    <text x="81" y="306" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">San Antonio Oeste / Las Grutas, Sierra Grande,</text>
    <text x="81" y="321" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:600;fill:#475569;">General Conesa y Río Colorado</text>
    
    <!-- Ref 3: Cabeceras Departamentales y Fuente -->
    <line x1="49" y1="346" x2="516" y2="346" style="stroke:#e2e8f0;stroke-width:1.2px;" />
    
    <circle cx="57" cy="362" r="5" fill="#dc2626" stroke="#7f1d1d" stroke-width="1.5" />
    <text x="71" y="366" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12px;font-weight:700;fill:#881337;">Cabecera Departamental</text>
    <text x="269" y="366" style="font-family:'Segoe UI',Arial,sans-serif;font-size:11.5px;font-style:italic;font-weight:700;fill:#0284c7;">Fuente: Elaboración propia.</text>
  </g>

  <!-- 10 Nodos Universitarios CURZAS + Sede Central (Coordenadas Cartográficas Exactas) -->
  {badge_jacobacci}
  {badge_maquinchao}
  {badge_los_menucos}
  {badge_sierra_colorada}
  {badge_ramos_mexia}
  {badge_valcheta}
  {badge_sao}
  {badge_sierra_grande}
  {badge_conesa}
  {badge_rio_colorado}
  {badge_viedma}
'''

final_svg = f'''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-90 0 1960 1260" width="100%" height="100%">
  <!-- 1. Fondo Marino Sólido -->
  <rect x="-90" y="0" width="1960" height="1260" fill="#e0f2fe" />

  <!-- 2. Capa 1: Polígonos de Departamentos y Rótulos Base (Con Nombres en Negro) -->
  {l1_str_black}

  <!-- 3. Capa 2: Puntos Rojos de Cabeceras Departamentales -->
  {l2_str}

  <!-- 4. Capa CURZAS: Red de Nodos con Poblaciones y Coordenadas Exactas -->
  {curzas_overlay}
</svg>'''

with open('Entregas/Actividad 4/quarto/assets/red_territorial.svg', 'w', encoding='utf-8') as f:
    f.write(final_svg)

print("MAPA CORREGIDO CON COORDENADAS CARTOGRÁFICAS EXACTAS GENERADO!")
