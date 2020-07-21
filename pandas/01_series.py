import pandas as pd

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
print(groceries)

print(groceries.shape) # shape of data
print(groceries.ndim) # number of dimensions
print(groceries.size) # total number of values

print(groceries.index)
print(groceries.values)

def isGroceries(item):
    return item in groceries

print(isGroceries('banana'))
print(isGroceries('bread'))