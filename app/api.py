from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import numpy as np
import os
from datetime import datetime
import uuid
import time
import pandas as pd
from dotenv import load_dotenv

# === CONFIGURACIÓN SUPABASE (opcional) ===
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


try:
    from supabase import create_client, Client
    if SUPABASE_URL and SUPABASE_KEY:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    print("⚠️ Nosupabase = None se pudo conectar con Supabase:", e)
    supabase = None

# === APP Y MODELO ===
app = FastAPI(title="Backend FastAPI - Diabetes Predictor")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model_lgbm.pkl")
model = joblib.load(MODEL_PATH)

# === DATOS DE ENTRADA ===
class PredictionInput(BaseModel):
    BMI: float
    Sex: int
    Age: int
    Education: int
    Income: int
    MentHlth: int
    PhysHlth: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    HvyAlcoholConsump: int
    GenHlth: int
    HighBP: int
    HighChol: int
    CholCheck: int
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    AnyHealthcare: int
    NoDocbcCost: int
    DiffWalk: int

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        data_dict = input_data.dict()
        patient_data_id = str(uuid.uuid4())

        # Predicción
        start = time.time()
        X = pd.DataFrame([data_dict])  # Usamos DataFrame para evitar warning
        pred = model.predict(X)[0]
        proba = model.predict_proba(X)[0]
        elapsed = round((time.time() - start) * 1000, 2)

        # Guardado en Supabase (si disponible)
        if supabase:
            try:
                form_record = {"id": patient_data_id, **data_dict}
                supabase.table("patient_data").insert(form_record).execute()

                prediction_record = {
                    "patient_data_id": patient_data_id,
                    "predicted_diabetes": int(pred),
                    "probability_no_diabetes": round(proba[0], 4),
                    "probability_prediabetes": round(proba[1], 4),
                    "probability_diabetes": round(proba[2], 4),
                    "processing_time_ms": elapsed
                }
                supabase.table("diabetes_predictions").insert(prediction_record).execute()

            except Exception as db_error:
                print("⚠️ Error al guardar en Supabase:", db_error)

        return {
            "prediction": int(pred),
            "probabilities": [round(p, 4) for p in proba]
        }

    except Exception as e:
        print("❌ Error general:", e)
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")


@app.get("/history")
def get_history():
    if not supabase:
        raise HTTPException(status_code=500, detail="No hay conexión con Supabase.")
    try:
        response = (
            supabase.table("diabetes_predictions")
            .select("*")
            .order("created_at", desc=True)
            .limit(5)
            .execute()
        )
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al recuperar historial: {e}")
