from solMatriz import *

A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])

b = np.array([[15],
              [10],
              [10],
              [10]])

# Utilizamos descomposición LU para resolver Ax = b
L, U = descomposicion_lu(A)
print("L:", L)
print("U:", U)

# Resolver Lz = b para obtener z
z = solve_Lz(L, b)
print("z:", z)

# Resolver Ux = z para obtener x
x = solve_Ux(z, U)
print("Solución x usando LU:", x)

# Probamos el método de Jacobi
x_inicial = np.zeros((A.shape[0], 1))
x_jacobi, iter_jacobi = jacobi_m(A, b[:,0], x_inicial)
print("Solución x usando Jacobi:", x_jacobi, "en", iter_jacobi, "iteraciones")

# Probamos el método de Gauss-Seidel
x_gauss_seidel, iter_gauss_seidel = GaussSeidel_m(A, b[:,0], x_inicial)
print("Solución x usando Gauss-Seidel:", x_gauss_seidel, "en", iter_gauss_seidel, "iteraciones")