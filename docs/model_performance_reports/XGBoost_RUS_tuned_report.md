# Performance Report for XGBoost (Tuned with RUS)

**Best Parameters (CV):**
```json
{'subsample': 0.7, 'n_estimators': 100, 'max_depth': 7, 'learning_rate': 0.01}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.4101

**Tuning Time:** 11.50 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.62      0.75     38012
 Prediabetes       0.03      0.29      0.06       926
    Diabetes       0.35      0.62      0.45      7019

    accuracy                           0.61     45957
   macro avg       0.44      0.51      0.42     45957
weighted avg       0.84      0.61      0.69     45957
```

## Confusion Matrix on Test Set
```
[[23440  6973  7599]
 [  251   271   404]
 [ 1096  1589  4334]]
```
