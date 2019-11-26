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