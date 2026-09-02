import geopandas as gpd
from pathlib import Path
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
file = PROJECT_ROOT / "data" / "raw" / "flood" / "Wayanad_Flood.geojson"

print("Reading flood GeoJSON...")

gdf = gpd.read_file(file)

print("\n===== BASIC INFO =====")
print("Features:", len(gdf))
print("CRS:", gdf.crs)

print("\n===== NAME VALUES =====")
print(gdf["Name"].value_counts())

print("\n===== DESCRIPTION SAMPLE =====")

for i in range(min(5, len(gdf))):
    description = gdf.iloc[i]["description"]

    print(f"\n--- FEATURE {i} ---")

    if description is None:
        print("No description")
        continue

    soup = BeautifulSoup(description, "html.parser")
    text = soup.get_text(" ", strip=True)

    print(text[:2000])