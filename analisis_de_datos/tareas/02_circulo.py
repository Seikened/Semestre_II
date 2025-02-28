import math as mt

radio = float(input("Dame tu radio: "))
pi = mt.pi
diametro = 2*radio
circunferencia = 2*pi*radio
area = pi*(radio**2)

print(f"Tu area es: {area:.2f}, el diametro es: {diametro:.2f} y la circunferencia es: {circunferencia:.2f}")