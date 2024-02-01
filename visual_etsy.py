import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datasets.csv")

# 전처리
# price 첫자리가 ,일시 제거
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

# 가격과 리뷰 column 값의 데이터를 float으로 변환
df['price'] = df['price'].astype(float)
df['review'] = df['review'].astype(float)


# 각 row의 가격과 리뷰에 대한 카테고리화
# 0-100, 100-200, 200-300, 300-400, 400-500, 500-600, 600-700, 700-800, 800-900, 900-1000
# 1000 이상
# 가격의 범주화
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

# 가격의 범주화를 데이터프레임에 추가
df['price_range'] = price_range


price_review = df.groupby('price_range')['review'].mean()
print(price_review)

# 가격 범주화별 리뷰의 평균을 막대 그래프로 표현
price_review.plot(kind='bar')
plt.title('Price Range vs Review')
plt.xlabel('Price Range')
plt.ylabel('Average Review')
plt.show()

