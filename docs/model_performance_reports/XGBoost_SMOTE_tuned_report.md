# Performance Report for XGBoost (Tuned with SMOTE)

**Best Parameters (CV):**
```json
{'subsample': 0.8, 'n_estimators': 200, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score:** 0.7229

**Tuning Time:** 120.39 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.88      0.92      0.90     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.47      0.41      0.44      7019

    accuracy                           0.83     45957
   macro avg       0.45      0.44      0.45     45957
weighted avg       0.80      0.83      0.81     45957
```

## Confusion Matrix on Test Set
```
[[35057     1  2954]
 [  704     0   222]
 [ 4147     0  2872]]
```
