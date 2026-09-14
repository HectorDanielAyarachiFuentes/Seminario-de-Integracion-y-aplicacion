with open('pruebas/doc1_full.txt', 'r', encoding='utf-8') as f:
    t1 = f.read()

with open('pruebas/doc2_full.txt', 'r', encoding='utf-8') as f:
    t2 = f.read()

print("==============================================")
print("DOC 1: METODOLOGIA Y RESULTADOS")
print("==============================================")
# Find where Metodología is in Doc 1
idx1 = t1.lower().find("metodología")
if idx1 != -1:
    print(t1[idx1:idx1+3500])

print("\n==============================================")
print("DOC 1: OBJETIVOS / INTRODUCCION")
print("==============================================")
idx_obj = t1.lower().find("objetivo")
while idx_obj != -1:
    print(t1[max(0, idx_obj-50):idx_obj+300])
    print("----")
    idx_obj = t1.lower().find("objetivo", idx_obj+300)
    if idx_obj > 8000:
        break
