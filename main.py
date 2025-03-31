import pygame
from pygame.display import update
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable
asteroid_field = AsteroidField()

Player.containers = (updatable, drawable)
player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    updatable.update(dt)

    screen.fill('black')

    for obj in drawable:
        obj.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()