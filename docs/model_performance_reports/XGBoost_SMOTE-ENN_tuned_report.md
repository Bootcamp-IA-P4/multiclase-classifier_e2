# Performance Report for XGBoost (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'subsample': 0.7, 'n_estimators': 200, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.7597

**Tuning Time:** 192.03 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.93      0.74      0.82     38012
 Prediabetes       0.03      0.02      0.02       926
    Diabetes       0.34      0.73      0.46      7019

    accuracy                           0.73     45957
   macro avg       0.43      0.50      0.44     45957
weighted avg       0.82      0.73      0.75     45957
```

## Confusion Matrix on Test Set
```
[[28197   354  9461]
 [  394    14   518]
 [ 1791    84  5144]]
```
