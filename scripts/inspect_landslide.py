import geopandas as gpd

file = r"D:\navashraya\data\raw\landslide\Wayanad\Wayanad_GSI_LS.shp"

print("Reading landslide dataset...")

gdf = gpd.read_file(file)

print("\n===== LANDSLIDE DATASET =====")
print("Number of features:", len(gdf))

print("\n===== COLUMNS =====")
print(gdf.columns.tolist())

print("\n===== CRS =====")
print(gdf.crs)

print("\n===== GEOMETRY TYPES =====")
print(gdf.geometry.geom_type.value_counts())

print("\n===== SUSCEPTIBILITY =====")
print(gdf["Susceptibi"].value_counts())

print("\n===== SAMPLE ATTRIBUTES =====")
print(
    gdf[["Susceptibi"]]
    .head(10)
    .to_string(index=False)
)