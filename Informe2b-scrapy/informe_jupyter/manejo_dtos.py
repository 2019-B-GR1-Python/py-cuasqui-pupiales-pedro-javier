# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:41:26 2020

@author: PedroW10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json



#CARGA DE DATOS
#Fuente: https://subscription.packtpub.com/book/application_development/9781785287466/3/ch03lvl1sec46/creating-a-pandas-dataframe-from-a-json-file
file = 'C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\04- scrapy\\Proyecto2B-scrapy\\scrapy_mercadol\\tmp\\productos-mercadol.json'
articulos_mercadol = pd.read_json(file)
df_3= pd.read_json(file)



################################################################33
#1) GRAFICO DE SECTORES: PORCENTAJE DE ARTÍCULOS POR CATEGORIA
categorias = df_3["categoria"].value_counts()

#Obtener los nombres del indice
indice = list(categorias.index)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = indice
sizes = categorias

#fig1, ax1 = plt.subplots()
plt.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Porcentaje de objetos por categoría")
plt.show()

###############################################################3#
#2)  GRAFICO DE SECTORES: PORCENTAJE DE ARTICULOS POR PROVINCIA
provincias = df_3["provincia"].value_counts()

#Obtener los nombres del indice
indice = list(provincias.index)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = indice
sizes = provincias
#fig1, ax1 = plt.subplots()
plt.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Porcentaje de objetos por provincia")
plt.show()

################################################################3
#3) GRÁFICO DE BARRAS: PRODUCTO CON MAYOR PRECIO POR CADA CATEGORÍA
maximos = df_3.groupby('categoria')["precio_fraccion"].max()

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = list(maximos.sort_values(ascending=True).index)
y_pos = np.arange(len(people))
performance = maximos.sort_values(ascending=True)
#error = np.random.rand(len(people))

ax.barh(y_pos, performance)
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Precio')
ax.set_title('Precios máxmos por cada categoría')

plt.show()
###################################################################3
#4) GRAFICO DE BARRAS: PALABRAS MAS FRECUENTES EN LOS TITULOS
from collections import Counter #Fuente https://stackoverflow.com/questions/29903025/count-most-frequent-100-words-from-sentences-in-dataframe-pandas
fp = Counter(" ".join(df_3["titulo"]).split()).most_common(50)
frec_pal_1= pd.DataFrame(fp)
frec_pal_1[0]



names = list(frec_pal_1[0])
values = list(frec_pal_1[1])
fig, axs = plt.subplots()
axs.bar(names, values)
fig.suptitle('Palabras más usadas en los títulos')
plt.xticks(rotation=90)
plt.show()
#fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
#axs[0].bar(names, values)
#axs[1].scatter(names, values)
#axs[2].plot(names, values)
################################################3333
#5) GRÁFICO DE LINEAS: NUMERO DE PRODUCTOS POR CATEGORÍA EN PICHINCHA VS GUAYAS


#codigo para buscar un string en una columna del dataframe
pichincha_completo= df_3[df_3["provincia"].str.contains("Pichincha")]
pichincha_categoria=pichincha_completo["categoria"].value_counts()
pichincha_categoria.sort_index(ascending=True)
guayas_completo= df_3[df_3["provincia"].str.contains("Guayas")]
guayas_categoria=guayas_completo["categoria"].value_counts()
guayas_categoria.sort_index(ascending=True)
categorias_provincias = list(guayas_categoria.sort_index(ascending=True).index) 


Pich = list(pichincha_categoria.sort_index(ascending=True))
Guay = list(guayas_categoria.sort_index(ascending=True))
activity = categorias_provincias

fig, ax = plt.subplots()
ax.plot(activity, Guay, label="Guayas")
ax.plot(activity,Pich, label="Pichincha")
ax.legend()
plt.xticks(rotation=90)
plt.title("Productos por categoria en Pichincha y Guayas")
plt.show()

############################################################3
#6) GRAFICO DE PUNTOS: NOMBRE DE PRODUCTOS REPETIDOS MAS DE 8 VECES

conteo_titulos_original = df_3["titulo"].value_counts()
conteo_titulos= conteo_titulos_original[(conteo_titulos_original>8)]


names = list(conteo_titulos.index)
values = list(conteo_titulos)
fig, axs = plt.subplots()
axs.scatter(names, values)
fig.suptitle('Productos con nombres repetidos')
plt.xticks(rotation=90)
plt.show()




