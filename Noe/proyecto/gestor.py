from funciones import *
import numpy as np
from numpy.linalg import matrix_rank as rank

#=========================================== MENU =========================================




def Solve(tipoMetodo,A,b):
    tipoMetodo = tipoMetodo.lower()
    
    A = np.array(A)

    b = np.array(b)
    match tipoMetodo:
        
        # CASO LU
        case "lu":
            # Utilizamos descomposición LU para resolver Ax = b
            L, U = descomposicion_lu(A)
            # Resolver Lz = b para obtener z
            z = solve_Lz(L, b)
            # Resolver Ux = z para obtener x
            x = solve_Ux(z, U)
            print("Solución x usando LU:", x)

        # CASO JACOBI
        case "jacobi":
            # Probamos el método de Jacobi
            x_inicial = np.zeros((A.shape[0], 1))
            x_jacobi, iter_jacobi = jacobi_m(A, b[:,0], x_inicial)
            print("Solución x usando Jacobi:", x_jacobi, "en", iter_jacobi, "iteraciones")

        # CASO SEIDEL
        case "seidel":
            # Probamos el método de Gauss-Seidel
            x_inicial = np.zeros((A.shape[0], 1))
            x_gauss_seidel, iter_gauss_seidel = GaussSeidel_m(A, b, x_inicial)
            print("Solución x usando Gauss-Seidel:", x_gauss_seidel, "en", iter_gauss_seidel, "iteraciones")



def verificar_matriz(A, b):
    A = np.array(A)

    b = np.array(b).reshape(-1, 1) 
    
    m, n = A.shape
    Ay = np.concatenate((A, b), axis=1)
    rangoAy = rank(Ay)
    rangoA = rank(A)

    etiqueta = 0
    if rangoAy == (rangoA + 1):
        print('No hay solución')
        etiqueta = -1
    elif rangoAy == rangoA:
        print('Hay almenos una solución')
        etiqueta = 0
    if rangoA == n:
        print('Hay una solución única')
        etiqueta = 1
    elif rangoA < n:
        print('Hay soluciones infinitas')
        etiqueta = 2
    return etiqueta
    

    







#================================== TEST ==================================




a = [[2, -1, 0],
    [-1, 3, -1],
    [0, -1, 2]]

b = [[1],
    [8],
    [-5]]

tipo = "jacobi"

tiene_sol = verificar_matriz(a, b)
if tiene_sol == 1:
    Solve(tipo,a,b)
else:
    print("No tiene solución")