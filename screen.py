import pygame
import random
import consts
from consts import START_SOLDIER, FLAG_START, NORMAL_COLOR, XRAY_COLOR


def screen_create():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    clock = pygame.time.Clock()
    xray = False
    running = True

    spawn_grass()
    spawn_mine()
    screen.blit(consts.SOLDIER, START_SOLDIER)
    screen.blit(consts.FLAG, FLAG_START)
    while True:

        while running:
            screen.fill(NORMAL_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    xray = True
            pygame.display.flip()
            clock.tick(60)
        while xray:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(XRAY_COLOR)
                    pygame.time.wait(1000)
                    xray = False
                    running = True
            pygame.display.flip()
            clock.tick(60)


def spawn_grass():
    for i in range(20):
        screen.blit(consts.GRASS, ((random.choice(range(int(consts.SCREEN_X-consts.GRASS_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.GRASS_SIZE[1])))))
def spawn_mine():
    for i in range(20):
        screen.blit(consts.MINE, ((random.choice(range(int(consts.SCREEN_X-consts.MINE_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.MINE_SIZE[1])))))
screen_create()
