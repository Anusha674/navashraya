import geopandas as gpd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

input_file = PROJECT_ROOT / "data" / "raw" / "flood" / "Flood_KML" / "Wayanad.kmz"
output_file = PROJECT_ROOT / "data" / "raw" / "flood" / "Wayanad_Flood.geojson"

print("Input:", input_file)

if not input_file.exists():
    print("ERROR: Wayanad.kmz not found!")
    raise SystemExit(1)

print("\nReading Wayanad flood data...")

gdf = gpd.read_file(input_file)

print("\n===== ORIGINAL DATA =====")
print("Features:", len(gdf))
print("CRS:", gdf.crs)

print("\n===== GEOMETRY TYPES =====")
print(gdf.geometry.geom_type.value_counts())

print("\n===== COLUMNS =====")
print(list(gdf.columns))

print("\n===== SAMPLE ATTRIBUTES =====")
print(gdf.drop(columns="geometry").head())

# Convert to WGS84
if gdf.crs is not None:
    gdf = gdf.to_crs(epsg=4326)

# Remove empty geometries
gdf = gdf[gdf.geometry.notna() & ~gdf.geometry.is_empty]

gdf.to_file(
    output_file,
    driver="GeoJSON"
)

print("\n===== CONVERSION COMPLETE =====")
print("Saved:", output_file)
print("Features:", len(gdf))
print("CRS:", gdf.crs)