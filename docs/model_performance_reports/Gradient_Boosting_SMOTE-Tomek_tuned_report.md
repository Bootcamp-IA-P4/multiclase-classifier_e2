# Performance Report for Gradient Boosting (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'n_estimators': 100, 'max_depth': 5, 'learning_rate': 0.2}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.7964

**Tuning Time:** 7997.85 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.86      0.95      0.91     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.53      0.29      0.38      7019

    accuracy                           0.83     45957
   macro avg       0.46      0.42      0.43     45957
weighted avg       0.79      0.83      0.81     45957
```

## Confusion Matrix on Test Set
```
[[36296     0  1716]
 [  790     0   136]
 [ 4958     0  2061]]
```
