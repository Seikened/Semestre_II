import math as mt
import numpy as np
import matplotlib.pyplot as plt

pi = mt.pi

def f(x):
    return mt.cos(x)



def taylor(x,x0,grado):
    y = f(x0)
    
    for n in range(1,grado):
        y += (-1)**n * (x-x0)**(2*n) / mt.factorial(2*n)
    return y



# invoca la función
x = 0
x0 = pi
grado = 4
print(taylor(x,x0,grado))


x_values = np.linspace(0, 2 * pi, 100)  # 100 puntos entre 0 y 2*pi
taylor_values = [taylor(x, pi, 4) for x in x_values]
exact_values = [f(x) for x in x_values]

# Graficamos la aproximación de Taylor y la función exacta
plt.figure(figsize=(10, 5))
plt.plot(x_values, taylor_values, label='Aproximación de Taylor')
plt.plot(x_values, exact_values, label='Cos(x) exacto', linestyle='--')
plt.title('Aproximación de Taylor de cos(x) centrada en pi')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()