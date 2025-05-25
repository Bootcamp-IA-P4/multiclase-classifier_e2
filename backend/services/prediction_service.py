import joblib
import pandas as pd
import os
import time
from core.logging_config import setup_logger

logger = setup_logger(__name__)

MODEL_PATH = os.getenv("MODEL_PATH", "data/model_lgbm.pkl")
_model = None

def get_model():
    global _model
    if _model is None:
        logger.info(f"Cargando modelo desde {MODEL_PATH}")
        try:
            _model = joblib.load(MODEL_PATH)
        except Exception as e:
            logger.exception(f"No se pudo cargar el modelo: {e}")
            raise
    return _model

def predict_diabetes(input_data: dict) -> dict:
    logger.info("Realizando predicción de diabetes")
    logger.debug(f"Datos recibidos para predicción: {input_data}")
    # Elimina patient_data_id si está presente
    input_data = dict(input_data)  # Copia para no modificar el original
    input_data.pop("patient_data_id", None)
    model = get_model()
    df = pd.DataFrame([input_data])
    start = time.time()
    prediction = model.predict(df)[0]
    proba = model.predict_proba(df)[0]
    elapsed = (time.time() - start) * 1000  # ms
    logger.info(f"Predicción: {prediction}, Probabilidades: {proba}, Tiempo: {elapsed:.2f} ms")
    return {
        "predicted_diabetes": int(prediction),
        "probability_no_diabetes": float(proba[0]),
        "probability_prediabetes": float(proba[1]),
        "probability_diabetes": float(proba[2]),
        "processing_time_ms": elapsed
    }