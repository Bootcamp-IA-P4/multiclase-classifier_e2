import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import os
import joblib

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, "..", "model", "model_lgbm.pkl")
MODEL_PATH = os.path.abspath(MODEL_PATH)  # Asegura que sea ruta absoluta
model = joblib.load(MODEL_PATH)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

def binary_question(label, id_):
    return html.Div([
        dbc.Label(label),
        dcc.Dropdown(
            options=[{"label": "Sí", "value": 1}, {"label": "No", "value": 0}],
            id=id_,
            placeholder="Seleccione una opción"
        ),
    ], className="mb-3")

def dropdown_question(label, id_, options):
    return html.Div([
        dbc.Label(label),
        dcc.Dropdown(
            options=[{"label": k, "value": v} for v, k in options.items()],
            id=id_,
            placeholder="Seleccione una opción"
        ),
    ], className="mb-3")


app.layout = dbc.Container([
    html.H2("Formulario de Predicción de Salud", className="mt-4"),
    dbc.Row([
        html.H3("Preguntas sobre su persona:", className="mt-4"),
        dbc.Col([
            html.Div([
                dbc.Label("Peso (kg)"),
                dcc.Input(id="Weight", type="number", step=0.1, className="form-control"),
                dbc.Label("Altura (cm)", className="mt-2"),
                dcc.Input(id="Height", type="number", step=0.1, className="form-control"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("Días de mala salud mental (últimos 30 días)"),
                dcc.Input(id="MentHlth", type="number", min=0, max=30, className="form-control"),
                dbc.Label("Días de mala salud física (últimos 30 días)", className="mt-2"),
                dcc.Input(id="PhysHlth", type="number", min=0, max=30, className="form-control"),
            ], className="mb-3"),
            dropdown_question("Salud general", "GenHlth", {
                1: "Excelente", 2: "Muy buena", 3: "Buena", 4: "Regular", 5: "Mala"
            }),
            dropdown_question("Sexo", "Sex", {0: "Femenino", 1: "Masculino"}),
            dropdown_question("Edad", "Age", {i: f"Grupo {i}" for i in range(1, 14)}),
        ]),
        html.H3("Preguntas sobre sus hábitos de vida:", className="mt-4"),
        dbc.Col([
            binary_question("¿Tiene presión arterial alta?", "HighBP"),
            binary_question("¿Tiene colesterol alto?", "HighChol"),
            binary_question("¿Revisión de colesterol en 5 años?", "CholCheck"),
            binary_question("¿Ha fumado 5 paquetes en su vida?", "Smoker"),
            binary_question("¿Ha tenido un derrame cerebral?", "Stroke"),
            binary_question("¿Enfermedad coronaria o infarto?", "HeartDiseaseorAttack"),
            binary_question("¿Actividad física en últimos 30 días?", "PhysActivity"),
            binary_question("¿Consume frutas diariamente?", "Fruits"),
            binary_question("¿Consume vegetales diariamente?", "Veggies"),
            binary_question("¿Es bebedor excesivo?", "HvyAlcoholConsump"),
            binary_question("¿Tiene cobertura médica?", "AnyHealthcare"),
            binary_question("¿No fue al médico por el costo?", "NoDocbcCost"),
            binary_question("¿Tiene dificultad al caminar?", "DiffWalk"),
            html.H3("Preguntas sobre educación y trabajo:", className="mt-4"),
            dropdown_question("Educación", "Education", {
                1: "Sin escuela",
                2: "Primaria",
                3: "Secundaria incompleta",
                4: "Secundaria completa",
                5: "Universidad 1-3 años",
                6: "Universidad 4+ años"
            }),
            dropdown_question("Ingresos", "Income", {
                1: "< $10,000",
                2: "$10,000–14,999",
                3: "$15,000–19,999",
                4: "$20,000–24,999",
                5: "$25,000–34,999",
                6: "$35,000–49,999",
                7: "$50,000–74,999",
                8: "≥ $75,000"
            }),
        ], md=6),
        
    ]),
    dbc.Button("Predecir", id="submit", color="primary", className="mt-3"),
    html.Hr(),
    html.Div(id="output", className="mt-3"),
], fluid=True)

@app.callback(
    Output("output", "children"),
    Input("submit", "n_clicks"),
    [State(x, "value") for x in [
        "HighBP", "HighChol", "CholCheck", "Weight", "Height", "Smoker", "Stroke",
        "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump",
        "AnyHealthcare", "NoDocbcCost", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk",
        "Sex", "Age", "Education", "Income"
    ]]
)
def predict(n_clicks, *values):
    if not n_clicks:
        return ""
    
    column_names = [
        "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke", "HeartDiseaseorAttack",
        "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "AnyHealthcare",
        "NoDocbcCost", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age",
        "Education", "Income"
    ]

    val_list = list(values)
    weight = val_list.pop(3)
    height = val_list.pop(3)

    if not weight or not height:
        return dbc.Alert("Por favor ingrese peso y altura válidos.", color="danger")

    try:
        bmi = round(float(weight) / ((float(height) / 100) ** 2), 1)
    except:
        return dbc.Alert("Error calculando el BMI.", color="danger")

    val_list.insert(3, bmi)

    input_df = pd.DataFrame([val_list], columns=column_names)
    try:
        prediction = model.predict(input_df)[0]
        return dbc.Alert(f"Predicción del modelo: {prediction}", color="success")
    except Exception as e:
        return dbc.Alert(f"Error en la predicción: {str(e)}", color="danger")

if __name__ == "__main__":
    app.run(debug=True)
