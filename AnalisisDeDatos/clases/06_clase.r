5+5


numero = 3
numero2 = 10
num = numero + numero2

valor <- 5
valor2 <- 15
valor3 <- valor + valor2

#Vectores de calificaciones
calificaciones <- c(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
calificaciones
calificaciones[1]
calificaciones[2:5]
calificaciones[c(1, 3, 5)] # esto es para seleccionar elementos de un vector
calificaciones[-c(1, 3, 5)]

# Matrices
matriz <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12), 4,3 )
matriz


matriz[1, 2]
matriz[1,]
matriz[,3]
matriz[,-2]
matriz[c(1,4), c(1,3)]
matriz[1:2,1:3]

#DATAFRAMES
nombre <- c('juan','maria','andrea','luis')
edad <- c(17,18,19,20)
estatura <- c(1.70, 1.60, 1.80, 1.75)
sexo <- c('M','F','F','M')


elementos <- data.frame(nombre,edad,estatura,sexo)

elementos[2,2]

elementos$nombre[3]

cbind()

str(elementos)
summary(elementos)


#Lectura de archivos
# Separador de variables ( , ; )
# Separador de decimales ( . , )
# Si tiene encabezados en las columnas
# Si tienen encabezado en las filas



#ruta <- '/Users/fernandoleonfranco/app/EjemploClientes.csv'
#ruta2 <- '/Users/fernandoleonfranco/app/EjemploEstudiantes.csv'
#clientes <- read.csv(ruta)
#estudiantes <- read.csv(ruta2)

setwd('/Users/fernandoleonfranco/app/')
datos <- read.table("EjemploClientes.csv", sep = ",", dec=".", header = TRUE , row.names = 1)

head(datos)
summary(datos)
str(datos)
