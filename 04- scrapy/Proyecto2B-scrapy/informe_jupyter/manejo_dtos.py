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
#1) 
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

################################################################3
#2
estado_civil_edad = df_3[["p02","p06"]]

sexo_masc_bol=estado_civil_edad["p02"]=="Hombre"
sexo_masc=estado_civil_edad[sexo_masc_bol]
ecsmc = sexo_masc["p06"].value_counts()
sexo_fem_bol=estado_civil_edad["p02"]=="Mujer"
sexo_fem=estado_civil_edad[sexo_fem_bol]
ecsfc = sexo_fem["p06"].value_counts()
etiquetasEstadoCivil=list(ecsfc.index)
labels = etiquetasEstadoCivil
men_means = ecsmc
women_means = ecsfc

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
plt.figure(figsize=(80,20))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Hombres')
rects2 = ax.bar(x + width/2, women_means, width, label='Mujeres')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Número de personas')
ax.set_title('Número de personas por estado civil y sexo')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()

plt.show()