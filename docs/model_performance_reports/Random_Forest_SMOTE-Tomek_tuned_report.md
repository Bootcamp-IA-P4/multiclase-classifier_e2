# Performance Report for Random Forest (Tuned with SMOTE-Tomek)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score:** 0.7935

**Tuning Time:** 2271.11 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.95      0.60      0.73     38012
 Prediabetes       0.03      0.09      0.04       926
    Diabetes       0.29      0.79      0.42      7019

    accuracy                           0.62     45957
   macro avg       0.42      0.49      0.40     45957
weighted avg       0.83      0.62      0.67     45957
```

## Confusion Matrix on Test Set
```
[[22730  2294 12988]
 [  243    85   598]
 [  977   491  5551]]
```
