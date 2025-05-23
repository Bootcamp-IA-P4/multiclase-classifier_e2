from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import joblib
import numpy as np
import os

app = FastAPI(title="Backend FastAPI - Diabetes Predictor")

# 📌 Cargar el modelo al arrancar el backend
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model_lgbm.pkl")
model = joblib.load(MODEL_PATH)

# 🧱 Clase que define los datos que recibimos desde el frontend
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

@app.get("/")
def read_root():
    return {"message": "Backend de predicción operativo"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Convertimos el input a array de entrada para el modelo
        values = list(input_data.dict().values())
        data = np.array(values).reshape(1, -1)

        prediction = model.predict(data)[0]
        proba = model.predict_proba(data)[0]

        return {
            "prediction": int(prediction),
            "probabilities": [round(p, 4) for p in proba]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")
