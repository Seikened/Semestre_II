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

class Votacion:
    cantidadEjerciciosVotacion = 0
    
    def __init__(self):
        self.__candidatos = []

    def AddCandidato(self, candidato):
        self.__candidatos.append(candidato)

    def __GeneradorVoto(self):
        return random.randint(1, len(self.__candidatos))

    def IniciarVotacion(self, cantidadVotos):
        Votacion.cantidadEjerciciosVotacion += 1
        for _ in range(cantidadVotos):
            voto = self.__GeneradorVoto()
            self.__candidatos[voto - 1].AddVoto()

    def GanadorActual(self):
        if not self.__candidatos:
            return "No hay candidatos"
        return max(self.__candidatos , key = lambda  candidato: candidato.GetVotos())
    
    def VotosTotales(self):
        return sum(candidato.GetVotos() for candidato in self.__candidatos)


    def __str__(self):
        candidatos_str = "\n".join([generarEmoji()+" "+str(candidato) for candidato in self.__candidatos])
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

# Iniciamos las elecciones
miVotacion = Votacion()

# Creación y añadido de candidatos
candidato_Fer = Candidato('Fernando Leon')
candidata_Claudia = Candidato('Claudia Seinbaun')
candidato_Mayra = Candidato('Mayra Rodriguez')

miVotacion.AddCandidato(candidato_Fer)
miVotacion.AddCandidato(candidata_Claudia)
miVotacion.AddCandidato(candidato_Mayra)

# Votamos
miVotacion.IniciarVotacion(1000)
miVotacion.IniciarVotacion(100)


print(miVotacion)