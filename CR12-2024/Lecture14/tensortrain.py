from truncated_svd import *
from unfolding import *

import numpy as np

def tensortrain(X, tol):
    ndims = len(X.shape)

    threshold_per_dim = tol/np.sqrt(ndims-1)
    r = 1
    C = X
    G = []

    for i in range(ndims-1):
        C = np.reshape(C, (r*X.shape[i], -1), order='F')
        U, S, VT = truncated_svd(C, threshold_per_dim)

        r2 = U.shape[1]
        G_i = np.reshape(U, (r, X.shape[i], r2), order='F')
        G.append(G_i)
        C = np.diag(S) @ VT
        r = r2

    G_d = np.reshape(C, (r, X.shape[ndims-1], 1), order='F')
    G.append(G_d)

    return G




