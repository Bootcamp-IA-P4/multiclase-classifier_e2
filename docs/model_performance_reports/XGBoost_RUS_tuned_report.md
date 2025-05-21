# Performance Report for XGBoost (Tuned with RUS)

**Best Parameters (CV):**
```json
{'subsample': 0.8, 'n_estimators': 200, 'max_depth': 3, 'learning_rate': 0.1}
```

**Best CV Score:** 0.4950

**Tuning Time:** 5.18 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.61      0.74     38012
 Prediabetes       0.03      0.34      0.06       926
    Diabetes       0.36      0.59      0.45      7019

    accuracy                           0.60     45957
   macro avg       0.45      0.51      0.42     45957
weighted avg       0.84      0.60      0.68     45957
```

## Confusion Matrix on Test Set
```
[[23164  7890  6958]
 [  231   315   380]
 [ 1027  1831  4161]]
```
