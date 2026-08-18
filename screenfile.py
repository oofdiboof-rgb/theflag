import pygame
import random
import consts
import game_field
from consts import FLAG_START, NORMAL_COLOR, XRAY_COLOR, FLAG

def screen_create():
    pygame.init()
    global screen
    clock = pygame.time.Clock()
    screen.fill(NORMAL_COLOR)
    Font = pygame.font.SysFont('comic sans', 18)
    font= Font.render('Welcome to The Flag game.\n Have Fun!', False, 'orange')
    screen.blit(font, (consts.GRID_POS_X*2, 0))
    for coords in grass_places:
        screen.blit(consts.GRASS, coords)
    screen.blit(FLAG, FLAG_START)
    create_soldier()
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
spawn_grass()
screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))

def create_soldier():
    pygame.display.flip()
    screen.blit(consts.SOLDIER, consts.XY_SOLDIER)


def create_night_soldier():
    pygame.display.flip()
    screen.blit(consts.SOLDIER_NIGHT, consts.XY_SOLDIER)