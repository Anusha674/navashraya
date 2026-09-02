import geopandas as gpd

file = r"D:\navashraya\data\processed\wayanad_villages.geojson"

gdf = gpd.read_file(file)

print("\n===== WAYANAD DATASET =====")
print("Number of villages:", len(gdf))

print("\n===== CRS =====")
print(gdf.crs)

print("\n===== VILLAGE NAMES =====")
print(gdf["village"].tolist())

print("\n===== POPULATION =====")
print(
    gdf[
        [
            "village",
            "total_population_village\n",
            "total_households\n",
            "total_geographical_area\n"
        ]
    ].to_string(index=False)
)

print("\n===== IMPORTANT COLUMNS =====")

important_columns = [
    "village",
    "district",
    "block",
    "subdistric",
    "gram_panchayat_name\n",
    "total_population_village\n",
    "total_households\n",
    "total_geographical_area\n",
    "forest_area\n",
    "nearest_town_name\n",
    "nearest_town_distance_from_village\n",
    "geometry"
]

for column in important_columns:
    if column in gdf.columns:
        print("✓", column)
    else:
        print("✗ MISSING:", column)