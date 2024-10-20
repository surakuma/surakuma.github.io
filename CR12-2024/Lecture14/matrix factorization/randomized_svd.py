import numpy as np
def randomized_svd(A, r):
    
    nrows = A.shape[0]
    ncols = A.shape[1]

    p = 5
    l = r+p
    l = min(l, nrows, ncols)

    RS = np.random.randn(ncols, l)

    Y = A @ RS

    Q, _ = np.linalg.qr(Y, mode='reduced')

    B = np.transpose(Q) @ A

    U, S, VT = np.linalg.svd(B, full_matrices=False)

    U = Q @ U

    r = min(r,l)
    U = U[:,0:r]
    S = S[0:r]
    VT = VT[0:r,:]
    return (U, S, VT)
    
