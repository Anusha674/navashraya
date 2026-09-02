# NAVASHRAYA — Research & Referral Master Specification

> **Comprehensive Research Methodology, Data Source Provenance, and Scientific References Guide**

---

## 1. Executive Summary & Research Framework

**NAVASHRAYA** is a research-backed decision support platform engineered for disaster management authorities (**MHA, NDRF, KSDMA**). The system combines remote sensing spatial datasets, machine learning hazard susceptibility modeling, Multi-Criteria Decision Making (MCDM), and Explainable AI (SHAP) to identify critical red zones and recommend safe, carrying-capacity-matched relocation habitations.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                      PRIMARY GEO-SPATIAL DATASETS                        │
│   • ISRO Bhuvan (LULC, Cartosat DEM)   • GSI Landslide Inventory        │
│   • Survey of India (SOI Boundaries)   • Census 2011 Population Data    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    PREDICTIVE MACHINE LEARNING                          │
│   • Random Forest Classifier (Terrain Factors: Slope, TWI, Aspect)     │
│   • Multi-Hazard Risk Aggregation: Risk = Hazard × Exposure × Vuln     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                 DECISION SUPPORT & RELOCATION RANKING                   │
│   • AHP (Saaty 1980) Pairwise Weighting                                 │
│   • TOPSIS (Hwang & Yoon 1981) Relative Closeness Ranking               │
│   • Carrying Capacity Matching & Safe Corridor Routing                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Key Geo-Spatial Platforms & Primary Data Sources

