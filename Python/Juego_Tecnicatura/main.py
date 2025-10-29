import pygame
import sys
import random
import os
from personaje import Personaje, Enemigo, Explosion
from constantes import SCREEN_WIDTH, SCREEN_HEIGHT, ASSETS_PATH, IMPERIAL_MARCH_PATH, START_IMAGE_PATH, ESTRELLA_PATH, FONDO1_PATH

# Inicializar Pygame
def mostrar_pantalla_inicio(screen):
    #cargar y mostrar la imagen de inicio
    imgen_inicio = pygame.image.load(START_IMAGE_PATH)
    imagen_inicio = pygame.transform.scale(imgen_inicio, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(imagen_inicio, (0, 0)) # Dibujar la imagen en la pantalla
    pygame.display.flip() # Actualizar la pantalla y se muestre la imagen

    # Reproducr audio
    pygame.mixer.music.load(IMPERIAL_MARCH_PATH) # Cargar la música
    pygame.mixer.music.play(-1) # Reproducir el audio en bucle

    # Espera a que tenime el audio
    while pygame.mixer.music.get_busy(): # Mientras la música esté sonando
        for event in pygame.event.get(): # Manejar eventos
            if event.type.QUIT: # Si se cierra la ventana
                pygame.quit() # Salir de Pygame
                sys.exit() # Salir del sistema

        # Actualizar la pantalla
        screen.blit(imagen_inicio, (0, 0))
        pygame.display.flip() 

def main() :
    pygame.init ( )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Amenaza Fantasma ')

    # Cargar los recursos de este juego
    icono = pygame.image.load(f'{ASSETS_PATH}/images/fondo001.jfjf')
    pygame.display.set_icon(icono)

    fondo = pygame.image.load(f'{ASSETS_PATH}/images/fondo001.jpg')
    fondo = pygame.transform.scale(fondo, (SCREEN_HEIGHT, SCREEN_WIDTH))

    estrella = pygame.image.load(ESTRELLA_PATH)
    estrella = pygame.transform.scale(estrella, (SCREEN_HEIGHT, SCREEN_WIDTH))


    fondo1 = pygame.image.load(FONDO1_PATH)
    fondo1 = pygame.transform.scale(fondo1, (SCREEN_WIDTH, SCREEN_HEIGHT))

    sonido_laser = pygame.mixer.Sound(f'{ASSETS_PATH}/sounds/explosion.mp3')

    personaje = Personaje(SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2)
    enemigos = [] # Lista para almacenar los enemigos
    explosiones = [] # Lista para almacenar las explosiones cada vez que toca el enemigo
    puntos = 0 # Puntos iniciales
    nivel = 1 # Nivel inicial

    clock = pygame.time.Clock() # Reloj para controlar los FPS
    running = True

    #Inicializar fondo actual con el fondo original
    fondo_actual = fondo

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        dx, dy = 0,0

        if keys [pygame.K_LEFT]: # tecla hacia la rechecha
            dx = -5
        if keys[pygame.K_RIGHT]: # tecla hacia laizquierda
            dx = 5
        if keys[pygame.K_UP]: # tecla hacia arriba
            dy = -5
        if keys[pygame.K_DOWN]: # tecla hacia abajo
            dy = 5

        personaje.mover(dx, dy)

        if keys[pygame.K_SPACE]:
            personaje.lanzar_laser()
            sonido_laser.play()

        # Actualizar posicion de enemigops y manejar colisiones
        for enemigo in enemigos [:]: # itera sobre una copia para eliminar de la lista original 
            enemigo.mover()
            if enemigo.rect.top > SCREEN_HEIGHT:
                enemigos.remove(enemigo)
            
            # verificar colisiones con los laseres
            for laser in personaje.lasers: # iterar sobre una copia para eliminar de la lista original
                if enemigo.rect.colliderect(laser.rect):
                    explosiones.append(Explosion(enemigo.rect.centerx, enemigo.rect.centery))
                    enemigos.remove(enemigo)
                    personaje.lasers.remove(laser)
                    sonido_laser.explosion.play()
                    puntos += 10  # se incrementa los puntos en + 10
                    break
                if enemigo.rect.colliderect(personaje.shape):
                    if not personaje.recibir_dano():
                        running = False # Terminar el juego si la energia llega a 0

        # Generar enemigos aleatoriamente
        if random.random() <0.02:
            x = random.randint(0, SCREEN_WIDTH - 50)
            enemigo = Enemigo(x, 0)
            enemigos.append(enemigo)

        #Actualizar explosiones
        explosiones = [explosion for explosion in explosiones if explosion.actualizar()]

        # Cambiar fonde de pantalla segun los puntos  250
        if puntos >= 0 and puntos % 250 == 0:
            if fondo_actual == fondo:
                fondo_actual = estrella 
        else:
            fondo_actual = fondo1 
            puntos = 0
            nivel += 1 # incrementa el nivel

        # Dibujar el fondo en ela pantalla
        screen.blit(fondo_actual, (0,0))

        # Dibujar el personaje
        personaje.dibujar(screen)

        # Dibujar los enemigos
        for enemigo in enemigos:
            enemigo.dibujar(screen)

        # Dibujar las explosiones
        for explosion in explosiones:
            explosion.dibujar(screen)

        # Mostrar el marcador y el nivel
        font = pygame.font.Font(None, 36)
        texto_puntos = font.render(f'Puntos: {puntos}', True, (255, 255, 255))
        texto_nivel = font.render(f'Nivel: {nivel}', True, (255, 255, 255))
        screen.blit(texto_puntos, (10, 50))
        screen.blit(texto_nivel, (10, 90))

        pygame.display.flip()
        clock.tick(60)

    # Mostrar mensaje de GAME OVER
    screen.fill((0, 0, 0))
    texto_game_over= font.render('GAME OVER', True, (255, 0, 0))
    texto_mensaje_final = font.render('QUE LA FUERZA TE ACOMPAÑE. !!', True, (255, 255, 255))

    # Mostrar GAME OVER
    screen.blit(texto_game_over, (SCREEN_WIDTH //2 -texto_game_over.get_width() //2, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # muestra la frase de game over po dos segundos

    # Desaparecer GAME OVER y mostrar mensaje final
    for alpha in range (255, -1, -5):
        screen.fill((0, 0, 0))
        texto_game_over.set_alpha (alpha)
        screen.blit(texto_game_over, (SCREEN_WIDTH //2 - texto_game_over.get_width() // 2 , SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(10)
    
    # Dibujar/mostrar texto en la pantalla
    screen.fill(0, 0, 0)
    screen.blit(texto_mensaje_final, (SCREEN_WIDTH // 2 - texto_mensaje_final.get_width() //2 , SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(5000) # mostrar mensaje final durante 5 segundos

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()