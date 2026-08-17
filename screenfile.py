import pygame
import random
import consts
import soldier
from consts import  FLAG_START, NORMAL_COLOR, XRAY_COLOR


def screen_create():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    clock = pygame.time.Clock()
    screen.fill(NORMAL_COLOR)
    spawn_grass()
    soldier.create_soldier(screen)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    # screen.blit(consts.SOLDIER, START_SOLDIER)
    pygame.display.flip()
    # clock.tick(60)


def spawn_grass():
    for i in range(20):
        screen.blit(consts.GRASS, ((random.choice(range(int(consts.SCREEN_X-consts.GRASS_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.GRASS_SIZE[1])))))
def spawn_mine():
    for i in range(20):
        screen.blit(consts.MINE, ((random.choice(range(int(consts.SCREEN_X-consts.MINE_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.MINE_SIZE[1])))))
