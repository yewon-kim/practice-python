import pandas as pd

items = [
    {
        'bikes': 20, 
        'pants': 30, 
        'watches': 35
    }, 
    {
        'watches': 10, 
        'glasses': 50, 
        'bikes': 15, 
        'pants': 5
    }
]

# Add index
store_items = pd.DataFrame(items, index=['store 1', 'store 2'])
print(store_items)


# GET
# Get column elements
print(store_items[['bikes']])
print(store_items[['bikes', 'pants']])

# Get index(row) elements
print(store_items.loc[['store 1']])

# Get the exact element
print(store_items['bikes']['store 2']) # df_name['column']['index(row)']



# ADD
# New column
store_items['shirts'] = [15, 2]
print(store_items)
store_items['suits'] = store_items['shirts'] + store_items['pants']
print(store_items)

# New row
new_items = [
    {
        'bikes': 20, 
        'pants': 30, 
        'watches': 35, 
        'glasses': 4
    }
]
new_store = pd.DataFrame(new_items, index=['store 3'])
store_items = store_items.append(new_store)
print(store_items)

# New column: split
store_items['new_watches'] = store_items['watches'][1:]
print(store_items)

store_items.insert(6, 'shoes', [8, 5, 0])
print(store_items)



# DELETE (pop/drop)
# pop: delete a column
store_items.pop('new_watches')
print(store_items)

# drop: delete rows or columns
store_items = store_items.drop(['watches', 'shoes'], axis = 1)
print(store_items)

store_items = store_items.drop(['store 1', 'store 2'], axis = 0)
print(store_items)



# RENAME
store_items = store_items.rename(columns={'bikes': 'hats'})
print(store_items)
store_items = store_items.rename(index={'store 3': 'last store'})
print(store_items)

# SET index
store_items = store_items.set_index('pants')
print(store_items)