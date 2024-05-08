#CORRELACIONES

setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('EjemploClientes.csv', sep = ',', dec = '.' , header = TRUE, row.names = 1)

head(datos)

library(corrplot)


cor(datos$Edad, datos$Antiguedad)

datosCor <- cor(datos)


corrplot(datosCor)






datosEjemploClientes <- read.csv('EjemploClientes.csv', sep = ',', dec = '.' , header = TRUE, row.names = 1)
datosEjemploClientes

summary(datosEjemploClientes)

str(datosEjemploClientes)

#Matriz de correlacion
cor(datosEjemploClientes)
correlacionesClientes <- cor(datosEjemploClientes)
correlacionesClientes


library(corrplot)

corrplot(correlacionesClientes)
?corrplot

corrplot(correlacionesClientes, type = "lower")
corrplot(correlacionesClientes, type = 'lower', method = 'circle')
corrplot(correlacionesClientes, type = 'lower', method = 'square')
corrplot(correlacionesClientes, type = 'lower', method = 'shade')
corrplot(correlacionesClientes, type = 'lower', method = 'number')
corrplot(correlacionesClientes, type = 'lower', method = 'color')
corrplot(correlacionesClientes, type = 'lower', method = 'pie')
corrplot(correlacionesClientes, type = 'lower', method = 'ellipse')
corrplot.mixed(correlacionesClientes, lower = 'color', upper = 'number')




#REGRESION LINEAL
datosingresos <- read.csv('R_Ejemplo Ingresos vs Egresos.csv' )

cor(datosingresos)

regresionSimple <- lm(Gastos ~ Ingresos, data = datosingresos)

plot(datosingresos$Ingresos, datosingresos$Gastos, xlab = 'Ingresos', ylab ='Gastos')
abline(regresionSimple)

#Intervalos de confianza
confint(regresionSimple,level = 0.5)
confint(regresionSimple,level = 0.10)


#Predicciones
nuevoIngreso <- data.frame(Ingresos = c(12400,19000,16000))
primeraPrediccion <- predict(regresionSimple, nuevoIngreso)[1]
segundaPrediccion <- predict(regresionSimple, nuevoIngreso)[2]
terceraPrediccion <- predict(regresionSimple, nuevoIngreso)[3]

primeraPrediccion
segundaPrediccion
terceraPrediccion

#Regresion multiple

regresionMultipleDatos <- read.csv('R_Ejemplo Construccion.csv')
regresionMultipleDatos

cor(regresionMultipleDatos)

#install.packages('ggplot2',dependencies = TRUE)
library(ggplot2)
library(grid)
library(gridExtra)
library(corrplot)


#Modelo
modelo <- lm(Impuesto ~ Periodo + Superficie + ventanas + calzada, 
             data = regresionMultipleDatos)

nuevosDatos <- data.frame(
  Periodo =    c(2014,2016,2015),
  Superficie = c(130 ,215,185),
  ventanas =   c(5   ,7,3),
  calzada =    c(22  ,27,16)
)

predicciones <- predict(modelo, nuevosDatos)
#Hay tres predicciones
predicciones

#install.packages('car',dependencies = TRUE)
library(car)

vif(modelo)


# graficamos
par(mfrow = c(2,2))
plot(modelo)


