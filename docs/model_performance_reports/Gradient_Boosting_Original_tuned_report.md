# Performance Report for Gradient Boosting (Tuned with Original)

**Best Parameters (CV):**
```json
{'n_estimators': 200, 'max_depth': 5, 'learning_rate': 0.1}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.0417

**Tuning Time:** 1310.04 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.85      0.98      0.91     38012
 Prediabetes       0.00      0.00      0.00       926
    Diabetes       0.58      0.20      0.29      7019

    accuracy                           0.84     45957
   macro avg       0.48      0.39      0.40     45957
weighted avg       0.79      0.84      0.80     45957
```

## Confusion Matrix on Test Set
```
[[37098     4   910]
 [  844     0    82]
 [ 5636     3  1380]]
```
