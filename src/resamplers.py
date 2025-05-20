# src/resamplers.py
from imblearn.combine import SMOTEENN, SMOTETomek
import pandas as pd # Para el value_counts

def apply_hybrid_resampling(X_train, y_train, method='smoteenn', random_state=42):
    print(f"\nAplicando técnica de remuestreo híbrida ({method})...")
    if method == 'smoteenn':
        resampler = SMOTEENN(random_state=random_state)
    elif method == 'smotetomek':
        resampler = SMOTETomek(random_state=random_state)
    else:
        raise ValueError("Método de remuestreo híbrido no soportado. Elija 'smoteenn' o 'smotetomek'.")

    X_resampled, y_resampled = resampler.fit_resample(X_train, y_train)
    print(f"Dataset {method.upper()}: X_resampled.shape={X_resampled.shape}, y_resampled.shape={y_resampled.shape}")
    print(f"Conteo de clases {method.upper()}:\n{pd.Series(y_resampled).value_counts()}")
    return X_resampled, y_resampled