from gestor import Solve



# Matriz ejemplo vista en clase para jacobi y seidel

a = [[2, -1, 0],
    [-1, 3, -1],
    [0, -1, 2]]

b = [[1],
    [8],
    [-5]]





#Gauss
tipo = "gauss"
Solve(tipo,a,b)

# # LU
# tipo = "lu"
# Solve(tipo,a,b)


# # Jacobi
# tipo = "jacobi"
# Solve(tipo,a,b)

# # Seidel
# tipo = "seidel"
# Solve(tipo,a,b)