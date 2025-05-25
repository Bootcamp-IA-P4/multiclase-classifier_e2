from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class PatientData(BaseModel):
    Age: int
    Sex: int
    BMI: float
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

class DiabetesPredictions(BaseModel):
    patient_data_id: UUID  # UUID o similar
    predicted_diabetes: int = Field(..., ge=0, le=2)  # 0, 1 o 2
    processing_time_ms: Optional[float] = None
    probability_no_diabetes: float = Field(..., ge=0, le=1)
    probability_prediabetes: float = Field(..., ge=0, le=1)
    probability_diabetes: float = Field(..., ge=0, le=1)


class DiabetesPredictionRequest(BaseModel):
    patient_data_id: UUID
    Age: int
    Sex: int
    BMI: float
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