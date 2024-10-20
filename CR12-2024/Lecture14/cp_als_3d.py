from unfolding import *
from krproduct import *
from approxtensor import *
from normalize import *

import numpy as np

def cp_als_3d(T, r):

    tensorshape = T.shape
    U0 = np.random.randn(tensorshape[0], r)
    U1 = np.random.randn(tensorshape[1], r)
    U2 = np.random.randn(tensorshape[2], r)


    approx_error = 1.0
    niterations = 0

    L = np.zeros((r, 1))

    while approx_error > 0.001:
        tmp1 = U1.T @ U1
        tmp2 = U2.T @ U2
        tmp = np.multiply(tmp1, tmp2)
        U0 = unfolding(T, 0) @ krproduct(U2,U1)
        U0 = U0 @ np.linalg.pinv(tmp)
        U0, L = normalize(U0)

        tmp0 = U0.T @ U0
        tmp2 = U2.T @ U2
        tmp = np.multiply(tmp0, tmp2)
        U1 = unfolding(T, 1) @ krproduct(U2, U0)
        U1 = U1 @ np.linalg.pinv(tmp)
        U1, L = normalize(U1)

        tmp0 = U0.T @ U0
        tmp1 = U1.T @ U1
        tmp = np.multiply(tmp0, tmp1)
        U2 = unfolding(T, 2) @ krproduct(U1, U0)
        U2 = U2 @ np.linalg.pinv(tmp)
        U2, L = normalize(U2)

        approxT = approxtensor(L, U0, U1, U2)
        approx_error = np.linalg.norm(T-approxT)
        
        print(approx_error)
        niterations += 1

    return (L, U0, U1, U2)
        

