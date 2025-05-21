# Performance Report for Logistic Regression (Tuned with RUS)

**Best Parameters (CV):**
```json
{'penalty': 'l1', 'C': 100}
```

**Best CV Score:** 0.4756

**Tuning Time:** 0.96 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.94      0.67      0.78     38012
 Prediabetes       0.03      0.25      0.06       926
    Diabetes       0.35      0.61      0.45      7019

    accuracy                           0.65     45957
   macro avg       0.44      0.51      0.43     45957
weighted avg       0.83      0.65      0.71     45957
```

## Confusion Matrix on Test Set
```
[[25377  5157  7478]
 [  285   234   407]
 [ 1381  1338  4300]]
```
