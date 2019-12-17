# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:50:09 2019

@author: PedroW10
"""

import pandas as pd
path_guardado_bin="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data_full.pickle"
df=pd.read_pickle(path_guardado_bin)


#df = df5.iloc[49980:50019,:].copy()


#obtener los nombres de los artistas
serie_artistas_repetidos = df["artist"]
#obtener los nombres no repetidos de cada artistas
artistas= pd.unique(serie_artistas_repetidos)
#longitus del arreglo
artistas.size
len(artistas)

#obtener solo las obras del artista BLAKE, William

blake = df["artist"]=='Blake, William'

blake.value_counts() #indica cuantos hay de cada uno

df["artist"].value_counts()
#Filtra en el mismo orden las obras de blake
df_blake = df[blake]