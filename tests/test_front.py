import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.front import predict
import dash_bootstrap_components as dbc

def test_predict_valid_input():
    n_clicks = 1

    args = [
        70, 170, 24.2, 1, 5, 4, 6, 2, 1, 1, 1, 1, 0, 2, 1, 1, 1, 0, 0, 0, 1, 0, 0
    ]

    try:
        output = predict(n_clicks, *args)
    except Exception as e:
        assert False, f"La función predict lanzó un error: {e}"

    # ✅ Validar tipo de componente y contenido sin acceder a .props
    assert isinstance(output, dbc.Alert), "La salida no es una alerta de Dash Bootstrap Components"
    assert output.children is not None, "La alerta no tiene contenido (children)"
    assert isinstance(output.children, list), "El contenido no es una lista de elementos HTML"
    assert any("Prediabetes" in str(c) or "Diabetes" in str(c) or "No presenta" in str(c) for c in output.children), \
        "El texto de predicción no está presente en la respuesta"


# Test nuevo: tests/test_predict_with_mock.py
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import requests_mock
from app.front import predict
import dash_bootstrap_components as dbc

def test_predict_mocked_backend_response():
    # Simulamos el input completo
    n_clicks = 1
    args = [
        70, 170, 24.2, 1, 5, 4, 6, 2, 1, 1, 1, 1, 0, 2, 1, 1, 1, 0, 0, 0, 1, 0, 0
    ]

    # URL que usarás en el futuro en tu función predict()
    url_api = "http://localhost:8000/predict"

    # Preparamos un mock para simular la respuesta del backend
    with requests_mock.Mocker() as m:
        m.post(url_api, json={
            "prediction": 2,
            "probabilities": [0.1, 0.2, 0.7]
        })

        # Llamamos a predict como si la API funcionara
        output = predict(n_clicks, *args)

    # Validamos que la alerta se ha generado correctamente
    assert isinstance(output, dbc.Alert), "La respuesta no es una alerta de Dash"
    assert output.children is not None
    assert any("Diabetes" in str(c) for c in output.children), \
        "No se encontró el mensaje esperado en la alerta"

""" Cuando conectemos el frontend con el backend:
Cambiar la función predict() para hacer requests.post(...)
Asegúrandonos de que la URL usada en el test (http://localhost:8000/predict) sea la misma que en el código real
Este test sigue funcionando sin backend real, porque intercepta la llamada """