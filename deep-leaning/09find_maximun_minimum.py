#problem: you need to find the maximum or minimum value in array   
#Use	NumPy’s	max	and	min	methods
import numpy as np
#create matrix
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
# return maximum element
print(np.max(matrix))
print(np.min(matrix))
#find maximum element in each column
print(np.max(matrix, axis = 0))
#find maximum element in each row 
print(np.max(matrix, axis = 1))