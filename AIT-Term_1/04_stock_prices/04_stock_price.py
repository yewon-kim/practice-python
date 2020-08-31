import pandas as pd

price_df = pd.read_csv(
    'C:/Users/user/Desktop/practice/practice-python/quant/04_Stock_Prices/prices.csv', 
    names=['ticker', 'date', 'open', 'high', 'low', 'close', 'volume', 'adj_close', 'adj_volume']
)

# DataFrame
print(price_df)

# groupby()
print(price_df.groupby('ticker')) # intermediate object 
print(price_df.groupby('ticker').median())
print(price_df.groupby('date')['volume'].sum()) # 일일 총 거래량
print(price_df.groupby('ticker')['close'].max()) # 종목별 최고 종가

# pivot()
open_prices = price_df.pivot(index='date', columns='ticker', values='open')
print(open_prices)