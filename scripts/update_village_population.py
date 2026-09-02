import geopandas as gpd
import psycopg2
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

file = PROJECT_ROOT / "data" / "raw" / "vb_soi_kl.GeoJSON"

print("Reading original Kerala village data...")

gdf = gpd.read_file(file)

# Keep Wayanad only
gdf = gdf[
    gdf["district"].astype(str).str.strip().str.lower() == "wayanad"
].copy()

population_column = "total_population_village\n"

print("Wayanad villages found:", len(gdf))

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="navashraya",
    user="navashraya",
    password="navashraya"
)

cur = conn.cursor()

updated = 0

for _, row in gdf.iterrows():

    village = str(row["village"]).strip()

    population = row[population_column]

    if population is None:
        continue

    population = int(float(population))

    cur.execute(
        """
        UPDATE villages
        SET population = %s
        WHERE LOWER(TRIM(name)) = LOWER(TRIM(%s));
        """,
        (population, village)
    )

    if cur.rowcount > 0:
        updated += 1

conn.commit()

cur.close()
conn.close()

print("\n===== POPULATION UPDATE COMPLETE =====")
print("Villages updated:", updated)