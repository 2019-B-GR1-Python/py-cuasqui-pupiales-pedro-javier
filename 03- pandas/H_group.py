# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:42 2020

@author: PedroW10
"""



import pandas as pd
import numpy as np
import math

path_guardado_bin="C:\\Users\\PedroW10\\Documents\\GitHub\\py-cuasqui-pupiales-pedro-javier\\03- pandas\\data\\artwork_data_full.pickle"
df=pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()


df_agrupado = seccion_df.groupby('artist')

type(df_agrupado)


for columna_agrupada, df_completo in df_agrupado:
    print(type(columna_agrupada))
    print(type(df_completo))
        
#el primer parametro devuelve los valroes de la columna agrupada
for columna_agrupada, df_completo in df_agrupado:
    print(columna_agrupada)
    print(df_completo)
    
#Definir una funcion que reciba una serie y ejecute ciertas operaciones
    
#contar valores por columna unit    
a=seccion_df['units'].value_counts() #retorna el numero de variables por cada valor diferente
#verifca si la columna se encuentra vacia
print(a)
a.empty

c=seccion_df['artist'].value_counts() #retorna el numero de variables por cada valor diferente
#verifca si la columna se encuentra vacia
print(c)
c.idxmax()


b=seccion_df['depth'].value_counts() #retorna vacio, entonces esta columna no podemos usarla
b.empty



def llenar_valores_vacios(series,tipo):
    lista_valores= series.value_counts()
    if(lista_valores.empty):
        return series
    else:
    #Se establecen dos estrategias para llenar los valores de columnas vacias 
        if(tipo == 'promedio'):
            #El for y su contenido puede ser reemplazado por numpy.nanmean
            #promedio = np.nanmean(series)
            #series_valores_llenos = series.fillna(promedio)
            #return series_valores_llenos
        
            suma = 0
            numero_valores = 0
            
            for valor_serie in series:
                if(isinstance(valor_serie,str)):
                    valor= int(valor_serie)
                #validar que el valor no sea nan en el registro 
                    numero_valores = numero_valores+1
                    suma= suma+ valor
                #transformar los vaores que por defecto se cargaron como strings a int
                else:
                    pass
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        if(tipo =="value_counts"):
            conteo_unidades = series.value_counts()          
            print(conteo_unidades.idxmax())
            series_valores_llenos = series.fillna(conteo_unidades.idxmax())
            return series_valores_llenos
       
        
            
    
#Se llamamrá a la funciona    
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df_agrupados= [] #esta lista contendrá los df con nan reemplazados
    
    for artista,df in df_artist:
        copia = df.copy() #se prueba con width y height
        serie_w= copia['width']
        serie_h= copia['height']
        serie_u= copia['units']
        serie_i= copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w,"promedio")
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h,"promedio")
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u,"value_counts")
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i,"value_counts")
        
        lista_df_agrupados.append(copia)
    df_completo_con_valores = pd.concat(lista_df_agrupados)
    return df_completo_con_valores
    
df_valores_llenos= transformar_df(seccion_df)
#el artista Wols no tiene valores en inscription por tanto no se modifican sus valores
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    