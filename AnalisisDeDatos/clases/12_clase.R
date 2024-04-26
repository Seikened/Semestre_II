setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploEstudiantes.csv', header = TRUE, sep = ";", dec = ",",
                  row.names = 1)
datos


grupos <- kmeans(datos,3, iter.max = 100)

# Inercia inter-cluster
grupos$betweenss


# Inercia intra-cluster
grupos$tot.withinss

# Inercia total
grupos$totss

# verificación del teorema de fisher
grupos$betweenss + grupos$tot.withinss


# Tamaño de los grupos (clousers)
grupos$size


#Centro de gravedad
grupos$centers

grupos$cluster


nuevosDatos <- cbind(datos, grupos$cluster)
nuevosDatos



# Gráfica de los clousters
library(scatterplot3d)
g3d  <-  scatterplot3d(datos)
g3d$points3d(grupos$centers, pch=19,col="blue", cex=2)
g3d$points3d(datos,col=grupos$cluster, pch=19)



# Codo de Jambu
inerciaIntraCluster <- rep(0,8)
for(k in 1:8){
  grupos2 <- kmeans(datos,k, iter.max = 100)
  inerciaIntraCluster[k] <- grupos2$tot.withinss
}

plot(inerciaIntraCluster,col="red",type="b")




# ------------------------------------------------------------------
setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploAlgoritmosRecomendacion.csv', header = TRUE, sep = ",", dec = ".",
                  row.names = 1)
datos



modelo <- prcomp(datos)
modelo

biplot(modelo)


grupos <- kmeans(datos,4, iter.max = 100)

# Inercia inter-cluster
grupos$betweenss


# Inercia intra-cluster
grupos$tot.withinss

# Inercia total
grupos$totss

# verificación del teorema de fisher
grupos$betweenss + grupos$tot.withinss


# Tamaño de los grupos (clousers)
grupos$size


#Centro de gravedad
grupos$centers

grupos$cluster


nuevosDatos <- cbind(datos, grupos$cluster)
nuevosDatos



# Gráfica de los clousters
library(scatterplot3d)
g3d  <-  scatterplot3d(datos)
g3d$points3d(grupos$centers, pch=19,col="blue", cex=2)
g3d$points3d(datos,col=grupos$cluster, pch=19)



# Codo de Jambu
inerciaIntraCluster <- rep(0,37)
for(k in 1:37){
  grupos2 <- kmeans(datos,k, iter.max = 100)
  inerciaIntraCluster[k] <- grupos2$tot.withinss
}

plot(inerciaIntraCluster,col="red",type="b")




#-----------------------------------------------------------------

setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploClientes.csv', header = TRUE, sep = ",", dec = ".",
                  row.names = 1)
datos



modelo <- prcomp(datos)
modelo

biplot(modelo)


grupos <- kmeans(datos,4, iter.max = 100)

# Inercia inter-cluster
grupos$betweenss


# Inercia intra-cluster
grupos$tot.withinss

# Inercia total
grupos$totss

# verificación del teorema de fisher
grupos$betweenss + grupos$tot.withinss


# Tamaño de los grupos (clousers)
grupos$size


#Centro de gravedad
grupos$centers

grupos$cluster


nuevosDatos <- cbind(datos, grupos$cluster)
nuevosDatos



# Gráfica de los clousters
library(scatterplot3d)
g3d  <-  scatterplot3d(datos)
g3d$points3d(grupos$centers, pch=19,col="blue", cex=2)
g3d$points3d(datos,col=grupos$cluster, pch=19)



# Codo de Jambu
inerciaIntraCluster <- rep(0,30)
for(k in 1:30){
  grupos2 <- kmeans(datos,k, iter.max = 100)
  inerciaIntraCluster[k] <- grupos2$tot.withinss
}

plot(inerciaIntraCluster,col="red",type="b")

