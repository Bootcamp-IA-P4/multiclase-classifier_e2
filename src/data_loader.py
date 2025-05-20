# src/data_loader.py

import pandas as pd
import os
import pyarrow.parquet as pq # Importar pyarrow para verificar la validez del archivo Parquet

def is_valid_parquet(filepath):
    """
    Verifica si un archivo Parquet existe y es válido (no vacío ni corrupto).
    """
    if not os.path.exists(filepath):
        return False
    if os.path.getsize(filepath) == 0:  # Archivo vacío
        return False
    try:
        # Intenta leer los metadatos sin cargar todo el contenido
        pq.read_metadata(filepath)
        return True
    except Exception as e:
        print(f"Advertencia: Archivo Parquet corrupto o inválido en {filepath}: {e}")
        return False

def load_raw_data(raw_data_path='../data/diabetes_012_health_indicators.csv'):
    """
    Carga el DataFrame original desde un archivo CSV.
    """
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"El archivo de datos brutos no se encuentra en: {raw_data_path}")
    print(f"Cargando datos brutos desde: {raw_data_path}")
    df = pd.read_csv(raw_data_path)
    print("Datos brutos cargados exitosamente.")
    return df