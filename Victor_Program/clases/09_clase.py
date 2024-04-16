import sys,pygame
from juego import *



pygame.init()

#creamos la ventana de jueto
tamano=(800,600)
deltaTiempo_s=1/20 #el tiempo que pasa entre un cuadro y otro
screen=pygame.display.set_mode(tamano)
juego1 = Juego()



salir=False
while salir==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: salir=True
                
    #Entrada por teclado
    key=pygame.key.get_pressed()    
    if key[pygame.K_ESCAPE]: salir=True

    #Aqui recalculamos todas las variables 

    
    
    #Aquí redibujamos todos los objetos.
    screen.fill((0,0,0))
    juego1.cancha.Dibuja(screen)
    

    
    
    #flip para pantalla
    pygame.display.flip()

    pygame.time.wait(int(deltaTiempo_s*1000))

    
pygame.display.quit()

print("fin del programa")

