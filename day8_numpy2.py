import numpy as np

#join
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1,arr2))
print(arr)
#--------------------------------------------
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1,arr2),axis=1)
print(arr)

#joining arrays using stack functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2),axis=1)
print(arr)

#stacking along rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1,arr2))
print(arr)

#stacking along columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1,arr2))
print(arr)

#stacking along height
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1,arr2))
print(arr)

#splitting numpy arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr,3)
print(newarr)

#splitting 2-D arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr,3)
print(newarr)
#-----------------------------------------------------------------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr,3)
print(newarr)
#-----------------------------------------------------------------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr,3,axis=1)
print(newarr)
#-----------------------------------------------------------------------------------------
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr,3)
print(newarr)

#search
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
#-------------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
#--------------------------------------------------------
x = np.where(arr%2 == 1)
print(x)

#search sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr,7)
print(x)
#---------------------------------------------------------
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr,7,side='right')
print(x)
#--------------------------------------------------------
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

#Sorting array
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
#-------------------------------------------------------
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
#-------------------------------------------------------
arr = np.array([True, False, True])
print(np.sort(arr))

#sorting 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

#filtering array
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

#creating filter array
arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#Creating Filter Directly From Array
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
#---------------------------------------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
