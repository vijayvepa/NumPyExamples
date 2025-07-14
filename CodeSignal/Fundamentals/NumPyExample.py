import numpy as np 

array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)


array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array_3d)

print("1d Size: ", array_1d.size)
print("2d Size: ", array_2d.size)
print("3d Size: ", array_3d.size)

print("1d Shape: ", array_1d.shape)
print("2d Shape: ", array_2d.shape)
print("3d Shape: ", array_3d.shape)

print("1d Data Type", array_1d.dtype)
print("2d Data Type", array_2d.dtype)
print("3d Data Type", array_3d.dtype)