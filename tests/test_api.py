import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.api import app  # Ajusta si el archivo tiene otro nombre o ruta

client = TestClient(app)

def test_predict_valid_input():
    # Entrada simulada válida que coincide con PredictionInput
    payload = {
        "BMI": 24.5,
        "Sex": 1,
        "Age": 5,
        "Education": 4,
        "Income": 6,
        "MentHlth": 1,
        "PhysHlth": 2,
        "PhysActivity": 1,
        "Fruits": 1,
        "Veggies": 1,
        "HvyAlcoholConsump": 0,
        "GenHlth": 2,
        "HighBP": 1,
        "HighChol": 1,
        "CholCheck": 1,
        "Smoker": 0,
        "Stroke": 0,
        "HeartDiseaseorAttack": 0,
        "AnyHealthcare": 1,
        "NoDocbcCost": 0,
        "DiffWalk": 0
    }

    response = client.post("/predict", json=payload)

    # Verificamos que la API responde correctamente
    assert response.status_code == 200, f"Error inesperado: {response.status_code} - {response.text}"
    
    result = response.json()

    # Verificamos que los campos esperados están presentes
    assert "prediction" in result, "Falta el campo 'prediction' en la respuesta"
    assert "probabilities" in result, "Falta el campo 'probabilities' en la respuesta"
    assert isinstance(result["prediction"], int), "'prediction' debe ser un int"
    assert isinstance(result["probabilities"], list), "'probabilities' debe ser una lista"
    assert len(result["probabilities"]) == 3, "'probabilities' debe tener 3 elementos"
