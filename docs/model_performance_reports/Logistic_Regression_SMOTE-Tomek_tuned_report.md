# Performance Report for Logistic Regression (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'penalty': 'l1', 'C': 1}
```

**Best CV Score:** 0.5008

**Tuning Time:** 97.10 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.94      0.66      0.78     38012
 Prediabetes       0.03      0.27      0.06       926
    Diabetes       0.37      0.60      0.45      7019

    accuracy                           0.65     45957
   macro avg       0.45      0.51      0.43     45957
weighted avg       0.83      0.65      0.71     45957
```

## Confusion Matrix on Test Set
```
[[25232  5847  6933]
 [  285   253   388]
 [ 1371  1439  4209]]
```
