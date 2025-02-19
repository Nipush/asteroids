import pygame
from constants import *

def main():
    print("Starting asteroids!")
    dt = 0 # Delta time
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the screen
    pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the program

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the screen
        pygame.time.Clock().tick(60)  # Set the frame rate to 60
        dt = pygame.time.Clock().tick(60) / 1000  # Get the delta time



if __name__ == "__main__":
    main()
