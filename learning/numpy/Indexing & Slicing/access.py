import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[0])
print(arr[2])
print(arr[-1])

# Slicing arr[start:stop:step]

print(arr[2:])
print(arr[1:4])
print(arr[:5])
print(arr[::2])
print(arr[4:0:-1])
print(arr[4:-1])
print(arr[::-1])
print(arr[::-2])

# Fancy Indexing

print(arr[[1, 3, 5]])

# Filtering / Boolean Masking

print(arr[arr < 35])
