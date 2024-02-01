import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datasets.csv")

# Number of rows and columns
print(df.shape)

# Check for missing values
print(df.isnull().sum())

# Remove rows where price is 0
df = df[df['price'] != '0']

# Data preprocessing
# Remove leading commas from the price column
df['price'] = df['price'].str.replace(',', '')

# Basic statistical measures
mean_value = df['review'].mean()
median_value = df['review'].median()
std_dev = df['review'].std()
most = df['review'].max()
least = df['review'].min()

print("Mean: ", mean_value)
print("Median: ", median_value)
print("Standard Deviation: ", std_dev)
print("Most: ", most)
print("Least: ", least)
print(df.head())

# Convert price and review columns to float data type
df['price'] = df['price'].astype(float)
df['review'] = df['review'].astype(float)

# Categorize each row's price and review
# 0-100, 100-200, 200-300, 300-400, 400-500, 500-600, 600-700, 700-800, 800-900, 900-1000
# Over 1000
# Categorization of price
price_range = []
for price in df['price']:
    price = float(price)
    if price < 100:
        price_range.append("~100")
    elif price < 200:
        price_range.append("~200")
    elif price < 300:
        price_range.append("~300")
    elif price < 400:
        price_range.append("~400")
    elif price < 500:
        price_range.append("~500")
    elif price < 600:
        price_range.append("~600")
    elif price < 700:
        price_range.append("~700")
    elif price < 800:
        price_range.append("~800")
    elif price < 900:
        price_range.append("~900")
    elif price < 1000:
        price_range.append("~1000")
    else:
        price_range.append("over 1000")

# Add price categorization to the dataframe
df['price_range'] = price_range

# Calculate the average review for each price range category
price_review = df.groupby('price_range')['review'].mean()
print(price_review)

# Visualize the average review by price range using a bar chart
price_review.plot(kind='bar')
plt.title('Price Range vs Review')
plt.xlabel('Price Range')
plt.ylabel('Average Review')
plt.show()
