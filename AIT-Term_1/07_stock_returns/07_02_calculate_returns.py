import pandas as pd

close = pd.DataFrame(
    {
        'ABC': [1, 5, 3, 6, 2],
        'EFG': [12, 51, 43, 56, 22],
        'XYZ': [35, 36, 36, 36, 37],
    },
    pd.date_range('10/01/2018', periods=5, freq='D')
)

print(close)
print(close.shift(1))
print((close - close.shift(1))/close.shift(1))