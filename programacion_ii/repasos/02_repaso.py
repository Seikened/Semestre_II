class Tiempo:
    estatica = 2
    def __init__(self, min, seg):
        self.minutos = min
        self.segundos = seg
        self.Normalizacion()
    
    def TiempoTotalSegundos(self):
        return (self.minutos*60) + (self.segundos)
    
    def Normalizacion(self):
        tiempoTotal = self.TiempoTotalSegundos()
        self.minutos =  tiempoTotal // 60
        resuduo = tiempoTotal- (self.minutos * 60)
        self.segundos = resuduo
    
    def __str__(self):
        return f" m {self.minutos} : s {self.segundos}"
    
    def __lt__(self,other):
        if self.TiempoTotalSegundos() < other.TiempoTotalSegundos():
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.TiempoTotalSegundos() > other.TiempoTotalSegundos():
            return True
        else:
            return False




class Competidor:
    
    competidoresConstruidos =  0
    
    def __init__(self,nombre,numero,escuderia):
        self.__nombre = nombre
        self.__numero = numero
        self.__escuderia = escuderia
        self.__tiempos = []
        Competidor.competidoresConstruidos += 1
    
    def AgregaTiempo(self,tiempo):
        self.__tiempos.append(tiempo)

    def TablaTiempos(self):
        print (f"""
        🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
        --------------------------------
        Tabla de {self.__nombre}
        --------------------------------
        Tempos:
        """)
        for tiempo in self.__tiempos:
            print(tiempo)
    
    def TiempoTotalAcumulado(self):
        suma = 0
        for tiempo in self.__tiempos:
            suma += tiempo.TiempoTotalSegundos()
        return Tiempo(0,suma)

    def __lt__(self,other):
        if self.TiempoTotalAcumulado() < other.TiempoTotalAcumulado():
            return True
        else:
            return False

    def __gt__(self,other):
        if self.TiempoTotalAcumulado() > other.TiempoTotalAcumulado():
            return True
        else:
            return False


import os
os.system("clear")
#Programa principal
t1=Tiempo(0,135)
t2=Tiempo(3,10)
t3=Tiempo(2,54)
print("t1 es igual a:", t1)
print(t1," es lo mismo que:", t1.TiempoTotalSegundos(),"segundos")
print("t1 mayor que t2? ",t1>t2)
print("t1 menor que t2? ",t1<t2)


c1=Competidor("Peter Solberg",5,"Subaru")
c1.AgregaTiempo(t1)
c1.AgregaTiempo(t2)
c1.AgregaTiempo(t3)
c1.AgregaTiempo(Tiempo(1,40))
c1.TablaTiempos()



c2=Competidor("Marcus Gronholm",5,"Peugeot")
c2.AgregaTiempo(Tiempo(2,23))
c2.AgregaTiempo(Tiempo(3,8))
c2.AgregaTiempo(Tiempo(2,40))
c2.AgregaTiempo(Tiempo(2,5))
c2.TablaTiempos()


print("Objetos construidos:", Competidor.competidoresConstruidos)
print("Tiempos totales")
tiempoTotalSolberg=c1.TiempoTotalAcumulado()
print("Tipo de dato de tTS:",type(tiempoTotalSolberg))
print("Solberg tiempo total:",c1.TiempoTotalAcumulado())
print("Gronholm tiempo total:",c2.TiempoTotalAcumulado())
ganaSolberg=c1<c2
print("Solberg gana? ",ganaSolberg )
print("GronHolm pierde? ",c2>c1)
