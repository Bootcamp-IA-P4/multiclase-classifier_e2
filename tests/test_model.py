import os
import joblib
import numpy as np

def test_model_load_and_predict():
    # 1. Ruta absoluta al modelo
    model_path = os.path.join("model", "model_lgbm.pkl")

    # 2. Cargar el modelo
    model = joblib.load(model_path)

    # 3. Crear un input simulado con el mismo número de columnas que usas en la predicción
    sample_input = np.array([[1, 1, 1, 27.5, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2, 0, 2, 0, 1, 8, 6, 4]])

    # 4. Hacer predicción
    pred = model.predict(sample_input)

    # 5. Validamos que el modelo devuelve una clase válida (0 = No diabetes, 1 = Prediabetes, 2 = Diabetes).
    assert pred[0] in [0, 1, 2]
