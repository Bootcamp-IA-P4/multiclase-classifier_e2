# Performance Report for Logistic Regression (Tuned with SMOTE)

**Best Parameters (CV):**
```json
{'penalty': 'l2', 'C': 10}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.3413

**Tuning Time:** 28.38 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.99      0.07      0.12     38012
 Prediabetes       0.02      0.98      0.04       926
    Diabetes       0.65      0.01      0.03      7019

    accuracy                           0.08     45957
   macro avg       0.55      0.35      0.06     45957
weighted avg       0.92      0.08      0.11     45957
```

## Confusion Matrix on Test Set
```
[[ 2517 35454    41]
 [   10   909     7]
 [   12  6917    90]]
```
