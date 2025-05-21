# Performance Report for Logistic Regression (Tuned with SMOTE)

**Best Parameters (CV):**
```json
{'penalty': 'l2', 'C': 10}
```

**Best CV Score:** 0.4990

**Tuning Time:** 43.30 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.94      0.67      0.78     38012
 Prediabetes       0.03      0.27      0.06       926
    Diabetes       0.36      0.60      0.45      7019

    accuracy                           0.65     45957
   macro avg       0.45      0.51      0.43     45957
weighted avg       0.83      0.65      0.71     45957
```

## Confusion Matrix on Test Set
```
[[25297  5728  6987]
 [  284   248   394]
 [ 1380  1403  4236]]
```
