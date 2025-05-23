# Performance Report for Random Forest (Tuned with Original)

**Best Parameters (CV):**
```json
{'n_estimators': 100, 'min_samples_leaf': 1, 'max_features': 'sqrt', 'max_depth': 20}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.0400

**Tuning Time:** 213.07 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.88      0.89      0.88     38012
 Prediabetes       0.03      0.01      0.02       926
    Diabetes       0.41      0.40      0.40      7019

    accuracy                           0.80     45957
   macro avg       0.44      0.43      0.44     45957
weighted avg       0.79      0.80      0.79     45957
```

## Confusion Matrix on Test Set
```
[[33953   240  3819]
 [  687    10   229]
 [ 4138    71  2810]]
```
