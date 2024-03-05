class Circulo:
    variableestatica = 20
    nuevo = 0
    
    def __init__(self,radio):
        self.radio = radio
        self.area = self.variableestatica * radio 
        Circulo.nuevo += 1
        self.numeroSerie = Circulo.nuevo
    
    def __str__(self):
        return f"El circul tiene un radio de {self.radio} y un area de {self.area} y es el NUMEROI DE SERIE {self.numeroSerie}"
    


# Programa principal

a = Circulo(2)
b = Circulo(3)
c= Circulo(7)
d = Circulo(8)

print(a)
print(b)
print(c)

print(d)

# class Config:
#     IDcam1 = "faser3412"
#     IDcam2 = "faser3413"

# class Camara:
#     def __init__(self,ID):
#         self.id = ID
    
#     def __str__(self):
#         return f"La camara tiene el ID => {self.id}"


# class Maquina:
#     def __init__(self):
#         self.camara = []
#         self.camara.append(Camara(Config.IDcam1))
#         self.camara.append(Camara(Config.IDcam2))


# Tesla = Maquina()
# test = Maquina()

# print(Tesla.camara[0])
# print(Tesla.camara[1])


# print("Holao")
