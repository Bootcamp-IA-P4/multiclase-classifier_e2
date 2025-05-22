from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os

# Задай свои параметры подключения
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://urqaflqmjogzzlbjoccm.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVycWFmbHFtam9nenpsYmpvY2NtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzkyODAzMTgsImV4cCI6MjA1NDg1NjMxOH0.FzZrGzGGR5pH_mb297IM44cTj6xDmk7M93HZCOMZ_S0")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class HealthForm(BaseModel):
    #user_id: str
    age: int
    sex: int
    bmi: float
    high_bp: bool
    high_chol: bool
    phys_activity: bool
    fruits: bool
    veggies: bool
    smoker: bool
    ment_hlth: int
    phys_hlth: int
    gen_hlth: int
    income: int
    education: int
    diff_walk: bool
    no_doc_bc_cost: bool
    any_healthcare: bool
    hvy_alcohol_consump: bool
    chol_check: bool
    stroke: bool
    heart_disease_or_attack: bool
    


class DiabetesPrediction(BaseModel):
    patient_data_id: str  # UUID в виде строки
    predicted_diabetes: int = Field(..., ge=0, le=2)  # 0, 1 или 2
    probability_no_diabetes: float = Field(..., ge=0, le=1)
    probability_prediabetes: float = Field(..., ge=0, le=1)
    probability_diabetes: float = Field(..., ge=0, le=1)
    max_probability: float = Field(..., ge=0, le=1)
    model_version: Optional[str] = "1.0.0"
    model_name: Optional[str] = "diabetes_classifier"
    processing_time_ms: Optional[float] = None 
    

@app.post("/forms")
def create_form(form: HealthForm):
    try:
        response = supabase.table("patient_data").insert(form.dict()).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/forms")
def get_forms():
    response = supabase.table("health_forms").select("*").execute()
    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))
    return response.data

@app.post("/predictions")
def save_prediction(pred: DiabetesPrediction):
    try:
        response = supabase.table("diabetes_predictions").insert(pred.dict()).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    