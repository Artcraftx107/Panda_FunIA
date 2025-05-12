import pandas as pd
import numpy as np

np.random.seed(1)

productos = pd.DataFrame({
    'id': range(1, 101),
    'precio_unitario': np.random.uniform(1, 1000, 100).round(2)
})

fechas = np.random.choice(
    pd.date_range('2024-01-01', '2024-12-31'), 
    5000)

ventas = pd.DataFrame({
    'fecha_venta': fechas,
    'id': np.random.randint(1, 101, 5000),
    'cantidad': np.random.randint(1, 31, 5000)
})

#Adding unit price and import 
ventas = ventas.merge(productos, on='id')
ventas['importe'] = ventas['cantidad']*ventas['precio_unitario']

#Grouping by month and product
ventas['mes'] = ventas['fecha_venta'].dt.to_period('M')
ventas_mensual = ventas.groupby(['mes', 'id'])['cantidad'].sum().reset_index()

#Media movil 3 meses 
ventas_mensual['mes'] = ventas_mensual['mes'].dt.to_timestamp()
ventas_mensual.sort_values(['id', 'mes'], inplace = True)
ventas_mensual['media_movil_3meses']= ventas_mensual.groupby('id')['cantidad'].transform(lambda x: x.rolling(3, min_periods = 1).mean())

#Detectar productos en declive 
def detectar_declive(serie): 
    return all(serie[i] > serie[i+1] for i in range(len(serie)-1))

productos_declive = []
for pid, grupo in ventas_mensual.groupby('id'):
    mm = grupo['media_movil_3meses'].values
    if len(mm)>=4: 
        for i in range(len(mm)-3): 
            if detectar_declive(mm[i:i+4]): 
                productos_declive.append(pid)
                break

productos_declive = list(set(productos_declive))

#Mostrar resultados 
print("Productos en declive (ID): ")
print(productos_declive)

print("\nEvolucion de ventas (media movil 3 meses) de productos en declive: ")
print(ventas_mensual[ventas_mensual['id'].isin(productos_declive)])




 