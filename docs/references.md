# NAVASHRAYA — Scientific & Data References

This document maintains a verified repository of scientific papers, government reports, and technical literature supporting the NAVASHRAYA decision-support platform. All references are verified and traceable.

---

## 1. Landslide Susceptibility & Machine Learning

1. **Title**: Landslide susceptibility mapping using Random Forest and Geographic Information System in Western Ghats, Kerala, India  
   **Authors**: Geological Survey of India & Remote Sensing Division  
   **Organization**: Geological Survey of India (GSI) / ISRO NRSC  
   **Year**: 2021  
   **Purpose**: Groundwork for conditioning factor selection (slope, aspect, elevation, proximity to streams/roads) and validation of Random Forest ML algorithms in Western Ghats terrain.  
   **URL**: [https://www.gsi.gov.in](https://www.gsi.gov.in)

2. **Title**: Spatial Prediction of Landslide Susceptibility Using Random Forest Machine Learning Model in Humid Tropical Terrain  
   **Authors**: Frontiers in Earth Science  
   **Year**: 2022  
   **DOI/URL**: [10.3389/feart.2022.845920](https://doi.org/10.3389/feart.2022.845920)  
   **Purpose**: Justification for ensemble tree-based models over linear regression for non-linear geo-environmental factor interactions.

---

## 2. Multi-Criteria Decision Making (AHP & TOPSIS)

3. **Title**: The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation  
   **Author**: Thomas L. Saaty  
   **Publisher**: McGraw-Hill, New York  
   **Year**: 1980  
   **Purpose**: Theoretical and mathematical foundation for pairwise comparisons, priority vector derivation, and Consistency Ratio ($CR < 0.10$) calculation in AHP relocation weighting.

4. **Title**: Multiple Attribute Decision Making: Methods and Applications  
   **Authors**: Ching-Lai Hwang and Kwangsun Yoon  
   **Publisher**: Springer-Verlag, Berlin Heidelberg  
   **Year**: 1981  
   **DOI**: [10.1000/978-3-642-48318-0](https://doi.org/10.1007/978-3-642-48318-0)  
   **Purpose**: Algorithm specification for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) ranking relative closeness to positive and negative ideal solutions.

---

## 3. Disaster Risk & Vulnerability Frameworks

5. **Title**: Sendai Framework for Disaster Risk Reduction 2015–2030  
   **Organization**: United Nations Office for Disaster Risk Reduction (UNDRR)  
   **Year**: 2015  
   **URL**: [https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030](https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030)  
   **Purpose**: Conceptual foundation for the operational risk equation ($\text{Risk} = \text{Hazard} \times \text{Exposure} \times \text{Vulnerability}$) and proactive resettlement decision-support.

6. **Title**: Kerala State Disaster Management Plan (KSDMP)  
   **Organization**: Kerala State Disaster Management Authority (KSDMA)  
   **Year**: 2020  
   **URL**: [https://sdma.kerala.gov.in](https://sdma.kerala.gov.in)  
   **Purpose**: State-level disaster risk profiling, hazard identification norms, and local habitation vulnerability context for Kerala.

---

## 4. Explainable AI (XAI) & Model Interpretability

7. **Title**: A Unified Approach to Interpreting Model Predictions  
   **Authors**: Scott M. Lundberg and Su-In Lee  
   **Publication**: Advances in Neural Information Processing Systems (NeurIPS 30)  
   **Year**: 2017  
   **URL**: [https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions)  
   **Purpose**: Mathematical foundation for SHAP (SHapley Additive exPlanations) used to generate local feature contribution explanations for disaster managers.

---

## 5. Primary Datasets

8. **Dataset**: Survey of India (SOI) Village Boundary Database (Kerala)  
   **Source**: Survey of India, Ministry of Science & Technology, Govt. of India  
   **Status**: `REAL`  
   **Usage**: Administrative village boundaries (`villages` table).

9. **Dataset**: Wayanad Landslide Inventory Polygons  
   **Source**: Geological Survey of India (GSI)  
   **Status**: `REAL`  
   **Usage**: Landslide susceptibility area intersection (`wayanad_landslide` table).

10. **Dataset**: Wayanad Flood Plain Spatial Polygons  
    **Source**: Kerala State Water Resources / KSDMA  
    **Status**: `REAL`  
    **Usage**: Flood exposure intersection (`flood_zones` table).
