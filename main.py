import pygame
from pygame.sprite import Group
from pygame.time import Clock
from modules import SCREEN_WIDTH
from modules import SCREEN_HEIGHT
from modules import log_state
from modules import Player
from modules import Asteroid
from modules import AsteroidField

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    dt: int = 0 # delta time

    #create groups to manage the game objects
    updatable: Group = pygame.sprite.Group()
    drawable: Group = pygame.sprite.Group()
    asteroids: Group = pygame.sprite.Group()

    AsteroidField.containers = updatable
    asteroidfield: AsteroidField = AsteroidField()

    Asteroid.containers = (asteroids, updatable, drawable)
    # asteroid: Asteroid = Asteroid()

    Player.containers = (updatable, drawable)
    player: Player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        clock.tick(60) #pauses game loop for 1/60th of a second
        
        dt: int= clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
