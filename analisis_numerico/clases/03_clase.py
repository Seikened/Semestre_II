from numpy.linalg import matrix_rank as rank
import numpy as np




# A = np.array([[4,3,5],[-2,-4,5],[7,8,0],[1,0,2],[9,1,-6]])
# y = np.array([[2,5,-3,1,6]])
# m,n = A.shape # esto es para obtener las dimensiones de la matriz M X N

# Ay = np.concatenate((A,y.T),axis=1)

# rangoAY = rank(Ay)
# rangoA = rank(A)

# print(f"Rango de Ay: {rangoAY}")
# print(f"Rango de A: {rangoA}")

# if rangoAY == (rangoA+1):
#     print("No hay solución")
# elif rangoAY == rangoA:
#     print("Hay al menos una solución")
#     if rangoA == n:
#         print("El sistema es compatible determinado")
#     elif rangoA < n:
#         print("Hay soluciones infinitas")

#----------------------------------------------------------------------------------

from numpy.linalg import matrix_rank as rank
import numpy as np

def verificar_matriz(A, y):
    m, n = A.shape
    Ay = np.concatenate((A, y.T), axis=1)
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
    
if __name__ == "__main__":
    
    # Suponga que un equipo de 3 paracaidistas esta unido por una cuerda ligera muentras esta en caida libre a una velocidad de 5 m*s
    # Calcule la tension en cada seccion de la cuerda segun la tensión de los datos
    # Paracaidista ,  masa kg    , coeficiente de arrastre
    # 1            ,   70        ,   10
    # 2            ,   60        ,   14
    # 3            ,   40        ,   17




    # c1v + T - m1g = -m1a
    # c2v + R - m2g -T = -m2a
    # c3v - m3g - R = -m3a


    m1 = 70
    m2 = 60
    m3 = 40
    v = 5
    c1 = 10
    c2 = 14
    c3 = 17
    g = 9.8

    A = np.array( [[1,0,m1],[-1,1,m2],[0,-1,m3]] )
    y = np.array( [ [ (m1*g)-(c1*v), (m2*g)-(c2*v), (m3*g)-(c3*v) ] ] )
    
    
    
    tiene_sol = verificar_matriz(A, y)
    if tiene_sol == 1:
        x = np.linalg.solve(A, y.T) # recibe y como vector fila, esta definido como vector columna
        print('x =\n', x)
        print('y = \n', np.dot(A, x))

