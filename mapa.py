import folium
import geopandas as gpd
import pandas as pd

# Cargar el archivo Shapefile (.shp) de las provincias de Argentina
provincias = gpd.read_file('provincia.shp')

# Cargar los datos del archivo de texto
data = pd.read_csv('resultados.txt', sep='|', encoding='utf-8')

# Contar el número de ocurrencias de cada provincia
provincia_counts = data['provincia'].value_counts().reset_index()
provincia_counts.columns = ['provincia', 'cantidad']

# Unir los datos de conteo con los datos de las provincias
provincias = provincias.merge(provincia_counts, on='provincia', how='left')

# Crear un mapa centrado en Argentina
mapa = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

# Agregar las provincias al mapa con círculos proporcionales al número de ocurrencias
for index, row in provincias.iterrows():
    folium.Circle(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],  # Centroides de las provincias
        radius=row['cantidad'] * 100,  # El radio se multiplica para que los círculos sean más visibles
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6,
        tooltip=row['provincia'] + ': ' + str(row['cantidad'])
    ).add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save('mapa_interactivo.html')