from pydantic import BaseModel, Field
from typing import Optional

class HealthForm(BaseModel):
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
    patient_data_id: str  # UUID o similar
    predicted_diabetes: int = Field(..., ge=0, le=2)  # 0, 1 o 2
    probability_no_diabetes: float = Field(..., ge=0, le=1)
    probability_prediabetes: float = Field(..., ge=0, le=1)
    probability_diabetes: float = Field(..., ge=0, le=1)
    processing_time_ms: Optional[float] = None