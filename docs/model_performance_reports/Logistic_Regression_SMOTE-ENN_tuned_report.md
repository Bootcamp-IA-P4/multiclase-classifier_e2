# Performance Report for Logistic Regression (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'penalty': 'l2', 'C': 1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.4217

**Tuning Time:** 20.92 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.99      0.09      0.17     38012
 Prediabetes       0.02      0.98      0.04       926
    Diabetes       0.65      0.02      0.05      7019

    accuracy                           0.10     45957
   macro avg       0.55      0.36      0.08     45957
weighted avg       0.92      0.10      0.15     45957
```

## Confusion Matrix on Test Set
```
[[ 3438 34493    81]
 [   10   904    12]
 [   21  6827   171]]
```
