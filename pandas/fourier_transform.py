import numpy as np
import matplotlib.pyplot as plt

# Sample rate and duration
sample_rate = 1000  # samples per second
duration = 1       # seconds

# Generate time vector
t = np.linspace(0, duration, sample_rate * duration, endpoint=False)

# Generate a signal with two different frequencies
freq1 = 5   # frequency of the first signal in Hz
freq2 = 50  # frequency of the second signal in Hz
signal1 = np.sin(2 * np.pi * freq1 * t)
signal2 = np.sin(2 * np.pi * freq2 * t)
combined_signal = signal1 + signal2

# Add random noise to the combined signal
noise = np.random.normal(0, 0.5, combined_signal.shape)
noisy_signal = combined_signal + noise

# Compute the Fourier Transform
fft_result = np.fft.fft(noisy_signal)
fft_freq = np.fft.fftfreq(len(noisy_signal), 1/sample_rate)

# Only use the positive part of the frequency spectrum
positive_freqs = fft_freq[:len(fft_freq)//2]
positive_fft_result = fft_result[:len(fft_result)//2]

# Plot the original combined signal
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, combined_signal)
plt.title('Original Combined Signal (Without Noise)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the noisy signal
plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal)
plt.title('Noisy Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude of the Fourier Transform (Amplitude Spectrum)
plt.subplot(3, 1, 3)
plt.plot(positive_freqs, np.abs(positive_fft_result))
plt.title('Fourier Transform of Noisy Signal (Amplitude Spectrum)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.xlim(0, 100)  # Limit frequency range for better visualization

plt.tight_layout()
plt.show()
