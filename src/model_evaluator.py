import joblib
import os

def save_model_and_report(model, model_name, set_name, best_params, best_score, tuning_time, report, cm, models_dir, reports_dir):
    """
    Guarda el modelo optimizado y genera un informe de rendimiento en formato Markdown.

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
    """
    # Guardar el modelo
    optimized_model_filename = os.path.join(models_dir, f"{model_name.replace(' ', '_')}_{set_name.replace(' ', '_')}_tuned.joblib")
    joblib.dump(model, optimized_model_filename)
    print(f"Modelo optimizado guardado: {optimized_model_filename}")

    # Guardar el informe en un archivo .md
    report_filename = os.path.join(reports_dir, f"{model_name.replace(' ', '_')}_{set_name.replace(' ', '_')}_tuned_report.md")
    with open(report_filename, 'w') as f:
        f.write(f"# Performance Report for {model_name} (Tuned with {set_name})\n\n")
        f.write(f"**Best Parameters (CV):**\n```json\n{best_params}\n```\n\n")
        f.write(f"**Best CV Score:** {best_score:.4f}\n\n") # Generalizamos el nombre del score
        f.write(f"**Tuning Time:** {tuning_time:.2f} seconds\n\n")
        f.write("## Classification Report on Test Set\n")
        f.write("```\n")
        f.write(report)
        f.write("```\n\n")
        f.write("## Confusion Matrix on Test Set\n")
        f.write("```\n")
        f.write(str(cm))
        f.write("\n```\n")
    print(f"Informe guardado: {report_filename}")