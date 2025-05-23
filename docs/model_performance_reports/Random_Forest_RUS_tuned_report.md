# Performance Report for Random Forest (Tuned with RUS)

**Best Parameters (CV):**
```json
{'n_estimators': 200, 'min_samples_leaf': 1, 'max_features': 'log2', 'max_depth': 20}
```

**Best CV Score (Validation - Precision Prediabetes):** 0.3732

**Tuning Time:** 13.20 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.96      0.38      0.55     38012
 Prediabetes       0.02      0.57      0.05       926
    Diabetes       0.35      0.45      0.39      7019

    accuracy                           0.40     45957
   macro avg       0.45      0.47      0.33     45957
weighted avg       0.85      0.40      0.51     45957
```

## Confusion Matrix on Test Set
```
[[14526 17988  5498]
 [  108   524   294]
 [  440  3428  3151]]
```
