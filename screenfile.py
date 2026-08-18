import pygame
import random
import consts
from consts import FLAG_START, NORMAL_COLOR, XRAY_COLOR, FLAG, XY_SOLDIER
import time
import sys


def screen_create():
    pygame.init()
    global screen
    clock = pygame.time.Clock()
    screen.fill(NORMAL_COLOR)
    for coords in grass_places:
        screen.blit(consts.GRASS, coords)
    Font = pygame.font.SysFont('comic sans', 18)
    font = Font.render('Welcome to The Flag game.\n Have Fun!', False, 'orange')
    screen.blit(font, (consts.GRID_POS_X * 2, 0))
    screen.blit(FLAG, FLAG_START)
    create_soldier()
    pygame.display.flip()
    clock.tick(60)


def spawn_grass():
    global grass_places
    grass_places = []
    for i in range(20):
        grass_places.append((random.choice(range(int(consts.SCREEN_X - consts.GRASS_SIZE[0]))),
                             (random.choice(range(int(consts.SCREEN_Y - consts.GRASS_SIZE[1]))))))
    return grass_places


spawn_grass()
screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))


def create_soldier():
    pygame.display.flip()
    screen.blit(consts.SOLDIER, consts.XY_SOLDIER)


def create_night_soldier():
    pygame.display.flip()
    screen.blit(consts.SOLDIER_NIGHT, consts.XY_SOLDIER)


def win():
    screen.fill((7, 10, 51))
    WIN = pygame.font.SysFont('comic sans', 200)
    font = WIN.render('you won!!', False, 'gold')
    screen.blit(font, (100, 100))
    pygame.display.flip()
    running = True
    while running:
        time.sleep(3)
        running = False
    sys.exit()


def lose():
    screen.blit(consts.EXPLOSION, (XY_SOLDIER[0], XY_SOLDIER[1] + consts.GRID_POS_Y))
    pygame.display.flip()
    running = True
    while running:
        time.sleep(1)
        running = False
    screen.fill(0)
    LOSE = pygame.font.SysFont('', 200)
    font = LOSE.render('you died', False, 'red')
    screen.blit(font, (200, 110))
    pygame.display.flip()
    running = True
    while running:
        time.sleep(3)
        running = False
    sys.exit()
