from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.forms import router as forms_router
from api.v1.routes.predictions import router as predictions_router
from api.v1.routes.bmi import router as bmi_router

app = FastAPI(title="Diabetes Prediction API")
app.include_router(forms_router, prefix="/api/v1")
app.include_router(predictions_router, prefix="/api/v1")
app.include_router(bmi_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8050"],  # En producción, reemplazar con ["https://tudominio.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)