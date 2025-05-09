# -*- coding: utf-8 -*-
"""
Created on Thu May  8 16:06:52 2025

@author: aag
"""
import pandas as pd 
df = pd.read_csv(r"bmw.csv")

#Mostrar 10 primeros registros tabla (ej1)

print(df.head(10))

#Obtener serie correspondiente a attrib 'year' a continuacion obtener tipo de dato y numero de registros
#de dicha serie (ej2)
serieAnyo=df['year']
print(serieAnyo)
print("----------------------------------")
serieAnyo.dtype #muestra tipo de dato
len(serieAnyo) #muestra cantidad de registros con dicho atrib
print("----------------------------------")

#Obtenga la serie correspondiente al atributo mileage, y después seleccione los
#registros de posición multiplo de 7 en dicha serie. (ej3)
millas = df['mileage']
print(millas)
print("----------------------------------")
millasMultiplosDe7 = millas.iloc[::7]
print(millasMultiplosDe7)
print("----------------------------------")

#Obtenga la serie correspondiente al atributo mileage, y despues seleccione
#aleatoriamente el 40% de los registros de dicha serie. (ej4) 
print(millas.sample(frac=0.4, random_state=1))
print("----------------------------------")

#Obtenga la serie correspondiente al atributo mileage, y después seleccione los
#registros de dicha serie con valor menor que 20000. (ej5)
print(millas[millas<20000])
print("----------------------------------")
#Extra: buscar coche con 1 milla y sacar info de el 
print(millas[millas==1])
print(df.iloc[2150])
print("----------------------------------")

#Obtenga la serie correspondiente al atributo mpg, y después ordene los registros de
#dicha serie. (ej6)
print(df['mpg'].sort_values())
print("----------------------------------")

#Calcule la media, la desviación ơpica, el mínimo y el máximo del atributo engineSize. (ej7)
print(df['engineSize'].agg(['mean', 'std', 'min', 'max']))
print("----------------------------------x")

#Obtenga el número de filas y columnas de la base de datos, así como el antepenúltimo
#registro. (ej8)
filas,columnas = df.shape
print(filas)
print(columnas)
print(df.iloc[-3])
print("----------------------------------")

#Obtenga los atributos mileage, price y mpg en un nuevo DataFrame, y después
#seleccione aleatoriamente el 20% de los registros. (ej9)
df_selected = df[['mileage', 'price', 'mpg']]
df_sample = df_selected.sample(frac=0.2, random_state = 2)
print(df_sample)
print("----------------------------------")
#Extra: pasar dataframe a excel 
print("----------------------------------")

#Obtenga los registros que tengan un valor de mileage inferior a 10000 y un valor de
#mpg mayor que 40. (ej10)
df_filtrao = df[(df['mileage']<10000) & (df['mpg'] > 40)]
print(df_filtrao)
print("----------------------------------")

#Modifique los valores del atributo model, de tal manera que los valores " x Series"
#pasen a ser "Serie x", siendo x un número entre 1 y 9. (ej11)
df['model']=df['model'].str.replace(r'(\d) Series', r'Series \1', regex=True)
print(df)
print("----------------------------------")

#Inserte un nuevo registro con los siguientes datos: model=" 3 Series", year=2023, price
#= 22572, transmission = "Automatic", mileage = 74120, fuelType = "Diesel", tax = 160,
#mpg = 58.4, engineSize = 2.0 (ej12)
micoche=pd.DataFrame([{
    'model': "3 Series", 
    'year': 2023, 
    'price': 22572, 
    'transmission': "Automatic", 
    'mileage': 74120, 
    'fuelType': "Diesel", 
    'tax': 160, 
    'mpg': 58.4, 
    'engineSize': 2.0}])
print(micoche)
print("----------------------------------")
#Hasta aqui he creado el registro, ahora lo inserto
df=pd.concat([df, micoche], ignore_index=True)
print(df)
print("----------------------------------")
print(df.iloc[len(df)-1])
print("----------------------------------")

#Convierta el DataFrame en un ndarray de numpy, e imprima el tipo de datos del
#ndarray obtenido (ej13)
matriz=df.to_numpy()
print(matriz)
print("----------------------------------")

#Calcule para cada registro el número medio de millas recorridas cada año. (ej14)
df['miles per year'] = df['mileage'] / (2025-df['year'])
print(df)




