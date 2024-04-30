import pandas as pd
import geopandas as gpd

provincias = gpd.read_file('provincia.shp')
print(provincias)

provincias.to_excel('output.xlsx', index=False)