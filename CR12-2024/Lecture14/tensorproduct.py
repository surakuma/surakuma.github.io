from unfolding import *

def tensorproduct(X, k1, Y, k2):
    dimsize1 = list(X.shape)
    dimsize2 = list(Y.shape)

    del dimsize1[k1]
    del dimsize2[k2]

    finaldim = dimsize1 + dimsize2

    X_k1 = unfolding(X, k1)
    Y_k2 = unfolding(Y, k2)

    XY = np.transpose(X_k1) @ Y_k2

    return np.reshape(XY, tuple(finaldim), order='F')

