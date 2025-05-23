from fastapi.testclient import TestClient
from app import api  # Ajusta si has renombrado tu archivo de FastAPI (Existe una carpeta llamada app/Dentro hay un archivo llamado api.py)

client = TestClient(api.app)  # Usamos la instancia "app" de FastAPI si por ejemplo existe  app = FastAPI()
# Si mi compañero lo define con otro nombre (por ejemplo, application = FastAPI()), tendrás que hacer:
# client = TestClient(main.application)
# Una vez que tenga el archivo real, lo abro y busco la línea donde se crea la app:
# app = FastAPI()

def test_get_forms_returns_status_200_or_500():
    response = client.get("/forms")
    assert response.status_code in [200, 500]  # Permitimos 500 por si falla Supabase

def test_post_forms_invalid_data():
    response = client.post("/forms", json={"age": "no es un número"})
    assert response.status_code == 422  # Error de validación de FastAPI

def test_post_predictions_invalid_class():
    # Este test envía un campo de clase inválido (por ejemplo, 4)
    prediction = {
        "patient_data_id": "1234",
        "predicted_diabetes": 4,  # Inválido
        "probability_no_diabetes": 0.3,
        "probability_prediabetes": 0.3,
        "probability_diabetes": 0.4,
        "max_probability": 0.4
    }
    response = client.post("/predictions", json=prediction)
    assert response.status_code == 422  # FastAPI lanza error por fuera de rango

# Mirar como se llaman las rutas
# response = client.get("/forms")
# response = client.post("/forms", json={...})
# response = client.post("/predictions", json={...})