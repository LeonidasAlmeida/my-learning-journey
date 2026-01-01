#You want to describe the shape, size, and dimensions of the matrix
#load library
import numpy as np
#create matrix
matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12]])
#view number of rows and columns
print(matrix.shape)
#view number of elements (rows * columns)
print(matrix.size)
#View number of dimensions
print(matrix.ndim)
#view all shape
print("number of rows and columns:{}\nsize of matrix:{}\ndimension of matrix:{}".format(matrix.shape,matrix.size,matrix.ndim))