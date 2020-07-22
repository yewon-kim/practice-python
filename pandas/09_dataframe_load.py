import pandas as pd

google_stock = pd.read_csv('C:/Users/user/Desktop/practice/practice-python/pandas/goog-1.csv')

print(type(google_stock))
print(google_stock.shape)

# GET: head(), tail()
print(google_stock.head(2)) # Default: (5)
print(google_stock.tail(2))
print(google_stock.isnull().any())

# describe()
print(google_stock.describe())
print(google_stock['Adj Close'].describe())

# Pandas Statistical Functions
print(google_stock.max())
print(google_stock.mean())
print(google_stock['Close'].min())

# Correlation: corr()
print(google_stock.corr())