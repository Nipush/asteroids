import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the program

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip() # Update the screen



if __name__ == "__main__":
    main()
