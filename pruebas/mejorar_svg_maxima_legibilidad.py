import re

svg_path = "entregas/actividad_4/quarto/assets/red_territorial.svg"
with open(svg_path, "r", encoding="utf-8") as f:
    svg = f.read()

# 1. Caja de referencias hiper-legible
leyenda_max = """  <!-- Placa de Referencias Cartográficas - Máxima Legibilidad -->
  <g id="header_institucional" filter="url(#shadow)">
    <!-- Marco de la tarjeta -->
    <rect x="25" y="25" width="600" height="360" rx="16" fill="#ffffff" fill-opacity="0.98" stroke="#0f3b7d" stroke-width="3" />
    
    <!-- Encabezado de la Leyenda -->
    <text x="55" y="72" style="font-family:'Segoe UI',Arial,sans-serif;font-size:32px;font-weight:900;fill:#0f3b7d;letter-spacing:1px;">REFERENCIAS</text>
    <line x1="55" y1="88" x2="590" y2="88" style="stroke:#c89632;stroke-width:3.5px;stroke-linecap:round;" />
    
    <!-- Ítem 1: Sede Central CURZAS -->
    <circle cx="85" cy="138" r="22" fill="#0f2d59" stroke="#c89632" stroke-width="3.5" />
    <text x="85" y="146" text-anchor="middle" style="font-family:'Segoe UI',Arial,sans-serif;font-size:24px;font-weight:900;fill:#c89632;">★</text>
    <text x="125" y="135" style="font-family:'Segoe UI',Arial,sans-serif;font-size:26px;font-weight:800;fill:#0f2d59;">Sede Central Viedma (CURZAS)</text>
    <text x="125" y="160" style="font-family:'Segoe UI',Arial,sans-serif;font-size:19px;font-weight:600;fill:#475569;">Gobierno, administración y cogobierno universitario</text>
    
    <!-- Ítem 2: Nodos Universitarios -->
    <circle cx="85" cy="222" r="20" fill="#0284c7" stroke="#ffffff" stroke-width="3.5" />
    <circle cx="85" cy="222" r="9" fill="#ffffff" />
    <circle cx="85" cy="222" r="4" fill="#0f3b7d" />
    <text x="125" y="219" style="font-family:'Segoe UI',Arial,sans-serif;font-size:26px;font-weight:800;fill:#0284c7;">Nodos Universitarios (10 localidades)</text>
    <text x="125" y="244" style="font-family:'Segoe UI',Arial,sans-serif;font-size:19px;font-weight:600;fill:#475569;">Aulas híbridas, tutorías y vinculación territorial</text>
    
    <!-- Ítem 3: Red de Conectividad e Itinerancia -->
    <line x1="60" y1="305" x2="110" y2="305" style="stroke="#0284c7;stroke-width:5px;stroke-dasharray:10,6;stroke-linecap:round;" />
    <circle cx="85" cy="305" r="5" fill="#0284c7" />
    <text x="125" y="302" style="font-family:'Segoe UI',Arial,sans-serif;font-size:26px;font-weight:800;fill:#0369a1;">Corredores de Itinerancia Académica</text>
    <text x="125" y="327" style="font-family:'Segoe UI',Arial,sans-serif;font-size:19px;font-weight:600;fill:#475569;">Ruta Nac. 23 (Línea Sur) y Rutas Nac. 3, 250 y 251</text>
  </g>"""

svg = re.sub(r'<g id="header_institucional".*?</g>', leyenda_max, svg, flags=re.DOTALL)

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg)
print("SVG con máxima legibilidad guardado!")
