# load libray
import numpy as np
#create row vector
vector = np.array([1,2,3,4,5,6])
#create matrix
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
#select third element of vector
print(vector[5])
print(matrix[1,2])

#select all elements of a vector
print(vector[:])
#select everything up to and including the third element
print(vector[:3])
#select everything up to and including 
print(vector[3:])
#select the last element
print(vector[-1])
#reverse the vector
print(vector[::-1])
#select the first two row and all columns of a matrix
print(matrix[:2,:])
#select all rows and the second column
print(matrix[:,1:2])