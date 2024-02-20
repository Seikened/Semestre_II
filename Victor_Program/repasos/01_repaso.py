# Cajero automatico modo clase y tiene que ser capa de devolver el billete mas grande posible
# Billetes de 500, 200, 100, 50, 20

class Cajero:
    def __init__(self):
        self.billetes = [500, 200, 100, 50, 20]

    def devolver_billetes(self, cantidad):
        for billete in self.billetes:
            if cantidad >= billete:
                print(f"Devuelvo {billete}")
                cantidad -= billete
                if cantidad > 0:
                    self.devolver_billetes(cantidad)
                break

cajero = Cajero()
# Impresion de la cantidad de billetes que se devuelven
print(f"""
Cantidad de billetes devueltos:
{cajero.devolver_billetes(500)}
""")
