import os
import joblib
import pandas as pd

# ✅ Test que verifica si el modelo se carga correctamente y predice una clase válida
def test_model_load_and_predict():
    # 1. Definimos la ruta relativa al archivo del modelo
    model_path = os.path.join("model", "model_lgbm.pkl")

    # 2. Cargamos el modelo entrenado usando joblib
    model = joblib.load(model_path)

    # 3. Creamos un DataFrame con una sola fila simulada
    # Los nombres de columna deben coincidir exactamente con los usados al entrenar el modelo
    sample_input = pd.DataFrame([{
        "Sex": 1,
        "HighBP": 1,
        "HighChol": 1,
        "BMI": 27.5,
        "Smoker": 1,
        "Stroke": 0,
        "HeartDiseaseorAttack": 0,
        "PhysActivity": 1,
        "Fruits": 1,
        "Veggies": 1,
        "HvyAlcoholConsump": 0,
        "GenHlth": 1,
        "DiffWalk": 0,
        "Age": 2,
        "Education": 0,
        "Income": 2,
        "NoDocbcCost": 0,
        "AnyHealthcare": 1,
        "MentHlth": 8,
        "PhysHlth": 6,
        "CholCheck": 4
    }])

    # 4. Hacemos la predicción con el modelo
    pred = model.predict(sample_input)

    # 5. Validamos que la clase predicha sea válida: 0 = No diabetes, 1 = Prediabetes, 2 = Diabetes
    assert pred[0] in [0, 1, 2]
