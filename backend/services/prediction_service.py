import joblib
import pandas as pd
import os
from core.logging_config import setup_logger

logger = setup_logger(__name__)

MODEL_PATH = os.getenv("MODEL_PATH", "model/model_lgbm.pkl")
_model = None

def get_model():
    global _model
    if _model is None:
        logger.info(f"Cargando modelo desde {MODEL_PATH}")
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_diabetes(input_data: dict) -> dict:
    logger.info("Realizando predicción de diabetes")
    model = get_model()
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0]
    logger.info(f"Predicción: {prediction}, Probabilidades: {proba}")
    return {
        "predicted_diabetes": int(prediction),
        "probability_no_diabetes": float(proba[0]),
        "probability_prediabetes": float(proba[1]),
        "probability_diabetes": float(proba[2]),
    }