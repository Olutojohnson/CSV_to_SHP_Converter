# Import required libraries
import pandas as pd
import geopandas as gpd

# Load the data from a CSV file
data = pd.read_csv('data.csv')

# Convert the DataFrame to a GeoDataFrame with geometry based on longitude and latitude
data_gdf = gpd.GeoDataFrame(
    data, 
    geometry=gpd.points_from_xy(data['longitude'], data['latitude'])
)

# Specify the Coordinate Reference System (CRS) in ESRI WKT format
crs_wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

# Save the GeoDataFrame as a shapefile
data_gdf.to_file(filename='data.shp', driver='ESRI Shapefile', crs_wkt=crs_wkt)

print("Shapefile created successfully: data.shp")
