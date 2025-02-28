class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def display_info(self):
        return f"Vehículo: {self.marca} {self.modelo}"


class Remolque:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def display_remolque_info(self):
        return f"Remolque tipo '{self.tipo}' con capacidad de {self.capacidad} toneladas"


class TrailerDobleFull(Vehiculo, Remolque):
    def __init__(self, marca, modelo, capacidad1, tipo1, capacidad2, tipo2):
        Vehiculo.__init__(self, marca, modelo)  # Inicializar la parte de Vehículo
        Remolque.__init__(self, capacidad1, tipo1)  # Inicializar la primera parte del remolque
        self.capacidad2 = capacidad2
        self.tipo2 = tipo2

    def display_full_info(self):
        vehiculo_info = self.display_info()
        remolque1_info = self.display_remolque_info()
        remolque2_info = f"Remolque tipo '{self.tipo2}' con capacidad de {self.capacidad2} toneladas"
        return f"{vehiculo_info}\n{remolque1_info}\n{remolque2_info}"




# Crear un objeto de la clase TrailerDobleFull

trailer = TrailerDobleFull("Volvo", "VNL 300", 20, "plataforma", 30, "cisterna")
print(trailer.display_full_info())