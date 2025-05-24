from core.logging_config import setup_logger

logger = setup_logger(__name__)

def calculate_bmi(weight: float, height: float) -> float:
    #logger.info(f"Calculando BMI para peso={weight}, altura={height}")
    if height <= 0:
        logger.error("Altura menor o igual a cero")
        raise ValueError("La altura debe ser mayor que cero.")
    bmi = round(weight / ((height / 100) ** 2), 2)
    #logger.info(f"BMI calculado: {bmi}")
    return bmi