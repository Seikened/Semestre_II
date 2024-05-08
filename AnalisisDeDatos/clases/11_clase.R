

#Endograma
#Distancia euclidia
# Agregraciones: ward


setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploEstudiantes.csv', header = TRUE, sep = ";", dec = ",",
                  row.names = 1)
datos



dist(datos)



# Salto maximo = compelte
# Salto minimo = single
# Salto promedio = average
# Salto de ward = ward

# salto maximo
modelo <-  hclust(dist(datos),method = "complete")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes maximo")
rect.hclust(modelo, k = 3, border = "blue")

# salto minimo
modelo <-  hclust(dist(datos),method = "single")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes minimo")
rect.hclust(modelo, k = 3, border = "green")

# salto promedio
modelo <-  hclust(dist(datos),method = "average")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes promedio")
rect.hclust(modelo, k = 3, border = "red")

# salto ward
modelo <-  hclust(dist(datos),method = "ward.D")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes ward")
rect.hclust(modelo, k = 3, border = "orange")


# Grupos y clasifica cada individuo y define un cluster
grupos <- cutree(modelo, k = 3)
grupos

datos

# instrucción que sirve para agregar la clasificación a los datos
nuevosDatos <- cbind(datos, grupos)
nuevosDatos

# Guardar los datos

write.csv(nuevosDatos, file = "EjemploEstudiantesCluster.csv")

nuevosDatosCsv <- read.csv("EjemploEstudiantesCluster.csv", header = TRUE, sep = ",", dec = ".")
nuevosDatosCsv



#install.packages("FactoMineR",dependencies=TRUE)

suppressMessages(library(FactoMineR))


res <- PCA(datos, scale.unit = TRUE, ncp = 5, graph = FALSE)
res


res.hcpc <- HCPC(res, min = 3, max = 3, graph = FALSE)
plot.HCPC(res.hcpc,choice = "map")
plot.HCPC(res.hcpc,choice = "3D.map",angle=60)


# Ejemplo algoritmo recomendación

#Endograma
#Distancia euclidia
# Agregraciones: ward


setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploAlgoritmosRecomendacion.csv', header = TRUE, sep = ",", dec = ".",
                  row.names = 1)
datos



dist(datos)



# Salto maximo = compelte
# Salto minimo = single
# Salto promedio = average
# Salto de ward = ward

# salto maximo
modelo <-  hclust(dist(datos),method = "complete")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes maximo")
rect.hclust(modelo, k = 3, border = "blue")

# salto minimo
modelo <-  hclust(dist(datos),method = "single")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes minimo")
rect.hclust(modelo, k = 3, border = "green")

# salto promedio
modelo <-  hclust(dist(datos),method = "average")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes promedio")
rect.hclust(modelo, k = 3, border = "red")

# salto ward
modelo <-  hclust(dist(datos),method = "ward.D")
plot(modelo, hang = -1, main = "Dendrograma de estudiantes ward")
rect.hclust(modelo, k = 3, border = "orange")


# Grupos y clasifica cada individuo y define un cluster
grupos <- cutree(modelo, k = 3)
grupos

datos

# instrucción que sirve para agregar la clasificación a los datos
nuevosDatos <- cbind(datos, grupos)
nuevosDatos

# Guardar los datos

write.csv(nuevosDatos, file = "EjemploEstudiantesCluster.csv")

nuevosDatosCsv <- read.csv("EjemploEstudiantesCluster.csv", header = TRUE, sep = ",", dec = ".")
nuevosDatosCsv



#install.packages("FactoMineR",dependencies=TRUE)

suppressMessages(library(FactoMineR))


res <- PCA(datos, scale.unit = TRUE, ncp = 5, graph = FALSE)
res


res.hcpc <- HCPC(res, min = 3, max = 3, graph = FALSE)
plot.HCPC(res.hcpc,choice = "map")
plot.HCPC(res.hcpc,choice = "3D.map",angle=60)






