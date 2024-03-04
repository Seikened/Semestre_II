from funcionesTaylor import *



x_values = np.linspace(0, 2* pi, 100)  # 100 puntos entre 0 y 2*pi
taylor_values = taylor(x_values, pi, 10) # Devuelvo los valores de y
cos_values = [f(x) for x in x_values]

error = error_relativo(x_values,taylor_values,cos_values)
print(error)

# Graficamos la aproximación de Taylor y la función exacta
plt.figure(figsize=(10, 5))
plt.plot(x_values, taylor_values, label='Aproximación de Taylor')
plt.plot(x_values, cos_values, label='Cos(x) exacto', linestyle='--')
plt.title('Aproximación de Taylor de cos(x) centrada en pi')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(x_values, error, label='Error relativo', color='red')
plt.title('Error relativo de la aproximación de Taylor de cos(x)')
plt.xlabel('x')
plt.ylabel('Error relativo')
plt.legend()
plt.grid(True)
plt.show()

