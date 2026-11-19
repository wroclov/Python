
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print(f"Printing first iris flower data {X[0]}")
print(f"It contains [sepal length,sepal width,petal length,petal width]")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# stratify makes sure the proportions of diff classes are approx preserved
# in both training and testing datasets

# X_train - training features
# X_test - testing features
# y_train - training labels
# y_test - testing labels

# Create XGBoost model
model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    objective="multi:softprob",
    num_class=3,
    eval_metric="mlogloss",
    random_state=42
)

# multi:softprob is used because model will predict the probability of each class
# and then selects class with the highest probability

# options:
# reg:squarederror
# reg:absoluteerror
# binary:logistic
# multi:softprob
# multi:softmax

# Parameter	Meaning
# n_estimators	Number of boosting trees
# max_depth	Maximum tree depth
# learning_rate	Contribution of each tree
# subsample	Fraction of training samples per tree
# colsample_bytree	Fraction of features per tree
# reg_alpha	L1 regularization
# reg_lambda	L2 regularization
# objective	Defines the prediction task

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Predict a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)

print("Predicted species:", iris.target_names[prediction[0]])

