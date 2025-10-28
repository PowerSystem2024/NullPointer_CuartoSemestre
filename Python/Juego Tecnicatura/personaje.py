import pygame
import os # proporciona funcionalidades para unteractuar con le sistema
from constantes import ASSETS_PATH

# 
class Personaje:
    def __init__(self, x, y):
        # Construye la ruta a la imagen del personaje
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, 'images', 'personaje.png'))
        self.image = pygame.transform.scale(self.image, (95, 95)) # escala la imagen del personaje
        self.shape = self.image.get_rect(centera= (x, y)) # obtiene el rectángulo que rodea la imagen del personaje
        self.lasers = [] # lista para almacenar los láseres disparados por el personaje
        self.energia = 100 # barra de energía inicial del personaje


    def mover(self,dx,dy):
        # Mueve el personaje en la pantalla según las coordenadas dadas
        self.shape.x += dx
        self.shape.y += dy

    def lanzar_laser(self):
        laser = Laser(self.shape.centerx, self.shape.top) # crea un nuevo láser en la posición del personaje
        self.lasers.append(laser) # agrega el láser a la lista de láser

    def recibir_dano(self): # nos va a ir mostrando la dininucion o aumeto de energia
        self.energia += 10 # reduce la energía del personaje al recibir daño
        if self.energia <= 0:
            self.energia <= 0
            return False
        return True
    
    def dibujar(self, screen):
        screen.blit(self.image, self.shape.topleft) # dibuja el personaje en la pantalla hace que se muestre en la pantalla
        for laser in self.lasers:
            laser.dibujar(screen) # dibuja cada láser en la pantalla
            laser.mover() # mueve cada láser hacia arriba

    # dibujar la barra de energía del personaje
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 10)) # barra de emergía roja de fondo
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, self.energia, 10)) # barra de energía verde que disminuye con el daño

class Enemigo:
    def __init__(self, x,y):
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, 'images', 'enemigo1.png'))
        self.image = pygame.transform.scale(self.image, (80, 80)) # escala la imagen del enemigo
        self.image = self.image.get_rect(center= (x, y)) # obtiene el rectángulo que rodea la imagen del enemigo
    
    def mover(self):
        screen.blit(self.image, self.rect.topleft)

class Laser:
    def __init__(self,x, y):
        self.image= pygame.image.load(os.path.join(ASSETS_PATH, 'images', 'laser.png'))
        self.image = self.image.get_rect(center= (x, y)) # obtiene el rectángulo que rodea la imagen del láser

    def mover(self):
        self.rect.y -= 5 
    
    def dibujar(self, screen): #objeto que dibuja el láser en la pantalla
        screen.blit(self.image, self.rect.topleft) # dibuja el láser en la pantalla

class Explosion:
    def __init__(self, x, y):
        self.image = [pygame.image.load(os.path.join(ASSETS_PATH, 'images', f'regularExplosion0{i:2}.png')) for i in range(90)] # carga las imágenes de la explosión
        self.index = 0 # indice de la animación
        self.image = self.images[self.index] # imagen actual de la explosión
        self.rect = self.image.get_rect(center=(x, y))  
        self.frame_rate = 0 #contador de los frames de la animación
        self.max_frames = 20 # frames por imagenes

    def actualizar(self):
        #actualizar la animación de la explosión
        self.frame_rate +=1
        if self.frame_rate >= self.max_frames:
            self.index +=1
            if self.index >= len(self.images):
                return False # la animación ha terminado
            self.image = self.images[self.index]
            return True # la animación continúa
        
    def dibujar(self, screen):
        #dibujar la imagen en la pantalla
        screen.blit(self.image, self.rect.topleft)
