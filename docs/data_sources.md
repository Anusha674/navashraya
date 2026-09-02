# NAVASHRAYA — Data Sources & Provenance Registry

Every dataset used in NAVASHRAYA is tracked with strict provenance classification to ensure complete scientific honesty and transparency for disaster management officers.

---

## Provenance Classification Definitions

- **`REAL`**: Official government or scientific dataset directly imported and used without spatial distortion.
- **`DERIVED`**: Mathematically or spatially calculated from real datasets (e.g., slope derived from DEM, intersection area % calculated via PostGIS `ST_Intersection`).
- **`PROXY`**: Scientifically defensible approximation used when exact fine-grained field data is unavailable.
- **`SYNTHETIC`**: Artificial demonstration data generated explicitly for prototype testing.

---

## Data Source Registry

| Dataset Name | Source Organization | Resolution / Scale | Provenance Status | Usage in System |
| :--- | :--- | :--- | :--- | :--- |
| **Kerala Village Boundaries** | Survey of India (SOI) | Vector MultiPolygon | **`REAL`** | Administrative boundary geometry for all villages in Wayanad |
| **Landslide Inventory** | Geological Survey of India (GSI) | Vector Shapefile | **`REAL`** | Historical landslide susceptibility zones (`High`, `Moderate`, `Low`) |
| **Wayanad Flood Plain** | KSDMA / State Water Dept | Vector GeoJSON | **`REAL`** | Spatial flood plain boundaries |
| **Village Population** | Census of India / Local Bodies | Village-level | **`REAL`** | Population exposure & carrying capacity demand |
| **Landslide Area Overlay %** | Derived via PostGIS (`calculate_landslide_exposure.sql`) | Spatial Intersection | **`DERIVED`** | Percentage of village area overlapping GSI landslide zones |
| **Flood Exposure Overlay %** | Derived via PostGIS (`calculate_flood_exposure.sql`) | Spatial Intersection | **`DERIVED`** | Percentage of village area overlapping flood plains |
| **Geodesic Village Distance** | Calculated via PostGIS (`ST_Distance` EPSG:32643) | Kilometers | **`DERIVED`** | Centroid-to-centroid distance between habitations |
| **Multi-Hazard Score** | Derived via composite weighting engine | Score [0, 100] | **`DERIVED`** | Integrated hazard risk indicator |
| **Relocation Priority Rank** | Derived via AHP & TOPSIS algorithms | Rank [1..N] | **`DERIVED`** | Ranked safe destination recommendations |
| **Usable Land Net Capacity** | Carrying Capacity Module | Estimated Population | **`PROXY`** | Demonstration carrying capacity estimate for safe destination sites |
