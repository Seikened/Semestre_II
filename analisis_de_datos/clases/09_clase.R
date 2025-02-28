#Series de tiempo

setwd('/Users/fernandoleonfranco/app/')

datos <- read.csv('R_Series de Tiempo.csv')
datos


Datos.Ts <- ts(datos$Ventas, frequency = 4) 

plot(Datos.Ts, ylab= 'Ventas', xlab='Trimestres')



# EJEMPLO DE SUAVIZADOS

plot(Datos.Ts,type="l")

st.1 <- filter(Datos.Ts, filter = rep(1/3,3))
st.2 <- filter(Datos.Ts, filter = rep(1/5,5))
st.3 <- filter(Datos.Ts, filter = rep(1/7,7))
lines(st.1,col="red")
lines(st.2,col="purple")
lines(st.3,col="green")




#install.packages("forecast",dependencies = TRUE)
library(forecast)
# FUNCION DE AUTOCORRELACION
autoplot(acf(Datos.Ts, plot = FALSE))
# Esto es la influencia de los datos pasados en los datos futuros


# HOLTWINTERS
res <- HoltWinters(Datos.Ts)
plot(Datos.Ts, 
     ylab = "Ventas", 
     xlab = "Trimestres",
     xlim = c(1, 7),
     ylim = c(4, 11))
prediccion  <- predict(res, n.ahead = 4)
prediccion
lines(prediccion, col = "red")


# EJEMPLO DE SERIES ANUALES
datosAnuales <- read.csv("Serie_Anual.csv")
datosAnuales
datos_ts_anuales <- ts(datosAnuales[1], frequency = 12, start=(c(2012,1)), end=c(2015,12))
datos_ts_anuales
plot(datos_ts_anuales, ylab = "Ventas", xlab = "Meses")
plot(stl(datos_ts_anuales, s.window = "periodic"))


# EJEMPLO DE SUAVIZADO
plot(datos_ts_anuales, type = "l")
st.1 <- filter(datos_ts_anuales, filter = rep(1/3,3))
st.2 <- filter(datos_ts_anuales, filter = rep(1/5,5))
st.3 <- filter(datos_ts_anuales, filter = rep(1/7,7))
lines(st.1,col="red")
lines(st.2,col="purple")
lines(st.3,col="green")

# PERIDIOGRAMA
res2 <- spec.pgram(datos_ts_anuales, log = "no")
res2
order(res2$spec, res2$freq, decreasing = TRUE)
max1 <- res2$freq[4]
max1
max2 <- res2$freq[8]
max2
max3 <- res2$freq[20]
max3

abline(v = max1,lty = "dotted", col = "red")
abline(v = max2,lty = "dotted", col = "blue")
abline(v = max3,lty = "dotted", col = "orange")


