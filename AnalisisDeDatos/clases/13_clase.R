# MAQUINAS DE SOPORTE VECTORIAL

setwd("/Users/fernandoleonfranco/app")

datos <- read.csv("iris.csv", header = TRUE, sep = ";",dec = ".")
datos


str(datos)


# Cambiar la variable objetivo a factor (Tipo categorico)

datos$tipo <- as.factor(datos$tipo)
str(datos)

dim(datos)


# Segmentar para entrenamiento y para testear

muestra <- sample(1:150,50)
muestra


ttesting <- datos[muestra,]
ttraining <- datos[-muestra,]


install.packages("e1071",dependencies = TRUE)
library(class)
library(e1071)

modelo <- svm(tipo~.,data=ttraining, kernel = "linear")
modelo

?svm
# Prediccion
prediccion <- predict(modelo, ttesting)
prediccion

# presiscion global
# presiscion positiva
# presiscion negativa
# falsos positivos
# falsos negativos
# asertividad positiva
# asertividad negativa


# Matriz de confusion
matrizDeConfusion <- table(ttesting$tipo, prediccion)
matrizDeConfusion


# porcentaje de presiscion
acierto <- sum(diag(matrizDeConfusion))/sum(matrizDeConfusion)
acierto

# Error
error <- 1 - acierto
error


#

