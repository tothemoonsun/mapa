import geopandas as gpd
import pandas as pd
import folium

# Cargar el archivo Shapefile de provincias
provincias = gpd.read_file('provincia.shp')

# Cargar el archivo de datos
data = pd.read_csv('resultados.txt', sep='|', encoding='utf-8')

# Contar el número de ocurrencias de cada provincia
provincia_counts = data['provincia'].value_counts().reset_index()
provincia_counts.columns = ['provincia', 'cantidad']

# Unir el DataFrame de conteo con el DataFrame de provincias
provincias = provincias.merge(provincia_counts, left_on='nam', right_on='provincia', how='left')

# Crear un mapa interactivo con Folium
mapa = folium.Map(location=[-38.4161, -63.6167], zoom_start=4)

# Agregar las geometrías de las provincias al mapa
folium.GeoJson(provincias,
                name='Provincias',
                style_function=lambda x: {'fillColor': 'blue', 'fillOpacity': 0.5, 'color': 'black', 'weight': 1},
                highlight_function=lambda x: {'fillColor': 'red', 'fillOpacity': 0.8},
                tooltip=folium.features.GeoJsonTooltip(fields=['nam', 'cantidad'],
                                                        aliases=['Provincia', 'Cantidad'],
                                                        labels=True,
                                                        sticky=True)
                ).add_to(mapa)

# Añadir control de capas
folium.LayerControl().add_to(mapa)

# Guardar el mapa como archivo HTML
mapa.save('mapa_interactivo.html')