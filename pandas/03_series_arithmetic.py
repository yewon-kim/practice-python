import pandas as pd

fruits = pd.Series([10, 6, 3], ['apples', 'oranges', 'bananas'])
print(fruits)
print(fruits + 2)
print(fruits - 2)
print(fruits * 2)
print(fruits / 2)

import numpy as np
print(np.sqrt(fruits))
print(np.exp(fruits))
print(np.power(fruits, 2))

fruits['bananas'] += 3
print(fruits)

fruits[2] -= 2
print(fruits)
fruits.iloc[2] -= 2
print(fruits)

fruits[['apples', 'oranges']] *= 2
print(fruits)
fruits.loc[['apples', 'oranges']] /= 2
print(fruits)

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])
print(groceries * 2) # works with Str!!
# print(groceries / 2) # does not work