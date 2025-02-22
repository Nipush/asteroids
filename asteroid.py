import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, ("white"), self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(30, 180)

        new_asteroid_1 = self.velocity.rotate(angle)
        new_asteroid_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_asteroid_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_asteroid_2 * 1.2
