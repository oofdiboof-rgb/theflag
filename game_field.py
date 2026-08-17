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
# spawn_mines()