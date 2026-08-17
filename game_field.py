import pygame

import main
import screenfile
import consts
import random

from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X


#
# def spawn_mines():
#     for i in range(20):
#         spot = random.choice(main.MATRIX)
#         print(spot)

def banans():
    screen = pygame.display.set_mode((consts.SCREEN_X, consts.SCREEN_Y))
    screen.fill(XRAY_COLOR)
    for row in range(MATRICS_Y):
        for column in range(MATRICS_X):
            pygame.draw.rect(screen, (9, 99, 0),[20 * column + 1,20 * row + 1,20,20], 1)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    return


def down():
    pass

def up():
    pass

def left():
    pass

def right():
    pass

# screen.blit(consts.FLAG, FLAG_START)
# def spawn_mine():
#     for i in range(20):
#         screen.blit(consts.MINE, ((random.choice(range(int(consts.SCREEN_X-consts.MINE_SIZE[0])))), random.choice(range(int(consts.SCREEN_Y-consts.MINE_SIZE[1])))))
# while xray:
#     for event in pygame.event.get():
#         spawn_mine()
#
#         screen.blit(consts.FLAG, FLAG_START)
#         if event.type == pygame.QUIT:
#             screen.fill(XRAY_COLOR)
#             pygame.time.wait(1000)
#             xray = False
#             running = True
#     pygame.display.flip()
#     clock.tick(60)
# screenfile.screen_create()
banans()
# spawn_mines()