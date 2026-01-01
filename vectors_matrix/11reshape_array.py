#problem : you want to change the shaep(number of rows and columns) of an array without  changing the element value
#soluction: use NumPy's reshape
#load library
import numpy as np
#creating a matrix 4x3
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12]])
#view normal matrix
print(matrix)
#reshape matrix int 2x6 matrix
print(matrix.reshape(2,-1))
#view the size of matrix
print(np.size(matrix))
#the len of matrix need to be equivalent
print(matrix.reshape(1,-1))