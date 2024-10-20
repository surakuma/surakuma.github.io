import numpy as np

def normalize(A):
    nrows = A.shape[0]
    ncols = A.shape[1]

    #L = np.linalg.norm(A, axis=0)
    #C = A/L
    # return (C, L)

    C = np.zeros((nrows, ncols))
    L = np.zeros((ncols, 1))

    for i in range(ncols):
        L[i] = np.linalg.norm(A[:,i])
        C[:,i] = A[:,i]/L[i]

    return (C, L)

