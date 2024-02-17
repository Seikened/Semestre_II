import numpy as np



import numpy as np

def GaussSeidel(a, b, x, max_iter=1000, error=1e-10):
    n = len(x)
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(a[i][j] * x[j] for j in range(i))
            sum2 = sum(a[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / a[i][i]
        # Incrementa k aquí para reflejar el número de iteraciones realizadas.
        if np.linalg.norm(x - x_old, np.inf) < error:
            return x, k + 1
    return x, max_iter

def GaussSeidel_m(a, b, x_inicial, error=1e-10, max_iter=1000):
    n = len(x_inicial)
    t = x_inicial.copy()
    for _ in range(max_iter):
        x, iter_count = GaussSeidel(a, b, t, max_iter, error)
        d = np.linalg.norm(x - t, np.inf)
        if d < error:
            return x, iter_count  # Usa iter_count para obtener el número de iteraciones desde GaussSeidel
        t = x.copy()
    return x, max_iter  # Devuelve x y el número de iteraciones si no converge dentro del max_iter



# definimos la matriz A y el vector b
# Definición de la matriz A de tamaño 4x4
A = np.array([
    [4, -1, 0, 1],
    [-1, 4, -1, 0],
    [0, -1, 4, -1],
    [1, 0, -1, 3]
])

# Definición del vector b
b = np.array([8, 7, 6, 5])

# definimos el vector inicial
x_inicial = np.zeros((A.shape[0], 1))

# Probamos el método de Gauss-Seidel
x_gauss_seidel, iter_gauss_seidel = GaussSeidel_m(A, b, x_inicial)
print("Solución x usando Gauss-Seidel:", x_gauss_seidel, "en", iter_gauss_seidel, "iteraciones")