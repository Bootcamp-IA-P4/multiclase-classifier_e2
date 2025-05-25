from fastapi import APIRouter, HTTPException
from models.schemas import DiabetesPredictionRequest, DiabetesPredictions
from services.prediction_service import predict_diabetes
from services.database_service import save_prediction_record
from core.logging_config import setup_logger
from services.database_service import supabase  # Asegúrate de que 'supabase' esté exportado en este módulo

logger = setup_logger(__name__)

router = APIRouter(prefix="/predictions", tags=["predictions"])

@router.post("/", response_model=DiabetesPredictions)
def save_prediction(pred: DiabetesPredictionRequest):
    logger.info("Nueva petición para guardar predicción")
    logger.debug(f"Payload recibido: {pred}")
    try:
        # 1. Realizar la predicción
        pred_result = predict_diabetes(pred.model_dump())
        logger.debug(f"Resultado de la predicción: {pred_result}")

        # 2. Preparar el registro para guardar en Supabase
        record = {
            "patient_data_id": str(pred.patient_data_id),
            "predicted_diabetes": pred_result["predicted_diabetes"],
            "processing_time_ms": round(pred_result.get("processing_time_ms", 0), 3),
            "probability_no_diabetes": round(pred_result["probability_no_diabetes"], 3),
            "probability_prediabetes": round(pred_result["probability_prediabetes"], 3),
            "probability_diabetes": round(pred_result["probability_diabetes"], 3),
        }
        logger.debug(f"Registro a guardar en Supabase: {record}")

        # 3. Guardar en la tabla diabetes_predictions
        result = save_prediction_record(record)
        logger.debug(f"Respuesta de Supabase: {result}")

        # 4. Devolver el registro guardado (primer elemento de la lista)
        return result[0]
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
        data = getattr(response, "data", None)
        error = getattr(response, "error", None)
        status_code = getattr(response, "status_code", None)

        if error:
            logger.error(f"Error al obtener predicciones: {error}")
            raise HTTPException(status_code=500, detail=str(error))

        if status_code and status_code != 200:
            logger.error(f"Error al obtener predicciones: Status code {status_code}")
            raise HTTPException(status_code=500, detail=f"Status code {status_code}")

        if data is None:
            logger.error("No se recibieron datos de Supabase")
            raise HTTPException(status_code=500, detail="No se recibieron datos de Supabase")

        return data

    except Exception as e:
        logger.exception("Excepción inesperada al obtener predicciones")
        raise HTTPException(status_code=500, detail=str(e))