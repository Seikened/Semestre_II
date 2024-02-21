from funciones import *


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





#================================== TEST ==================================




a = [[2, -1, 0],
    [-1, 3, -1],
    [0, -1, 2]]

b = [[1],
    [8],
    [-5]]

tipo = "seidel"

Solve(tipo,a,b)
