from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.bmi_service import calculate_bmi

router = APIRouter(prefix="/bmi", tags=["bmi"])

class BMIInput(BaseModel):
    weight: float
    height: float

@router.post("/")
def bmi_endpoint(data: BMIInput):
    try:
        bmi = calculate_bmi(data.weight, data.height)
        return {"bmi": bmi}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))