# inventario.py
import pygame
from config import Config
from sprites import *

class Inventario:
    def __init__(self, pantalla,finanzas,huerto, capacidad=10):
        self.pantalla = pantalla
        self.finanzas = finanzas
        self.saldo = finanzas.saldo
        self.huerto = huerto   
        self.capacidad = capacidad
        self.slots = [{'id': None, 'cantidad': 0} for _ in range(capacidad)]
        self.activa = False
        self.dialogoActivo = False
        self.fuente = pygame.font.Font(None, 24)
        self.hoveredItemIndex = None  # Índice del slot sobre el que está el cursor

    def agregarItem(self, item_id, cantidad=1):
        for slot in self.slots:
            if slot['id'] == item_id:
                slot['cantidad'] += cantidad
                return True
            elif slot['id'] is None:
                slot['id'] = item_id
                slot['cantidad'] = cantidad
                return True
        return False

    def quitarItem(self, item_id, cantidad=1):
        for slot in self.slots:
            if slot['id'] == item_id and slot['cantidad'] >= cantidad:
                slot['cantidad'] -= cantidad
                if slot['cantidad'] == 0:
                    slot['id'] = None
                return True
        return False

    def renderizar(self):
        if not self.activa:
            return
        
        altura_fondo = 60 + 30 * self.capacidad  # Ajuste dinámico del fondo según la cantidad de slots
        fondoInventario = pygame.Surface((300, altura_fondo))
        fondoInventario.fill((139, 69, 19))  # Marrón tipo madera
        rectFondoInventario = fondoInventario.get_rect(center=(Config.ventanaAncho // 2, Config.ventanaAlto // 2))
        self.pantalla.blit(fondoInventario, rectFondoInventario.topleft)
        pygame.draw.rect(self.pantalla, (255, 255, 255), rectFondoInventario, 3)  # Borde blanco

        textoTitulo = self.fuente.render("Inventario", True, (255, 255, 255))
        self.pantalla.blit(textoTitulo, (rectFondoInventario.left + 10, rectFondoInventario.top + 10))

        for i, slot in enumerate(self.slots):
            y_pos = rectFondoInventario.top + 50 + i * 30
            infoItem = f"{slot['id'] if slot['id'] else 'Vacío'}  x {slot['cantidad']}" if slot['id'] else "Vacío"
            colorTexto = (255, 255, 255) if i != self.hoveredItemIndex else (200, 200, 200)
            textoSlot = self.fuente.render(infoItem, True, colorTexto)
            self.pantalla.blit(textoSlot, (rectFondoInventario.left + 10, y_pos))

        if self.dialogoActivo and self.hoveredItemIndex is not None:
            self.renderizarDialogo()
    
    def renderizarDialogo(self):
        dialogo_fondo = pygame.Surface((200, 100))
        dialogo_fondo.fill((255, 250, 250))  # Fondo claro para el diálogo
        rectDialogo = dialogo_fondo.get_rect(center=(Config.ventanaAncho // 2, Config.ventanaAlto // 2))
        self.pantalla.blit(dialogo_fondo, rectDialogo.topleft)

        opciones = ["Plantar", "Vender"]
        for i, opcion in enumerate(opciones):
            texto_opcion = self.fuente.render(opcion, True, (0, 0, 0))
            self.pantalla.blit(texto_opcion, (rectDialogo.left + 10, rectDialogo.top + 10 + i * 30))


    def venderItem(self, item_id):
        # Encuentra el artículo en la lista de items
        item = next((item for item in Config.items if item[id] == item_id), None)
        if item:
            precio = item['precio']
            if self.quitarItem(item_id):
                self.finanzas.recolectarMonedas(precio)
                print(f"Vendido: {item['nombre']} por ${precio} y tu Saldo actual: {self.saldo}")
            else:
                print(f"No se pudo vender {item['nombre']}")
        else:
            print("Ítem no encontrado.")
    
    def agregarItemAHuerto(self, item_id):
        if item_id == 'macetaCafe' or item_id == 'macetaNegra':
            maceta = Maceta(item_id)
            self.huerto.agregarMaceta(maceta)
        elif item_id == 'plantaFase1':
            planta = Planta(item_id)
            if not self.huerto.plantarEnMaceta(planta):
                print("No hay macetas disponibles para plantar")
        else:
            print("No se puede plantar este ítem")
        self.quitarItem(item_id)
    
    
    
    def manejarEventos(self, eventos):
        if not self.activa:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rectFondoInventario = pygame.Rect(0, 0, 300, 60 + 30 * self.capacidad)
        rectFondoInventario.center = (Config.ventanaAncho // 2, Config.ventanaAlto // 2)
        
        self.hoveredItemIndex = None
        for i, slot in enumerate(self.slots):
            y_pos = rectFondoInventario.top + 50 + i * 30
            item_rect = pygame.Rect(rectFondoInventario.left + 10, y_pos, 280, 30)
            if item_rect.collidepoint(mouse_x, mouse_y):
                self.hoveredItemIndex = i  # Identifica el ítem sobre el que se encuentra el cursor
                break  # Termina el loop una vez que se encuentra el ítem hovered

        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and self.hoveredItemIndex is not None:
                # Solo muestra el diálogo si el ítem no es "Vacío"
                item_id = self.slots[self.hoveredItemIndex]['id']
                if item_id is not None:
                    self.mostrarDialogo(item_id)

        if self.dialogoActivo:
            self.manejarEventosDialogo(eventos)

    def manejarEventosDialogo(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Suponiendo que las opciones están dibujadas a una altura de 30 pixels cada una
                rectDialogo = pygame.Rect(Config.ventanaAncho // 2 - 100, Config.ventanaAlto // 2 - 50, 200, 100)
                if rectDialogo.collidepoint(x, y):
                    index = (y - rectDialogo.top) // 30
                    if index == 0:  # Plantar
                        self.agregarItemAHuerto(self.opcionSeleccionada)
                    elif index == 1:  # Vender
                        self.venderItem(self.opcionSeleccionada)
                    self.dialogoActivo = False
                    
    def toggle_activa(self):
        self.activa = not self.activa

    def mostrarDialogo(self, item_id):
        self.dialogoActivo = True
        self.opcionSeleccionada = item_id