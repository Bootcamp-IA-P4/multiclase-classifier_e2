# Performance Report for Random Forest (Tuned with RUS)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score:** 0.4888

**Tuning Time:** 16.16 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.62      0.75     38012
 Prediabetes       0.03      0.34      0.06       926
    Diabetes       0.36      0.59      0.45      7019

    accuracy                           0.61     45957
   macro avg       0.45      0.52      0.42     45957
weighted avg       0.84      0.61      0.69     45957
```

## Confusion Matrix on Test Set
```
[[23529  7489  6994]
 [  242   312   372]
 [ 1072  1803  4144]]
```
