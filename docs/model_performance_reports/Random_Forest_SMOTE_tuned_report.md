# Performance Report for Random Forest (Tuned with SMOTE)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score:** 0.8805

**Tuning Time:** 5889.03 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.88      0.90      0.89     38012
 Prediabetes       0.06      0.00      0.01       926
    Diabetes       0.44      0.43      0.44      7019

    accuracy                           0.81     45957
   macro avg       0.46      0.45      0.45     45957
weighted avg       0.80      0.81      0.81     45957
```

## Confusion Matrix on Test Set
```
[[34349    46  3617]
 [  653     4   269]
 [ 3956    18  3045]]
```
