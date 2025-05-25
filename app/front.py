import dash
from dash import ctx, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import requests


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "DIABETEST"
server = app.server


def binary_question(label, id_):
    return html.Div(
        [
            dbc.Label(label),
            dcc.Dropdown(
                options=[{"label": "Sí", "value": 1}, {"label": "No", "value": 0}],
                id=id_,
                placeholder="Seleccione una opción",
            ),
        ],
        className="mb-3",
    )


def dropdown_question(label, id_, options):
    return html.Div(
        [
            dbc.Label(label),
            dcc.Dropdown(
                options=[{"label": k, "value": v} for v, k in options.items()],
                id=id_,
                placeholder="Seleccione una opción",
            ),
        ],
        className="mb-3",
    )


def section_card(title, content, id_):
    return dbc.Card(
        [dbc.CardHeader(html.H4(title)), dbc.CardBody(content)],
        className="glass-card mb-4",
        id=id_,
    )


app.layout = dbc.Container(
    [
        dbc.Col(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(
                                src="assets/logo.png",
                                style={"width": "300px", "marginTop": "10px"},
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Ver historial",
                                id="history-btn",
                                color="info",
                                style={"marginTop": "20px"},
                            ),
                            width="auto",
                            className="d-flex justify-content-end align-items-center",
                        ),
                    ],
                    className="mb-4 justify-content-between",
                ),
                html.H2(
                    "Formulario de Predicción de Salud", className="text-center mt-4"
                ),
                dcc.Store(id="step", data=1),
                # Tarjeta paso 1
                section_card(
                    "Preguntas sobre su persona",
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label("Peso (kg)"),
                                        dcc.Input(
                                            id="Weight",
                                            type="number",
                                            step=0.1,
                                            className="form-control mb-3",
                                        ),
                                        dbc.Label("Altura (cm)"),
                                        dcc.Input(
                                            id="Height",
                                            type="number",
                                            step=0.1,
                                            className="form-control mb-3",
                                        ),
                                        dbc.Label("Índice de Masa Corporal (BMI)"),
                                        dcc.Input(
                                            id="BMI",
                                            type="number",
                                            className="form-control mb-3",
                                            disabled=True,
                                        ),
                                        dropdown_question(
                                            "Sexo",
                                            "Sex",
                                            {0: "Femenino", 1: "Masculino"},
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                                dbc.Col(
                                    [
                                        dropdown_question(
                                            "Edad",
                                            "Age",
                                            {
                                                1: "18-24",
                                                2: "25-29",
                                                3: "30-34",
                                                4: "35-39",
                                                5: "40-44",
                                                6: "45-49",
                                                7: "50-54",
                                                8: "55-59",
                                                9: "60-64",
                                                10: "65-69",
                                                11: "70-74",
                                                12: "75-79",
                                                13: "80 o más",
                                            },
                                        ),
                                        dropdown_question(
                                            "Educación",
                                            "Education",
                                            {
                                                1: "Sin escuela",
                                                2: "Primaria",
                                                3: "Secundaria incompleta",
                                                4: "Secundaria completa",
                                                5: "Universidad 1-3 años",
                                                6: "Universidad 4+ años",
                                            },
                                        ),
                                        dropdown_question(
                                            "Ingresos",
                                            "Income",
                                            {
                                                1: "< $10,000",
                                                2: "$10,000–14,999",
                                                3: "$15,000–19,999",
                                                4: "$20,000–24,999",
                                                5: "$25,000–34,999",
                                                6: "$35,000–49,999",
                                                7: "$50,000–74,999",
                                                8: "≥ $75,000",
                                            },
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                            ]
                        )
                    ],
                    id_="step-1",
                ),
                # Tarjeta paso 2
                section_card(
                    "Preguntas sobre sus hábitos de vida",
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Label(
                                            "Días de mala salud mental (últimos 30 días)"
                                        ),
                                        dcc.Input(
                                            id="MentHlth",
                                            type="number",
                                            min=0,
                                            max=30,
                                            className="form-control mb-3",
                                        ),
                                        dbc.Label(
                                            "Días de mala salud física (últimos 30 días)"
                                        ),
                                        dcc.Input(
                                            id="PhysHlth",
                                            type="number",
                                            min=0,
                                            max=30,
                                            className="form-control",
                                        ),
                                        binary_question(
                                            "¿Actividad física en últimos 30 días?",
                                            "PhysActivity",
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                                dbc.Col(
                                    [
                                        binary_question(
                                            "¿Consume frutas diariamente?", "Fruits"
                                        ),
                                        binary_question(
                                            "¿Consume vegetales diariamente?", "Veggies"
                                        ),
                                        binary_question(
                                            "¿Es bebedor excesivo?", "HvyAlcoholConsump"
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                            ]
                        )
                    ],
                    id_="step-2",
                ),
                # Tarjeta paso 3
                section_card(
                    "Preguntas sobre su salud general",
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dropdown_question(
                                            "Salud general",
                                            "GenHlth",
                                            {
                                                1: "Excelente",
                                                2: "Muy buena",
                                                3: "Buena",
                                                4: "Regular",
                                                5: "Mala",
                                            },
                                        ),
                                        binary_question(
                                            "¿Tiene presión arterial alta?", "HighBP"
                                        ),
                                        binary_question(
                                            "¿Tiene colesterol alto?", "HighChol"
                                        ),
                                        binary_question(
                                            "¿Revisión de colesterol en 5 años?",
                                            "CholCheck",
                                        ),
                                        binary_question(
                                            "¿Ha fumado 5 paquetes en su vida?",
                                            "Smoker",
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                                dbc.Col(
                                    [
                                        binary_question(
                                            "¿Ha tenido un derrame cerebral?", "Stroke"
                                        ),
                                        binary_question(
                                            "¿Enfermedad coronaria o infarto?",
                                            "HeartDiseaseorAttack",
                                        ),
                                        binary_question(
                                            "¿Tiene cobertura médica?", "AnyHealthcare"
                                        ),
                                        binary_question(
                                            "¿No fue al médico por el costo?",
                                            "NoDocbcCost",
                                        ),
                                        binary_question(
                                            "¿Tiene dificultad al caminar?", "DiffWalk"
                                        ),
                                    ],
                                    xs=12,
                                    md=6,
                                ),
                            ]
                        )
                    ],
                    id_="step-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                "Anterior",
                                id="prev-btn",
                                color="secondary",
                                className="me-2",
                                disabled=True,
                            ),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Button("Siguiente", id="next-btn", color="primary"),
                            width="auto",
                        ),
                        dbc.Col(
                            dbc.Button(
                                "Predecir",
                                id="submit",
                                color="success",
                                style={"display": "none"},
                            ),
                            width="auto",
                        ),
                    ],
                    className="mt-3 justify-content-center",
                ),
                html.Div(id="output", className="mt-4"),
                html.Div(id="history-output", className="mt-5"),
            ],
            width=12,
            lg=10,
            xl=8,
        )
    ],
    fluid=True,
    className="d-flex justify-content-center",
)


