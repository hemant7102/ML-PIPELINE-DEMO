import numpy as np
import pandas as pd

import pickle
import json

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score
)

# Load the trained model
with open("model.pkl", "rb") as file:
    clf = pickle.load(file)

# Load test data
test_data = pd.read_csv("./data/features/test_bow.csv")

# Separate features and target
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Generate predictions
y_pred = clf.predict(X_test)
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

# Calculate ROC-AUC
auc = roc_auc_score(
    y_test,
    y_pred_proba,
    labels=clf.classes_
)

# Store evaluation metrics
metrics_dict = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "auc": float(auc)
}

# Save metrics to JSON
with open("metrics.json", "w") as file:
    json.dump(metrics_dict, file, indent=4)

# Display evaluation results
print("\nModel Evaluation Metrics")
print("-" * 30)

for metric, value in metrics_dict.items():
    print(f"{metric.capitalize()}: {value:.4f}")

print("\nMetrics saved successfully to metrics.json")