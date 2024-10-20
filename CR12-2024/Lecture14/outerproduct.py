import numpy as np

def outerproduct(a, b, c):

    nc = len(c)

    C = np.zeros((len(a), len(b), nc))

    for i in range(nc):
        C[:,:,i] = np.outer(a,b) * c[i]

    return C