@app.callback(
    Output("BMI", "value"), Input("Weight", "value"), Input("Height", "value")
)
def update_bmi(weight, height):
    if weight and height and height > 0:
        bmi = round(weight / ((height / 100) ** 2), 2)
        return bmi
    return None


# Paso entre secciones
@app.callback(
    Output("step", "data"),
    Input("prev-btn", "n_clicks"),
    Input("next-btn", "n_clicks"),
    State("step", "data"),
    prevent_initial_call=True,
)
def update_step(prev_clicks, next_clicks, current_step):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if current_step is None:
        current_step = 1

    if button_id == "next-btn":
        current_step += 1
    elif button_id == "prev-btn":
        current_step -= 1

    return max(1, min(current_step, 4))


# Mostrar secciones según paso
@app.callback(
    Output("step-1", "style"),
    Output("step-2", "style"),
    Output("step-3", "style"),
    Output("prev-btn", "disabled"),
    Output("next-btn", "style"),
    Output("submit", "style"),
    Input("step", "data"),
)
def display_step(step):
    style_hidden = {"display": "none"}
    style_visible = {"display": "block"}

    return (
        style_visible if step == 1 else style_hidden,
        style_visible if step == 2 else style_hidden,
        style_visible if step == 3 else style_hidden,
        step == 1,
        style_visible if step < 3 else style_hidden,
        style_visible if step == 3 else style_hidden,
    )


