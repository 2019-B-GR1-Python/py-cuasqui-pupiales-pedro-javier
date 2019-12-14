# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:40 2019

@author: PedroW10
"""
#Apuntes:
#Cuando usar pandas o numpy : https://medium.com/@ericvanrees/pandas-series-objects-and-numpy-arrays-15dfe05919d7
import pandas as pd
import os 
#archivos que se pueden leer con pandas
# 1) JSON, CSV, HTML, XML
# 2) Binay Files
# 3) Ralational Databases

path="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data.csv"

df= pd.read_csv(path,nrows=10)
#Seleccionar columnas especificas
columnas=['id','artist','title','medium','year','acquisitionYear','height','width','units']
df2= pd.read_csv(path,nrows=10,usecols=columnas)

#Asignar la columna id al indice
df3= pd.read_csv(path,nrows=10,usecols=columnas, index_col="id")

#Guardar el dataframe en formato pickle
pathGuardado="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data.pickle"
df3.to_pickle(pathGuardado)

pathGuardadoCompleto="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data_full.pickle"
df4= pd.read_csv(path)
df4.to_pickle(pathGuardadoCompleto)

df5= pd.read_pickle(pathGuardadoCompleto)
#

#Practica de carga archivo spss (.sav)
#Fuente: https://stackoverflow.com/questions/14647006/is-there-a-python-module-to-open-spss-files
path_sav="C:\\Users\\PedroW10\\Downloads\\BDD_ENEMDU_2019_06_SPSS\\BDD_ENEMDU_2019_06_SPSS\\201906_EnemduBDD_15anios.sav"
#Carga con pyreadstat
#pip install pyreadstat
import pyreadstat
df_3, meta = pyreadstat.read_sav(path_sav,apply_value_formats=True)

hombresMujeres= df_3["p02"].value_counts()
#Obtener los nombre de los indices 1
indice = list(hombresMujeres.index)
#Obtener los nombre de los indices 2
indicesHomMuj = list(hombresMujeres.head().index)


#Ejemplo de gráfica
import matplotlib.pyplot as plt
plt.plot(indicesHomMuj,hombresMujeres)
plt.show()

descripcion= df_3.describe()
#group by
agrupacion = df_3.groupby(["area","vivienda"])
df_1=agrupacion.first()

df_3[""]



                                   


#  _ _ _                   _           
# | (_) |__  _ __ ___ _ __(_) __ _ ___ 
# | | | '_ \| '__/ _ \ '__| |/ _` / __|
# | | | |_) | | |  __/ |  | | (_| \__ \
# |_|_|_.__/|_|  \___|_|  |_|\__,_|___/
#                                      
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyreadstat



#CARGA DE DATOS
#Fuente: https://stackoverflow.com/questions/14647006/is-there-a-python-module-to-open-spss-files
#path_sav="C:\\Users\\PedroW10\\Downloads\\BDD_ENEMDU_2019_06_SPSS\\BDD_ENEMDU_2019_06_SPSS\\201906_EnemduBDD_15anios.sav"
path_sav="https://github.com/2019-B-GR1-Python/py-cuasqui-pupiales-pedro-javier/blob/master/Informe1b/201906_EnemduBDD_15anios.sav"
#Carga con pyreadstat
df_3, meta = pyreadstat.read_sav(path_sav,apply_value_formats=True)







#1 GRAFICO DE PASTEL del PORCENTAJE DE ENCUESTADOS 
hombresMujeres= df_3["p02"].value_counts()
#Obtener los nombre de los indices 1
indice = list(hombresMujeres.index)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = indice
sizes = hombresMujeres

#fig1, ax1 = plt.subplots()
plt.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Porcentaje de encuestados por sexo")
plt.show()









# ESTADO CIVIL DE LOS ENCUSTADOS
estadocivilvalores= df_3["p06"].value_counts()
estadociviltag = list(hombresMujeres.index)








#2 ESTADO CIVIL POR SEXO
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










#3 PERSONAS POR CADA TIPO DE INSTRUCCION
#edades unicas
edades= df_3["p03"]
edades_1=edades.replace({"98 y más": 98, "No informa": 150})
unicas1 = edades_1.drop_duplicates()


# Fixing random state for reproducibility
#np.random.seed(19680801)
instruccionEdad= df_3[["p03","p10a"]]
instruccionEdad_1=instruccionEdad.groupby("p10a").count()
cod_instruccion=[2,7,5,1,10,4,6,9,8]
instruccionEdad_1["cod_instruccion"]=cod_instruccion

#edades_unique = instruccion.drop_duplicates()

N = 50
x = instruccionEdad_1["p03"]
y = instruccionEdad_1["cod_instruccion"]
colors = ["red","green","blue","orange","violet","brown","yellow","red","red"]
area = (30 *1 )**2  # 0 to 15 point radii
#np.random.rand(10)
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title("Número de personas por nivel académico")
plt.xlabel("Número de personas")
plt.ylabel("Nivel académico")
plt.show()
#
#p10a	p03	cod_instruccion
#Centro de alfabetización	161	2
#Educación  Media	7203	7
#Educación Básica	13499	5
#Ninguno	2306	1
#Post-grado	672	10
#Primaria	13463	4
#Secundaria	10709	6
#Superior Universitario	7527	9
#Superior no universitario	885	8



# 4INGRESO PER CAPITA EN EL SECTOR URBANO Y RURAL
df_ingreso_per_capita = df_3[["area","ingpc"]]
df_ingreso_per_capita_grouped= df_ingreso_per_capita.groupby("area").mean()
df_ingreso_per_capita_grouped.index
plt.barh(df_ingreso_per_capita_grouped.index, df_ingreso_per_capita_grouped["ingpc"])
plt.title("Ingreso per cápita promedio por area")
plt.text(150,1,df_ingreso_per_capita_grouped["ingpc"][1])
plt.text(50,0,df_ingreso_per_capita_grouped["ingpc"][0])
plt.xlabel("Ingreso promedio $")
plt.ylabel("Area")
plt.show()






# 5 HISTOGRAMA DE EDADES 
# the histogram of the data
edades = df_3["p03"]
edades_2=edades.replace({"98 y más": 98, "No informa": 150})

n, bins, patches = plt.hist(edades_2, 75, density=True, facecolor='g', alpha=1)
plt.xlabel('Edad')
plt.ylabel('Número de personas')
plt.title('Número de personas entrevistadas por edad')
#plt.xlim(40, 160)
#plt.ylim(0, 1)
plt.grid(True)
plt.show()
















#6 IMÁGEN DE INGRESOS PER CAPITA
#Fuente: https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/subplots_adjust.html#sphx-glr-gallery-subplots-axes-and-figures-subplots-adjust-py
# Fixing random state for reproducibility

np.sqrt(np.size(df_3["ingpc"]))
ingpc_matrix = np.array(df_3["ingpc"])[0:60270].reshape(245,246)
plt.subplot(212)
plt.imshow(ingpc_matrix, cmap=plt.cm.BuPu_r)

plt.subplots_adjust(bottom=0.1, right=1, top=2)
cax = plt.axes([0.85, 0.1, 0.075, 0.865])
plt.colorbar(cax=cax)
plt.title("Imágen de ingresos per capita")
plt.show()










# 7 NUMERO DE PERSONAS POR SEGURO DE VIDA

#Fuente: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/polar_bar.html#sphx-glr-gallery-pie-and-polar-charts-polar-bar-py
personas_seguro= df_3["p05A"].value_counts()/ len(df_3["p05A"])

numero_personas_seguro= np.size(np.array(personas_seguro))

theta = np.linspace(0.0, 2 * np.pi, numero_personas_seguro, endpoint=False)
#radii = 10 * np.random.rand(N)
radii = 10 * personas_seguro
width = np.pi / 4 * personas_seguro
colors = plt.cm.viridis(radii / 10.)

ax = plt.subplot(111, projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
plt.title("Porcentaje de personas que contratan un seguro de vida")
plt.show()











#8 NUMERO DE AÑOS VIVIENDO EN EL MISMO LUGAR 
anios_viviendo_lugar= df_3["p16b"].value_counts()

anios_viviendo_diferentes= list(anios_viviendo_lugar.index)
# Fixing random state for reproducibility
np.random.seed(19680801)
x = anios_viviendo_diferentes
y = anios_viviendo_lugar
plt.figure()
# Scatter plot on top of lines
plt.subplot(212)
plt.plot(x, y, 'C3', zorder=1, lw=3)
plt.scatter(x, y, s=120, zorder=2)
plt.title('Años viviendo en el mismo lugar')
plt.xlabel("Número de años")
plt.ylabel("Número de personas")
plt.tight_layout()









# 9 NUMERO DE SEMANAS QUE UNA PERSONA NO HA TRABAJADO
semanas_no_trabaja = df_3["p39"].value_counts()
semanas_no_trabaja_index = list(semanas_no_trabaja.index)

ax = plt.subplot(111)
t1 = semanas_no_trabaja
#for n in [1, 2, 3, 4]:
plt.plot(semanas_no_trabaja_index, t1, label="semanas")

leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)

plt.title("Número de semanas que no ha trabajado por numero de personas")
plt.xlabel("Número de semanas")
plt.ylabel("Número de personas")
plt.show()











#10 ETNIA A LA QUE CONSIDERA QUE PERTENECE
#Fuente; lhttps://www.youtube.com/watch?v=5yVKSB-WtuM
como_se_considera = df_3["p15"].value_counts() /len(df_3["p15"])


labels= list(como_se_considera.index)
sizes= como_se_considera

plt.pie(sizes,labels=labels, autopct='%1.1f%%')
plt.axis('equal')

circle=plt.Circle(xy=(0,0), radius= 0.65, facecolor="white")
plt.gca().add_artist(circle)
plt.title("Como se consideran las personas entrevistadas")
plt.show()











#