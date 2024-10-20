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
        ri
        extri = np.zeros((nrows, nrows))
        for j in range(i):
            extri[j,j] = 1

        extri[i:,i:] = ri

        newA = extri @ newA
        Q = Q @ extri


    print("Q matrix:")
    print(Q)
    print("R matrix:")
    print(A)


mat = np.array([[1, 5], [2, 6], [3, 7], [4,8]])
householder_qr(mat)            

x = np.array([[1, 5], [2, 6], [3, 7], [4,8]])
x0 = x[:,0]
y0 = np.array([-np.linalg.norm(x0), 0, 0, 0])
v0 = x0 - y0
u0 = v0/np.linalg.norm(v0)
r0 = np.identity(4) - 2* np.outer(u0, u0)
modA = r0 @x
tmpx1 = modA[1:,1]
y1 = np.array([-np.linalg.norm(tmpx1), 0, 0])
v1 = tmpx1 - y1
u1 = v1/np.linalg.norm(v1)
r1 = np.identity(3) - 2* np.outer(u1, u1)
extr1 = np.zeros((4, 4))
extr1[0,0] =1
extr1[1:,1:] = r1
householder_q = r0 @ extr1


[Q, r] = np.linalg.qr(x, mode='complete')
[U, S, VT] = np.linalg.svd(A, full_matrices=False)
origA = U @ np.diag(S) @ VT

