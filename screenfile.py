import pygame
import random
import consts
import game_field
from consts import START_SOLDIER, FLAG_START, NORMAL_COLOR, XRAY_COLOR


def screen_create():
    pygame.init()
    spawn_grass()
    global screen
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    clock = pygame.time.Clock()
    screen.fill(NORMAL_COLOR)
    for i in grass_places:
        screen.blit(consts.GRASS, i)
    # game_field.spawn_mines(screen)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    pygame.display.flip()
    clock.tick(60)


def spawn_grass():
    global grass_places
    grass_places = []
    for i in range(20):
        grass_places.append((random.choice(range(int(consts.SCREEN_X-consts.GRASS_SIZE[0]))), (random.choice(range(int(consts.SCREEN_Y-consts.GRASS_SIZE[1]))))))
    return grass_places
# def spawn_mine():
#     for i in range(20):
#         screen.blit(consts.MINE, ((random.choice(range(int(consts.SCREEN_X-consts.MINE_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.MINE_SIZE[1])))))
