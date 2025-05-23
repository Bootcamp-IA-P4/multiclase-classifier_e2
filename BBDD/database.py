from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os
from configuration import SUPABASE_URL, SUPABASE_KEY
from fastapi import FastAPI, HTTPException
from models import HealthForm, DiabetesPrediction


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app = FastAPI()


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
    
@app.get("/predictions/recent")
def get_recent_predictions(limit: int = 10):
    try:
        response = (
            supabase
            .table("diabetes_predictions")
            .select("*")
            .order("created_at", desc=True)
            .limit(limit)
            .execute()
        )
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    