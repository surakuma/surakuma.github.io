import numpy as np

def outerproduct(a, b, c):

    #ab = np.tensordot(a, b, axes=0)
    #abc = np.tensordot(ab, c, axes=0)
 
    nc = len(c)
    C = np.zeros((len(a), len(b), nc))

    for i in range(nc):
        C[:,:,i] = np.outer(a,b) * c[i]


    #print(np.linalg.norm(C-abc))

    return C

