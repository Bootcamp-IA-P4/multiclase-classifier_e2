# Performance Report for Random Forest (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'n_estimators': 300, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None}
```

**Best CV Score:** 0.8199

**Tuning Time:** 1699.69 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.96      0.51      0.67     38012
 Prediabetes       0.03      0.14      0.05       926
    Diabetes       0.27      0.81      0.41      7019

    accuracy                           0.55     45957
   macro avg       0.42      0.49      0.37     45957
weighted avg       0.84      0.55      0.62     45957
```

## Confusion Matrix on Test Set
```
[[19465  3753 14794]
 [  169   126   631]
 [  602   715  5702]]
```
