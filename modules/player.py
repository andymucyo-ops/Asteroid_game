import pygame
from pygame.math import Vector2 # noqa: F401
from .circleshape import CircleShape
from .constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation: int = 0

    def triangle(self) -> list[int]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
       pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH) 

    def rotate(self, dt: int) -> int :
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt: int) -> int:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return self.rotate(-dt)

        if keys[pygame.K_d]:
            return self.rotate(dt)

        if keys[pygame.K_s]:
            return self.move(-dt)

        if keys[pygame.K_w]:
            return self.move(dt)

    def move(self, dt:int): 
        unit_vector: Vector2 = pygame.Vector2(0,1) 
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_with_speed: Vector2 = rotated_vector * PLAYER_SPEED * dt 
        self.position += rotated_vector_with_speed


