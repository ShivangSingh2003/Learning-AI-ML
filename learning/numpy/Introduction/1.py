import numpy as np

python_list = [1, 2, 3, 4, 5]
print(python_list)

numpy_array = np.array([1, 2, 3, 4, 5])
print(numpy_array)

ar_1d = np.array([1, 2, 3, 4, 5])
ar_2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(ar_1d)
print(ar_2d)

# arrays with default values

# initialized with 0

zeros_1d = np.zeros(5)
zeros_2d = np.zeros((3,3))

print(zeros_1d)
print(zeros_2d)

# initialized with 1

ones_1d = np.ones(5)
ones_2d = np.ones((3,3))

print(ones_1d)
print(ones_2d)

# initialized with specific value

filled_1d = np.full(5, 10)
filled_2d = np.full((3,4), 10)

print(filled_1d)
print(filled_2d)

# creating a sequence

seq = np.arange(0, 10, 2) # returns the sequence in a numpy array
print(seq)

# creating ientity matrix

identity_matrix = np.eye(3)
print(identity_matrix)