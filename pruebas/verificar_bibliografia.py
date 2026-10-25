import re
from pathlib import Path

content = Path('Entregas/Actividad 4/quarto/tp4_proyecto_tfg_integral.qmd').read_text(encoding='utf-8')
bib_content = Path('Entregas/Actividad 4/quarto/referencias.bib').read_text(encoding='utf-8')

text_cites = sorted(set(re.findall(r'@([a-zA-Z0-9_:\-]+)', content)) - {'gmail'})
print(f'Total cited keys in text: {len(text_cites)}')

bib_entries = {}
current_key = None
current_entry = []
for line in bib_content.splitlines():
    m = re.match(r'@\w+\s*\{\s*([^,]+),', line)
    if m:
        if current_key:
            bib_entries[current_key] = '\n'.join(current_entry)
        current_key = m.group(1).strip()
        current_entry = [line]
    else:
        if current_key:
            current_entry.append(line)
if current_key:
    bib_entries[current_key] = '\n'.join(current_entry)

print(f'Total bib entries in .bib: {len(bib_entries)}')

print("\n--- CITAS EN EL TEXTO Y SU ENTRADA EN BIBLIOGRAFÍA ---")
for key in text_cites:
    if key in bib_entries:
        entry = bib_entries[key]
        author = re.search(r'author\s*=\s*[\{"](.*?)[\}"]', entry, re.I | re.DOTALL)
        year = re.search(r'year\s*=\s*[\{"](.*?)[\}"]', entry, re.I)
        title = re.search(r'title\s*=\s*[\{"](.*?)[\}"]', entry, re.I | re.DOTALL)
        auth_str = author.group(1).replace('\n', ' ').strip()[:28] if author else 'INSTITUCIONAL/NO AUTH'
        yr_str = year.group(1).strip() if year else 'S/F'
        tit_str = title.group(1).replace('\n', ' ').strip()[:45] if title else 'NO TITLE'
        print(f'{key:22} | {yr_str:5} | {auth_str:28} | {tit_str}')
    else:
        print(f'FALTA EN BIBLIOGRAFIA: {key}')

print("\n--- ENTRADAS EN BIBLIOGRAFÍA QUE NO ESTÁN CITADAS EN EL TEXTO ---")
not_cited = set(bib_entries.keys()) - set(text_cites)
for key in sorted(not_cited):
    entry = bib_entries[key]
    author = re.search(r'author\s*=\s*[\{"](.*?)[\}"]', entry, re.I | re.DOTALL)
    year = re.search(r'year\s*=\s*[\{"](.*?)[\}"]', entry, re.I)
    title = re.search(r'title\s*=\s*[\{"](.*?)[\}"]', entry, re.I | re.DOTALL)
    auth_str = author.group(1).replace('\n', ' ').strip()[:28] if author else 'INSTITUCIONAL/NO AUTH'
    yr_str = year.group(1).strip() if year else 'S/F'
    tit_str = title.group(1).replace('\n', ' ').strip()[:45] if title else 'NO TITLE'
    print(f'{key:22} | {yr_str:5} | {auth_str:28} | {tit_str}')
