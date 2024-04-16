import pygame

verde = (0,255,0)

class Juego():
    def __init__(self):
        self.cancha = Cancha(20,20,780,580)
    

class Cancha():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def Dibuja(self,screen):
        ancho = self.x2 - self.x1
        alto = self.y2 - self.y1
        rect=(self.x1,self.y1,ancho,alto)
        pygame.draw.rect(screen,verde,rect)
        