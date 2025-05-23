# Performance Report for Logistic Regression (Tuned with RUS)

**Best Parameters (CV):**
```json
{'penalty': 'l1', 'C': 100}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.3368

**Tuning Time:** 0.54 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.99      0.03      0.06     38012
 Prediabetes       0.02      0.99      0.04       926
    Diabetes       0.73      0.00      0.01      7019

    accuracy                           0.05     45957
   macro avg       0.58      0.34      0.04     45957
weighted avg       0.93      0.05      0.05     45957
```

## Confusion Matrix on Test Set
```
[[ 1136 36868     8]
 [    6   919     1]
 [    4  6991    24]]
```
