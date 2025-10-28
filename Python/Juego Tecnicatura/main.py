import pygame # biblioteca para crear videojuegos
import sys # para interactuar con el sistema
import random # para generar números aleatorios
import os # para que se conecte con el sistema operativo

from personaje import Personaje, Enemigo, Explosion
from constantes import SCREEN_WIDTH, SCREEN_HEIGHT, ASSETS_PATH

# Inicializa EL JUEGO 
def mostrar_imagen_inicial(screen, imagen_path, duracion): # Muestra una imagen inicial durante un tiempo determinado
    imagen = pygame.image.load(imagen_path).convert() # Carga la imagen
    imagen = pygame.transform.scale(imagen, (SCREEN_WIDTH, SCREEN_HEIGHT)) # Escala la imagen al tamaño de la pantalla
    
    # Bucle para mostrar la imagen princpal con la opacidad
    alpha = 255 # Opacidad inicial
    Clock = pygame.time.Clock() # Reloj para controlar el tiempo

    tiempo_inicial = pygame.time.get_ticks() # Tiempo inicial
    tiempo_total = duracion # Duración en milisegundos de (8.000 milesegundos para 8 segundos)

    while pygame.time.get_ticks() - tiempo_inicial < tiempo_total: # Mientras no haya pasado el tiempo total
        for event in pygame.event.get(): # Maneja los eventos
            if event.type == pygame.QUIT: # Si se cierra la ventana
                pygame.quit() # Sale de pygame
                sys.exit() # Sale del sistema
    
    keys = pygame.key.get_pressed() # Obtiene las teclas presionadas
    dx, dy = 0, 0 # Inicializa el movimiento en x e y
    if keys[pygame.K_LEFT]: # Si se presiona la flecha izquierda
        dx = -5 # Mueve a la izquierda
    if keys[pygame.K_RIGHT]: # Si se presiona la flecha derecha
        dx = 5 # Mueve a la derecha
    if keys[pygame.K_UP]: # Si se presiona la flecha arriba
        dy = -5 # Mueve hacia arriba
    if keys[pygame.K_DOWN]: # Si se presiona la flecha abajo
        dy = 5 # Mueve hacia abajo

    personaje.mover(dx, dy) # Mueve el personaje

    if keys[pygame.K_SPACE]: # Si se presiona la barra espaciadora
        personaje.lanzar_laser() # El personaje lanza un láser
        sonido_laser.play() # Reproduce el sonido del láser

    #actualizar posicion de enemigo y manejar las colisiones
    for enemigo in enemigos[:]: # iterar para eliminar la lista principal
        enemigo.mover()
        if enemigo.rect.top > SCREEN_HEIGHT: # si el enemigo sale de la pantalla
            enemigos.remove(enemigo) # eliminar el enemigo de la lista

    # verificar colision con el laser 
    for laser in persinaje.laser [:]:
        if enemigo.rect.colliderect(laser.react):
            explosiones.append(Explosion(enemigo.rect.centerx, enemigo.rect.centery)) # crear una explosión en la posición del enemigo
            enemigos.remove(enemigo) # eliminar el enemigo de la lista
            personaje.lasers.remove(laser) # eliminar el láser de la lista
            sonido_explosion.play()
            puntos +=10 #incrementa el puntaje
            break # salir del bucle para evitar errores

    
    if enemigo.rect.colliderect(personaje.shape):
        if not personaje.recibir_dano(): # si el personaje recibe daño y su energía llega a 0
            running = False # termina el juego si la energia llega a 0

    # Generar enemigos de forma aleatoria
    if random.randint(1,10)<2:
        x = random.randint(0, SCREEN_WIDTH - 50) #Nos asegura de tener al enemigo dentro de la pantalla 
        enemigo = Enemigo(x, -50) # crea un nuevo enemigo en una posición aleatoria en la parte superior de la pantalla
        enemigo.appens(enemigo)

    #Actualizar explosiones
    explosion = [explosion for explosion in explosiones if explosion.actualizar()] # actualiza las explosiones y elimina las que han terminado

    # Actualizar el fondo cada 250 puntos
    if puntos > 0 and puntos % 250 == 0:
        if fondo_actual == fondo2:
            fondo_actual = fondo3
        else:
            fondo_actual = fondo2
            puntos += 10 # Aumneta puntos y cambia el fondo
    
    # Dibujar el fondo y obejetos en la pantalla
    screen.blit(fondo_actual, (0, 0)) # dibuja el fondo actual
    personaje.dibujar(screen) # dibuja el personaje
    for enemigo in enemigos:
        enemigo.mover(screen)
    for explosion in explosiones:
        explosion.dibujar(screen) 

# CAMBIOS PENDIENTES
