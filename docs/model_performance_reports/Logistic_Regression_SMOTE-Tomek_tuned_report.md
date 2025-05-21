# Performance Report for Logistic Regression (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'penalty': 'l2', 'C': 1}
```

**Best CV Score:** 0.3442

**Tuning Time:** 33.65 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.99      0.07      0.13     38012
 Prediabetes       0.02      0.98      0.04       926
    Diabetes       0.65      0.01      0.03      7019

    accuracy                           0.08     45957
   macro avg       0.56      0.35      0.06     45957
weighted avg       0.92      0.08      0.11     45957
```

## Confusion Matrix on Test Set
```
[[ 2544 35426    42]
 [   10   909     7]
 [   13  6913    93]]
```
