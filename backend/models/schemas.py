from pydantic import BaseModel, Field
from typing import Optional

class HealthForm(BaseModel):
    Age: int
    Sex: int
    BMI: int
    HighBP: int
    HighChol: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    Smoker: int
    MentHlth: int
    PhysHlth: int
    GenHlth: int
    Income: int
    Education: int
    DiffWalk: int
    NoDocbcCost: int
    AnyHealthcare: int
    HvyAlcoholConsump: int
    CholCheck: int
    Stroke: int
    HeartDiseaseorAttack: int

class DiabetesPrediction(BaseModel):
    patient_data_id: str  # UUID o similar
    predicted_diabetes: int = Field(..., ge=0, le=2)  # 0, 1 o 2
    probability_no_diabetes: float = Field(..., ge=0, le=1)
    probability_prediabetes: float = Field(..., ge=0, le=1)
    probability_diabetes: float = Field(..., ge=0, le=1)
    processing_time_ms: Optional[float] = None