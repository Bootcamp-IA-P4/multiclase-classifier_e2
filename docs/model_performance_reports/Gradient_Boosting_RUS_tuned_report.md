# Performance Report for Gradient Boosting (Tuned with RUS)

**Best Parameters (CV):**
```json
{'n_estimators': 100, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.4156

**Tuning Time:** 53.00 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.61      0.74     38012
 Prediabetes       0.03      0.34      0.06       926
    Diabetes       0.36      0.60      0.45      7019

    accuracy                           0.60     45957
   macro avg       0.45      0.52      0.42     45957
weighted avg       0.84      0.60      0.68     45957
```

## Confusion Matrix on Test Set
```
[[23230  7650  7132]
 [  234   315   377]
 [  999  1822  4198]]
```
