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

print("Fouth element:", array_1d[3])
print("Last element:", array_1d[-1])

print("2d first row col", array_2d[0, 0])
print("2d last row last col", array_2d[-1, -1])


array_filters = np.array([8,4,7,3,4,11])
even_index = array_filters % 2 == 0
print("Even items", array_filters[even_index])
print("Odd items", array_filters[array_filters % 2 != 0])
print(
    "Odd items greater than 2", array_filters[(array_filters % 2 != 0) & (array_filters > 2)]
)
print("Even numbers or numbers greater than 5", array_filters[(array_filters % 2 == 0) | (array_filters > 5)])

print("First three elements", array_filters[0:3])
print("Every second element", array_filters[1:6:2])
