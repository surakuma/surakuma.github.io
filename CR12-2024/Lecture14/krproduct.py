import numpy as np

def krproduct(A, B):
    n1 = A.shape[0]
    n2 = B.shape[0]

    r = A.shape[1]

    C = np.zeros((n1*n2, r))
    for i in range(r):
        a = A[:,i]
        b = B[:,i]
        C[:,i] = np.outer(b,a).flatten(order='F')

    return C



