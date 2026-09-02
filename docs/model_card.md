# NAVASHRAYA — Model Card Specification

This model card documents the machine learning algorithms and decision-support scoring models integrated into NAVASHRAYA.

---

## 1. Landslide Susceptibility Model (Random Forest)

- **Model Name**: Navashraya Landslide Susceptibility Classifier (NLSC-v1)
- **Model Type**: Random Forest Classifier / XGBoost Ensemble
- **Version**: 1.0.0
- **Primary Purpose**: Predict high-resolution spatial landslide susceptibility probabilities across Wayanad habitations based on geo-environmental terrain factors.
- **Target Variable**: Landslide Occurrence (`1` = Landslide location, `0` = Non-landslide background sample).
- **Predictor Features**:
  1. Elevation (DEM metres)
  2. Slope angle (degrees)
  3. Aspect (degrees)
  4. Topographic Wetness Index (TWI)
  5. Distance to Drainage / Streams (metres)
  6. Distance to Road Cuts (metres)
  7. Land-Use / Land-Cover (LULC class)
  8. Lithology / Soil Type
  9. Antecedent Rainfall (mm)
- **Training Method**: 80/20 Spatial Block Cross-Validation (to prevent spatial autocorrelation data leakage).
- **Evaluation Metrics**: ROC-AUC, PR-AUC, Precision, Recall, F1-Score, Spatial Confusion Matrix.
- **Explainability Engine**: SHAP (SHapley Additive exPlanations) tree explainer.
- **Limitations**: Model predictions reflect physical terrain susceptibility under historic rainfall patterns. Extreme unmodeled cloudburst events (>300mm/24h) require dynamic scenario simulation.

---

## 2. Multi-Hazard & Risk Fusion Model

- **Model Name**: Composite Multi-Hazard Risk Aggregator (CMHRA-v1)
- **Methodology**: Weighted Normalized Risk Index ($\text{Risk} = \text{Hazard} \times \text{Exposure} \times \text{Vulnerability}$).
- **Hazard Components**: Landslide Susceptibility ($50\%$), Flood Exposure ($30\%$), Rainfall Scenario ($20\%$).
- **Exposure/Vulnerability**: Population Density, Critical Infrastructure Exposure.

---

## 3. Relocation Decision Engine (AHP + TOPSIS)

- **Model Name**: Optimal Relocation Site Selector (ORSS-v1)
- **Methodology**: Analytic Hierarchy Process (AHP) criteria weighting + TOPSIS ideal vector ranking.
- **Criteria**:
  - Safety Score (AHP weight ~0.40)
  - Distance Score (AHP weight ~0.25)
  - Infrastructure & Services Access (AHP weight ~0.20)
  - Carrying Capacity & Usable Land (AHP weight ~0.15)
- **Consistency Verification**: Rejects weighting matrices with Consistency Ratio $CR \ge 0.10$.
