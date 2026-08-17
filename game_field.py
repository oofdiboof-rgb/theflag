import pygame

import main
import screenfile
import consts
import random

from consts import XRAY_COLOR, MATRICS_Y, MATRICS_X


def create_matrix():
    for row in range(consts.MATRICS_Y):
        consts.MATRIX.append([])
        for col in range(consts.MATRICS_X):
            consts.MATRIX[row].append('0')

def spawn_mines():
    for mines in range(20):
        row = random.choice(range(len(consts.MATRIX)))
        spot = random.choice(range(len(consts.MATRIX[row])))
        if (consts.MATRIX[row][spot] or consts.MATRIX[row][spot+1] or consts.MATRIX[row][spot+2]) != "MINE":
            consts.MATRIX[row][spot] = "MINE"
            consts.MATRIX[row][spot+1] = "MINE"
            consts.MATRIX[row][spot+2] = "MINE"


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
# banans()