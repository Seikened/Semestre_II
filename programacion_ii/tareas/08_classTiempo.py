class Tiempo:
    def __init__(self, dia, hora, min, seg):
        total_segundos = seg + min * 60 + hora * 3600 + dia * 86400
        self.dia, self.hora, self.minuto, self.segundo = self.descomponer_segundos(total_segundos)

    def fecha_segundos(self):
        return self.segundo + self.minuto * 60 + self.hora * 3600 + self.dia * 86400

    def descomponer_segundos(self, total_segundos):
        dia = total_segundos // 86400
        resto_dia = total_segundos % 86400
        hora = resto_dia // 3600
        resto_hora = resto_dia % 3600
        minuto = resto_hora // 60
        segundo = resto_hora % 60
        return dia, hora, minuto, segundo
    
    def __str__(self):
        return f"Día: {self.dia}, Tiempo => {self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
    def __sub__(self, other):
        self_segundos = self.fecha_segundos()
        other_segundos = other.fecha_segundos()
        segundos_diferencia = abs(self_segundos - other_segundos)
        return Tiempo(0, 0, 0, segundos_diferencia)

#============================= Test =============================

fecha_uno = Tiempo(3, 23, 59, 60)
fecha_dos = Tiempo(5, 12, 5, 77)

print(fecha_uno, fecha_dos)

fecha_restante = fecha_uno - fecha_dos
print(fecha_restante)
