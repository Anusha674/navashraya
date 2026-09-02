import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, List

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
MODEL_FILE = PROJECT_ROOT / "data" / "processed" / "wayanad_landslide_rf.joblib"
FEATURE_COLUMNS = ["elevation", "slope", "aspect", "dist_stream", "dist_road", "twi"]

class LandslidePredictor:
    """
    Inference Engine for Landslide Susceptibility ML Model.
    """

    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            if not MODEL_FILE.exists():
                from app.ml.train_landslide import train_landslide_susceptibility_model
                train_landslide_susceptibility_model()
            cls._model = joblib.load(MODEL_FILE)
        return cls._model

    @classmethod
    def predict_susceptibility(cls, feature_dict: Dict[str, float]) -> Dict[str, Any]:
        """
        Calculates Landslide Susceptibility Probability & Score (0-100) for a feature vector.
        """
        model = cls.load_model()
        df_feat = pd.DataFrame([feature_dict])[FEATURE_COLUMNS]
        
        prob = float(model.predict_proba(df_feat)[0, 1])
        score = round(prob * 100.0, 2)
        
        level = "High" if score >= 60.0 else ("Moderate" if score >= 35.0 else "Low")
        
        return {
            "susceptibility_probability": round(prob, 4),
            "susceptibility_score": score,
            "susceptibility_level": level
        }
