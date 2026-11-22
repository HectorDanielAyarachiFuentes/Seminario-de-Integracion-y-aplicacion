import os
import shutil

dest_root = 'bibliografia'
os.makedirs(os.path.join(dest_root, '1_estado_del_arte'), exist_ok=True)
os.makedirs(os.path.join(dest_root, '2_marco_teorico_y_gestion_publica'), exist_ok=True)
os.makedirs(os.path.join(dest_root, '3_metodologia_y_epistemologia'), exist_ok=True)
os.makedirs(os.path.join(dest_root, '4_normativa_institucional'), exist_ok=True)

# Copias desde seminario_integracion y entregas/actividad_3
copies = [
    # Metodologia
    ('seminario_integracion/4_metodologia/bibliografia_metodologia/Flyvbjerg (2005).pdf', 'bibliografia/3_metodologia_y_epistemologia/Flyvbjerg (2005) - Cinco malentendidos acerca del estudio de caso.pdf'),
    ('seminario_integracion/4_metodologia/bibliografia_metodologia/Gimenez (2012).pdf', 'bibliografia/3_metodologia_y_epistemologia/Gimenez (2012) - El estatuto metodologico del estudio de caso.pdf'),
    ('seminario_integracion/4_metodologia/bibliografia_metodologia/HERNANDEZ SAMPIERI - Metodología.pdf', 'bibliografia/3_metodologia_y_epistemologia/Hernandez Sampieri - Metodologia de la investigacion.pdf'),
    ('seminario_integracion/4_metodologia/bibliografia_metodologia/SAUTU - Metodología.pdf', 'bibliografia/3_metodologia_y_epistemologia/Sautu - Metodologia de investigacion.pdf'),
    ('seminario_integracion/1_introduccion/bibliografia_metodologica_general/12.Sautu y otros. 2005. “Manual de metodología de investigación.pdf', 'bibliografia/3_metodologia_y_epistemologia/Sautu et al. (2005) - Manual de metodologia de investigacion.pdf'),
    ('seminario_integracion/1_introduccion/bibliografia_metodologica_general/4-Guber, Rosana-2011- El trabajo de campo.......pdf', 'bibliografia/3_metodologia_y_epistemologia/Guber (2011) - El trabajo de campo.pdf'),
    ('seminario_integracion/1_introduccion/bibliografia_metodologica_general/17.Strauss y Corbin.2002. ” Bases de la investigación cualitativa .pdf', 'bibliografia/3_metodologia_y_epistemologia/Strauss y Corbin (2002) - Bases de la investigacion cualitativa.pdf'),
    ('seminario_integracion/3_estado_cuestion_marco_teorico/bibliografia_marco_teorico/De la Garza (2001).pdf', 'bibliografia/3_metodologia_y_epistemologia/De la Garza Toledo (2001) - La epistemologia critica.pdf'),
    
    # Normativa
    ('seminario_integracion/recursos_tfg/reglamentacion_curza_a_tener_en_cuenta/resol_0266_2023_deroga_resol_0226_2015_y_0160_2015_aprueba_reglamento_de_trabajos_finales_de_graduacion_tfg_1.pdf', 'bibliografia/4_normativa_institucional/Resolucion CD-CURZA 266-23 - Reglamento TFG.pdf'),
    ('seminario_integracion/recursos_tfg/reglamentacion_de_la_unco_curza_que_debo_tener_en_cuenta/1_estatuto_universidad_nacional_del_comahue.pdf', 'bibliografia/4_normativa_institucional/Estatuto Universidad Nacional del Comahue (Texto Historico).pdf'),
    
    # Fuentes y Autores (Actividad 3)
    ('entregas/actividad_3/Fuentes y Autores (Archivos Completos)/1 - Normativa Oficial UNCo y CURZAS/Estatuto UNCo (Ordenanza CS 0988-2025) - Título X Carrera Docente.pdf', 'bibliografia/4_normativa_institucional/Ordenanza CS 0988-2025 - Estatuto UNCo Titulo X Carrera Docente.pdf'),
    ('entregas/actividad_3/Fuentes y Autores (Archivos Completos)/1 - Normativa Oficial UNCo y CURZAS/Reglamento de Carrera Docente UNCo (Ordenanza CS 0910-1997 y modif).pdf', 'bibliografia/4_normativa_institucional/Ordenanza CS 0910-1997 - Reglamento de Carrera Docente UNCo.pdf'),
    ('entregas/actividad_3/Fuentes y Autores (Archivos Completos)/1 - Normativa Oficial UNCo y CURZAS/CURZAS UNCo - Nodos Territoriales y Modalidad Híbrida (Guía 2026).pdf', 'bibliografia/4_normativa_institucional/CURZAS UNCo - Nodos Territoriales y Modalidad Hibrida (Guia 2026).pdf'),
    ('entregas/actividad_3/Fuentes y Autores (Archivos Completos)/4 - Marco Teórico y Gestión Pública/Oszlak (2020) - El Estado en la era exponencial (INAP).pdf', 'bibliografia/2_marco_teorico_y_gestion_publica/Oszlak (2020) - El Estado en la era exponencial.pdf'),
    ('entregas/actividad_3/Fuentes y Autores (Archivos Completos)/2 - Epistemología y Metodología (Cátedra SIA)/Torraco (2016).pdf', 'bibliografia/3_metodologia_y_epistemologia/Torraco (2016) - Writing integrative literature reviews.pdf'),
    
    # Estado del Arte
    ('bibliografia/Estado del arte/Estadio Internacional/1/Dialnet-LaEvaluacionDe360AplicadaAlPersonalDocenteDeNivelS-7242790.pdf', 'bibliografia/1_estado_del_arte/Sifuentes Ocegueda et al. (2016) - Evaluacion 360 personal docente superior (RITI).pdf'),
    ('bibliografia/Estado del arte/Estadio Internacional/2/ms-articulo-2749.pdf', 'bibliografia/1_estado_del_arte/Obando Freire et al. (2014) - Evaluacion docente modelo 360 y portafolio (Medisur).pdf'),
    ('bibliografia/Estado del arte/Estadio Internacional/3/Metaevaluacion_del_sistema_de_evaluacion_docente_e.pdf', 'bibliografia/1_estado_del_arte/Hernandez-Villafana & Luna Serrano (2023) - Metaevaluacion docente universidad publica (EPAA).pdf'),
    ('bibliografia/Estado del arte/Estadio Nacional/1/Hay_una_profesion_academica_argentina_A.pdf', 'bibliografia/1_estado_del_arte/Marquina (2013) - Profesion academica argentina (Pensamiento Universitario).pdf'),
    ('bibliografia/Estado del arte/Estadio Nacional/2/admin,+Año+14,+Nº+27,+julio+-+diciembre+2021-103-120.pdf', 'bibliografia/1_estado_del_arte/Vazquez Cid de Leon et al. (2021) - Evaluacion 360 tutorias presenciales y en linea (UNACIENCIA).pdf'),
    ('bibliografia/Estado del arte/Estadio Regional y Local/3/2/COMPILACION-RES-CD_INFORME-DECANA_2022_1.pdf', 'bibliografia/4_normativa_institucional/Resolucion CD-CURZA 196-2022 (Compilacion resoluciones 2022).pdf')
]

# Buscar Wainerman y Sautu dinamicamente
for root, dirs, files in os.walk('seminario_integracion'):
    for f in files:
        if 'wainerman' in f.lower():
            copies.append((os.path.join(root, f), 'bibliografia/3_metodologia_y_epistemologia/Wainerman y Sautu (2001) - La trastienda de la investigacion.pdf'))

for src, dst in copies:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'COPIADO: {src} -> {dst}')
    else:
        print(f'NO EXISTE: {src}')

print('\nCOPIA FINALIZADA CON EXITO.')
