# src/model_utilities.py

import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def save_model_and_report(model, model_name, set_name, best_params, best_score, tuning_time, report, cm, models_dir, reports_dir, show_plot=False, train_score=None):
    """
    Guarda el modelo optimizado y genera un informe de rendimiento en formato Markdown.
    También puede mostrar la matriz de confusión.

    Args:
        model: El modelo de sklearn entrenado y optimizado.
        model_name (str): El nombre del modelo (e.g., 'Logistic Regression', 'Random Forest').
        set_name (str): El nombre del conjunto de datos utilizado para el entrenamiento (e.g., 'Original', 'SMOTE').
        best_params (dict): Los mejores hiperparámetros encontrados durante la optimización.
        best_score (float): El mejor score de validación cruzada obtenido.
        tuning_time (float): El tiempo que tomó el proceso de optimización.
        report (str): El informe de clasificación generado por sklearn.
        cm (ndarray): La matriz de confusión.
        models_dir (str): Directorio donde guardar el modelo.
        reports_dir (str): Directorio donde guardar el informe.
        show_plot (bool): Si es True, muestra la matriz de confusión como un plot.
        train_score (float, optional): El score del modelo en el conjunto de entrenamiento. Usado para detectar overfitting.
    """
    # Asegurar que los directorios existan
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

    # Guardar el modelo
    optimized_model_filename = os.path.join(models_dir, f"{model_name.replace(' ', '_')}_{set_name.replace(' ', '_')}_tuned.joblib")
    joblib.dump(model, optimized_model_filename)
    print(f"Modelo optimizado guardado: {optimized_model_filename}")

    # Guardar el informe en un archivo .md
    report_filename = os.path.join(reports_dir, f"{model_name.replace(' ', '_')}_{set_name.replace(' ', '_')}_tuned_report.md")
    with open(report_filename, 'w') as f:
        f.write(f"# Performance Report for {model_name} (Tuned with {set_name})\n\n")
        f.write(f"**Best Parameters (CV):**\n```json\n{best_params}\n```\n\n")
        f.write(f"**Best CV Score (Validation - Precision Prediabetes):** {best_score:.4f}\n\n") # Cambiado para claridad
        
        if train_score is not None:
            f.write(f"**Train Score (Precision Prediabetes):** {train_score:.4f}\n\n") # Añadido el score de entrenamiento
            
            # Calcular y explicar el overfitting
            overfitting_diff = train_score - best_score
            f.write(f"## Overfitting Analysis\n\n")
            f.write(f"The difference between the Train Score ({train_score:.4f}) and the Best CV Score (Validation) ({best_score:.4f}) is: **{overfitting_diff:.4f}**.\n\n")
            f.write("A large positive difference indicates potential overfitting, meaning the model performs much better on the training data than on unseen validation data. A value closer to 0 suggests a better balance between bias and variance.\n\n")
            
        f.write(f"**Tuning Time:** {tuning_time:.2f} seconds\n\n")
        f.write("## Classification Report on Test Set\n")
        f.write("```\n")
        f.write(report)
        f.write("```\n\n")
        f.write("## Confusion Matrix on Test Set\n")
        f.write("```\n")
        f.write(str(cm)) # Convertir la matriz de confusión a string para escribirla
        f.write("\n```\n")
    print(f"Informe guardado: {report_filename}")

    if show_plot:
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['No Diabetes', 'Prediabetes', 'Diabetes'],
                    yticklabels=['No Diabetes', 'Prediabetes', 'Diabetes'])
        plt.title(f'Matriz de Confusión - {model_name} (Optimizado con {set_name})')
        plt.xlabel('Predicción')
        plt.ylabel('Real')
        plt.show()
