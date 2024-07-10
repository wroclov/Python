import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Generate synthetic time series data
def generate_time_series(batch_size, n_steps):
    freq1, freq2, offsets1, offsets2 = np.random.rand(4, batch_size, 1)
    time = np.linspace(0, 1, n_steps)
    series = 0.5 * np.sin((time - offsets1) * (freq1 * 10 + 10))  # wave 1
    series += 0.2 * np.sin((time - offsets2) * (freq2 * 30 + 30))  # wave 2
    series += 0.1 * (np.random.rand(batch_size, n_steps) - 0.5)    # noise
    return series[..., np.newaxis].astype(np.float32)

# Generate data
n_steps = 50
series = generate_time_series(10000, n_steps + 1)
X_train, y_train = series[:7000, :n_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :n_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :n_steps], series[9000:, -1]

# Define the LSTM model
model = models.Sequential([
    layers.LSTM(50, return_sequences=True, input_shape=[None, 1]),
    layers.LSTM(50),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=30, validation_data=(X_valid, y_valid))

# Evaluate the model
mse = model.evaluate(X_test, y_test)
print(f'Test MSE: {mse}')

# Predict and plot the results
y_pred = model.predict(X_test)

# Plotting
plt.figure(figsize=(10, 5))

# Plot true values and predicted values
plt.plot(y_test, label='True', linestyle='-', color='b')
plt.plot(y_pred, label='Predicted', linestyle='-', color='r')

# Labeling the plot
plt.xlabel('Time Steps')
plt.ylabel('Value')
plt.title('True vs Predicted Values')
plt.legend()
plt.grid(True)
plt.show()
