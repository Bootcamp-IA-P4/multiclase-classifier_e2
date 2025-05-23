from fastapi import APIRouter, HTTPException
from models.schemas import DiabetesPrediction
from db.database import supabase
from core.logging_config import setup_logger
from services.database_service import save_prediction_record

logger = setup_logger(__name__)

router = APIRouter(prefix="/predictions", tags=["predictions"])



@router.post("/")
def save_prediction(pred: DiabetesPrediction):
    logger.info("Nueva petición para guardar predicción")
    try:
        result = save_prediction_record(pred.model_dump())  # Usa el servicio
        return result
    except Exception as e:
        logger.exception("Excepción inesperada al guardar predicción")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/recent")
def get_recent_predictions(limit: int = 10):
    logger.info(f"Petición para obtener las {limit} predicciones más recientes")
    try:
        response = (
            supabase
            .table("diabetes_predictions")
            .select("*")
            .order("created_at", desc=True)
            .limit(limit)
            .execute()
        )
        if response.error:
            logger.error(f"Error al obtener predicciones: {response.error}")
            raise HTTPException(status_code=500, detail=str(response.error))
        return response.data
    except Exception as e:
        logger.exception("Excepción inesperada al obtener predicciones")
        raise HTTPException(status_code=500, detail=str(e))