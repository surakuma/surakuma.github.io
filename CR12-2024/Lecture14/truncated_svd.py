import numpy as np
def truncated_svd(A, accr):
    nrows = A.shape[0]
    ncols = A.shape[1]

    U, S, VT = np.linalg.svd(A, full_matrices=False)

    accr2 = accr * accr
    trunc_error2 = 0.0

    r_trunc = 0

    for k in reversed(range(min(nrows, ncols))):
        trunc_error2 += S[k] * S[k]
        if trunc_error2 > accr2:
            r_trunc = k +1
            break

    U = U[:,0:r_trunc]
    S = S[0:r_trunc]
    VT = VT[0:r_trunc,:]
    return (U, S, VT)

