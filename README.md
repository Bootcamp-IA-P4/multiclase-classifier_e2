# Proyecto VII para FactoriaF5 : Problema de clasificación multiclase

<p align="center">
  <img src="docs/images/DIABETEST.png" alt="logo diabetest" width="300"/>
</p>


Este proyecto tiene como finalidad desarrollar un modelo de machine learning capaz de resolver un problema real utilizando algoritmos de clasificación multiclase.

Para ello hemos elegido el dataset **"diabetes_012_health_indicators_BRFSS2015.csv"** desde [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data) .

Usaremos este dataset para determinar si una persona **está sana, tiene prediabetes o tiene diabetes**. Este modelo de machine learning, al que hemos llamado DIABETEST, está orientado a centros de salud que deseen realizar un análisis preventivo de sus pacientes, con el objetivo de identificar casos que requieran seguimiento médico temprano.

Para ello deberán rellenar de un formulario que consta de 23 preguntas y devuelve una de las siguientes opciones:
- "No presenta diabetes."
- "Prediabetes detectada. Se recomienda vigilancia médica."
- "¡Diabetes diagnosticada! Consulte a un especialista."

El proyecto consta de un backend realizado con FastApi y conectado a una base de datos en línea en Supabase, y un frontend con Dash.

![Demo de persona sana](./docs/images/demo2.gif)
![Demo de persona con diabetes](./docs/images/demo1.gif)

### Para poner en marcha el proyecto usa los siguientes comandos:

Clona el repositorio en tu PC:
````
git clone https://github.com/Bootcamp-IA-P4/multiclase-classifier_e2.git
````
Entra al repositorio:
````
cd multiclase-classifier_e2
````
Crea tu entorno virtual en Mac:
````
python3 -m venv .venv
source .venv/bin/activate
````
Crea tu entorno virtual en Windows:
````
python -m venv .venv
.venv\Scripts\activate
````
Instala las dependencias:
````
pip install -r requirements.txt
````
Corre el backend en un nuevo terminal:
````
cd backend
uvicorn main:app --reload
````
Corre el frontend en un nuevo terminal:
````
python app/front.py
````
Ahora puedes entrar a las rutas correspondientes:
- http://127.0.0.1:8050/ : para frontend
- http://127.0.0.1:8000/ : para backend

### Test para el buen funcionamiento del programa

### Loggers para la trazabilidad del programa