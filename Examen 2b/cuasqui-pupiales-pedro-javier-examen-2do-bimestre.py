# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:31:11 2020

@author: PedroW10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Examen
#1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros

df1=pd.DataFrame(np.random.rand(10,6))

df1.head(5) #primeras 5
df1.tail(5) #ultimas 5





#2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988

indices=["2013-01-01","2013-01-02","2013-01-03","2013-01-04","2013-01-05","2013-01-06"]

df2= pd.DataFrame(np.random.rand(6,4), index=indices, columns=["A","B","C","D"])






#4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.

df3=pd.DataFrame(np.random.rand(10,6))

list(df3.columns) #columnas
df3.values #valores





#5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe
df5=pd.DataFrame(np.random.rand(10,6))

df3.describe() # descripci'on, minimo, maximo, average, etc..





#6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos
df6=pd.DataFrame(np.random.rand(10,6))
df6T= df6.T




#7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente
df7=pd.DataFrame(np.random.rand(10,6))
df7.sort_values(by=[0], ascending=False)
df7.sort_values(by=[0], ascending=True)
df7.sort_values(by=[1], ascending=False)
df7.sort_values(by=[1], ascending=True)
df7.sort_values(by=[2], ascending=False)
df7.sort_values(by=[2], ascending=True)
df7.sort_values(by=[3], ascending=False)
df7.sort_values(by=[3], ascending=True)
df7.sort_values(by=[4], ascending=False)
df7.sort_values(by=[3], ascending=True)
df7.sort_values(by=[5], ascending=False)
df7.sort_values(by=[5], ascending=True)






# 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7
df8=pd.DataFrame(np.random.randint(1,10,(10,6)))

df8f=df8[:][df8>7]








#9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.
df9=df8f
df9.replace({np.nan:0})









#10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio
df10 = pd.DataFrame(np.random.randint(1,10,(10,6)))

df10.median() #Mediana
df10.mean() #Media, Promedio






#11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

df11= pd.DataFrame(np.random.randint(1,10,(10,6)))
df11_1= pd.DataFrame(np.random.randint(1,10,(10,6)))

df11.append(df11_1)








#12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

listaStrings=["a","b","c","d","e","f","g","h","i","j"]

df12= pd.DataFrame(np.random.choice(listaStrings,(10,6)))

df12["01"]=df12[0].str.cat(df12[1])
df12["12"]=df12[2].str.cat(df12[3])
df12["13"]=df12[4].str.cat(df12[5])









#13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna

df13 = pd.DataFrame(np.random.randint(1,10,(10,6)))


for columna in df13:
    print(df13[columna].value_counts())







#14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C
df14 = pd.DataFrame(np.random.randint(1,10,(10,3)), columns=["A","B","C"])

df14["A*B/C"]= (df14["A"]*df14["B"])/df14["C"]
