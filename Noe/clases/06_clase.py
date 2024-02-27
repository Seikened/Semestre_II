import numpy as np
import matplotlib.pyplot as plt
import math as mt


def  maclauren(x, x0, grados):
    y = 0
    for n in range(0,grados+1):
        y+= ((-1)**n) * ( ((x-x0)**(2*n+1))/(mt.factorial(2*n+1)) )
    return y


x = np.arange( 0, 2*np.pi , 0.1 )
x0 = np.pi/2
y1 = [maclauren(i, x0, 0) for i in x]
y2 = [maclauren(i, x0, 1) for i in x]
y3 = [maclauren(i, x0, 2) for i in x]
y4 = [maclauren(i, x0, 3) for i in x]

plt.plot(x,np.sin(x), label='sin(x)')
plt.plot(x,y1, '-',label='constante')
plt.plot(x,y2, '--',label='cuadratica')
plt.plot(x,y3, '-.',label='cubica')
plt.plot(x,y4, ':',label='quintica')
plt.legend()
plt.show()