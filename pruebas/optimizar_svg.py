import re

svg_path = "entregas/actividad_4/quarto/assets/red_territorial.svg"
with open(svg_path, "r", encoding="utf-8") as f:
    svg = f.read()

# 1. Nueva caja de referencias
nueva_leyenda = """  <!-- Placa de Referencias Cartográficas Limpia y Legible (Sector Noroeste) -->
  <g id="header_institucional" filter="url(#shadow)">
    <!-- Marco de la tarjeta -->
    <rect x="30" y="35" width="560" height="310" rx="14" fill="#ffffff" fill-opacity="0.98" stroke="#0f3b7d" stroke-width="2.5" />
    
    <!-- Encabezado de la Leyenda -->
    <text x="60" y="75" style="font-family:'Segoe UI',Arial,sans-serif;font-size:26px;font-weight:900;fill:#0f3b7d;letter-spacing:0.8px;">REFERENCIAS</text>
    <line x1="60" y1="90" x2="550" y2="90" style="stroke:#c89632;stroke-width:3px;stroke-linecap:round;" />
    
    <!-- Ítem 1: Sede Central CURZAS -->
    <circle cx="85" cy="132" r="18" fill="#0f2d59" stroke="#c89632" stroke-width="3" />
    <text x="85" y="139" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:20px;font-weight:900;fill:#c89632;">★</text>
    <text x="120" y="130" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    <text x="120" y="150" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:600;fill:#475569;">Gobierno, administración y cogobierno universitario</text>
    
    <!-- Ítem 2: Nodos Universitarios -->
    <circle cx="85" cy="198" r="16" fill="#0284c7" stroke="#ffffff" stroke-width="3" />
    <circle cx="85" cy="198" r="7" fill="#ffffff" />
    <circle cx="85" cy="198" r="3.5" fill="#0f3b7d" />
    <text x="120" y="196" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0284c7;">Nodos Universitarios (10 sedes locales)</text>
    <text x="120" y="216" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:600;fill:#475569;">Aulas híbridas, tutorías y vinculación territorial</text>
    
    <!-- Ítem 3: Red de Conectividad e Itinerancia -->
    <line x1="65" y1="266" x2="105" y2="266" style="stroke:#0284c7;stroke-width:4.5px;stroke-dasharray:8,5;stroke-linecap:round;" />
    <circle cx="85" cy="266" r="4" fill="#0284c7" />
    <text x="120" y="262" style="font-family:'Segoe UI',Arial,sans-serif;font-size:22px;font-weight:800;fill:#0369a1;">Corredores de Itinerancia Académica</text>
    <text x="120" y="282" style="font-family:'Segoe UI',Arial,sans-serif;font-size:16px;font-weight:600;fill:#475569;">Ruta Nac. 23 (Línea Sur) y Rutas Nac. 3, 250 y 251</text>
  </g>"""

# Reemplazar header_institucional
svg = re.sub(r'<g id="header_institucional".*?</g>', nueva_leyenda, svg, flags=re.DOTALL)

# 2. Mejorar la placa de VIEDMA CURZAS
viedma_antiguo = """    <!-- Placa Viedma CURZA -->
    <rect x="1463.6" y="884" width="220" height="48" rx="8" fill="#0f2d59" stroke="#c89632" stroke-width="2.2" />
    <text x="1573.6" y="905" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:15px;font-weight:900;fill:#ffffff;letter-spacing:0.5px;">VIEDMA CURZAS</text>
    <text x="1573.6" y="922" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:11.5px;font-weight:700;fill:#c89632;">Sede Central (80.632 hab.)</text>"""

viedma_nuevo = """    <!-- Placa Viedma CURZAS -->
    <rect x="1440.0" y="880" width="250" height="56" rx="10" fill="#0f2d59" stroke="#c89632" stroke-width="2.8" />
    <text x="1565.0" y="905" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:18px;font-weight:900;fill:#ffffff;letter-spacing:0.8px;">VIEDMA CURZAS</text>
    <text x="1565.0" y="925" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:14px;font-weight:700;fill:#c89632;">Sede Central (80.632 hab.)</text>"""

svg = svg.replace(viedma_antiguo, viedma_nuevo)

# Guardar
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG optimizado con éxito!")
