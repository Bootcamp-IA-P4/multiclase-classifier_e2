# Proyecto VII para FactoriaF5 : Problema de clasificación multiclase

Este proyecto tiene como finalidad desarrollar un modelo de machine learning capaz de resolver un problema real utilizando algoritmos de clasificación multiclase.

Para ello hemos elegido el dataset **"diabetes_012_health_indicators_BRFSS2015.csv"** desde [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data) .

Usaremos este dataset para determinar si una persona puede **está sana, tiene prediabetes o tiene diabetes**. Este modelo de machine learning está orientado a centros de salud que deseen realizar un análisis preventivo de sus pacientes, con el objetivo de identificar casos que requieran seguimiento médico temprano.

Para ello deberán rellenar de un formulario que consta de 23 preguntas y devuelve una de las siguientes opciones:
- "No presenta diabetes."
- "Prediabetes detectada. Se recomienda vigilancia médica."
- "¡Diabetes diagnosticada! Consulte a un especialista."

El proyecto consta de un backend realizado con FastApi y conectado a una base de datos en línea en Supabase, y un frontend con Dash.
