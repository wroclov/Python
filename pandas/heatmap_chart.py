import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import matplotlib.colors as mcolors
import string
import seaborn as sns

# Set seaborn style and matplotlib parameters
sns.set()
plt.rcParams['font.family'] = ['Times New Roman', 'sans-serif']
plt.rcParams['figure.dpi'] = 144

# Data array
values = np.array([
    [ 1. ,  0.5,  0.8,  0.2,  0.3, -0.7, -0.5, -0.5, -0.2, -0.1,  0.3],
    [ 0.5,  1. ,  0.7,  0.8,  0.8, -0.2, -0.5, -0.9, -0.8, -0.8, -0.6],
    [ 0.8,  0.6,  1. ,  0.8,  0.7, -0.2, -0.7, -0.9, -0.3, -0.2, -0.1],
    [ 0.5,  0.8,  0.8,  1. ,  0.8, -0.6, -0.9, -0.7, -0.5, -0.4, -0.3],
    [ 0.3,  0.8,  0.6,  0.8,  1. , -0.4, -0.8, -0.9, -0.8, -0.6, -0.5],
    [-0.9, -0.2, -0.6, -0.3, -0.4,  1. ,  0.8,  0.5,  0.1, -0.3, -0.2],
    [-0.5, -0.5, -0.7, -0.9, -0.8,  0.8,  1. ,  0.7,  0.5,  0.2,  0.8],
    [-0.5, -0.9, -0.9, -0.9, -0.9,  0.5,  0.7,  1. ,  0.8,  0.7,  0.6],
    [-0.3, -0.8, -0.3, -0.8, -0.8,  0.1,  0.5,  0.5,  1. ,  0.7,  0.7],
    [-0.1, -0.8, -0.2, -0.4, -0.6, -0.3,  0.2,  0.7,  0.7,  1. ,  0.8],
    [ 0.3, -0.6, -0.1, -0.3, -0.5, -0.2,  0.2,  0.6,  0.7,  0.8,  1. ]
])

# Make the data symmetric and set diagonal to 1
values = (values + values.T - np.diag(np.diag(values))) / 2
np.fill_diagonal(values, 1)

# Create a DataFrame for the correlation matrix
corr_matrix = pd.DataFrame(values, columns=list(string.ascii_uppercase[:values.shape[1]]))
print(corr_matrix)

# Heatmap of the correlation matrix
sns.heatmap(corr_matrix, cmap='coolwarm_r')
plt.show()

# Create a white grid with the same dimensions as the correlation matrix
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('white')
ax.imshow(np.ones_like(corr_matrix), cmap='gray_r', interpolation='nearest')

# Set the tick labels and rotation for the x and y axes
ax.set_xticks(np.arange(len(corr_matrix.columns)))
ax.set_yticks(np.arange(len(corr_matrix.columns)))
ax.tick_params(axis='x', which='both', labelbottom=False, labeltop=True, bottom=False, top=True, length=0)
ax.set_yticklabels(corr_matrix.columns, fontsize=20, color="orange", fontweight="bold")
ax.set_xticklabels(corr_matrix.columns, fontsize=20, color="orange", fontweight="bold")

# Create grid lines between the tick labels
ax.set_xticks(np.arange(len(corr_matrix.columns) + 1) - .5, minor=True)
ax.set_yticks(np.arange(len(corr_matrix.columns) + 1) - .5, minor=True)
ax.grid(which="minor", color="lightgray", linestyle="solid", linewidth=2)

# Add rectangle around the grid
rect = Rectangle((-.5, -.5), len(corr_matrix.columns), len(corr_matrix.columns), linewidth=5, edgecolor='lightgray', facecolor='none')
ax.add_patch(rect)

# Create circles with radius proportional to the absolute value of correlation
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        correlation = corr_matrix.iat[i, j]
        norm = plt.Normalize(-1, 1)
        sm = plt.cm.ScalarMappable(norm=norm, cmap='coolwarm_r')
        color = sm.to_rgba(correlation)
        circle = Circle((i, j), radius=abs(correlation) / 2.5, facecolor=color)
        ax.add_patch(circle)

# Add color bar
norm = mcolors.Normalize(vmin=-1, vmax=1)
c_scale = plt.cm.ScalarMappable(norm=norm, cmap='coolwarm_r')
cbar = plt.colorbar(c_scale, ax=ax)
plt.show()
