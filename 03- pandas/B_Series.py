# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:37 2019

@author: PedroW10
"""
import numpy as np
import pandas as pd

#SEries  en pandas
lista_numeros=  [1,2,3,4]
tupla_numeros= (1,2,3,4)
np_numeros=  np.array((1,2,3,4))

#creacion de series
serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)

serie_d = pd.Series([True, False, 12,
                     12.12, "Adrian", 
                     None, (),[],
                     {"par":"valor"}])

serie_d[3]
#lista de ciudades
lista_ciudades = ["Ambato","Cuenca", "Loja", "Quito"]

#crear una serie sin uqe los indices sean solo los numeros, 

serie_ciudades= pd.Series(lista_ciudades, index=
                          ['A','C','L','Q'])
serie_ciudades[3]

valores_ciudad={
        "Ibarra":500,
        "Guayaquil":654,
        "Cuenca":654,
        "Quito":789,
        "Loja":1000}

serie_valor_ciudad= pd.Series(valores_ciudad)

serie_valor_ciudad["Guayaquil"]

serie_ciudades_menor_700 = serie_valor_ciudad[serie_valor_ciudad<700]
#Aniadir un 10* mas a todas las ciudadess
serie_presupuesto_mas_10=serie_valor_ciudad*1.1

#penalizar a Quito
#bajar 50% a Quito
 serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"]*0.5
 
 #
 print ("Lima" in serie_valor_ciudad)
 print ("Loja" in serie_valor_ciudad)


#USO DE UNIVERSASL FUNCTIONS EN SERIES,
# EL RESULTADO ES OTRA SERIES
#Elevar al cuadrado el presupuesto de todos
 r_square= np.square(serie_valor_ciudad)
 #sacar el seno
 r_sin = np.sin(serie_valor_ciudad)



ciudades_uno= pd.Series(
        {
                "Montañita":300,
                "Guayaquil":10000,
                "Quito":2000})

ciudades_dos= pd.Series(
        {
                "Loja":300,
                "Guayaquil":10000
                })

#Calcular la suma de los valores
print(ciudades_uno + ciudades_dos)

ciudades_uno["Loja"]= 65465
ciudades_dos["Montañita"]= 123456
ciudades_dos["Quito"]= 4000

ciudades_uno+ciudades_dos


#ci
ciudad= ciudades_uno.add(ciudades_dos)

ciudades_concatenadas = pd.concat([ciudades_uno, ciudades_dos])
ciudades_concatenadas_vi = pd.concat([ciudades_uno, ciudades_dos],verify_integrity=True)

ciud_append= ciudades_uno.append(ciudades_dos)


ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)


#Estadistica
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

#obetener los cinco primeros datos
ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(ascending=False).tail(2)



















