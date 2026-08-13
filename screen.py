import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1500, 750))
clock = pygame.time.Clock()
running = True
bush_x = 1500
bush_y = 750
for i in range(20):
    screen.fill((9, 99, 0))
    screen.blit(GRASS, (random.choice(range(bush_x)), random.choice(range(bush_y))))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)