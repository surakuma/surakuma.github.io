import numpy as np
def lu_fact(A):
    nrows = len(A)
    ncols = len(A[0])
    for k in range(nrows):
        for i in range(k+1,nrows):
            A[i][k] = A[i][k]/A[k][k]
        for i in range(k+1,nrows):
            for j in range(k+1,ncols):
                A[i][j] = A[i][j] - A[i][k]*A[k][j]



mat = np.array([[2, 6, 5], [4, 15, 11], [6, 30, 23]])
print("Initial matrix is:")
print(mat)
lu_fact(mat)
print("LU factorization:")
print(mat)
