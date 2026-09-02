import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

input_file = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "flood"
    / "Wayanad_Flood.geojson"
)

output_file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "wayanad_flood_zones.geojson"
)

output_file.parent.mkdir(parents=True, exist_ok=True)

print("Reading flood data...")

gdf = gpd.read_file(input_file)

# Keep only useful columns
gdf = gdf[["id", "Name", "geometry"]].copy()

# Rename columns
gdf = gdf.rename(columns={
    "id": "flood_id",
    "Name": "flood_type"
})

# Ensure WGS84
gdf = gdf.to_crs(epsg=4326)

# Remove invalid/empty geometries
gdf = gdf[gdf.geometry.notna()]
gdf = gdf[~gdf.geometry.is_empty]

print("\n===== FLOOD ZONES =====")
print("Features:", len(gdf))
print("\nFlood types:")
print(gdf["flood_type"].value_counts())

print("\nCRS:", gdf.crs)

gdf.to_file(
    output_file,
    driver="GeoJSON"
)

print("\nSaved:")
print(output_file)