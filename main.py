import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Crio a tela
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField() # Crio o campo de asteroides

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Crio o player

    running = True
    dt = 0 # Delta time

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Fecha o jogo

        screen.fill((0, 0, 0))  # Preenche a tela de preto
        updatable.update(dt) # Atualiza os objetos

        for pedra in asteroids:
            if pedra.collides_with(player):
                print("Game Over!")
                running = False

            for shot in shots:
                if pedra.collides_with(shot):
                    pedra.split()
                    shot.kill()


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Atualiza a tela
        #clock.tick(60)  # Travo o FPS para 60
        dt = clock.tick(60) / 1000  # Transformo o tempo em segundos
        


if __name__ == "__main__":
    main()
