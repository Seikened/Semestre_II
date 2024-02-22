from funciones import *
import numpy as np
from numpy.linalg import matrix_rank as rank

#=========================================== MENU =========================================

def Solve(tipoMetodo,A,b):
    """
    

    Parametros
    ----------
    tipoMetodo : Cadena de Texto
        El tipo de metodo por el que se va a resolver la matriz.
    A : Matriz
        La matriz A.
    b : Matriz
        Vector con las igualdades de las filas.

    Regresa
    -------
    La matriz resuelta

    """

    while True:
        Solve_matrix(tipoMetodo,A,b)
        userResponse = input("Quieres continuar? (s/n)=> ")
        if userResponse.lower()!="s":
            break
        else:
            cambiarDatos = input("\nQuieres cambiar algun dato? (s/n)=> ").lower()
            if cambiarDatos == "s":
            
                tipoMetodo = input("Dame tu metodo: ")
                print(" INGRESA LA MATRIZ A\n")
                A = solicitar_matriz("A")
                
                
                print(" \n INGRESA LA EL VECTOR DE TERMINOS INDEPENDIENTES\n")
                b =  solicitar_matriz("VECTOR DE TERMINOS INDEPENDIENTES")



#=========================================== Resolver matrx =========================================
def Solve_matrix(tipoMetodo,A,b):
    tipoMetodo = tipoMetodo.lower()
    if verificar_matriz(A,b):
        
        A = np.array(A)

        b = np.array(b)
        match tipoMetodo:
            case "gauss":
                x = Gauss(A,b)
                print("Solución x usando Gauss de numpy:", x)

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
    else:
        print("Ingrese otra matriz no se puede resolver esta matríz")


#=========================================== Verifica diagonal =========================================
def VerificaDiagonal(A):
    sum = 0
    elemntoSumado = None
    diagonal = None
    
    for filas in range(len(A)):
        sum = 0
        
        for columnas in range(len(A)):

            if filas != columnas:
                sum += A[filas][columnas]
                elemntoSumado = sum
            else:
                diagonal = A[filas][columnas]
        if diagonal > elemntoSumado:
            continue
        else:
            return False
    return True


#=========================================== Verifica matrix =========================================
def verificar_matriz(a, b):
    A = np.array(a)
    b = np.array(b).reshape(-1, 1)
    
    m, n = A.shape
    Ay = np.concatenate((A, b), axis=1)
    rangoAy = rank(Ay)
    rangoA = rank(A)

    # Comprobación de rango para consistencia del sistema
    if rangoAy > rangoA:
        print('El sistema es inconsistente, no hay solución ❌')
        return False
    elif rangoAy == rangoA:
        if rangoA == n:
            print('Hay una solución única ✅')
            # Si adicionalmente quieres verificar la diagonal dominante
            if VerificaDiagonal(a):
                print("La matriz es adecuada para métodos iterativos")
                return True
            else:
                print("La matriz NO es adecuada para métodos iterativos")
                return False
        else:
            print('Hay soluciones infinitas ∞')
            return False
    else:
        print('Hay al menos una solución, pero hay algo inusual 🤔')
        return False




def solicitar_matriz(texto):
    filas = int(input(f"INGRESA EL TAMAÑO DE LA MATRIZ {texto}: "))
    matriz = []
    for i in range(filas):
        fila_str = input(f"Ingresa los elementos de la fila {i + 1} separados por espacio y terminando da enter: ")
        fila = [int(x) for x in fila_str.split()]
        matriz.append(fila)
    return matriz






#================================== TEST ==================================



# #Uno
# a = [
#     [1, 2, 3],
#     [2, 4, 6],
#     [1, 2, 3]
# ]

# b = [[4], [8], [7]]






# tipo = "gauss"


# Solve(tipo,a,b)



