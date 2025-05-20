# src/data_preprocessor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter
import joblib
import os
import pyarrow.parquet as pq

# Importar la función auxiliar del data_loader para la validación de parquet
from .data_loader import is_valid_parquet

# src/data_preprocessor.py (Actualizado)

import pandas as pd
import os
import pyarrow.parquet as pq
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


# Importar la función auxiliar del data_loader para la validación de parquet
# Asumiendo que is_valid_parquet está en data_loader.py
from .data_loader import is_valid_parquet


def remove_duplicates_and_save(df, data_dir='../data/processed_data', target_column='Diabetes_012'):
    """
    Elimina filas duplicadas de un DataFrame, imprime estadísticas de duplicados
    y guarda el DataFrame resultante en formato Parquet.

    Args:
        df (pd.DataFrame): El DataFrame de entrada que puede contener duplicados.
        data_dir (str): Directorio donde se guardará el DataFrame sin duplicados.
        target_column (str): Nombre de la columna objetivo para la visualización.

    Returns:
        pd.DataFrame: El DataFrame sin duplicados.
    """
    df_unique_path = os.path.join(data_dir, 'df_unique.parquet')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Directorio creado: {data_dir}")

    if is_valid_parquet(df_unique_path):
        print(f"Cargando df_unique desde {df_unique_path}...")
        df_unique = pd.read_parquet(df_unique_path)
        print("df_unique cargado exitosamente.")
    else:
        print("df_unique no encontrado o corrupto. Realizando eliminación de duplicados y guardando...")

        # Identificar el número de veces que se repite cada fila
        duplicate_counts = df.groupby(df.columns.tolist()).size().reset_index(name='counts')
        repeated_rows = duplicate_counts[duplicate_counts['counts'] > 1].sort_values(by='counts', ascending=False)
        print("Filas duplicadas y su frecuencia:")
        # Limita la impresión si hay muchas duplicadas
        print(repeated_rows.head(10) if len(repeated_rows) > 10 else repeated_rows)


        total_duplicates = df.duplicated(keep='first').sum()
        print(f"\nNúmero total de filas duplicadas (sin contar la primera ocurrencia): {total_duplicates}")

        df_unique = df.drop_duplicates(keep='first').reset_index(drop=True)
        print(f"\nTamaño del DataFrame original: {len(df)}")
        print(f"Tamaño del DataFrame después de eliminar duplicados: {len(df_unique)}")

        # Visualización de la distribución de la variable objetivo
        # NOTA: La visualización se deja en la función para mostrar la lógica completa,
        # pero para cuadernos interactivos, a veces es preferible que la visualización
        # se haga en el propio cuaderno después de obtener el df_unique.
        # Aquí la incluyo para que la salida sea igual a tu snippet original.
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df_unique, x=target_column) # Usar df_unique aquí
        plt.title(f'Distribución de la Variable Objetivo ({target_column}) después de eliminar duplicados')
        plt.xlabel('0: No Diabetes, 1: Prediabetes, 2: Diabetes')
        plt.ylabel('Número de Individuos')
        plt.show()

        print("\nProporción de cada clase en la variable objetivo después de eliminar duplicados:")
        print(df_unique[target_column].value_counts(normalize=True))

        print(f"\nGuardando df_unique en {df_unique_path}...")
        df_unique.to_parquet(df_unique_path, index=False)
        print("df_unique guardado exitosamente.")

    return df_unique

# Mantén el resto de las funciones en data_preprocessor.py como estaban
# (preprocess_and_resample_data y check_and_load_processed_data)
# ...

