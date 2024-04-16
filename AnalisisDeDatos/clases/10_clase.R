setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploEstudiantes.csv', header = TRUE, sep = ";", dec = ",",
                  row.names = 1)
datos

install.packages("FactoMineR",dependencies=TRUE)
library(FactoMineR)

res <- PCA(datos, scale.unit = TRUE, ncp = 5, graph = FALSE)
res

#Plano principal
plot(res, axes = c(1,2),choix = "ind", col.ind = "red", new.plot = TRUE)

# Circulo de correlaciones
plot(res, axes = c(1,2), choix = "var", col.var = "blue", new.plot = FALSE)

# Mal representados con coseno cuadrado

res$ind$cos2
res$var$cos2

res$ind$cos2[,1] + res$ind$cos2[,2]


res$var$cos2[,1] + res$var$cos2[,2]

# BITPLOT

modelo <- prcomp(datos)
modelo

biplot(modelo)


# EJEMPLO CLIENTES ------------------------------------------------------------
setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploClientes.csv', header = TRUE, sep = ",", dec = ".",
                  row.names = 1)
datos

#install.packages("FactoMineR",dependencies=TRUE)
library(FactoMineR)

res <- PCA(datos, scale.unit = TRUE, ncp = 5, graph = FALSE)
res

#Plano principal
plot(res, axes = c(1,2),choix = "ind", col.ind = "red", new.plot = TRUE)

# Circulo de correlaciones
plot(res, axes = c(1,2), choix = "var", col.var = "blue", new.plot = FALSE)

# Mal representados con coseno cuadrado

res$ind$cos2
res$var$cos2

res$ind$cos2[,1] + res$ind$cos2[,2]


res$var$cos2[,1] + res$var$cos2[,2]

# BITPLOT

modelo <- prcomp(datos)
modelo

biplot(modelo)



# EJEMPLO algoritmo ------------------------------------------------------------

# EJEMPLO CLIENTES ------------------------------------------------------------
setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploAlgoritmosRecomendacion.csv', header = TRUE, sep = ",", dec = ".",
                  row.names = 1)
datos

#install.packages("FactoMineR",dependencies=TRUE)
library(FactoMineR)

res <- PCA(datos, scale.unit = TRUE, ncp = 5, graph = FALSE)
res

#Plano principal
plot(res, axes = c(1,2),choix = "ind", col.ind = "red", new.plot = TRUE)

# Circulo de correlaciones
plot(res, axes = c(1,2), choix = "var", col.var = "blue", new.plot = FALSE)

# Mal representados con coseno cuadrado

res$ind$cos2
res$var$cos2

res$ind$cos2[,1] + res$ind$cos2[,2]


res$var$cos2[,1] + res$var$cos2[,2]

# BITPLOT

modelo <- prcomp(datos)
modelo

biplot(modelo)


