import pygame
from constants import *

screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.Surface.fill(screen, color='black')  # put here screen var and color
    pygame.display.flip()
    dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()