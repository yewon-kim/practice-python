import pandas as pd

items = [
    {
        'bikes': 20, 
        'pants': 30, 
        'watches': 35, 
        'shirts': 15, 
        'shoes': 8, 
        'suits': 45
    }, 
    {
        'watches': 10, 
        'glasses': 50, 
        'bikes': 15, 
        'pants': 5, 
        'shirts': 2, 
        'shoes': 5, 
        'suits': 7
    }, 
    {
        'bikes': 20, 
        'pants': 30, 
        'watches': 35, 
        'glasses': 4, 
        'shoes': 10
    }
]

store_items = pd.DataFrame(items, index=['store 1', 'store 2', 'store 3'])
print(store_items)



# Count NaN: isnull()
x = store_items.isnull()
print(x)
x = store_items.isnull().sum() # sum each column
print(x)
x = store_items.isnull().sum().sum()
print(x)



# Delete NaN: dropna() / out of place
print(store_items.dropna(axis=0)) # drop rows
print(store_items.dropna(axis=1)) # drop columns



# Fill NaN / out of place
## fillna()
### 0
print(store_items.fillna(0))

### ffill: forward fill
print(store_items.fillna(method='ffill', axis=0)) # copy the previous row's value
print(store_items.fillna(method='ffill', axis=1)) # copy the previous columns's value

### backfill: backward fill
print(store_items.fillna(method='backfill', axis=0)) # copy the next row's value
print(store_items.fillna(method='backfill', axis=1)) # copy the next columns's value

## interpolate()
### linear
print(store_items)
print(store_items.interpolate(method='linear', axis=0))
print(store_items.interpolate(method='linear', axis=1))