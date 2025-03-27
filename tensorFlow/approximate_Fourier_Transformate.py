import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


# Generate training data: Time-domain signals (sum of sine waves)
def generate_signal(num_samples=1000, num_points=128):
    x_values = np.linspace(0, 2 * np.pi, num_points)  # Time domain
    signals = []
    fourier_coeffs = []

    for _ in range(num_samples):
        freqs = np.random.randint(1, 10, size=3)  # 3 random frequencies
        amps = np.random.rand(3)  # 3 random amplitudes
        phase = np.random.rand(3) * 2 * np.pi  # 3 random phase shifts

        signal = sum(amp * np.sin(freq * x_values + p) for amp, freq, p in zip(amps, freqs, phase))
        signals.append(signal)

        # Compute Discrete Fourier Transform (DFT)
        fourier_transform = np.fft.fft(signal).real  # Use only real part for simplicity
        fourier_coeffs.append(fourier_transform[:num_points // 2])  # Only keep first half (symmetry)

    return np.array(signals), np.array(fourier_coeffs)


# Generate dataset
num_samples = 2000
num_points = 128
x_train, y_train = generate_signal(num_samples, num_points)

# Split into training and test sets
split_idx = int(0.8 * num_samples)
x_test, y_test = x_train[split_idx:], y_train[split_idx:]
x_train, y_train = x_train[:split_idx], y_train[:split_idx]

# Build the neural network model
model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape=(num_points,)),  # Input: Time-domain signal
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(num_points // 2)  # Output: Fourier coefficients
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1)

# Test the model
y_pred = model.predict(x_test)

# Visualize results
plt.figure(figsize=(10, 5))

# Choose a sample index to visualize
sample_idx = np.random.randint(0, len(x_test))

plt.subplot(1, 2, 1)
plt.plot(x_test[sample_idx], label="Original Signal")
plt.title("Time-Domain Signal")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(y_test[sample_idx], label="True Fourier Coefficients", linestyle="dashed")
plt.plot(y_pred[sample_idx], label="NN Approximation", linestyle="solid")
plt.title("Fourier Transform Approximation")
plt.legend()

plt.show()
