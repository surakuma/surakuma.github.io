import numpy as np
def direct_unfolding(X, k):
    perm = list(range(0,len(X.shape)))
    del perm[k]
    perm.insert(0,k)
    return np.reshape(np.transpose(X, perm), (X.shape[k], -1), order='F')


import numpy as np

X = np.zeros((3,3,3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            X[i][j][k] = (i+1) + (j+1)**2 + (k+1)**3

print(direct_unfolding(X,0))
print(direct_unfolding(X,1))
print(direct_unfolding(X,2))
