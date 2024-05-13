import json
import os

class Sesion:
    def __init__(self, finanzas, huerto, inventario):
        self.finanzas = finanzas
        self.huerto = huerto
        self.inventario = inventario
        self.archivo_estado = 'estado_juego.json'
        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.archivo_completo = os.path.join(self.ruta, self.archivo_estado)  # Ruta completa del archivo

    def cargarSesion(self):
        if os.path.exists(self.archivo_completo):  # Usar la ruta completa del archivo
            with open(self.archivo_completo, 'r') as f:
                data = json.load(f)
            self.finanzas.cargar(data.get('finanzas', {}))
            self.inventario.cargar(data.get('inventario', {}))
            self.huerto.cargar(data.get('huerto', {}))
            print("Estado cargado correctamente.")
        else:
            print("No se encontró archivo de estado, iniciando con valores por defecto.")

    def guardarSesion(self):
        data = {
            'finanzas': self.finanzas.guardar(),
            'inventario': self.inventario.guardar(),
            'huerto': self.huerto.guardar(),
        }
        with open(self.archivo_completo, 'w') as f:  # Usar la ruta completa del archivo
            json.dump(data, f)
        print("Estado guardado correctamente.")
