# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:21 2019

@author: PedroW10
"""

import numpy as np
import pandas as pd

#randint(valormas bajo, valor mas alto, tamanio del arreglo)
arr_pand = np.random.randint(0,10,6).reshape(2,3)
arr_pand

df1= pd.DataFrame(arr_pand)
s1= df1[0]
s2= df1[1]
s3= df1[2]

s4=pd.Series(np.arange(2))
df1[3]=s4
df1[4]= s1*s2

datos_fisicos1 = pd.DataFrame(arr_pand,columns=["Estatura (cm)","Peso (Kg)","Edad (anios)"])
datos_fisicos1["Estatura (cm)"]
datos_fisicos2=pd.DataFrame(arr_pand,index=["Adrian","Vicente"],columns=["Estatura (cm)","Peso (Kg)","Edad (anios)"])

df1.index=["Adrian","Vicente"]
df1.index[0]="a" #Index does not support mutable operations
df1.columns=["A","B","C","D","E"]