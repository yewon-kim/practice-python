import numpy as np

# Arithmetic Operations
x = np.arange(1, 5)
y = np.arange(5, 9)
print(x)
print(y)
print(x + y)
print(np.add(x, y))
print(x - y)
print(np.subtract(x, y))
print(x * y)
print(np.multiply(x, y))
print(x / y)
print(np.divide(x, y))

X = np.arange(1, 5).reshape(2, 2)
Y = np.arange(5, 9).reshape(2, 2)
print(X + Y)
print(np.add(X, Y))

print(x)
print(np.sqrt(x)) # root
print(np.exp(x)) # exponential
print(np.power(x, 2)) # square

# Statistics
print(X)
print(X.mean())
print(X.mean(axis = 0))
print(X.mean(axis = 1))

print(X.sum())
print(X.sum(axis = 0))
print(X.sum(axis = 1))

print(X.std()) # Standard Deviation
print(np.median(X))
print(X.max())
print(X.min())

# Broadcast: operate with all the elements
print(X)
print(X + 3)
print(X - 3)
print(X * 3)
print(X / 3)

Y = np.arange(9).reshape(3, 3)
print(Y)
x = np.arange(3)
print(x)
print(Y + x)
z = np.arange(3).reshape(3, 1)
print(z)
print(Y + z)

# Quiz: create ndarray
X = np.ones((4, 4)) + np.arange(4)
print(X)
X = np.ones((4, 4)) * np.arange(1, 5)
print(X)