# NAVASHRAYA — Research-Backed Methodology Specification

## 1. Overview & Pipeline

NAVASHRAYA is an intelligent decision support platform designed for disaster management authorities (NDRF, MHA, KSDMA) to identify hazard red zones, perform carrying capacity assessment, and recommend optimal habitation relocation.

```text
MULTI-SOURCE GIS DATA (DEM, Rainfall, Land Use, GSI Shapefiles, Census)
        ↓
FEATURE ENGINEERING (Elevation, Slope, Aspect, Drainage, Road Proximity)
        ↓
HAZARD SUSCEPTIBILITY (Random Forest / XGBoost ML Model)
        ↓
MULTI-HAZARD FUSION (Landslide + Flood + Rainfall Scenario)
        ↓
EXPOSURE & VULNERABILITY (Population, Social/Physical Infrastructure)
        ↓
COMPOSITE RISK (Hazard × Exposure × Vulnerability)
        ↓
RELOCATION PRIORITIZATION (Immediate, Short-Term, Medium-Term, Monitor)
        ↓
SAFE SITE IDENTIFICATION (Safety Filter, Usable Land Filter)
        ↓
SITE SUITABILITY RANKING (Analytic Hierarchy Process + TOPSIS)
        ↓
CARRYING CAPACITY (Usable Land Area, Housing, Infrastructure, Resource Constraints)
        ↓
HABITATION → SITE MATCHING (Optimal Allocation & Capacity Balance)
        ↓
EXPLAINABLE AI (SHAP Feature Importance Attribution)
        ↓
OFFICER DECISION SUPPORT (Interactive GIS Map, Scenario Simulation, Reports)
```

---

## 2. Landslide Susceptibility Methodology

Predictive machine learning models (Random Forest, XGBoost) evaluate environmental factor rasters derived from Digital Elevation Models (DEM) and remote sensing data:
- **Predictor Variables**: Elevation, Slope, Aspect, Curvature, Distance to Streams, Distance to Roads, Land-Use/Land-Cover (LULC), Soil Type, Lithology/Geology.
- **Historical Inventory**: Geological Survey of India (GSI) landslide inventory polygons.
- **Validation**: Spatial block k-fold cross-validation to prevent spatial autocorrelation leakage.

---

## 3. Multi-Hazard Fusion

Composite hazard calculation normalizes independent hazard layers on a 0–100 scale:
$$\text{Composite Hazard} = W_1 \cdot H_{\text{landslide}} + W_2 \cdot H_{\text{flood}} + W_3 \cdot H_{\text{rainfall\_scenario}} + W_4 \cdot H_{\text{historical}}$$

---

## 4. Disaster Risk Assessment

Standard UNDRR risk framework:
$$\text{Risk} = \text{Hazard} \times \text{Exposure} \times \text{Vulnerability}$$
Normalized to an operational range [0, 100].

---

## 5. Analytic Hierarchy Process (AHP) & TOPSIS Ranking

- **AHP**: Derives objective weights for relocation criteria (Safety, Distance, Road Access, Healthcare, Education, Usable Land) through pairwise comparisons, ensuring Consistency Ratio $CR < 0.10$.
- **TOPSIS**: Ranks candidate relocation sites by measuring relative closeness to the Positive Ideal Solution ($A^*$) and Negative Ideal Solution ($A^-$).

---

## 6. Carrying Capacity Assessment

Calculates net safe population capacity for safe destination zones:
$$\text{Available Capacity} = \left( \frac{\text{Usable Safe Land Area}}{\text{Land Area Per Capita Requirement}} \right) \times \text{Resource Constraint Factor} - \text{Existing Population}$$

---

## 7. Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) values provide local model feature attribution, allowing disaster officers to inspect exact factor contributions (e.g., Slope +0.24, Rainfall +0.16) for any red-zone classification.
