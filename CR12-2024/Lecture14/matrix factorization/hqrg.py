import numpy as np

def householder_qr(A):
    nrows = len(A)
    ncols = len(A[0])
    newA = A

    Q = np.identity(nrows)

    for i in range(ncols):
        xi = newA[i:,i];
        yi = np.zeros(len(xi))
        yi[0] = np.linalg.norm(xi)
        if xi[0] > 0:
            yi[0] = - yi[0]
        vi = xi-yi
        ui = vi/np.linalg.norm(vi)
        

        ri = np.identity(len(ui)) - 2 * np.outer(ui, ui)
        print(ri)
        extri = np.zeros((nrows, nrows))
        for j in range(i):
            extri[j,j] = 1

        extri[i:,i:] = ri

        newA = extri @ newA
        Q = Q @ extri


    print("Q matrix:")
    print(Q)
    print("R matrix:")
    print(newA)


mat = np.array([[1, 5], [2, 6], [3, 7], [4,8]])
householder_qr(mat)            


