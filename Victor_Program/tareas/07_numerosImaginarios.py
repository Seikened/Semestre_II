class Complejo():
    def __init__(self,re:float,im:float):
        self.real = re
        self.imaginario = im
    def Magnitud(self)-> float:
        mag=((self.real**2)+(self.imaginario**2))**(1/2)
        return mag




a = Complejo(10,3)
b = Complejo(5,20)

print(a.real,a.imaginario) 
print(b.real,b.imaginario)
print(a.Magnitud())

