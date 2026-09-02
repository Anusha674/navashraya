import geopandas as gpd
from pathlib import Path

folder = Path("data/raw/flood")

files = list(folder.glob("*.shp")) + list(folder.glob("*.geojson")) + list(folder.glob("*.GeoJSON"))

if not files:
    print("ERROR: No flood GIS file found.")
    print("Put the .shp or .GeoJSON flood file inside:")
    print(folder.resolve())
    raise SystemExit(1)

file = files[0]

print(f"Reading: {file}")
gdf = gpd.read_file(file)

print("\n===== FLOOD DATASET =====")
print("Number of features:", len(gdf))

print("\n===== COLUMNS =====")
print(list(gdf.columns))

print("\n===== CRS =====")
print(gdf.crs)

print("\n===== GEOMETRY TYPES =====")
print(gdf.geometry.geom_type.value_counts())

print("\n===== SAMPLE ATTRIBUTES =====")
print(gdf.drop(columns="geometry").head())

print("\n===== BOUNDS =====")
print(gdf.total_bounds)