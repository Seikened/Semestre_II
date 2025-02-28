import sys
import numpy as np

# Información del tipo de dato float de doble precisión
print('Información del tipo de dato float (doble precisión): \n', sys.float_info)

# Epsilon de la máquina para doble precisión
eps_double = sys.float_info.epsilon  # Corregido aquí


n = 7.0

# Evaluamos a partir de qué valor de epsilon se detecta que 2 números son diferentes (doble precisión)
print("Comparaciones con doble precisión:")
for k in range(1, 5):
    m = n + k * eps_double
    if n == m:
        print('Iguales')
    else:
        print('Diferentes')

# Información para float32 (precisión simple)
info_float32 = np.finfo(np.float32)
print('\nInformación para float32 (precisión simple): \n', info_float32)

# Epsilon de la máquina para simple precisión
eps_single = np.float32(info_float32.eps)

# Evaluamos a partir de qué valor de epsilon se detecta que 2 números son diferentes (simple precisión)
print("Comparaciones con simple precisión:")
for k in range(1, 5):
    m = np.float32(n) + k * eps_single
    if np.float32(n) == m:
        print('Iguales')
    else:
        print('Diferentes')
