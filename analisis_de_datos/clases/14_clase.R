setwd("/Users/fernandoleonfranco/app")
datos <- read.csv("iris.csv", header = TRUE, sep = ";",dec = ".")
datos


# ARBOLES DE DESICION
str(datos)
datos$tipo <- as.factor(datos$tipo)
str(datos)

muestra <- sample(1:250,50)
ttesting <- datos[muestra,]
ttraining <- datos[-muestra,]

library(rpart)
#install.packages("rpart.plot",dependencies = TRUE)
library(rpart.plot)

modelo <- rpart(tipo ~ ., data = ttraining)
rpart.plot(modelo)


#prediccion <- predict(modelo, ttesting)
prediccion <- predict(modelo, ttesting, type = "class")
prediccion

prp(modelo,extra = 104,branch.type = 2, box.col=c("pink","green")[modelo$frame$yval2])

# Matriz de confusion
MC <- table(ttesting$tipo, prediccion)
MC

acierto <- sum(diag(MC))/sum(MC) 
acierto


error <- 1 - acierto
error





