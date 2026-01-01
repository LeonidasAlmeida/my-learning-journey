#problem: you want to calculate some descriptive statistcs about an array
#Solution : use NumPy mean,var and std

#load library
import numpy as np
#create matrix
matrix=np.matrix([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
#return mean(média)
print(np.mean(matrix))
#return variance
print(np.var(matrix))
#return standard deviation(desvio padrão)
print(np.std(matrix))

#find the mean value in each colum
print(np.mean(matrix, axis=0))
#find the mean value in each row
print(*np.mean(matrix, axis=1))