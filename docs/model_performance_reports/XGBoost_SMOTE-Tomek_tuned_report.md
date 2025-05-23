# Performance Report for XGBoost (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'subsample': 0.7, 'n_estimators': 200, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.7477

**Tuning Time:** 254.62 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.88      0.92      0.90     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.47      0.42      0.44      7019

    accuracy                           0.82     45957
   macro avg       0.45      0.45      0.45     45957
weighted avg       0.80      0.82      0.81     45957
```

## Confusion Matrix on Test Set
```
[[34880     3  3129]
 [  688     0   238]
 [ 4077     0  2942]]
```
