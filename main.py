import pygame
from modules.constants import SCREEN_WIDTH,SCREEN_HEIGHT
import modules.logger # noqa: F401

def main():
    print(f"Starting Asteroids with the pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
