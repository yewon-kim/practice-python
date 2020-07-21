import time
import numpy as np

# x = np.random.random(1000000)

# start = time.time()
# sum(x) / len(x)
# print(time.time() - start)

# start = time.time()
# np.mean(x)
# print(time.time() - start)

x = np.array([1, 2, 3, 4, 5])
print(x)
print(type(x))
print(x.dtype)

x = np.array(['Hello', 'World'])
print(x)
print(type(x))
print(x.dtype)

# rank 2(2 dimentional) ndarray
Y = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(Y)
print(Y.shape)
print(Y.size)
print(type(Y))
print(Y.dtype)

# 스칼라/단위/대각 행렬
X = np.zeros((4,3))
X = np.ones((4,3))
E = np.eye(3)
X = np.diag([1, 2, 3, 4])

# arange / linspace : 등간격 1차원 배열
x = np.arange(5)
print(x) # [0 1 2 3 4]
x = np.arange(4, 10)
print(x) # [4 5 6 7 8 9]

x = np.arange(1, 10, 2)
print(x) # [1 3 5 7 9]
print(x.dtype) # int32

y = np.linspace(1, 9, 5)
print(y) # [1. 3. 5. 7. 9.]
print(y.dtype) # float64
print(x == y) # [ True  True  True  True  True]
y = np.linspace(1, 11, 5, endpoint=False)
print(y) # [1. 3. 5. 7. 9.]
print(x == y) # [ True  True  True  True  True]

# reshape
x = np.arange(1, 21)
X = np.reshape(x, (4, 5))
print(X)

# random
X = np.random.random((2, 3))
print(X) # 실수
X = np.random.randint(0, 10, (2, 3))
print(X) # 정수
X = np.random.normal(0, 0.1, size=(2, 2))
print(X) # 정규분포

# save
x = np.array([1, 2, 3, 4, 5])
np.save('my_array', x)
y = np.load('my_array.npy')
print(y)

# quiz
X = np.linspace(2, 32, 16).reshape(4, 4)
print(X)
X = np.arange(2, 33, 2).reshape(4, 4)
print(X)