### 2.1 ISRO Bhuvan (National Remote Sensing Centre - NRSC / ISRO)
- **Organization**: Indian Space Research Organisation (ISRO) / NRSC, Hyderabad
- **Portal**: [Bhuvan Geo-Spatial Platform](https://bhuvan.nrsc.gov.in)
- **Role in NAVASHRAYA**:
  - **Digital Elevation Model (DEM)**: Utilizes Cartosat-1 30m DEM and ALOS PALSAR Datasets derived from ISRO Bhuvan to extract terrain elevation, slope gradient (in degrees), aspect, and Topographic Wetness Index (TWI).
  - **Land Use / Land Cover (LULC)**: 1:50,000 scale LULC maps from Bhuvan for vegetation cover, plantation boundaries, and built-up land detection.
  - **Disaster Management Support Services (DMSS)**: Provides satellite-based inundation overlays and historical flood frequency data during extreme monsoon events in the Western Ghats (Wayanad region).

### 2.2 Geological Survey of India (GSI) — NLSM Project
- **Organization**: Geological Survey of India, Ministry of Mines, Govt. of India
- **Dataset**: National Landslide Susceptibility Mapping (NLSM) 1:50,000 Scale Inventory
- **Role in NAVASHRAYA**:
  - Provides historical landslide occurrence polygons, debris flow channels, and high-susceptibility zone boundaries.
  - Serves as the ground-truth target vector for training the Random Forest landslide prediction model.

### 2.3 Survey of India (SOI)
- **Organization**: National Survey and Mapping Organization of India
- **Dataset**: Official Administrative Village Boundaries (Kerala State)
- **Role in NAVASHRAYA**:
  - Provides precise administrative boundary MultiPolygons (`villages` database geometry) in EPSG:4326 WGS84 and UTM Zone 43N projections.

### 2.4 Census of India (Registrar General & Census Commissioner)
- **Dataset**: Census 2011 Primary Census Abstract (PCA) for Wayanad District
- **Role in NAVASHRAYA**:
  - Delivers official village-level population figures used to calculate human exposure density and destination carrying capacity limits.

### 2.5 Kerala State Disaster Management Authority (KSDMA)
- **Organization**: Government of Kerala
- **Dataset**: KSDMP Hazard Maps & Extreme Rainfall Trigger Thresholds
- **Role in NAVASHRAYA**:
  - Provides state-level flood plain vector overlays, river basin geometries, and extreme monsoon (+25% intensity) scenario simulation thresholds.

---

## 3. Scientific Methodology & Analytical Models

### 3.1 Machine Learning Landslide Susceptibility Model
Predicts landslide susceptibility probability ($0 - 100\%$) across Wayanad habitations using an ensemble Random Forest model trained on geo-environmental conditioning factors:
- **Conditioning Variables**:
  1. Slope Angle ($>35^\circ$ critical threshold)
  2. Elevation (meters above sea level)
  3. Proximity to Streams / Drainage Channels
  4. Proximity to Road Cuts (Anthropogenic instability)
  5. Topographic Wetness Index ($\text{TWI} = \ln(a / \tan \beta)$)
  6. Land Use / Land Cover (ISRO Bhuvan classification)

### 3.2 Multi-Hazard Risk Aggregation (UNDRR Sendai Framework)
Combines independent hazard layers into a unified operational risk score:

$$\text{Risk Score} = \text{Hazard Score} \times \text{Exposure Factor} \times \text{Vulnerability Index}$$

$$\text{Multi-Hazard Score} = (0.50 \times \text{Landslide Score}) + (0.50 \times \text{Flood Exposure } \%)$$

### 3.3 Analytic Hierarchy Process (AHP) — Saaty (1980)
Determines objective criterion weights for relocation destination evaluation through pairwise comparisons:
- **Criteria**: Safety Index ($W_1 = 0.40$), Geodesic Distance ($W_2 = 0.25$), Road Access ($W_3 = 0.15$), Available Safe Land ($W_4 = 0.20$).
- **Consistency Verification**: Ensures Consistency Ratio $CR = \frac{CI}{RI} < 0.10$ to prevent subjective bias.

### 3.4 TOPSIS Relocation Ranking — Hwang & Yoon (1981)
Ranks safe candidate destination habitations by calculating relative closeness ($C_i^*$) to the Positive Ideal Solution ($A^*$) and Negative Ideal Solution ($A^-$):

$$C_i^* = \frac{D_i^-}{D_i^* + D_i^-}$$

Where $D_i^*$ is Euclidean distance to ideal safe attributes and $D_i^-$ is distance to anti-ideal attributes.

### 3.5 Explainable AI (SHAP) — Lundberg & Lee (2017)
Provides feature contribution attribution ($\phi_i$) for disaster response officers to inspect why a specific village is classified as High Risk (e.g., Slope $+0.24$, Rainfall $+0.16$).

---

## 4. Bibliographic References Registry

1. **ISRO Bhuvan Geo-Spatial Data Portal (2022)**  
   *National Remote Sensing Centre (NRSC), Indian Space Research Organisation (ISRO).*  
   URL: [https://bhuvan.nrsc.gov.in](https://bhuvan.nrsc.gov.in)  
   *Application*: Source for Cartosat DEM, satellite imagery, LULC layers, and disaster inundation mapping.

2. **Geological Survey of India (GSI) (2021)**  
   *National Landslide Susceptibility Mapping (NLSM) Protocol & Western Ghats Inventory Report.*  
   URL: [https://www.gsi.gov.in](https://www.gsi.gov.in)  
   *Application*: Spatial landslide inventory polygons and susceptibility classification guidelines.

3. **Saaty, Thomas L. (1980)**  
   *The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation.*  
   McGraw-Hill, New York.  
   *Application*: Pairwise comparison matrix mathematics for AHP criterion weight derivation.

4. **Hwang, Ching-Lai & Yoon, Kwangsun (1981)**  
   *Multiple Attribute Decision Making: Methods and Applications.*  
   Springer-Verlag, Berlin Heidelberg. DOI: [10.1007/978-3-642-48318-0](https://doi.org/10.1007/978-3-642-48318-0)  
   *Application*: TOPSIS algorithm implementation for candidate relocation site ranking.

5. **United Nations Office for Disaster Risk Reduction (UNDRR) (2015)**  
   *Sendai Framework for Disaster Risk Reduction 2015–2030.*  
   URL: [https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030](https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030)  
   *Application*: Disaster risk equation conceptual framework and resettlement priorities.

6. **Lundberg, Scott M. & Lee, Su-In (2017)**  
   *A Unified Approach to Interpreting Model Predictions (SHAP).*  
   Advances in Neural Information Processing Systems (NeurIPS 30).  
   URL: [https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions)  
   *Application*: Explainable AI tree SHAP values for model feature interpretability.

7. **Kerala State Disaster Management Authority (KSDMA) (2020)**  
   *Kerala State Disaster Management Plan & Wayanad Risk Profile.*  
   URL: [https://sdma.kerala.gov.in](https://sdma.kerala.gov.in)  
   *Application*: State hazard zoning, flood plain boundaries, and rainfall scenario benchmarks.

---

© NAVASHRAYA Decision Support Platform — *Safe Today, Stronger Tomorrow.*
