# Performance Report for Random Forest (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.8259

**Tuning Time:** 1359.00 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.60      0.74     38012
 Prediabetes       0.03      0.07      0.04       926
    Diabetes       0.29      0.81      0.43      7019

    accuracy                           0.62     45957
   macro avg       0.42      0.49      0.40     45957
weighted avg       0.83      0.62      0.68     45957
```

## Confusion Matrix on Test Set
```
[[22871  1725 13416]
 [  238    64   624]
 [  960   364  5695]]
```
