# y = 1/2
# x = 3/2

# sumar_dos_numeros = lambda x,y : x+y
# valor = sumar_dos_numeros(x,y)
# print(f"La suma {y} y {x} es {valor}")
# x = 6
# y = 2
# valor = sumar_dos_numeros(x,y)
# print(f"La suma {y} y {x} es {valor}")


# print(type(range(0,51)))

import matplotlib.pyplot as plt
import numpy as np


# #Generar datos para la impresion
# X = list(range(-50,51,3))
# y1 = [1/(x+1) for x in X]
# y2 = [x**2 for x in X]
# y3 = [x**3 for x in X]
# y4 = [np.sin(x) for x in X]


# fig = plt.figure()
# ax1 = fig.add_subplot(221)
# ax1.plot(X,y1)
# ax2 = fig.add_subplot(222)
# ax2.plot(X,y2)
# ax3 = fig.add_subplot(223)
# ax3.plot(X,y3)
# ax4 = fig.add_subplot(224)
# ax4.plot(X,y4)
# plt.show()


# X =list(range(0,51))

# y1 = [1/(x+1) for x in X]
# y2 = [x**2 for x in X]

# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax1.plot(X,y1, color = 'm',linewidth = 2.5, linestyle ='-', label = 'Hipérbola')
# ax1.legend()
# ax1.set_xlabel('x-axis')
# ax1.set_ylabel('y-axis')
# ax1.set_xlim(auto=True)
# ax1.set_ylim(auto=True)
# ax1.grid()
# ax1.set_aspect('equal')
# ax2 = fig.add_subplot(122)
# ax2.plot(X,y2)

# plt.show()






X = list(range(-50,50))

y1 = [(x**4+(2*(x**2))) for x in X]
y2 = [(x**3) + (2*x) for x in X]

fig = plt.figure()  
ax1 = fig.add_subplot(121)
ax1.plot(X,y1, color = 'm',linewidth = 2.5, linestyle ='-', label = 'Gráfica')
ax1.legend()
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax2 = fig.add_subplot(122)
ax2.plot(X,y2)

plt.show()