with open('pruebas/doc2_full.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()

lines2 = t2.split('\n')
for i, l in enumerate(lines2):
    if l.strip().isupper() and len(l.strip()) > 3:
        print(f"Line {i}: {l.strip()}")

print("\n--- METODOLOGIA COMPLETA DE DOC 2 ---")
idx_met = t2.lower().find("metodología")
if idx_met != -1:
    print(t2[idx_met:idx_met+2500])

print("\n--- CONCLUSIONES / RESULTADOS DE DOC 2 ---")
idx_res = t2.lower().find("resultados")
if idx_res != -1:
    print(t2[idx_res:idx_res+2000])

idx_con = t2.lower().find("conclusiones")
if idx_con != -1:
    print(t2[idx_con:idx_con+2000])
