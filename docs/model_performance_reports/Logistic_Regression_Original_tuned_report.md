# Performance Report for Logistic Regression (Tuned with Original)

**Best Parameters (CV):**
```json
{'penalty': 'l1', 'C': 0.01}
```

**Best CV Score:** 0.7980

**Tuning Time:** 25.26 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.89      0.89      0.89     38012
 Prediabetes       0.08      0.01      0.01       926
    Diabetes       0.43      0.49      0.46      7019

    accuracy                           0.81     45957
   macro avg       0.47      0.46      0.45     45957
weighted avg       0.80      0.81      0.80     45957
```

## Confusion Matrix on Test Set
```
[[33677    44  4291]
 [  617     6   303]
 [ 3570    23  3426]]
```
