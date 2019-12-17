# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:14 2019

@author: PedroW10
"""

import pandas as pd
import numpy as np

path_guardado_bin="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data_full.pickle"
df=pd.read_pickle(path_guardado_bin)

primero = df.loc[1035, 'artist']
primero

primero1 = df.loc[1035]
primero1



df2 = df.set_index('id')
#uso de iloc
primero2 = df.iloc[1035]
primero2


#####################

"""
            nota1   disciplina
Pepito        7         5
Juanita       8         9
Maria         9         2


"""

valores ={
        "Pepito":{
                "nota1": 7,
                "disciplina":5
                },
        "Juanita":{
                "nota1": 8,
                "disciplina":9
                },
        "Maria":{
                "nota1": 9,
                "disciplina":2
                },
        }
        
df3= pd.DataFrame(valores)





valores1 ={
         "nota1":{
                  "Pepito": 7,
                  "Juanita":8,
                  "Maria":9
                 },
        "disciplina":{
                  "Pepito": 5,
                  "Juanita":9,
                  "Maria":2
                 }
         
        }
df3= pd.DataFrame(valores1)
##LOC PUEDE FILRAR CON LABELS O INDICES
pepito_loc= df3.loc[0]
pepito_loc= df3.loc["Pepito"]

##ILOC SOLO PERMITE INDICES
pepito_iloc= df3.iloc[0]

##
df3.loc["Pepito","disciplina"]
#otener varias columnas con el loc, enviar un arreglo de strings
df3.loc["Pepito",["disciplina", "nota1"]]
#        indice , arreglo de campos
#

df3.loc[["Pepito","Juanita"],["disciplina", "nota1"]]
#       arreglo de indices  ,  arreglo de columnas

#se puede filtrar con un arreglo de condiciones
df3.loc[df3["nota1"]>7]



df3.loc[df3["nota1"]>7][ df3["disciplina"]>7]

df3.loc[["Maria"],["disciplina"]] =7


#a quienes tienen mas de 7 setear a 7
df3.loc[df3["nota1"]>7] =7




#agregar el mismo valor a Pepito, por buen comportamiento
df3.loc[["Pepito"]] =10

#solo la columna de disciplina de todos 
#los estudiantes bjar a 7
#usar : para seleccionar todos los indices
df3.loc[:,["disciplina"]] =7



#Aniadir la columna promedio
df3["promedio"] = 0
df3["promedio"] = df3["nota1"] * df3["disciplina"] /2

