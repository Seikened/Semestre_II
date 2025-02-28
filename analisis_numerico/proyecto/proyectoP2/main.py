from defRoots import *
from termcolor import colored
import os




f = lambda x: 1 + 2*x - 3*x**2*np.exp(-x) + 2*x**3*np.sin(x)*np.exp(-x/5)
df = lambda x: 2 - 6*x*np.exp(-x) + 2*np.sin(x)*np.exp(-x/5) - 6*x**2*np.exp(-x) + 6*x**3*np.cos(x)*np.exp(-x/5) - 2*x**2*np.sin(x)*np.exp(-x/5) - 3*x**2*np.exp(-x) + 6*x**2*np.sin(x)*np.exp(-x/5) - 2*x**3*np.cos(x)*np.exp(-x/5) - 2*x**3*np.sin(x)*np.exp(-x/5)/5
a = 15.80556
b = 15.80558
g_de_x =  lambda x: x - (f(x) / df(x))


ec_biseccion = Root(f=f,a=a,b=b)
ec_false_position = Root(f=f,a=a,b=b)
ec_punto_fijo = Root(g=g_de_x,a=a)
ec_newton = Root(f=f,a=a,df=df)


# Resuelvo la ecuaciónes
ec_biseccion.biseccion()
ec_false_position.falsa_posicion()
ec_punto_fijo.punto_fijo()
ec_newton.newton()

os.system('clear')
print(colored("Autor: Fernando Leon Franco", 'blue'))
print(colored("Descripción: El programa utiliza diferentes métodos numéricos para encontrar las raíces de una función dada. Se utilizan los métodos de bisección, falsa posición, punto fijo y Newton. Cada método se aplica a la función definida en el archivo 'defRoots.py' y se muestra la raíz encontrada junto con una gráfica de la función y la aproximación de la raíz. El programa utiliza la biblioteca 'termcolor' para imprimir mensajes coloreados en la consola.", 'blue'))

print(colored("Enter para continuar", 'green'))
input()

os.system('clear')
print(colored("Raíz encontrada por el método de bisección: ", 'green'), ec_biseccion)
ec_biseccion.graficar()
print(colored("SE GRAFICO BISECCION", 'green'))

print("\n" * 2)  

print(colored(f"Raíz encontrada por el método de falsa posición: ", 'blue'), ec_false_position)
ec_false_position.graficar()
print(colored("SE GRAFICO FALSA POSICION", 'blue'))

print("\n" * 2) 

print(colored("Raíz encontrada por el método de punto fijo: ", 'yellow'), ec_punto_fijo)
ec_punto_fijo.graficar()
print(colored("SE GRAFICO PUNTO FIJO", 'yellow'))

print("\n" * 2)  

print(colored("Raíz encontrada por el método de Newton: ", 'red'), ec_newton)
ec_newton.graficar()
print(colored("SE GRAFICO NEWTON", 'red'))

