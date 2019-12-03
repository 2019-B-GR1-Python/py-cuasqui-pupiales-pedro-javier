# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:58:11 2019

@author: PedroW10
"""

import pandas as pd
import os

path_guardado_bin="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data_full.pickle"
df5=pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50019,:].copy()
#Tipos de archivos a los que s epuede convertir
 #JSON
 #Excel
 #SQL
 
 ######EXCEL###############33
path_destino = "C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\mi_df_completo.xlsx"
 
df.to_excel(path_destino, index = False)
columnas =["artist","title", "year"]
#cwd = os.getcwd()
df.to_excel(path_destino, columns= columnas ,index = False)


###ESCRIIR MULTIPLES HOJAS DE TRABAJO con pandas
#Se crea una instancia de pandas  excel weriter
path_multiple = "C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\mi_df_multiple.xlsx"
writer = pd.ExcelWriter(path_multiple, engine="xlsxwriter")
#definicion de hojas excel
df.to_excel(writer, sheet_name="Primera")
df.to_excel(writer, sheet_name="Segunda", index= False)
df.to_excel(writer, sheet_name="Tercera", columns= columnas)

writer.save()






#Conteo de numero de artistas
num_artistas = df['artist'].value_counts()
path_colores = "C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\mi_df_colores.xlsx"
writer_colores = pd.ExcelWriter(path_colores, engine="xlsxwriter")

num_artistas.to_excel(writer_colores,sheet_name='Artistas')
hoja_artistas  = writer_colores.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)
formato_artistas={
        "type":"2_color_scale",
        "min_value":"10",
        "min_type": "percentile",
        "max_value":"99",
        "max_type":"percentile"
        }

hoja_artistas.conditional_format(rango_celdas,formato_artistas)
writer_colores.save()




























