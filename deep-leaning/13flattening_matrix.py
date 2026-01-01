#problem:  you need to transform a matrix into a one-dimensional array
#soluction:use Flatten
#load libray
import numpy as np
#create matrix 
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
#View normal output
print(matrix)
#view flatte matrix
flatte = matrix.flatten()
print(flatte)

#OBS:flatten method make a change matrix into array