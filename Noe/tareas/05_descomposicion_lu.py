import numpy as np

# Descomposición LU
def descomposicion_lu(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for k in range(n):
        L[k][k] = 1
        for j in range(k, n):
            suma1 = sum(L[k][s] * U[s][j] for s in range(k))
            U[k][j] = A[k][j] - suma1
        for i in range(k + 1, n):
            suma2 = sum(L[i][s] * U[s][k] for s in range(k))
            L[i][k] = (A[i][k] - suma2) / U[k][k]
    return L, U


# Sustitución hacia adelante Lz = b

def solve_Lz(L, b):
    n,m = L.shape
    z= np.zeros((n,1))
    z[0] = b[0][0]
    for i in range(1,n):
        mult = L[i][0] * z[0] 
        for j in range(1,i):
            mult += L[i][j]*z[j]
        z[i] = b[0][i] - mult
    return z

# Sustitución hacia atras
def solve_Ux(z,U):
    n,m = U.shape
    x= np.zeros((n,1))
    x[n-1] = z[n-1]/U[n-1][n-1]
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += U[i][j]*x[j]
        x[i] = (z[i] - sum)/U[i][i]
    return x





# matriz A
A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])

L, U = descomposicion_lu(A)


b = np.array([[0,0,1]])

z= solve_Lz(L,b)
print(f"Solucónes de Lz=b: {z}")

x = solve_Ux(z,U)
print(f"Solucónes de Lz=b: {x}")