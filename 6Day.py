import numpy as np
arr = np.array([
    [5, 4, 3, 1],
    [7, 3, 9, 3],
    [6, 4, 2, 4]



])
# print(arr[:2]) #rows
print(arr, arr.shape)

s_arr = arr[:2, 1:3]
print(s_arr, s_arr.shape)

# extract last rows and col 0, col 1
print(arr[-1, :2])
# Extract second row
print(arr[-2, :])
# Extract third column
print(arr[:, 2:3])
# Extract col 1 and col 2
print(arr[:, 1:3])