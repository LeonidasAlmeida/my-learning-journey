#problem you need to pre-allocate arrays of a given size with same value
#Load libray
import numpy as np
#generate a vector of shape (1,5) containing all zeros
vector = np.zeros(shape = 5)
#view the vector
print(vector)
#generate a matrix of shape (3,3) containing all ones
matrix = np.full(shape=(3,3), fill_value=1)
print(matrix)