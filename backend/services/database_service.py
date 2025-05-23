from db.database import supabase
from core.logging_config import setup_logger

logger = setup_logger(__name__)

def save_form_record(data: dict) -> dict:
    try:
        logger.info("💾 Guardando formulario en base de datos Supabase...")
        response = supabase.table("patient_data").insert(data).execute()
        if response.error:
            logger.error(f"❌ Error al guardar formulario: {response.error}")
            raise Exception(str(response.error))
        logger.info("✅ Formulario guardado exitosamente")
        return response.data
    except Exception as e:
        logger.exception("❌ Excepción al guardar formulario en BD")
        raise

def save_prediction_record(data: dict) -> dict:
    """Guarda una predicción en la tabla diabetes_predictions de Supabase."""
    try:
        logger.info("💾 Guardando predicción en base de datos Supabase...")
        response = supabase.table("diabetes_predictions").insert(data).execute()
        if response.error:
            logger.error(f"❌ Error al guardar predicción: {response.error}")
            raise Exception(str(response.error))
        logger.info("✅ Predicción guardada exitosamente")
        return response.data
    except Exception as e:
        logger.exception("❌ Excepción al guardar predicción en BD")
        raise

def get_all_forms() -> list:
    """Obtiene todos los formularios de la tabla patient_data."""
    try:
        logger.info("📄 Obteniendo todos los formularios de la base de datos Supabase...")
        response = supabase.table("patient_data").select("*").execute()
        if response.error:
            logger.error(f"❌ Error al obtener formularios: {response.error}")
            raise Exception(str(response.error))
        logger.info("✅ Formularios obtenidos exitosamente")
        return response.data
    except Exception as e:
        logger.exception("❌ Excepción al obtener formularios en BD")
        raise