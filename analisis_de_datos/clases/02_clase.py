# # Estructuras de control repetitiva initas (FOR)
# # Cuando estableces el limite inferior y superior

# for i in range(0,10):
#     print(i)

# # Cuando solo estableces el limite superior
# for i in range(10):
#     print(i)
    
# # Cuando se establece el salto
# for i in range(0,10,2):
#     print(i)

# For desecendente

# for i in range(15,1,-1):
#     print(i)
    
# # for anidados
# for i in range(1,10):
#     print(i)
#     for j in range(1,10):
#         print(j)

# FOREACH

# lista_alumnos = ['Juan','Maria','Pedro','Jose']
# for alumno in lista_alumnos:
#     print(alumno)

# Ejercicio 1
# Crea una lista que solo muestre los numeros pares
# Ahora que sume del 50 al 100


# suma=0
# for i in range(1,101):
#     if (i % 2 == 0) and (i <= 50):
# #        print(i)
#         suma += i
        

#print(suma)

# Realizar tabla de multiplicar del definir el multiplo y siempre sera hasta el 10
#multiplicador  = int(input("Ingresa el numero a multiplicar: "))
#rango_inicial = int(input("Desde donde quieres que comience: "))
#rango_final = int(input("Hasta donde quieres que comience: "))
# for i in range(rango_inicial,rango_final+1):
#     #print(f"{multiplicador} x {i} = {multiplicador*i}")
#     pass
# Factorial

# factorial = int(input("Factorial de: "))

# suma = 1
# for i in range(factorial,0,-1):
#     suma *= i
# print(f"Factorial de {factorial} es = {suma}")

# Escribir un número de 5 digitos e identificar si se trata de una capicua

# numero = int(input("Ingresa tu numero: "))

# diesK = numero//10000
# miles = (numero//1000)-(diesK*10)
# cientos = (numero//100)-((diesK*100)+(miles*10))
# decimales = numero//10-((diesK*1000)+(miles*100)+(cientos*10))
# unos = numero // 1 - (((diesK*10000)+(miles*1000)+(cientos*100)+(decimales*10)))

# if (diesK==unos) and (miles==decimales):
#     print("Es capicua")
# else:
#     print("No es capicua")


# Ejercicio 6
# de un listado del 1 al 100, mostrar los números que al sumar sus digitos sean 12

decimas = 0
unidades = 0
for i in range(1,101):
    decimales = i//10
    unidades = i%10
    if (decimales+unidades)== 12:
        print(f"El {i} en sus componentes es 12")