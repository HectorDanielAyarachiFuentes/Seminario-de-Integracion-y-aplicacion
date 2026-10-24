import re
from pathlib import Path

bib_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Entregas\Actividad 4\quarto\referencias.bib")
dest_path = Path(r"c:\Users\Ramoncito\.antigravity-ide\Seminario de Integración y Aplicación\Seminario de Integración y Aplicación\4 - Metodología\Trabajo Práctico n° 4\referencias.bib")

content = bib_path.read_text(encoding="utf-8")

replacements = [
    (r"Est{\\'e}vez", "Estévez"),
    (r"Est{\'e}vez", "Estévez"),
    (r"M{\\'o}nica", "Mónica"),
    (r"M{\'o}nica", "Mónica"),
    (r"Introducci{\\'o}n", "Introducción"),
    (r"Introducci{\'o}n", "Introducción"),
    (r"Administraci{\\'o}n", "Administración"),
    (r"Administraci{\'o}n", "Administración"),
    (r"P{\\'u}blica", "Pública"),
    (r"P{\'u}blica", "Pública"),
    (r"Naci{\\'o}n", "Nación"),
    (r"Naci{\'o}n", "Nación"),
    (r"{Hern{'a}ndez Sampieri}", "Hernández Sampieri"),
    (r"{Fern{'a}ndez Collado}", "Fernández Collado"),
    (r"{Baptista Lucio}", "Baptista Lucio"),
    (r"Mar{'i}a", "María"),
    (r"Metodolog{'i}a", "Metodología"),
    (r"investigaci{'o}n", "investigación"),
    (r"Espa{\\~n}ola", "Española"),
    (r"Espa{\~n}ola", "Española"),
    (r"Sociol{'o}gicas", "Sociológicas"),
    (r"Gim{'e}nez", "Giménez"),
    (r"metodol{'o}gico", "metodológico"),
    (r"An{'a}lisis", "Análisis"),
    (r"Naci{'o}n", "Nación"),
    (r"Protecci{'o}n", "Protección"),
    (r"Bolet{'i}n", "Boletín"),
    (r"Rep{'u}blica", "República"),
]

for old, new in replacements:
    content = content.replace(old, new)

bib_path.write_text(content, encoding="utf-8")
print(f"Updated {bib_path}")

dest_path.write_text(content, encoding="utf-8")
print(f"Updated {dest_path}")
