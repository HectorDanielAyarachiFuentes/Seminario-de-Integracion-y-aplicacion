import pymupdf

doc = pymupdf.open('Entregas/Actividad 4/TP4_Ayarachi_Fuentes.pdf')
page = doc[5] # page 6
crop_rect = pymupdf.Rect(50, 180, page.rect.width - 50, 540)
pix = page.get_pixmap(clip=crop_rect, dpi=200)
pix.save('pruebas/verificacion_mapa_con_placa.png')
print('Cropped map saved to pruebas/verificacion_mapa_con_placa.png')

