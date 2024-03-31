import random
import os
import random

os.system("clear")

def generarEmoji():
    # List of emojis
    emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸"]

    # Return a random emoji from the list
    return random.choice(emojis)

class Candidato:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__votos = 0
    
    def AddVoto(self):
        self.__votos += 1 

    def __str__(self):
        return f"{self.__nombre} con la cantidad de votos de: {self.__votos}"
    
    def GetVotos(self):
        return self.__votos
    
    def ResetVotos(self):
        self.__votos = 0 

class Votacion:
    cantidadEjerciciosVotacion = 0
    
    def __init__(self):
        self.candidatos = []

    def AddCandidato(self, candidato):
        self.candidatos.append(candidato)

    def __GeneradorVoto(self, abstencion_A=50, abstencion_B=47, abstencion_C=53):
        votoRandom = random.uniform(0,100)

        if votoRandom < 10:
            abstencion = random.uniform(0,100)
            if abstencion <= abstencion_A:
                return 1
        elif votoRandom < 50:
            abstencion = random.uniform(0,100)
            if abstencion <= abstencion_B:
                return 2
        elif votoRandom <= 100:
            abstencion = random.uniform(0,100)
            if abstencion <= abstencion_C:
                return 3
        return 0


    def IniciarVotacion(self, cantidadVotosEfectivos, abstencion_A=50, abstencion_B=47, abstencion_C=53):
        Votacion.cantidadEjerciciosVotacion += 1
        votos_contados = 0
        while votos_contados < cantidadVotosEfectivos:
            voto = self.__GeneradorVoto(abstencion_A=abstencion_A, abstencion_B=abstencion_B, abstencion_C=abstencion_C)
            if voto > 0:
                self.candidatos[voto - 1].AddVoto()
                votos_contados += 1

    def GanadorActual(self):
        if not self.candidatos:
            return "No hay candidatos"
        return max(self.candidatos , key = lambda  candidato: candidato.GetVotos())
    
    def VotosTotales(self):
        return sum(candidato.GetVotos() for candidato in self.candidatos)


    def __str__(self):
        candidatos_str = "\n".join([generarEmoji()+" "+str(candidato) for candidato in self.candidatos])
        ganador = self.GanadorActual()
        ganador_str = str(ganador) if ganador else "Sin votos"
        return f"""
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦

{Votacion.cantidadEjerciciosVotacion} ejercicios de votos
La suma total de votos es: {self.VotosTotales()}
----------------------------
CANDIDATOS:
{candidatos_str}

CANDIDATO GANADOR: {ganador_str}
"""



# Iniciar las elecciones y añadir candidatos
miVotacion = Votacion()
miVotacion.AddCandidato(Candidato('Fernando Leon'))  # Candidato A
miVotacion.AddCandidato(Candidato('Claudia Seinbaun'))  # Candidato B
miVotacion.AddCandidato(Candidato('Mayra Rodriguez'))  # Candidato C

def realizarSimulacion(abstencion_B):
    victorias_B = 0
    for _ in range(50000):  # Realizar 100 simulaciones

        for candidato in miVotacion.candidatos:
            candidato.ResetVotos()

        # Realizar votación con la tasa de abstencionismo actual para B
        miVotacion.IniciarVotacion(1000, abstencion_B=abstencion_B)  # Asumiendo 1000 votos efectivos
        
        # Contar victorias de B
        if miVotacion.candidatos[1].GetVotos() > miVotacion.candidatos[2].GetVotos():
            victorias_B += 1

    print(f"Con una tasa de abstencionismo del {abstencion_B}% para B, gana en {victorias_B} de las 100 simulaciones.")

# Ejecutar la simulación con una tasa de abstencionismo inicial para B
realizarSimulacion(47)  # Comenzar con la tasa de abstencionismo del 47% para B

print(miVotacion)