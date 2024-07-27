import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the top 20 countries
data = {
    'Country': ['USA', 'China', 'Russia', 'Germany', 'UK', 'Japan', 'France', 'Italy', 'Australia', 'Canada',
                'South Korea', 'Netherlands', 'Brazil', 'Spain', 'Ukraine', 'Hungary', 'Poland', 'New Zealand',
                'Cuba', 'Sweden'],
    'Gold': [39, 38, 20, 10, 22, 27, 10, 8, 17, 7,
             12, 10, 7, 4, 2, 5, 3, 6, 4, 2],
    'Silver': [41, 32, 28, 18, 21, 14, 12, 10, 23, 15,
               10, 12, 6, 10, 7, 6, 6, 3, 6, 4],
    'Bronze': [33, 18, 23, 16, 22, 17, 11, 20, 22, 12,
               8, 14, 6, 4, 8, 6, 7, 4, 6, 5]
}

df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(15, 8))

# Set the positions and width for the bars
positions = range(len(df['Country']))
bar_width = 0.25

# Create bars for Gold, Silver, and Bronze medals
bars_gold = plt.bar(positions, df['Gold'], color='gold', width=bar_width, label='Gold')
bars_silver = plt.bar([p + bar_width for p in positions], df['Silver'], color='silver', width=bar_width, label='Silver')
bars_bronze = plt.bar([p + bar_width*2 for p in positions], df['Bronze'], color='#cd7f32', width=bar_width, label='Bronze')

# Add the country names to the x-axis
ax.set_xticks([p + bar_width for p in positions])
ax.set_xticklabels(df['Country'], rotation=90)

# Set labels and title
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('Olympic Medals Distribution by Top 20 Countries')
plt.legend()

# Add a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
