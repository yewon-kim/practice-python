import numpy as np
import pandas as pd

codes = ['A000010', 'A000020']
prices = [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
               [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]]
df = pd.DataFrame(prices, index=codes).T
df_buy = pd.DataFrame([50, 800], index=codes).T


for i in range(len(df)):
    for code in codes:
        price = df[code][i]
        buy_at = df_buy[code][0]
        if (price >= buy_at):
            print('%s %7s %7s [매수]' % (code, price, buy_at))
        else:
            print('%s %7s %7s' % (code, price, buy_at))
