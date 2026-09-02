import geopandas as gpd

file = r"D:\navashraya\data\raw\vb_soi_kl.GeoJSON"

gdf = gpd.read_file(file)

print("\n===== DATASET INFORMATION =====")
print("Number of villages:", len(gdf))

print("\n===== COLUMNS =====")
print(gdf.columns.tolist())

print("\n===== COORDINATE SYSTEM =====")
print(gdf.crs)

print("\n===== FIRST 5 RECORDS =====")
print(gdf.head())