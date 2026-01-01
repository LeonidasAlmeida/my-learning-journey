#problem : you need to know the rank of a matrix
#soluction : use NumPy linear algebra method matrix_rank 
#load library
import numpy as np
#create  matrix
matrix =  np.array([[1,1,1],
                    [1,1,10],
                    [1,1,15]])
#return matrix rank
print(np.linalg.matrix_rank(matrix))