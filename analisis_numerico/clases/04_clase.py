import numpy as np


matriz_L = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])
b = np.array([[1,0,0]])


def sustitucionDelante(L,b):
    n,m = L.shape
    z=np.zeros((n,1))
    z[0] = b[0]
    for i in range(1,n):
        mult = 0
        for j in range(0,i-1):
            mult += L[i][j] * z[i]
        z[i] = b[i]-mult
    return z