def preprocess_and_resample_data(df_unique, data_dir='../data/processed_data', random_state=42):
    """
    Realiza el preprocesamiento de datos (división, escalado) y aplica técnicas de remuestreo (SMOTE, RUS).
    Guarda los datasets resultantes y el escalador.

    Args:
        df_unique (pd.DataFrame): El DataFrame limpio y único de entrada.
        data_dir (str): Directorio donde se guardarán los datos procesados.
        random_state (int): Semilla para la reproducibilidad.

    Returns:
        tuple: Contiene X_train_scaled, X_test_scaled, y_train, y_test, scaler,
               X_train_smote, y_train_smote, X_train_rus, y_train_rus.
    """
    print("Datos preprocesados no encontrados o incompletos/corruptos. Realizando preprocesamiento desde el inicio...")

    # Asegurar que el directorio de datos procesados exista
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Directorio creado: {data_dir}")

    # Nombres de archivo para los datasets procesados
    X_train_scaled_path = os.path.join(data_dir, 'X_train_scaled.parquet')
    X_test_scaled_path = os.path.join(data_dir, 'X_test_scaled.parquet')
    y_train_path = os.path.join(data_dir, 'y_train.parquet')
    y_test_path = os.path.join(data_dir, 'y_test.parquet')
    X_train_smote_path = os.path.join(data_dir, 'X_train_smote.parquet')
    y_train_smote_path = os.path.join(data_dir, 'y_train_smote.parquet')
    X_train_rus_path = os.path.join(data_dir, 'X_train_rus.parquet')
    y_train_rus_path = os.path.join(data_dir, 'y_train_rus.parquet')
    scaler_path = os.path.join(data_dir, 'scaler.joblib')

    # Separar la variable objetivo (y) de las características (X)
    X = df_unique.drop('Diabetes_012', axis=1)
    y = df_unique['Diabetes_012']

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state, stratify=y)

    print("\n")
    print("Tamaño del conjunto de entrenamiento de características:", X_train.shape)
    print("Tamaño del conjunto de prueba de características:", X_test.shape)
    print("Tamaño del conjunto de entrenamiento de la variable objetivo:", y_train.shape)
    print("Tamaño del conjunto de prueba de la variable objetivo:", y_test.shape)

    # Inicializar y aplicar el escalador StandardScaler
    scaler = StandardScaler()
    numerical_cols = X_train.columns

    X_train_scaled = scaler.fit_transform(X_train[numerical_cols])
    X_test_scaled = scaler.transform(X_test[numerical_cols])

    X_train_scaled = pd.DataFrame(X_train_scaled, columns=numerical_cols, index=X_train.index)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=numerical_cols, index=X_test.index)

    print("\nPrimeras 5 filas del conjunto de entrenamiento escalado:")
    print(X_train_scaled.head())
    print("\nPrimeras 5 filas del conjunto de prueba escalado:")
    print(X_test_scaled.head())

    # --- Aplicar SMOTE y Random Under-Sampling ---
    smote = SMOTE(random_state=random_state)
    X_train_smote_array, y_train_smote_array = smote.fit_resample(X_train_scaled, y_train)
    print("\nDistribución de clases después de SMOTE:", Counter(y_train_smote_array))

    rus = RandomUnderSampler(random_state=random_state)
    X_train_rus_array, y_train_rus_array = rus.fit_resample(X_train_scaled, y_train)
    print("Distribución de clases después de Random Under-Sampling:", Counter(y_train_rus_array))

    X_train_smote = pd.DataFrame(X_train_smote_array, columns=numerical_cols)
    y_train_smote = pd.Series(y_train_smote_array, name='Diabetes_012')

    X_train_rus = pd.DataFrame(X_train_rus_array, columns=numerical_cols)
    y_train_rus = pd.Series(y_train_rus_array, name='Diabetes_012')

    # --- Guardar los datos procesados y el escalador ---
    print("\nGuardando datos preprocesados y escalador...")
    X_train_scaled.to_parquet(X_train_scaled_path, index=True)
    X_test_scaled.to_parquet(X_test_scaled_path, index=True)
    y_train.to_frame(name='Diabetes_012').to_parquet(y_train_path, index=True)
    y_test.to_frame(name='Diabetes_012').to_parquet(y_test_path, index=True)
    X_train_smote.to_parquet(X_train_smote_path, index=True)
    y_train_smote.to_frame(name='Diabetes_012').to_parquet(y_train_smote_path, index=True)
    X_train_rus.to_parquet(X_train_rus_path, index=True)
    y_train_rus.to_frame(name='Diabetes_012').to_parquet(y_train_rus_path, index=True)
    joblib.dump(scaler, scaler_path)
    print("Datos y escalador guardados exitosamente para futuras sesiones.")

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X_train_smote, y_train_smote, X_train_rus, y_train_rus

def check_and_load_processed_data(data_dir='../data/processed_data'):
    """
    Verifica si los datos preprocesados y remuestreados existen y son válidos,
    y los carga si es así.

    Args:
        data_dir (str): Directorio donde se buscan los datos procesados.

    Returns:
        tuple: (bool, data_tuple) donde bool indica si los datos fueron cargados,
               y data_tuple contiene los datos cargados o None si no se cargaron.
    """
    X_train_scaled_path = os.path.join(data_dir, 'X_train_scaled.parquet')
    X_test_scaled_path = os.path.join(data_dir, 'X_test_scaled.parquet')
    y_train_path = os.path.join(data_dir, 'y_train.parquet')
    y_test_path = os.path.join(data_dir, 'y_test.parquet')
    X_train_smote_path = os.path.join(data_dir, 'X_train_smote.parquet')
    y_train_smote_path = os.path.join(data_dir, 'y_train_smote.parquet')
    X_train_rus_path = os.path.join(data_dir, 'X_train_rus.parquet')
    y_train_rus_path = os.path.join(data_dir, 'y_train_rus.parquet')
    scaler_path = os.path.join(data_dir, 'scaler.joblib')

    all_files_exist_and_valid = (
        is_valid_parquet(X_train_scaled_path) and
        is_valid_parquet(X_test_scaled_path) and
        is_valid_parquet(y_train_path) and
        is_valid_parquet(y_test_path) and
        is_valid_parquet(X_train_smote_path) and
        is_valid_parquet(y_train_smote_path) and
        is_valid_parquet(X_train_rus_path) and
        is_valid_parquet(y_train_rus_path) and
        os.path.exists(scaler_path)
    )

    if all_files_exist_and_valid:
        print("Cargando datos preprocesados y escalador desde archivos...")
        try:
            X_train_scaled = pd.read_parquet(X_train_scaled_path)
            X_test_scaled = pd.read_parquet(X_test_scaled_path)
            y_train = pd.read_parquet(y_train_path).squeeze()
            y_test = pd.read_parquet(y_test_path).squeeze()
            X_train_smote = pd.read_parquet(X_train_smote_path)
            y_train_smote = pd.read_parquet(y_train_smote_path).squeeze()
            X_train_rus = pd.read_parquet(X_train_rus_path)
            y_train_rus = pd.read_parquet(y_train_rus_path).squeeze()
            scaler = joblib.load(scaler_path)
            print("Datos cargados exitosamente.")
            return True, (X_train_scaled, X_test_scaled, y_train, y_test, scaler,
                          X_train_smote, y_train_smote, X_train_rus, y_train_rus)
        except Exception as e:
            print(f"Error al cargar datos. Se recomienda reprocesar: {e}")
            return False, None
    else:
        print("Algunos datos preprocesados no encontrados o incompletos/corruptos.")
        return False, None