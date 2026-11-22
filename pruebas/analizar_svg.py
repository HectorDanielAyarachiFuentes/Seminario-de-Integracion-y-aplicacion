import re

svg_path = "entregas/actividad_4/quarto/assets/red_territorial.svg"
with open(svg_path, "r", encoding="utf-8") as f:
    text = f.read()

m_all = re.findall(r'<g id="(nodo_[^"]+|sede_viedma)"[^>]*>(.*?)</g>', text, re.DOTALL)
for gid, body in m_all:
    print(f"=== {gid} ===")
    print(body.strip())
