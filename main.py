import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    dt = 0 # Delta time
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crio a tela
    pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Crio o player

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Fecha o jogo

        screen.fill((0, 0, 0))  # Preenche a tela de preto
        player.draw(screen)  # Desenha o player
        player.update(dt) # Atualiza o player
        pygame.display.flip()  # Atualiza a tela
        pygame.time.Clock().tick(60)  # Seta o FPS para 60
        dt = pygame.time.Clock().tick(60) / 1000  # Pegar o delta time
        


if __name__ == "__main__":
    main()
