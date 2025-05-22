# Performance Report for Gradient Boosting (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'n_estimators': 200, 'max_depth': 5, 'learning_rate': 0.1}
```

**Best CV Score:** 0.8107

**Tuning Time:** 13328.21 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.92      0.80      0.85     38012
 Prediabetes       0.07      0.01      0.01       926
    Diabetes       0.37      0.67      0.47      7019

    accuracy                           0.76     45957
   macro avg       0.45      0.49      0.45     45957
weighted avg       0.82      0.76      0.78     45957
```

## Confusion Matrix on Test Set
```
[[30274    54  7684]
 [  464     5   457]
 [ 2292    14  4713]]
```
