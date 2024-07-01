import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate x values
x = np.linspace(-40, 40, 1000)  # Adjusting the range to see more oscillations

# Step 2: Compute the cosine of each x value and sin(x)/x
y_cos = np.cos(x)
y_sinx_over_x = np.sin(x) / x

# Handle the singularity at x=0 for sin(x)/x by using np.where to replace with 1
y_sinx_over_x = np.where(x == 0, 1, y_sinx_over_x)

# Step 3: Plot the cosine wave
plt.plot(x, y_cos, label='cos(x)', linestyle='--')

# Plot sin(x)/x
plt.plot(x, y_sinx_over_x, label='sin(x)/x')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cosine Wave and sinc(x) Function')

# Add a legend
plt.legend()

# Add horizontal line at y=0
plt.axhline(0, color='black', linewidth=0.5)

# Display the plot
plt.show()
