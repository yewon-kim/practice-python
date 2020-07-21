import numpy as np

# Slicing
X = np.arange(1, 21).reshape(4, 5)
print(X)
z = X[1:4, 2:5]
print(z)
z = X[1:, 2:]
print(z)
z = X[:3, 2:]
print(z)
z = X[:, 2]
print(z)
z = X[:, 2:3]
print(z)

# Update
X = np.arange(1, 21).reshape(4, 5)
print(X)
z = X[1:, 2:]
z[2, 2] = 99
print(z)
print(X)

# Copy
X = np.arange(1, 21).reshape(4, 5)
print(X)
z = X[1:, 2:].copy()
z[2, 2] = 99
print(z)
print(X)

# indices
indices = np.array([1, 3])
y = X[indices, :]
print(y)
y = X[:, indices]
print(y)

# diag
z = np.diag(X)
print(z)
z = np.diag(X, k = 1)
print(z)
z = np.diag(X, k = -1)
print(z)

# unique
X = np.array([[1, 2, 3], [5, 2, 8], [1, 2, 3]])
print(np.unique(X))