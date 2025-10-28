import os # para que se conecte con el sistema operativo
from constantes import ASSETS_PATH
import pygame

class Explosion:
    def __init__(self, x, y):
        self.images = [pygame.image.load(os.path.join(ASSETS_PATH, 'images', f'regularExplosion0{i:2}.png')) for i in range(9)] # carga las imágenes de la explosión
        self.index = 0 # indice de la animación
        self.image = self.images[self.index] # imagen actual de la explosión
        self.rect = self.image.get_rect(center=(x, y))  
        self.frame_rate = 0 #contador de los frames de la animación
        self.frames = 20 # frames de la imagenes

    def actualizar(self):
        #actualizar la animación de la explosión
        self.frame_rate +=1
        if self.frame_rate >= self.frames:
            self.index +=1
            if self.index >= len(self.images):
                return False # la animación ha terminado
            self.image = self.images[self.index]
        return True # la animación continúa

    def dibujar(self, screen):
        #dibujar la imagen en la pantalla
        screen.blit(self.image, self.rect.topleft)