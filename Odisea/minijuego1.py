import pygame
from personaje import Player
from sistemaOleada import SistemaOleada
from entidad import Fondo

pygame.init()

ANCHO = 900
ALTO = 550

#FONDO
screen= pygame.display.set_mode((ANCHO, ALTO))
ruta_imagen = "animacion/fondo/fondo_2.png"

fondo = Fondo (ruta_imagen, ANCHO, ALTO)

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("La Odisea - Beat'em Up")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None,40)

player = Player(400,300,100,5)

oleadas = SistemaOleada()
oleadas.iniciar_oleada()

running = True

while running:

    clock.tick(60)

    fondo.draw (screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_j:
                player.ataque_rapido(oleadas.enemigos)

            if event.key == pygame.K_k:
                player.ataque_fuerte(oleadas.enemigos)

            if event.key == pygame.K_l:
                player.esquivar()


    teclas = pygame.key.get_pressed()

    player.move(teclas)
    player.temp_invul()

    player.draw(screen)
    player.barra_vida(screen)

    for enemigo in oleadas.enemigos[:]:

        enemigo.separar_enemigo(oleadas.enemigos)
        enemigo.move(player)
        enemigo.attack(player)


        enemigo.draw(screen)

        if enemigo.estado == "muerto" and enemigo.frame_index >= len(enemigo.muerte_frames) - 1:
            oleadas.enemigos.remove(enemigo)


    oleadas.fin_oleada()


    if player.vida <= 0:

        texto = font.render("GAME OVER", True, (255,0,0))
        screen.blit(texto,(300,280))

        pygame.display.update()
        pygame.time.delay(3000)

        running = False


    pygame.display.update()

pygame.quit()

