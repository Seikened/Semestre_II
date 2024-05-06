##Metodo de potenciacion

library (ada)
install.packages("ada", dependencies = TRUE)

setwd("C:/App")
datos <- read.table("MuestraCredito_Completo.csv",
                    sep = ";",
                    dec = ".",
                    header = TRUE,
                    )
datos
str(datos)

datos$MontoCredito = as.factor(datos$MontoCredito)
datos$IngresoNeto = as.factor(datos$IngresoNeto)
datos$CoefCreditoAvaluo = as.factor(datos$CoefCreditoAvaluo)
datos$MontoCuota = as.factor(datos$MontoCuota)
datos$GradoAcademico = as.factor(datos$GradoAcademico)
datos$BuenPagador = as.factor(datos$BuenPagador)


#SEGMENTAR PARA ENYTRENAMIENTO Y PARA TESTING
dim(datos)
muestra <- sample(1:5000, 1000)
ttesting <- datos[muestra,]
taprendizaje <- datos[muestra,]


modelo <- ada(BuenPagador~., data = taprendizaje, iter = 20, nu = 1, type = "discrete")



#Graficacion del Modelo
plot(modelo,TRUE,TRUE)

#IMPORTANCIA DE LAS VARIABLES
varplot(modelo)


#PREDICCION 
prediccion <- predict(modelo, ttesting)
prediccion


"MATRIZ DE CONFUSION"
MC <- table(ttesting[,6], prediccion)
MC

#PORCENTAJE (PRECISION)
acierto <- (sum(diag(MC))/sum(MC))
acierto

#PORCENTAJE DE ERROR
error <- 1 - acierto
error