# Predicción
@app.callback(
    Output("output", "children"),
    Input("submit", "n_clicks"),
    [
        State("Weight", "value"),
        State("Height", "value"),
        State("BMI", "value"),
        State("Sex", "value"),
        State("Age", "value"),
        State("Education", "value"),
        State("Income", "value"),
        State("MentHlth", "value"),
        State("PhysHlth", "value"),
        State("PhysActivity", "value"),
        State("Fruits", "value"),
        State("Veggies", "value"),
        State("HvyAlcoholConsump", "value"),
        State("GenHlth", "value"),
        State("HighBP", "value"),
        State("HighChol", "value"),
        State("CholCheck", "value"),
        State("Smoker", "value"),
        State("Stroke", "value"),
        State("HeartDiseaseorAttack", "value"),
        State("AnyHealthcare", "value"),
        State("NoDocbcCost", "value"),
        State("DiffWalk", "value"),
    ],
)
def predict(
    n_clicks,
    Weight,
    Height,
    BMI,
    Sex,
    Age,
    Education,
    Income,
    MentHlth,
    PhysHlth,
    PhysActivity,
    Fruits,
    Veggies,
    HvyAlcoholConsump,
    GenHlth,
    HighBP,
    HighChol,
    CholCheck,
    Smoker,
    Stroke,
    HeartDiseaseorAttack,
    AnyHealthcare,
    NoDocbcCost,
    DiffWalk,
):

    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    try:
        input_data = pd.DataFrame(
            [
                {
                    "BMI": BMI,
                    "Sex": Sex,
                    "Age": Age,
                    "Education": Education,
                    "Income": Income,
                    "MentHlth": MentHlth,
                    "PhysHlth": PhysHlth,
                    "PhysActivity": PhysActivity,
                    "Fruits": Fruits,
                    "Veggies": Veggies,
                    "HvyAlcoholConsump": HvyAlcoholConsump,
                    "GenHlth": GenHlth,
                    "HighBP": HighBP,
                    "HighChol": HighChol,
                    "CholCheck": CholCheck,
                    "Smoker": Smoker,
                    "Stroke": Stroke,
                    "HeartDiseaseorAttack": HeartDiseaseorAttack,
                    "AnyHealthcare": AnyHealthcare,
                    "NoDocbcCost": NoDocbcCost,
                    "DiffWalk": DiffWalk,
                }
            ]
        )

        if input_data.isnull().any().any():
            return dbc.Alert(
                "Por favor complete todos los campos antes de predecir.", color="danger"
            )

            # Convertimos los datos a diccionario plano
        input_dict = {
            "BMI": BMI,
            "Sex": Sex,
            "Age": Age,
            "Education": Education,
            "Income": Income,
            "MentHlth": MentHlth,
            "PhysHlth": PhysHlth,
            "PhysActivity": PhysActivity,
            "Fruits": Fruits,
            "Veggies": Veggies,
            "HvyAlcoholConsump": HvyAlcoholConsump,
            "GenHlth": GenHlth,
            "HighBP": HighBP,
            "HighChol": HighChol,
            "CholCheck": CholCheck,
            "Smoker": Smoker,
            "Stroke": Stroke,
            "HeartDiseaseorAttack": HeartDiseaseorAttack,
            "AnyHealthcare": AnyHealthcare,
            "NoDocbcCost": NoDocbcCost,
            "DiffWalk": DiffWalk,
        }

        # Validación por si hay campos vacíos
        if any(v is None for v in input_dict.values()):
            return dbc.Alert(
                "Por favor complete todos los campos antes de predecir.", color="danger"
            )

        # Hacer la petición al backend
        response = requests.post("http://localhost:8000/predict", json=input_dict)
        response.raise_for_status()  # lanza error si status != 200
        result = response.json()

        prediction = result["prediction"]
        prediction_proba = result["probabilities"]

        if prediction == 0:
            result_text = "No presenta diabetes."
            color = "success"
        elif prediction == 1:
            result_text = "Prediabetes detectada. Se recomienda vigilancia médica."
            color = "warning"
        elif prediction == 2:
            result_text = "¡Diabetes diagnosticada! Consulte a un especialista."
            color = "danger"
        else:
            result_text = "Resultado desconocido."
            color = "secondary"

        return dbc.Alert(
            [
                html.H4(result_text),
                html.P(
                    f"Probabilidades: "
                    f"No diabetes: {prediction_proba[0] * 100:.1f}%, "
                    f"Prediabetes: {prediction_proba[1] * 100:.1f}%, "
                    f"Diabetes: {prediction_proba[2] * 100:.1f}%"
                ),
            ],
            color=color,
        )

    except Exception as e:
        return dbc.Alert(f"Error en la predicción: {str(e)}", color="danger")


@app.callback(
    Output("history-output", "children"),
    Input("history-btn", "n_clicks"),
    prevent_initial_call=True,
)
def show_history(n_clicks):
    try:
        # Petición al backend para obtener historial
        response = requests.get("http://localhost:8000/history")
        response.raise_for_status()
        data = response.json()

        if not data:
            return dbc.Alert("No hay historial disponible.", color="info")

        df = pd.DataFrame(data)

        # Tabla estilizada
        table = dbc.Table.from_dataframe(
            df[
                [
                    "predicted_diabetes",
                    "probability_no_diabetes",
                    "probability_prediabetes",
                    "probability_diabetes",
                    "processing_time_ms",
                ]
            ],
            striped=True,
            bordered=True,
            hover=True,
            responsive=True,
        )

        # Estilo tipo tarjeta glassmórfica
        return dbc.Card(
            [
                dbc.CardHeader(
                    html.H5("Últimas 5 predicciones", className="text-center")
                ),
                dbc.CardBody(table),
            ],
            className="glass-card mt-4",
        )

    except Exception as e:
        return dbc.Alert(f"Error al cargar historial: {str(e)}", color="danger")


if __name__ == "__main__":
    app.run(debug=True)
