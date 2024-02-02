import matplotlib.pyplot as plt
import numpy as np

def err_absoluto(x, y):
    return np.abs(x - y)

def err_relativo(x, y):
    return np.abs(x - y) / np.abs(x)

def err_relativo_porcentual(x, y):
    return err_relativo(x, y) * 100


def Errores():
    x_real = np.random.rand(4)
    x_aprox = np.random.rand(4)

    plt.plot(x_real, '-*', label='x real')
    plt.plot(x_aprox, '-o', label='x aprox')
    plt.grid()
    plt.legend()
    plt.show()



#------------------------------------------------------------

