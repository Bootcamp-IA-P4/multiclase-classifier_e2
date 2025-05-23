# Performance Report for Random Forest (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.8468

**Tuning Time:** 1108.27 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.96      0.52      0.67     38012
 Prediabetes       0.03      0.11      0.05       926
    Diabetes       0.27      0.83      0.41      7019

    accuracy                           0.56     45957
   macro avg       0.42      0.49      0.37     45957
weighted avg       0.84      0.56      0.62     45957
```

## Confusion Matrix on Test Set
```
[[19635  3020 15357]
 [  173   105   648]
 [  600   569  5850]]
```
