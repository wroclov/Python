import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Generate training data
x_train = np.linspace(-10, 10, 1000).reshape(-1, 1)
y_train = x_train ** 2  # Function: f(x) = x²
y_derivative = 2 * x_train  # Derivative: f'(x) = 2x

# Different epoch values to test
EPOCH_VALUES = [15, 30, 50]

# Store results for plotting
results_fx = {}
results_fx_derivative = {}

# Train models for different epoch values
for epochs in EPOCH_VALUES:
    print(f"Training models for {epochs} epochs...")

    # Define and train f(x) = x² model
    model_fx = keras.Sequential([
        keras.layers.Dense(32, activation='relu', input_shape=(1,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1)  # Output: f(x) = x²
    ])
    model_fx.compile(optimizer='adam', loss='mse')
    model_fx.fit(x_train, y_train, epochs=epochs, verbose=0)

    # Define and train f'(x) = 2x model
    model_fx_derivative = keras.Sequential([
        keras.layers.Dense(32, activation='relu', input_shape=(1,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(1)  # Output: f'(x) = 2x
    ])
    model_fx_derivative.compile(optimizer='adam', loss='mse')
    model_fx_derivative.fit(x_train, y_derivative, epochs=epochs, verbose=0)

    # Generate test data and store predictions
    x_test = np.linspace(-10, 10, 200).reshape(-1, 1)
    results_fx[epochs] = model_fx.predict(x_test)
    results_fx_derivative[epochs] = model_fx_derivative.predict(x_test)

print("Training completed. Plotting results...")

# Plot the results
plt.figure(figsize=(12, 6))

# Plot f(x) = x² approximations
plt.subplot(1, 2, 1)
plt.plot(x_test, x_test ** 2, label="True x²", linestyle="dashed")
for epochs in EPOCH_VALUES:
    plt.plot(x_test, results_fx[epochs], label=f"{epochs} epochs", linestyle="solid")
plt.legend()
plt.title("Approximation of x²")

# Plot f'(x) = 2x approximations
plt.subplot(1, 2, 2)
plt.plot(x_test, 2 * x_test, label="True 2x (Derivative)", linestyle="dashed")
for epochs in EPOCH_VALUES:
    plt.plot(x_test, results_fx_derivative[epochs], label=f"{epochs} epochs", linestyle="solid")
plt.legend()
plt.title("Approximation of 2x (Derivative)")

plt.show()
