import pandas as pd
from front import predict

def test_predict_valid_input():
    # Simulamos el click (por eso n_clicks = 1)
    n_clicks = 1

    # Creamos un conjunto de valores válidos simulados
    args = [
        70,     # Weight
        170,    # Height
        24.2,   # BMI
        1,      # Sex
        5,      # Age
        4,      # Education
        6,      # Income
        2,      # MentHlth
        1,      # PhysHlth
        1,      # PhysActivity
        1,      # Fruits
        1,      # Veggies
        0,      # HvyAlcoholConsump
        2,      # GenHlth
        1,      # HighBP
        1,      # HighChol
        1,      # CholCheck
        0,      # Smoker
        0,      # Stroke
        0,      # HeartDiseaseorAttack
        1,      # AnyHealthcare
        0,      # NoDocbcCost
        0       # DiffWalk
    ]

    # Llamamos a la función directamente
    output = predict(n_clicks, *args)

    # Verificamos que el resultado sea un componente Dash (como una alerta)
    assert output is not None
    assert hasattr(output, 'props')
    assert 'children' in output.props
