# Gráficar

import matplotlib.pyplot as plt

x = 1/2
ecuacion_uno = -x**3+1
ecuacion_dos = (1-x)**(1/3)
ecuacion_tres = ( 2 * x**(3) + 1 ) / ( 3 * x**(2) + 1 )

lista_x = [x]
lista_y = []

error = 0.0001

while abs(ecuacion_uno - ) > error:
    lista_y.append(ecuacion_uno)
    x = ecuacion_uno
    ecuacion_uno = -x**3+1
    ecuacion_dos = (1-x)**(1/3)
    ecuacion_tres = ( 2 * x**(3) + 1 ) / ( 3 * x**(2) + 1 )
    lista_x.append(x)


plt.plot(lista_x, lista_y)
plt.show()