import numpy as np

# Boolean Indexing
X = np.arange(25).reshape(5, 5)
print(X)
print(X[X > 10])
print(X[(X > 10) & (X < 17)])

X[(X > 10) & (X < 17)] = -1
print(X)

# Set Operations
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 7, 8])
print(np.intersect1d(x, y))
print(np.setdiff1d(x, y))
print(np.setdiff1d(y, x))
print(np.union1d(x, y))

# Sorting
x = np.random.randint(1, 11, size = (10, ))
print(x)

y = np.sort(x)
print(y)
print(x) # x unchanged

x.sort()
print(x) # x changed

print(np.sort(np.unique(x)))

X = np.random.randint(1, 11, size = (5, 5))
print(X)
print(np.sort(X, axis = 0)) # sort each row
print(np.sort(X, axis = 1)) # sort each column

# Quiz: Pick Odd
X = np.arange(1, 26).reshape(5, 5)
Y = X[X % 2 == 1]
print(Y)