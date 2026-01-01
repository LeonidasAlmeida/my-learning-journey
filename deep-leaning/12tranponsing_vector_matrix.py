#problem:you need to tranponse a vector or matrix
#soluction: use the T method
#load libray
import numpy as np

A = np.array([[1,2,3],
             [4,5,6]])
AT = A.T 
#View normal matrix
print(A)
#View transpose of matrix
print(AT) 
#the transpose change the order of matrix(row for columns)