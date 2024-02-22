from gestor import Solve



# Matriz ejemplo vista en clase para jacobi y seidel

a = [[2, -1, 0],
    [-1, 3, -1],
    [0, -1, 2]]

b = [[1],
    [8],
    [-5]]







tipo = "seidel"


Solve(tipo,a,b)