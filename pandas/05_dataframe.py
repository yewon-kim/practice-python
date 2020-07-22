import pandas as pd

# dict to DataFramme
items = {
    'Bob': pd.Series([245, 25, 55], index=['bike', 'pants', 'watch']),
    'Alice': pd.Series([40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])
}
shopping_carts = pd.DataFrame(items)
print(shopping_carts)

# no index
data = {
    'Bob': pd.Series([245, 25, 55]),
    'Alice': pd.Series([40, 110, 500, 45])
}
df = pd.DataFrame(data)
print(df) # index = [0, 1, 2, 3...]

# attributes
print(shopping_carts.shape) # shape of data: (5, 2)
print(shopping_carts.ndim) # number of dimensions: 2
print(shopping_carts.size) # total number of values: 10

# indexing
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])
print(bob_shopping_cart)

sel_shopping_cart = pd.DataFrame(items, index=['pants', 'book'])
print(sel_shopping_cart)

alice_sel_shopping_cart = pd.DataFrame(items, index=['glasses', 'bike'], columns=['Alice'])
print(alice_sel_shopping_cart)

# Add index
data = {
    'Intergers': [1, 2, 3],
    'Floats': [4.5, 8.2, 9.6]
}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=['label 1', 'label 2', 'label 3'])
print(df)