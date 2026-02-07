
import random
import pygame
from modules.circleshape import CircleShape
from modules.constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from modules.logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        
        first_new_asteroid_movement = self.velocity.rotate(split_angle)
        second_new_asteroid_movement = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2: Asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = first_new_asteroid_movement * 1.2
        new_asteroid_2.velocity = second_new_asteroid_movement * 1.2
