import pandas as pd 
import numpy as np

#Cargar CSV y mostrar la info
peliculas = pd.read_csv('peliculas.csv')
print(peliculas.info())

#Asignar genero aleatorio
generos = ['Accion', 'Comedia', 'Drama', 'Terror', 'Ciencia Ficcion']
peliculas['genero'] = np.random.choice(generos, len(peliculas))

#Eliminar ultima columna (vacia)
peliculas = peliculas.iloc[:, :-1]

#Director unknown si NaN
peliculas['director'] = peliculas['director'].fillna('Desconocido')

#Recaudacion = mediana si NaN
peliculas['recaudacion'] = peliculas['recaudacion'].fillna(peliculas['recaudacion'].median())

#Eliminar duplicados 
peliculas = peliculas.drop_duplicates()

#Promedio puntacion por genero
promedio_puntuacion = peliculas.groupby('genero')['puntuacion'].mean().reset_index()
print("\nPuntuacion media por genero: ")
print(promedio_puntuacion)

#Clasificar exito
p75 = peliculas['recaudacion'].quantile(0.75)
peliculas['exito'] = np.where(peliculas['recaudacion']>p75, 'Alta Recaudacion', 'Baja Recaudacion')

#Mostrar resumen de peliculas con exito
print("\nPeliculas clasificadas por exito: ")
print(peliculas[['titulo', 'recaudacion', 'exito']].head())

#Mostrar distribucion de recaudacion (tabla)
describe_ingresos = peliculas['recaudacion'].describe()
print("\nResumen estadistico de ingresos: ")
print(describe_ingresos)