import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)


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

        # Compute Discrete Fourier Transform (DFT), using only real part
        fourier_transform = np.fft.rfft(signal).real  # Use rfft to automatically handle real input
        fourier_coeffs.append(fourier_transform)

    return np.array(signals), np.array(fourier_coeffs)


# Generate dataset
num_samples = 2000
num_points = 128
x_data, y_data = generate_signal(num_samples, num_points)

# Normalize input and output
x_mean, x_std = x_data.mean(), x_data.std()
y_mean, y_std = y_data.mean(), y_data.std()

x_data = (x_data - x_mean) / x_std
y_data = (y_data - y_mean) / y_std

# Train/test split
split_idx = int(0.8 * num_samples)
x_train, y_train = x_data[:split_idx], y_data[:split_idx]
x_test, y_test = x_data[split_idx:], y_data[split_idx:]

# Reshape for Conv1D: (samples, timesteps, channels)
x_train_cnn = x_train[..., np.newaxis]
x_test_cnn = x_test[..., np.newaxis]

# Build the Conv1D model
model = keras.Sequential([
    keras.layers.Conv1D(32, kernel_size=5, activation='relu', input_shape=(num_points, 1)),
    keras.layers.MaxPooling1D(pool_size=2),
    keras.layers.Conv1D(64, kernel_size=5, activation='relu'),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(y_train.shape[1])  # Output: number of FFT real coefficients
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(x_train_cnn, y_train, epochs=10, batch_size=32, verbose=1)

# Predict and de-normalize
y_pred = model.predict(x_test_cnn)
y_pred = y_pred * y_std + y_mean
y_test_denorm = y_test * y_std + y_mean

# Visualize a prediction
import random
sample_idx = random.randint(0, len(x_test) - 1)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_test[sample_idx])
plt.title("Time-Domain Signal")

plt.subplot(1, 2, 2)
plt.plot(y_test_denorm[sample_idx], label="True FFT", linestyle="dashed")
plt.plot(y_pred[sample_idx], label="Predicted FFT", linestyle="solid")
plt.title("Fourier Coefficients (Real Part)")
plt.legend()

plt.tight_layout()
plt.show()
