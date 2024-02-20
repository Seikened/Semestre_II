import math as mt
import numpy as np




pi = mt.pi

def taylor(x,x0,grado):
    y = 0
    for n in range(0,grado+1):
        y += (-1)**n * (x-x0)**(2*n) / mt.factorial(2*n)
        return y

# invoca la función
x = pi/4
x0 = 0
grado = 2
print(taylor(x,x0,grado))