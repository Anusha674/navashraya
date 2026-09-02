# NAVASHRAYA — Disaster Relocation Decision Support Platform

> **Motto:** *Safe Today, Stronger Tomorrow.*

NAVASHRAYA is an intelligent decision support platform designed for disaster management authorities (**MHA, NDRF, KSDMA**) to conduct multi-hazard risk assessments, evaluate carrying capacity, and identify optimal habitation relocation corridors.

---

## 🌟 Key Features

- **Multi-Hazard Risk Fusion**: Integrates landslide susceptibility index models and flood plain spatial overlays.
- **AHP + TOPSIS Site Recommendation**: Ranks safe candidate relocation zones based on safety, carrying capacity, road accessibility, and geodesic proximity.
- **Carrying Capacity Matching**: Computes usable safe land area against population housing requirements to prevent destination overcrowding.
- **What-If Extreme Rainfall Simulation**: Interactive scenario toggling to simulate +25% extreme rainfall escalation on terrain stability.
- **Executive Decision Reports**: Dynamic printable report generation with structured risk metrics, relocation corridors, and administrative directives.
- **GIS Relocation Map**: Leaflet-powered GIS mapping displaying affected source habitations (Red), recommended safe destinations (Green), and relocation corridors (Blue).

---

## 📐 Core Analytical Formulas

### 1. Disaster Risk Framework (UNDRR Standard)
```text
Risk = Hazard × Exposure × Vulnerability
```

### 2. Multi-Hazard Fusion Index
```text
Multi-Hazard Score = (0.50 × Landslide Score) + (0.50 × Flood Exposure %)
```

### 3. Safe Relocation Ranking (AHP + TOPSIS)
```text
Relocation Score = (0.60 × Safety Score) + (0.25 × Proximity Score) + 15
```

### 4. Destination Carrying Capacity
```text
Available Capacity = (Usable Safe Land Area ÷ Land Required per Person) - Existing Population
```

---

## 🏗 Project Architecture

```text
navashraya/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI REST Endpoints (Villages, Hazards, Relocation)
│   │   ├── core/         # Configuration & Database connection
│   │   ├── gis/          # PostGIS spatial feature extraction
│   │   ├── ml/           # Landslide Susceptibility RF Model & Inference Engine
│   │   └── services/     # GIS & Relocation decision logic
│   ├── database.py
│   └── main.py           # Application entry point
├── frontend/
│   ├── index.html        # Main dashboard interface
│   ├── style.css         # Clean 2-Color Green & White styling system
│   ├── app.js            # Leaflet map logic, API interactions & report generator
│   └── logo.jpg          # Platform brand logo
├── data/                 # Processing spatial datasets & GeoJSON geometry
├── docs/                 # Methodology, Model Cards, and References
└── docker-compose.yml    # Container orchestration configuration
```

---

## 🛠 Tech Stack

- **Backend**: FastAPI (Python 3.12), PostGIS / PostgreSQL, GeoPandas, Scikit-learn
- **Frontend**: HTML5, Vanilla CSS3 (Green & White Palette), JavaScript (ES6+), Leaflet.js
- **GIS Data**: Survey of India (SOI) boundaries, Geological Survey of India (GSI) inventory, Census 2011 Data

---

## 🚀 Quick Start (Local Setup)

### 1. Backend Server Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
The API server will run at `http://127.0.0.1:8000`.

### 2. Frontend Launch
Serve the `frontend/` directory using any HTTP server:
```bash
cd frontend
python -m http.server 8080
```
Open `http://127.0.0.1:8080/index.html` in your web browser.

---

## 🚢 Deployment

### Docker Deployment
```bash
docker-compose up --build -d
```

### GitHub Pages / Static Hosting
The `frontend/` directory is static and ready to be served directly via GitHub Pages or Vercel/Netlify pointing to `frontend/index.html`.

---

## 📜 References & Standard Guidelines

- **Geological Survey of India (2021)**: Landslide susceptibility mapping in Western Ghats, Kerala.
- **Thomas L. Saaty (1980)**: The Analytic Hierarchy Process (AHP).
- **Hwang & Yoon (1981)**: Technique for Order Preference by Similarity to Ideal Solution (TOPSIS).

---

© NAVASHRAYA Decision Support Platform — *Safe Today, Stronger Tomorrow.*
