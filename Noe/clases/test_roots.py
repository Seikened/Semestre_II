import numpy as np
import matplotlib.pyplot as plt
import roots as rt



    

f = lambda x : 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
#fdot = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
g = lambda x : x - f(x)

x0 = np.pi/4
a = 9
b = 10 


# Metodo de Newton Raphson
xr,interaciones,error = rt.newton_raphson(x0,f)
print(f" Metodo de Newton Raphson xr = {xr} con {interaciones} interaciones y un error de {error}")

# Metodo de la bisección
xr,interaciones = rt.biseccion(f,a,b)
print(f" Metodo de la bisección xr = {xr} con {interaciones} interaciones")

# Metodo de punto fijo
xr,interaciones,ea= rt.punto_fijo(g,x0)
print(f" Metodo de punto fijo xr = {xr} con {interaciones} interaciones y un error de {ea}")


# Metodo de posición falsa
xr = rt.falsa_posicion(f,a,b)
print(f" Metodo de posición falsa xr = {xr} con {interaciones} interaciones")




X = np.linspace(a,b,200,endpoint=True)
Y = f(X)


# #mpl.style.use('seaborn')
# fig = plt.figure(facecolor='tab:pink')
# ax = fig.add_subplot(1,1,1)
# ax.set_facecolor('#FFC0CB')
# ax.plot(X,Y,linewidth=2.5,linestyle='-',label="$f(x) = cos(x) - x$", color='#00FaFF')
# ax.legend()
# ax.set_xlabel('x',color='c')
# ax.set_ylabel('y', color='tab:blue')
# ax.grid(linestyle='--',linewidth=0.5,color='.25',zorder=-10)
# ax.annotate('Raiz',xy=(xr,0),xytext=(0.8,-0.5),arrowprops = dict(facecolor='black',shrink=0.025))
# ax.tick_params(labelcolor='#40E0D0')
# plt.show()

