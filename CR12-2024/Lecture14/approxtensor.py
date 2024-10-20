from outerproduct import *

def approxtensor(L, U1, U2, U3):
    ncols = len(L)

    n1 = U1.shape[0]
    n2 = U2.shape[0]
    n3 = U3.shape[0]

    T = np.zeros((n1, n2, n3))

    for k in range(ncols):
        T += L[k] * outerproduct(U1[:,k], U2[:, k], U3[:, k])

    return T
