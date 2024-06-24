import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Import Pandas and Read the CSV File
df = pd.read_csv('sales_data.csv')

# Step 2: Inspect the Data
print(f"df.head():\n", df.head())
print("df.info():", df.info())
print("df.describe():\n", df.describe())

# Step 3: Data Cleaning and Preparation
print("df.isnull().sum():\n", df.isnull().sum())
df['Date'] = pd.to_datetime(df['Date'])
df['Average_Price'] = df['Revenue'] / df['Sales']
print("df.describe() 2nd after adding columns:\n", df.describe())

# Step 4: Data Analysis

# Total Sales and Revenue by Product
product_summary = df.groupby('Product')[['Sales', 'Revenue']].sum().reset_index()
print("Product summary:\n", product_summary)

# Daily Sales Trend
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
print("Daily sales:\n", daily_sales)

# Top Selling Products
top_products = product_summary.sort_values(by='Sales', ascending=False)
print("Top products by Sales:\n", top_products)

# Step 5: Visualization

# Plot Daily Sales Trend
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['Sales'], marker='x')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Bar Plot of Total Sales by Product
plt.figure(figsize=(10, 6))
plt.bar(top_products['Product'], top_products['Sales'], color='lightblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()
