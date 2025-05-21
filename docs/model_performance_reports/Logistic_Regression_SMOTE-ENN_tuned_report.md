# Performance Report for Logistic Regression (Tuned with SMOTE-ENN)

**Best Parameters (CV):**
```json
{'penalty': 'l1', 'C': 0.1}
```

**Best CV Score:** 0.5563

**Tuning Time:** 79.41 seconds

## Classification Report on Test Set
```
              precision    recall  f1-score   support

 No Diabetes       0.96      0.57      0.72     38012
 Prediabetes       0.03      0.38      0.05       926
    Diabetes       0.36      0.57      0.44      7019

    accuracy                           0.57     45957
   macro avg       0.45      0.51      0.40     45957
weighted avg       0.85      0.57      0.66     45957
```

## Confusion Matrix on Test Set
```
[[21789  9481  6742]
 [  208   349   369]
 [  812  2180  4027]]
```
