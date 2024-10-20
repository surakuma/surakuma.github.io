import numpy as np
def unfolding(X, k):
    shape = X.shape
    ndims = len(shape)
    nrows = shape[k]
    ncols = X.size//nrows

    Xk = np.zeros((nrows, ncols))

    offset = np.asarray(shape)
    offset[k] = 1

    t=1
    for i in range(ndims):
        oldt = t
        t = t * offset[i]
        offset[i] = oldt
    
    for icol in range(ncols):
        current_id = icol
        index = np.zeros(ndims, dtype=int)
    
        for i in reversed(range(ndims)):
            if (i != k):
                index[i] = current_id // offset[i]
                current_id = current_id % offset[i]
    
        for i in range(nrows):
            index[k] = i
            Xk[i][icol] = X[tuple(index)]

    return Xk
    


X = np.zeros((3,3,3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            X[i][j][k] = (i+1) + (j+1)**2 + (k+1)**3


print(unfolding(X,0))
print(unfolding(X,1))
print(unfolding(X,2))

