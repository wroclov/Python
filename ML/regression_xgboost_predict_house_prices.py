from xgboost import XGBRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = fetch_california_housing()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    objective="reg:squarederror"
)

# reg:squarederror is used for regression
# XGBoost needs a way to measure how wrong its predictions are.
# The algorithm tries to minimize the total squared prediction
# errors by building additional decision trees.

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, predictions))
print("Predictions", predictions)