from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import os
from supabase import create_client, Client
from datetime import datetime
import uuid

# === CONFIGURACIÓN SUPABASE ===
from dotenv import load_dotenv
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# === APP Y MODELO ===
app = FastAPI(title="Backend FastAPI - Diabetes Predictor")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model_lgbm.pkl")
model = joblib.load(MODEL_PATH)

# === DATOS DE ENTRADA (mismo formato que espera el modelo) ===
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
        # Preparamos input
        data_dict = input_data.dict()
        values = list(data_dict.values())
        X = np.array(values).reshape(1, -1)

        # Predicción
        pred = model.predict(X)[0]
        proba = model.predict_proba(X)[0]

        # Guardamos en Supabase
        record = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.utcnow().isoformat(),
            "input_data": data_dict,
            "predicted_diabetes": int(pred),
            "probability_no_diabetes": round(proba[0], 4),
            "probability_prediabetes": round(proba[1], 4),
            "probability_diabetes": round(proba[2], 4),
        }

        response = supabase.table("diabetes_predictions").insert(record).execute()
        if response.error:
            raise HTTPException(status_code=500, detail=str(response.error))

        # Devolvemos respuesta
        return {
            "prediction": int(pred),
            "probabilities": [round(p, 4) for p in proba]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")
