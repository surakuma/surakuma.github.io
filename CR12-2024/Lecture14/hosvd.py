from truncated_svd import *
from unfolding import *
from tensorproduct import *

import numpy as np

def hosvd(X, tol):

    ndims = len(X.shape)
    threshold_per_dim = tol/np.sqrt(ndims)


    r = np.zeros(ndims, dtype=int)
    F = []

    for i in range(ndims):
        X_i = unfolding(X, i)
        U, _, _ = truncated_svd(X_i, threshold_per_dim)
        F.append(U)
        r[i] = U.shape[1]


    G = X

    for i in range(ndims):
        G = tensorproduct(G, 0, F[i], 0)

    return (G, F)

