from defRoots import *
import os




f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
df = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
a = 18
b = 19
g_de_x = lambda x: np.arcsin((-1 - 2*x + 3*x**2 * np.exp(-x)) / (2*x**3 * np.exp(-x/5)))


ec_biseccion = Root(f=f,a=a,b=b)
ec_false_position = Root(f=f,a=a,b=b)
ec_punto_fijo = Root(g=g_de_x,a=a)
ec_newton = Root(f=f,a=a,df=df)


# Resuelvo la ecuaciónes
ec_biseccion.biseccion()
ec_false_position.falsa_posicion()
ec_punto_fijo.punto_fijo()
ec_newton.newton()





print(ec_punto_fijo)