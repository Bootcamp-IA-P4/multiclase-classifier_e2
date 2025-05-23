# Performance Report for Gradient Boosting (Tuned with SMOTE)

**Best Parameters (CV):**
```json
{'n_estimators': 200, 'max_depth': 5, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.7966

**Tuning Time:** 8683.85 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.86      0.96      0.91     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.53      0.29      0.37      7019

    accuracy                           0.84     45957
   macro avg       0.46      0.41      0.43     45957
weighted avg       0.79      0.84      0.81     45957
```

## Confusion Matrix on Test Set
```
[[36365     0  1647]
 [  794     0   132]
 [ 4997     0  2022]]
```
