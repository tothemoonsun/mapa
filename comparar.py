import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Shapefile (.shp) desde la misma carpeta que el script
provincias = gpd.read_file('provincia.shp')

# Cargar el archivo de texto con los datos de provincias
data = pd.read_csv('resultados.txt', sep='|', encoding='utf-8')

# Contar el número de ocurrencias de cada provincia
provincia_counts = data['provincia'].value_counts().reset_index()
provincia_counts.columns = ['provincia', 'cantidad']

# Unir el DataFrame de provincias con el de conteo
provincias = provincias.merge(provincia_counts, left_on='nam', right_on='provincia', how='left')

# Visualizar el mapa
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
provincias.plot(column='cantidad', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, legend_kwds={'label': 'Cantidad de Ocurrencias', 'orientation': 'vertical'})
ax.set_title('Cantidad de Ocurrencias por Provincia en Argentina', fontsize=16)
ax.set_xlabel('Longitud', fontsize=12)
ax.set_ylabel('Latitud', fontsize=12)

# Agregar etiquetas de texto con valores
for idx, row in provincias.iterrows():
    ax.text(row.geometry.centroid.x, row.geometry.centroid.y, str(row['cantidad']), fontsize=8, ha='center', color='black')

# Agregar la rosa de los vientos en la esquina superior derecha
ax.annotate('N', xy=(0.98, 0.98), xycoords='axes fraction', ha='center', fontsize=12, color='black')
ax.annotate('S', xy=(0.98, 0.02), xycoords='axes fraction', ha='center', fontsize=12, color='black')
ax.annotate('E', xy=(0.02, 0.98), xycoords='axes fraction', ha='center', fontsize=12, color='black')
ax.annotate('O', xy=(0.98, 0.98), xycoords='axes fraction', ha='center', fontsize=12, color='black')

plt.show()