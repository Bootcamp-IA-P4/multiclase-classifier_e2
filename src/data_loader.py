# src/data_loader.py
import pandas as pd
import joblib
import os
import pyarrow.parquet as pq

def is_valid_parquet(filepath):
    if not os.path.exists(filepath):
        return False
    if os.path.getsize(filepath) == 0:
        return False
    try:
        pq.read_metadata(filepath)
        return True
    except Exception as e:
        return False

def load_processed_data(data_dir='../data/processed_data'):
    X_train_scaled_path = os.path.join(data_dir, 'X_train_scaled.parquet')
    X_test_scaled_path = os.path.join(data_dir, 'X_test_scaled.parquet')
    y_train_path = os.path.join(data_dir, 'y_train.parquet')
    y_test_path = os.path.join(data_dir, 'y_test.parquet')
    scaler_path = os.path.join(data_dir, 'scaler.joblib')

    if not (is_valid_parquet(X_train_scaled_path) and
            is_valid_parquet(X_test_scaled_path) and
            is_valid_parquet(y_train_path) and
            is_valid_parquet(y_test_path) and
            os.path.exists(scaler_path)):
        raise FileNotFoundError("Algunos archivos de datos preprocesados o el escalador no existen o están corruptos.")

    X_train_scaled = pd.read_parquet(X_train_scaled_path)
    X_test_scaled = pd.read_parquet(X_test_scaled_path)
    y_train = pd.read_parquet(y_train_path).squeeze()
    y_test = pd.read_parquet(y_test_path).squeeze()
    scaler = joblib.load(scaler_path)

    # Cargar los datasets SMOTE y RUS preexistentes si existen
    X_train_smote_prev, y_train_smote_prev = None, None
    smote_paths = (os.path.join(data_dir, 'X_train_smote.parquet'), os.path.join(data_dir, 'y_train_smote.parquet'))
    if is_valid_parquet(smote_paths[0]) and is_valid_parquet(smote_paths[1]):
        X_train_smote_prev = pd.read_parquet(smote_paths[0])
        y_train_smote_prev = pd.read_parquet(smote_paths[1]).squeeze()

    X_train_rus_prev, y_train_rus_prev = None, None
    rus_paths = (os.path.join(data_dir, 'X_train_rus.parquet'), os.path.join(data_dir, 'y_train_rus.parquet'))
    if is_valid_parquet(rus_paths[0]) and is_valid_parquet(rus_paths[1]):
        X_train_rus_prev = pd.read_parquet(rus_paths[0])
        y_train_rus_prev = pd.read_parquet(rus_paths[1]).squeeze()

    print("Datos preprocesados cargados exitosamente.")
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X_train_smote_prev, y_train_smote_prev, X_train_rus_prev, y_train_rus_prev