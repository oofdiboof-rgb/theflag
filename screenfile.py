import pygame
import random
import consts
import game_field
from consts import FLAG_START, NORMAL_COLOR, XRAY_COLOR, FLAG


def screen_create():
    pygame.init()
    spawn_grass()
    global screen
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    clock = pygame.time.Clock()
    screen.fill(NORMAL_COLOR)
    # game_field.spawn_mines(screen)
    for coords in grass_places:
        screen.blit(consts.GRASS, coords)
    # game_field.spawn_mines(screen)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    screen.blit(FLAG, FLAG_START)
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
