import pygame
from modules.constants import SCREEN_WIDTH,SCREEN_HEIGHT
from modules.logger import log_state
from modules.player import Player

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0 # delta time
    player: Player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(60) #pauses game loop for 1/60th of a second
        player.update(dt)
        
        dt: float= clock.tick()
        


if __name__ == "__main__":
    main()
