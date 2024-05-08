# Redes neuronales
# Instalar y cargar la librería necesaria
# install.packages("neuralnet")
library(neuralnet)

# Establecer el directorio de trabajo
setwd('/Users/fernandoleonfranco/app')

# Leer el conjunto de datos
datos <- read.csv('EjemploEstudiantes.csv', header = TRUE, sep = ";", dec = ",", row.names = 1)

# Crear una nueva columna para la variable objetivo (ejemplo de aprobación/reprobación)
datos$Aprobado <- ifelse(rowMeans(datos) >= 7.0, 1, 0)

# Normalizar los datos (opcional)
max_val <- apply(datos, 2, max)
min_val <- apply(datos, 2, min)
datos_norm <- as.data.frame(scale(datos, center = min_val, scale = max_val - min_val))

# Dividir el conjunto de datos en entrenamiento y prueba
muestra <- sample(1:nrow(datos_norm), round(0.7 * nrow(datos_norm)))
ttraining <- datos_norm[muestra,]
ttesting <- datos_norm[-muestra,]

# Entrenar la red neuronal
formula_nn <- as.formula(paste("Aprobado ~", paste(names(ttraining)[!names(ttraining) %in% "Aprobado"], collapse = " + ")))
modelo <- neuralnet(formula_nn, data = ttraining, hidden = c(5, 3), linear.output = FALSE)

# Visualizar la red neuronal
plot(modelo)

# Predicciones~
resultados <- compute(modelo, ttesting[, -which(names(ttesting) == "Aprobado")])
predicciones <- ifelse(resultados$net.result > 0.5, 1, 0)

# Matriz de confusión
matriz <- table(ttesting$Aprobado, predicciones)
print(matriz)