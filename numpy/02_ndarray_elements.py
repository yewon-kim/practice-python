import numpy as np

# Access / Update
x = np.arange(1, 6)
print(x)
x[4] = 6
print(x)

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X[0, 1])
print(X[1, 2])
print(X[2, 0])
X[2, 0] = 0
print(X[2, 0])

# Delete
x = np.arange(1, 6)
print(x) # [1 2 3 4 5]
x = np.delete(x, [0, 4])
print(x) # [2 3 4]

Y = np.arange(1, 10).reshape(3, 3)
print(Y)
W = np.delete(Y, 0, axis = 0)
print(W)
V = np.delete(Y, [0, 2], axis = 1)
print(V)

# Append
x = np.arange(1, 6)
x = np.append(x, 6)
print(x)
x = np.append(x, [7, 8, 9]).reshape(3, 3)
print(x)
x = np.append(x, [[10, 11, 12]], axis = 0)
print(x)
x = np.append(x, [[-1], [-2], [-3], [-4]], axis = 1)
print(x)

# Insert
x = np.array([1, 2, 5, 6])
x = np.insert(x, 2, [3, 4])
x = np.insert(x, 6, [7, 8])
print(x)

Y = np.array([[1, 2, 3], [7, 8, 9]])
W = np.insert(Y, 1, [4, 5, 6], axis = 0)
print(W)
V = np.insert(Y, 1, 5, axis = 1)
print(V)

# vstack / hstack
x = np.array([1, 2])
Y = np.arange(4, 8).reshape(2, 2)
Z = np.vstack((x, Y))
print(Z)
W = np.hstack((x.reshape(2, 1), Y))
print(W)