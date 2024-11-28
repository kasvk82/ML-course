import numpy as np

myList = [1, 2, 3]
print(type(myList))

print(np.array(myList))

myArray = np.array(myList)
print(myArray)
print(type(myArray))

myMatrix = [[1,2,3],[4,5,6],[7,8,9]]
print(myMatrix)

print(np.array(myMatrix))

print(np.arange(0, 101, 20))

print(np.zeros(5))

print(np.zeros((2,5)))

print(np.ones((5)))

print(np.linspace(0,10,11))

print(np.linspace(0,5,21))

print(len(np.linspace(0,5,21)))

print(np.eye(5))

print(np.random.rand(5,2))

print(np.random.randn(2,3))

print(np.random.randint(0,101,(4,5)))

np.random.seed(101)
print(np.random.rand(5))


arr = np.arange(0,25)
print(arr)
print(arr.reshape(5,5))


ranarr = np.random.randint(0,101,10)
print(ranarr)

print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())

print(ranarr.dtype)




