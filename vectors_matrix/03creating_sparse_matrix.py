#the matrix sparse is a matrix with a lote value zero 
import numpy as np
from scipy import sparse
#create a matrix
matrix  = np.array([[0,0],[0,1],[3,0]])
#creating compressed sparse row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix)
print(matrix_sparse)
#create a large matrix
matrix_large = np.array([[0,0,0,0,0,0,0,0,0,0],
                         [0,1,0,0,0,0,0,0,0,0],
                         [3,0,0,0,0,0,0,0,0,0]])
#creating compressed sparse row 
matrix_sparse_large = sparse.csr_matrix(matrix_large)
#View  larger sparse matrix
print(matrix_sparse_large)