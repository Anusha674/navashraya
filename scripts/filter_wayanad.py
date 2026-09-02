import geopandas as gpd
import os

# Input Kerala village dataset
input_file = r"D:\navashraya\data\raw\vb_soi_kl.GeoJSON"

# Output folder
output_folder = r"D:\navashraya\data\processed"
os.makedirs(output_folder, exist_ok=True)

# Read Kerala villages
gdf = gpd.read_file(input_file)

print("Total Kerala villages:", len(gdf))

# Check district names
print("\nDistricts found:")
print(sorted(gdf["district"].dropna().unique()))

# Filter Wayanad
wayanad = gdf[
    gdf["district"]
    .astype(str)
    .str.strip()
    .str.lower()
    == "wayanad"
].copy()

print("\nWayanad villages:", len(wayanad))

# Convert to standard web mapping CRS
wayanad = wayanad.to_crs(epsg=4326)

# Save Wayanad dataset
output_file = os.path.join(
    output_folder,
    "wayanad_villages.geojson"
)

wayanad.to_file(output_file, driver="GeoJSON")

print("\nSaved to:")
print(output_file)