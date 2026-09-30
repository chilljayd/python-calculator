import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 2. Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 4. Make predictions on the test set
y_pred = clf.predict(X_test)

# 5. Evaluate Performance
accuracy = accuracy_score(y_test, y_pred)

# 'weighted' or 'macro' averaging accounts for multi-class targets (3 species)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')

print("=" * 45)
print("     DECISION TREE MODEL EVALUATION METRICS")
print("=" * 45)
print(f"Overall Accuracy  : {accuracy:.4f}")
print(f"Weighted Precision: {precision:.4f}")
print(f"Weighted Recall   : {recall:.4f}")
print("-" * 45)

# Detailed per-class classification report
print("\nClassification Report (Per-Species Breakout):\n")
print(classification_report(y_test, y_pred, target_names=target_names))

# Print decision logic structure
print("=" * 45)
print("          DECISION TREE RULES LOGIC")
print("=" * 45)
print(export_text(clf, feature_names=feature_names))
