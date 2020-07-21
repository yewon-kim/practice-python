import pandas as pd

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

# Access elements
print(groceries['eggs'])
print(groceries[['milk', 'bread']])

print(groceries[0])
print(groceries[-1])
print(groceries[[0, 1]])

# Attribute
print(groceries.loc[['eggs', 'apples']])
print(groceries.iloc[[2, 3]])

# Update
groceries['eggs'] = 2
print(groceries)

# Delete
groceries.drop('apples')
print(groceries) # unchanged

groceries.drop('apples', inplace = True)
print(groceries) # changed