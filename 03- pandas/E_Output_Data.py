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
num_artistas = df5['artist'].value_counts()
path_colores = "C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\mi_df_colores.xlsx"
writer_colores = pd.ExcelWriter(path_colores, engine="xlsxwriter")

num_artistas.to_excel(writer_colores,sheet_name='Artistas')
num_artistas.to_excel(writer_colores,sheet_name='Grafico')
#Guardamos temporalmente la hojja de artistas para trabajar en ella
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

workbook = writer_colores.book
worksheet = writer_colores.sheets['Grafico']
chart = workbook.add_chart({'type': 'column'})
writer_colores.save()


###########EJEMPLO DE INTERNET ADAPTADO DATOS LOCALES

# Some sample data to plot.
#list_data =df5

# Create a Pandas dataframe from the data.
#df = pd.DataFrame(list_data)
df= df5['artist'].value_counts()
# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\mi_df_grafico.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
# This is equivalent to the following using XlsxWriter on its own:
#
#    workbook = xlsxwriter.Workbook('filename.xlsx')
#    worksheet = workbook.add_worksheet()
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
#'values':     '=Sheet1!$B$2:$B${}'.format(len(sheet_name.index)+1),
chart.add_series({
    'values':     '=Sheet1!$B$2:$B$300',
    'gap':        2,
})

# You can also use array notation to define the chart values.
#    chart.add_series({
#        'values':     ['Sheet1', 1, 1, 7, 1],
#        'gap':        2,
#    })

# Configure the chart axes.
chart.set_y_axis({'major_gridlines': {'visible': False}})

# Turn off chart legend. It is on by default in Excel.
chart.set_legend({'position': 'none'})

# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()






















