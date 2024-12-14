import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a URL or local path
data_url = "https://raw.githubusercontent.com/Vicky5697/Supermarket-Sales-Data-Analysis/main/Supermarket_Sales.csv"
df = pd.read_csv(data_url)

# Display basic information about the dataset
print("Dataset Info:\n")
df.info()
print("\nFirst 5 rows:\n", df.head())

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Add a month column for grouping by month
df['Month'] = df['Date'].dt.month

# Basic Descriptive Statistics
print("\nDescriptive Statistics:\n", df.describe())

# Total sales by product line
sales_by_product = df.groupby('Product line')['Total'].sum().sort_values(ascending=False)
print("\nTotal Sales by Product Line:\n", sales_by_product)

# Visualize total sales by product line
plt.figure(figsize=(10, 6))
sales_by_product.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product Line')
plt.ylabel('Total Sales')
plt.xlabel('Product Line')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales distribution by payment method
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Payment', palette='viridis')
plt.title('Sales Distribution by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Average rating by product line
avg_rating_by_product = df.groupby('Product line')['Rating'].mean().sort_values(ascending=False)
print("\nAverage Rating by Product Line:\n", avg_rating_by_product)

# Visualize average rating by product line
plt.figure(figsize=(10, 6))
avg_rating_by_product.plot(kind='bar', color='coral')
plt.title('Average Rating by Product Line')
plt.ylabel('Average Rating')
plt.xlabel('Product Line')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gross income by branch
income_by_branch = df.groupby('Branch')['gross income'].sum().sort_values(ascending=False)
print("\nGross Income by Branch:\n", income_by_branch)

# Visualize gross income by branch
plt.figure(figsize=(8, 6))
sns.barplot(x=income_by_branch.index, y=income_by_branch.values, palette='coolwarm')
plt.title('Gross Income by Branch')
plt.xlabel('Branch')
plt.ylabel('Gross Income')
plt.tight_layout()
plt.show()

# Monthly sales trend
monthly_sales = df.groupby('Month')['Total'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', color='purple')
plt.title('Monthly Sales Trend')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.grid()
plt.tight_layout()
plt.show()


print("Analysis complete. Visualizations displayed.")
