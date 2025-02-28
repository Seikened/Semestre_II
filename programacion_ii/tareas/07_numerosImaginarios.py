class Complejo():
    def __init__(self,re:float,im:float):
        self.real = re
        self.imaginario = im
    def Magnitud(self)-> float:
        mag=((self.real**2)+(self.imaginario**2))**(1/2)
        return mag
    def __str__(self):
        if self.imaginario < 0:
            return f" {self.real} - {abs(self.imaginario)}i"
        else:
            return f" {self.real} + {self.imaginario}i"
    def __add__(self,other):
        return Complejo(self.real + other.real , self.imaginario + other.imaginario)
    def __sub__(self,other):
        return Complejo(self.real - other.real , self.imaginario-other.imaginario)
    def __mul__(self,other):
        real_part = (self.real * other.real) - (self.imaginario * other.imaginario)
        imaginary_part = (self.real * other.imaginario) + (self.imaginario * other.real)
        return Complejo(real_part, imaginary_part)
    def __gt__(self,other):
        return self.Magnitud() > other.Magnitud()
    def __lt__(self,other):
        return self.Magnitud() < other.Magnitud()


#-------------------Pruebas-------------------
a = Complejo(10,-3)
b = Complejo(5,20)

# print(a.real,a.imaginario) 
# print(b.real,b.imaginario)
# print(a.Magnitud())

# print(a)

print("-"*100)
print(f"La suma de {a} y {b} es {a+b} \n")
print(f"La resta de {a} y {b} es {a-b} \n")
print(f"La multiplicación de {a} y {b} es {a*b} \n")
print(f"La magnitud de {a} es {a.Magnitud()} \n")
print(f"La magnitud de {b} es {b.Magnitud()} \n")
print(f"La magnitud de {a} es mayor que la magnitud de {b} es {a>b} \n")
print(f"La magnitud de {a} es menor que la magnitud de {b} es {a<b} \n")
print("-"*100)