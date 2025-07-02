import numpy as np


# Mathematical Operations

arr = np.array([10, 20, 30, 40, 50])

arr += 5

print(arr + 5)
print(arr - 3)
print(arr * 10)
print(arr ** 2)

# Aggregation Functions

sum = np.sum(arr)
min = np.min(arr)
max = np.max(arr)
mean = np.mean(arr)
variance = np.var(arr)
std_dev = np.std(arr)

print(sum)
print(min)
print(max)
print(mean)
print(variance)
print(std_dev)
