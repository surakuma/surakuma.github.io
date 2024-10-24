from cp_als_3d import *

import numpy as np

T=np.zeros((4,4,4))
T[0, 0, 0] = 1
T[1, 2, 0] = 1
T[0, 1, 1] = 1
T[1, 3, 1] = 1
T[2, 0, 2] = 1
T[3, 2, 2] = 1
T[2, 1, 3] = 1
T[3, 3, 3] = 1

r=7
L, U0, U1, U2 = cp_als_3d(T, r)
