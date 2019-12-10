# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:40 2019

@author: PedroW10
"""

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
path_sav="C:\\Users\\PedroW10\\Downloads\\BDD_ENEMDU_2019_06_SPSS\\BDD_ENEMDU_2019_06_SPSS\\201906_EnemduBDD_15anios.sav"
df1 = pd.read_stata(path_sav);
#no funcionan 
# pd.read_sas
# pd.read_stata


#Carga con pyreadstat
#pip install pyreadstat
import pyreadstat
path_sav_1="C:/Users/PedroW10/Downloads/BDD_ENEMDU_2019_06_SPSS/BDD_ENEMDU_2019_06_SPSS/201906_EnemduBDD_15anios.sav"
df_3, meta = pyreadstat.read_sav(path_sav,apply_value_formats=True)
























