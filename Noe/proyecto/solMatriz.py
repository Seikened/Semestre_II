import numpy as np




#============================  Metodo de descomposicion LU  ================================
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
    n, m = L.shape
    z = np.zeros((n, 1))
    z[0] = b[0][0]
    for i in range(1, n):
        mult = L[i][0] * z[0]
        for j in range(1, i):
            mult += L[i][j] * z[j]
        z[i] = b[i][0] - mult  # Aquí está la corrección
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
#==========================  Fin de descomposicion LU  ==============================


#================================  Metodo Jacobi  ===================================
# Aqui se implementa el metodo de Jacobi para resolver sistemas de ecuaciones lineales
def jacobi(a, b, x):
    n = len(x)
    t = x.copy()
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j: 
                s += a[i][j] * t[j]
        x[i] = (b[i] - s) / a[i][i]
    return x


# Verificar convergencia
def jacobi_m(a,b,x,error=1e-10,max_iter=1000):
    n = len(x)
    t = x.copy()
    for k in range(max_iter):
        x = jacobi(a,b,x)
        d = np.linalg.norm(np.array(x)-np.array(t),np.inf)
        if d < error:
            return x,k
        else:
            t = x.copy()
    return[],max_iter
#============================  Fin de metodo de Jacobi  ================================

#============================  Metodo de Gauss-Seidel  ================================
# Aqui se implementa el metodo de Gauss-Seidel para resolver sistemas de ecuaciones lineales
def GaussSeidel(a, b, x, max_iter=1000, error=1e-10):
    n = len(x)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(a[i][j] * x[j] for j in range(i))
            sum2 = sum(a[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / a[i][i]
        if np.linalg.norm(x - x_old, np.inf) < error:
            return x, k
    return x, max_iter




# Verificar convergencia
def GaussSeidel_m(a, b, x_inicial, error=1e-10, max_iter=1000):
    n = len(x_inicial)
    t = x_inicial.copy()
    for k in range(max_iter):
        x, _ = GaussSeidel(a, b, t, max_iter, error)  # Ajuste aquí para separar los valores devueltos
        d = np.linalg.norm(np.array(x) - np.array(t), np.inf) # Esto es lo que tengo que cambiar
        if d < error:
            return x, k
        t = x.copy()
        print(f"Esta es la iteración: {k}")
        
    return x, max_iter  # Devuelve x y el número de iteraciones si no converge dentro del max_iter




#==========================  Fin de metodo de Gauss-Seidel  ==============================

#=========================================== test =========================================


# A = np.array([[4, -1, 0, 0],
#               [-1, 4, -1, 0],
#               [0, -1, 4, -1],
#               [0, 0, -1, 3]])

# b = np.array([[15],
#               [10],
#               [10],
#               [10]])

# # Utilizamos descomposición LU para resolver Ax = b
# L, U = descomposicion_lu(A)
# print("L:", L)
# print("U:", U)

# # Resolver Lz = b para obtener z
# z = solve_Lz(L, b)
# print("z:", z)

# # Resolver Ux = z para obtener x
# x = solve_Ux(z, U)
# print("Solución x usando LU:", x)

# # Probamos el método de Jacobi
# x_inicial = np.zeros((A.shape[0], 1))
# x_jacobi, iter_jacobi = jacobi_m(A, b[:,0], x_inicial)
# print("Solución x usando Jacobi:", x_jacobi, "en", iter_jacobi, "iteraciones")

# # Probamos el método de Gauss-Seidel
# x = GaussSeidel(A, b, x)


# x_gauss_seidel, iter_gauss_seidel = GaussSeidel_m(A, b[:,0], x_inicial)
# print("Solución x usando Gauss-Seidel:", x_gauss_seidel, "en", iter_gauss_seidel, "iteraciones")