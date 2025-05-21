# Performance Report for Random Forest (Tuned with Original)

**Best Parameters (CV):**
```json
{'n_estimators': 200, 'min_samples_leaf': 1, 'max_features': 'log2', 'max_depth': 20}
```

**Best CV Score:** 0.7944

**Tuning Time:** 376.27 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.88      0.90      0.89     38012
 Prediabetes       0.04      0.01      0.02       926
    Diabetes       0.41      0.40      0.41      7019

    accuracy                           0.80     45957
   macro avg       0.44      0.44      0.44     45957
weighted avg       0.79      0.80      0.80     45957
```

## Confusion Matrix on Test Set
```
[[34057   210  3745]
 [  675    10   241]
 [ 4141    58  2820]]
```
