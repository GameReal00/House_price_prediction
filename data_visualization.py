import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
# Assuming the dataset is in CSV format in the repository
# df = pd.read_csv('path/to/nigeria_house_prices.csv')  # Update this path

# Data Cleaning
# Check for missing values
# print(df.isnull().sum())

# Visualization
# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Histogram of House Prices
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True)
plt.title('Distribution of House Prices in Nigeria')
plt.xlabel('House Price')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of House Sizes vs Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='size', y='price', data=df)
plt.title('House Size vs Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price')
plt.show()

# Box plot of Prices by Neighborhood
plt.figure(figsize=(12, 8))
sns.boxplot(x='neighborhood', y='price', data=df)
plt.title('House Prices by Neighborhood')
plt.xticks(rotation=45)
plt.xlabel('Neighborhood')
plt.ylabel('House Price')
plt.show()