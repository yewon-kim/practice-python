import numpy as np
import pandas as pd

dates = pd.date_range('22/07/2020', periods=11, freq='D')
close_prices = np.arange(len(dates))

close = pd.Series(close_prices, dates)
print(close)

print(close.resample('3D').first())

df = pd.DataFrame(
    {
        'days': close,
        'weeks': close.resample('W').first()
    }
)
print(df)
print(close.resample('D').sum()) # 각 일의 값 총합
print(close.resample('W').sum()) # 각 주의 값 총합
print(close.resample('W').first()) # 각 주의 open 값
print(close.resample('W').last()) # 각 주의 close 값

print(close.resample('W').ohlc()) # 각 주의 OHLC 값