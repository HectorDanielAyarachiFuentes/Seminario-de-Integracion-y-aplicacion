import re

path = 'Entregas/Actividad 4/quarto/assets/red_territorial.svg'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace header block
patron = r'<g id="header_institucional".*?</g>\s*</g>'
# Let's inspect using regex or precise substring
old_start = '  <!-- 6. Placa de Encabezado Institucional y Referencias (Sector Noroeste Limpio) -->'
old_end = '  <!-- 7. Marcadores y Cápsulas de los 10 Nodos Universitarios (Sin ninguna superposición) -->'

idx1 = content.find(old_start)
idx2 = content.find(old_end)

if idx1 != -1 and idx2 != -1:
    nuevo_bloque = """  <!-- 6. Placa de Encabezado Institucional y Referencias (Sector Noroeste Limpio) -->
  <g id="header_institucional" transform="translate(25, 35)" filter="url(#shadow)">
    <rect x="0" y="0" width="510" height="345" rx="12" fill="#ffffff" fill-opacity="0.97" stroke="#0f3b7d" stroke-width="2.2" />
    
    <text x="24" y="34" style="font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:900;fill:#0f3b7d;letter-spacing:0.2px;">UNIVERSIDAD NACIONAL DEL COMAHUE</text>
    <text x="24" y="58" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:700;fill:#0369a1;letter-spacing:0.2px;">CURZAS — Sede Central Viedma</text>
    <line x1="24" y1="70" x2="486" y2="70" style="stroke:#c89632;stroke-width:2.5px;stroke-linecap:round;" />
    
    <text x="24" y="96" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15.5px;font-weight:800;fill:#1e293b;">Red Territorial de Nodos Universitarios</text>
    <text x="24" y="116" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;font-style:italic;fill:#475569;">Resolución CD-CURZA N° 196/2022 (Docencia Híbrida)</text>
    
    <line x1="24" y1="130" x2="486" y2="130" style="stroke:#e2e8f0;stroke-width:1.5px;" />
    
    <!-- Ref 1: Sede Central Viedma -->
    <g transform="translate(24, 144)">
      <circle cx="14" cy="10" r="12" fill="#c89632" stroke="#0f2d59" stroke-width="2.5" />
      <text x="14" y="16" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:900;fill:#ffffff;">★</text>
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14.5px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    </g>
    
    <!-- Ref 2: Nodos Universitarios -->
    <g transform="translate(24, 180)">
      <circle cx="14" cy="10" r="10" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
      <circle cx="14" cy="10" r="4.5" fill="#ffffff" />
      <text x="36" y="15" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14.5px;font-weight:800;fill:#0369a1;">Nodos Universitarios (10 Localidades):</text>
    </g>
    
    <!-- Detalle de los 10 Nodos agrupados por región -->
    <g transform="translate(42, 212)">
      <text x="0" y="14" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Región Sur (Línea Sur):</text>
      <text x="14" y="32" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Los Menucos, Sierra Colorada, Valcheta,</text>
      <text x="14" y="48" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">Ramos Mexía, Maquinchao y Comallo</text>
      
      <text x="0" y="74" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;font-weight:700;fill:#1e293b;">• Valle Medio y Costa Atlántica:</text>
      <text x="14" y="92" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">San Antonio Oeste, General Conesa, Lamarque</text>
      <text x="14" y="108" style="font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;font-weight:600;fill:#475569;">y Sierra Grande</text>
    </g>
  </g>

"""
    nuevo_contenido = content[:idx1] + nuevo_bloque + content[idx2:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(nuevo_contenido)
    print("PLACA INSTITUCIONAL ACTUALIZADA EXITOSAMENTE!")
else:
    print(f"Indices: idx1={idx1}, idx2={idx2}")

