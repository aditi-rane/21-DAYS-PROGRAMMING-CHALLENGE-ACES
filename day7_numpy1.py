import numpy as np

arr=np.array([5,6,7,8,9])   #1D array
print(arr)
print(type(arr))

arr = np.array(23)
print(arr)

arr = np.array([[1,2,3], [4,5,6]])   #2D array
print(arr)

arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])   #3D array
print(arr)

#check no of dimension
a = np.array(23)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#higher dimensional array
arr = np.array([1, 2, 3, 4], ndmin=4)
print(arr)
print('number of dimensions :', arr.ndim)

#access 1D array elements
arr = np.array([1, 2, 3, 4])
print(arr[1])

#access 2D array elements
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 2])

#access 3D array elements
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#slicing 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

#slicing 2D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])

#copy()
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[1] = 45
print(arr)
print(x)

#view()
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[1] = 45
print(arr)
print(x)

#shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#reshape 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#reshape 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#reshape into any shape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 78
print(arr)
print(x)

#Check if Array Owns it's Data
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

#flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)