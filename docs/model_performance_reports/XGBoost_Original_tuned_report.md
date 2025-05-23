# Performance Report for XGBoost (Tuned with Original)

**Best Parameters (CV):**
```json
{'subsample': 0.7, 'n_estimators': 200, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.0000

**Tuning Time:** 62.84 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.85      0.98      0.91     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.59      0.20      0.30      7019

    accuracy                           0.84     45957
   macro avg       0.48      0.39      0.40     45957
weighted avg       0.79      0.84      0.80     45957
```

## Confusion Matrix on Test Set
```
[[37126     0   886]
 [  843     0    83]
 [ 5631     0  1388]]
```
