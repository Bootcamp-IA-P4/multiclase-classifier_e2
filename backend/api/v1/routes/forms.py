from fastapi import APIRouter, HTTPException
from services.database_service import save_form_record
from models.schemas import PatientData
from db.database import supabase
from core.logging_config import setup_logger
from services.database_service import get_all_forms

logger = setup_logger(__name__)

router = APIRouter(prefix="/forms", tags=["forms"])

@router.post("/")
def create_form(form: PatientData):
    logger.info("Nueva petición para guardar formulario")
    try:
        result = save_form_record(form.model_dump())
        logger.info("Formulario guardado correctamente")
        return result
    except Exception as e:
        logger.exception("Excepción inesperada al guardar formulario")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_forms():
    logger.info("Petición para obtener formularios")
    try:
        result = get_all_forms()  # <--- Usa el servicio
        return result
    except Exception as e:
        logger.exception("Excepción inesperada al obtener formularios")
        raise HTTPException(status_code=500, detail=str(e))