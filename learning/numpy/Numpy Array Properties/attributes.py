import numpy as np

# dimension of array

arr_2d = np.array([[1,2,3],
                   [4,5,6]])

print(arr_2d.shape)

# total number of elements in an array

print(arr_2d.size)

# number of dimensions of the array

arr_3d = np.array([[[1,2], [3,4], [4,5], [6,7]]])

print(arr_2d.ndim)
print(arr_3d.ndim)

# datatype of element

arr = np.array([34, 65, 89.7, 90, 95])

print(arr.dtype)


arr1 = np.array([34, 65, 89.7, "hello"])
print(arr1)
print(arr)
print(arr_2d)

# Type Conversion

arr = np.array([3.5, 6.7, 8.9, 12.6])

int_arr = arr.astype(int)

print(arr)
print(arr.dtype)

print(int_arr)
print(int_arr.dtype)