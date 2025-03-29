import pygame
from constants import *

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.Surface.fill(screen, color='black')  # put here screen var and color
    pygame.display.flip()


def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()