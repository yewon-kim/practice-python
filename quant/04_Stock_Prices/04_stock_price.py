import pandas as pd

price_df = pd.read_csv(
    'C:/Users/user/Desktop/practice/practice-python/quant/04_Stock_Prices/prices.csv', 
    names=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume']
)

print(price_df)
print(price_df.groupby('ticker').median())

open_prices = price_df.pivot(index='date', columns='ticker', values='open')
print(open_prices.sort_values(by='date', ascending=False).T)