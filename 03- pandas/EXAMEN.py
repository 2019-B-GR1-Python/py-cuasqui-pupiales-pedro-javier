# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:17:36 2019

@author: PedroW10
"""

#2) Crear un vector de ceros de tamaño 10

import numpy as np
arr_ceros=np.zeros(10)






#3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
diez= np.zeros(10)
diez[5]=1









#4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc
arr_50= np.arange(51)
arr_50_inver= arr_50[::-1]






#5) Crear una matriz de 3 x 3 con valores del cero al 8
cinco= np.arange(9).reshape(3,3)









#6) Encontrar los indices que no sean cero en un arreglo
#import numpy as np
arreglo = [1,2,0,0,4,0]
arr_1=np.array(arreglo)
cond =(arr_1!=0)
arr_1[cond]







#7) Crear una matriz de identidad 3 x 3
np.identity(3)







#8) Crear una matriz 3 x 3 x 3 con valores randomicos
random = np.random.rand(3,3,3)
random





#9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
matriz = np.arange(100).reshape(10,10)
menor = matriz.min()
mayor = matriz.max()

#**************************************
#10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

import numpy as np
img = np.arange(144).reshape(6,8,3)
import matplotlib.pyplot as plt
plt.imshow(img)

unicos= np.unique(img, axis=1)
unicos



#11) ¿Como crear una serie de una lista, diccionario o arreglo?
import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

mylistS= pd.Series(mylist)
myarrS= pd.Series(myarr)
mydictS= pd.Series(mydict)









#12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
df= pd.DataFrame(ser, columns=["indice"])




#13) ¿Como combinar varias series para hacer un DataFrame?
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

dataframe = pd.DataFrame(ser1)
dataframe[1]=ser2




#14) ¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

unicos =np.isin(ser1,ser2, invert=True)
serUnicos= ser1[unicos]




#**************************************************************
#15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

nocomunes= np.intersect1d(ser1,ser2 )


#16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
dfcounts= pd.DataFrame(ser)
conteo_repetidos= dfcounts[0].value_counts()

#*********************************************
#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))




#************************************************
#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
#shape(7,5)
transforma= pd.DataFrame(ser)






#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u

ser[pos]




#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
# serie vertical 
dataSerie = pd.DataFrame(ser1)
dataSerie[1]=ser2
#serie horizontal
dataSerie1 = pd.concat([ser1,ser2],axis=0)

#21)¿Obtener la media de una serie agrupada por otra serie?
#groupby tambien esta disponible en series.
#
#frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
#pesos = pd.Series(np.linspace(1, 10, 10))
#print(pesos.tolist())
#print(frutas.tolist())
##> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
##> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']
#
## Los valores van a cambiar por ser random
## apple     6.0
## banana    4.0
## carrot    5.8
## dtype: float64
#




#22)¿Como importar solo columnas especificas de un archivo csv?
#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.
import os
path= "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
dfImportado= pd.read_csv(path)
columnas=["crim","age"]
dfImportado_1= pd.read_csv(path,usecols=columnas)






