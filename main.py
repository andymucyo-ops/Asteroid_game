import pygame
from modules.constants import SCREEN_WIDTH,SCREEN_HEIGHT
from modules.logger import log_state

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        clock.tick(60) #pauses game loop for 1/60th of a second
        dt = clock.tick()


if __name__ == "__main__":
    main()
