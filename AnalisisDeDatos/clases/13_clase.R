# MAQUINAS DE SOPORTE VECTORIAL

setwd("/Users/fernandoleonfranco/app")

# Carga de datos
datos <- read.csv("iris.csv", header = TRUE, sep = ";", dec = ".")
str(datos)

# Convertir la variable objetivo a factor
datos$tipo <- as.factor(datos$tipo)

# Segmentar para entrenamiento y para prueba
muestra <- sample(1:150, 50)
ttesting <- datos[muestra, ]
ttraining <- datos[-muestra, ]

# Cargar las librerías necesarias
library(e1071)

# Entrenar el modelo SVM
modelo <- svm(tipo ~ ., data = ttraining, kernel = "linear")

# Predecir con el modelo
prediccion <- predict(modelo, ttesting)

# Matriz de confusión
matrizDeConfusion <- table(ttesting$tipo, prediccion)
matrizDeConfusion

# Gráfico de los resultados
plot(modelo, ttraining, s.largo ~ s.ancho)

# También puedes graficar las predicciones realizadas sobre el conjunto de prueba
plot(modelo, ttesting, p.largo ~ p.ancho)
