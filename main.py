import pygame
import sys
from pygame.sprite import Group
from pygame.time import Clock
from modules import SCREEN_WIDTH
from modules import SCREEN_HEIGHT
from modules import log_state
from modules import Player
from modules import Asteroid
from modules import AsteroidField
from modules import log_event
from modules.shot import Shot

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = pygame.time.Clock()
    dt: int = 0 # delta time (time ellapsed between frames)

    #create groups to manage the game objects
    updatable: Group = pygame.sprite.Group()
    drawable: Group = pygame.sprite.Group()
    asteroids: Group = pygame.sprite.Group()
    shots: Group = pygame.sprite.Group()

    #atribute groups to each class
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable
    asteroidfield: AsteroidField = AsteroidField()

    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)
    player: Player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update game state
        updatable.update(dt)

        #check for asteroid collision with player
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                log_event("player_hit")
                print("GAME OVER!")
                sys.exit()

        #check for asteroid collision with player
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()



        # add background
        screen.fill("black")

        # draw items 
        for item in drawable:
            item.draw(screen)

        # render all to screen
        pygame.display.flip()
        
        # manage FPS
        clock.tick(60) 
        dt: int= clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
